---
title: MediaWiki with nginx on Linode
author: Issa Rice
created: 2015-06-23
date: 2015-06-23
status: notes
belief: possible
---

**This page is really old.
I recently installed MediaWiki again for a different project, and
wrote [more detailed instructions](https://github.com/riceissa/nginx-mediawiki).**

# Preventing spam

Append the following lines to your `LocalSettings.php` *before*
uploading it to production. This will prevent user registration and
anonymous editing, i.e., you'll be the only one able to make any
changes.

~~~ { .php }
# From https://www.mediawiki.org/wiki/Manual:Preventing_access
# Prevent new user registrations except by sysops
$wgGroupPermissions['*']['createaccount'] = false;

# Disable anonymous editing
$wgGroupPermissions['*']['edit'] = false;
~~~

# Rewriting URLs

By default, MediaWiki uses the `/index.php?title=Page_name` syntax for
articles.  But this is ugly, so it's better to use rewrite rules in
nginx to change this to `/wiki/Page_name` like on Wikipedia.

In some place nginx can read[^cp_wiki]:

~~~
# Modified from https://www.mediawiki.org/wiki/Manual:Short_URL/wiki/Page_title_--_nginx_rewrite--root_access
location / {
    index index.php index.php5;
    error_page 404 = @mediawiki;
}

location @mediawiki {
    rewrite ^/wiki([^?]*)(?:\?(.*))? /index.php?title=$1&$2 last;
}
~~~

In `LocalSettings.php`:

~~~ { .php }
# From https://www.mediawiki.org/wiki/Manual:Short_URL/wiki/Page_title_--_nginx_rewrite--root_access
$wgScriptPath       = "";
$wgArticlePath      = "/wiki/$1";
$wgUsePathInfo      = true;
~~~

# Math

Below I'll outline steps to get both the image-style rendering of math
and Mathjax to work on Mediawiki.

First create an `uploads` directory in your MediaWiki directory.  Make
sure `www-data` owns this.  Install texvc as instructed on MediaWiki's
documentation page.  You might also need to change the permissions of
the `images` directory.

~~~ { .php }
# For math
require_once "$IP/extensions/Math/Math.php";

$wgUploadDirectory = "/var/www/cp_mediawiki/public_html/uploads";
$wgUploadPath = "/uploads";

$wgTexvc = "/usr/bin/texvc";

$wgMathValidModes[] = MW_MATH_MATHJAX; // Define MathJax as one of the valid math rendering modes
$wgUseMathJax = true; // Enable MathJax as a math rendering option for users to pick
#$wgDefaultUserOptions['math'] = MW_MATH_MATHJAX; // Set MathJax as the default rendering option for all users (optional)
#$wgDefaultUserOptions['mathJax'] = true; // Enable the MathJax preference option by default (optional)
$wgMathDisableTexFilter = true; // or compile "texvccheck"
~~~

If you want to modify the MathJax settings, you'll have to go change
`includes/OutputPage.php`, as explained in [this answer][wm se].

[wm se]: https://webmasters.stackexchange.com/questions/76459/how-to-configure-mathjax-in-mediawiki

In my case, I changed the relevant part to:

~~~ { .php }
$ret .= $this->buildCssLinks();

$ret .= "<script type='text/x-mathjax-config'>MathJax.Hub.Config({
'HTML-CSS': {
    // TeX font has better spacing on Linux browsers
    availableFonts: ['TeX'],
    preferredFont: 'TeX'
}
});</script>";

$ret .= $this->getHeadScripts() . "\n";
~~~

# cite web

Quite surprisingly, I could find almost nothing on the internet about
installying the very useful cite web template.  The best I could find
was [a Yahoo Answers page from 2009][yah], which proved to be at least
somewhat helpful.  I'll provide the full steps.

[yah]: https://answers.yahoo.com/question/index?qid=20090505163559AAWxN84

As noted, you have to install [ParserFunctions].  In addition, I found
that you need [Scribunto] to process the Lua code that cite web
apparently uses.

[ParserFunctions]: https://www.mediawiki.org/wiki/Extension:ParserFunctions
[Scribunto]: https://www.mediawiki.org/wiki/Extension:Scribunto

Now, go to Wikipedia's [Special:Export] page, and export the following
(make sure you check "Include templates" at the bottom, so that it pulls
in dependencies[^dep]) and save to a file:

```
Template:Citation/core
Template:Citation
Template:!
Template:Cite web
Module:Citation/CS1
Module:Citation/CS1/Configuration
Module:Citation/CS1/Whitelist
Module:Citation/CS1/Date validation
Module:Citation/CS1/Suggestions
```

Now go to your own wiki's Special:Import page. In my case, this was at
`http://wiki.causeprioritization.org/wiki/Special:Import`.  Now browse
for the file you just exported from Wikipedia, and click "Upload file"
to import everything.

With any luck, cite web should now work![^ghost]


[Special:Export]: https://en.wikipedia.org/wiki/Special:Export
[^dep]: Or at least that's what I think it does.

[^ghost]: In my case it wasn't so simple: at first, I got a `Lua error
in package.lua at line 80: module 'Module:Citation/CS1/Configuration'
not found.` error even though I had already installed
Module:Citation/CS1/Configuration!  It turned out though that when
logged out, cite web worked fine.  I ended up editing the page once, and
that seemed to make the page finally re-render.

[^cp_wiki]: In the case of the Cause Prioritization Wiki, which was the
reason I installed MediaWiki, this was stored in
`/etc/nginx/sites-available/causeprioritization.org` (with a symbolic
link to the `sites-enabled` counterpart). The full file is
as follows:

    ````
    server {
        listen 80;
        listen [::]:80;

        server_name wiki.causeprioritization.org;

        root /var/www/cp_mediawiki/public_html;
        index index.php index index.html;

        # Modified from https://www.mediawiki.org/wiki/Manual:Short_URL/wiki/Page_title_--_nginx_rewrite--root_access
        location / {
            index index.php index.php5;
            error_page 404 = @mediawiki;
        }

        location @mediawiki {
            rewrite ^/wiki([^?]*)(?:\?(.*))? /index.php?title=$1&$2 last;
        }

        # Modification of https://www.linode.com/docs/websites/nginx/nginx-and-phpfastcgi-on-debian-6-squeeze
        location ~ \.php$ {
            try_files $uri =404;
            include /etc/nginx/fastcgi_params;
            fastcgi_pass 127.0.0.1:9000;
            fastcgi_index index.php;
            fastcgi_param SCRIPT_FILENAME /var/www/cp_mediawiki/public_html$fastcgi_script_name;
        }

        access_log /var/www/cp_mediawiki/log/access.nginx.log;
    }
    ````

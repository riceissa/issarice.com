---
title: Digital preservation
author: Issa Rice
created: 2015-01-01
date: 2016-11-03
bigtable: true
---

For now, this will be somewhat of a  backup of my [Quora blog on the topic](https://www.quora.com/Issa-Rice/Data-Archiving), which is now not being maintained.
(I'm trying to integrate content from here to more fitting pages.)

Thoughts on storing information in a useful/easily-accessible way. Archiving, backups, single-source publishing, source code management, redundancy (local, cloud), link rot, etc. Essentially, how can we best store thoughts so that later (a day? month? years?) we can easily find them again.

# High-level overview of strategies for archiving browser activity

- Using a download program external to the browser. This is what gwern
  does; he uses wget to download a list of URLs. The list of URLs are
  obtained from places.sqlite, which Firefox generates.

- Using a browser plugin to save the page content to disk. The idea of
  this one is: You already *have* the webpage content in memory *by
  virtue of browsing the page*, so why not just store that to disk?
  However, this turns about to be harder than I thought, because first
  you need to understand JavaScript, and then you need to understand the
  plugin architecture of each major browser, and then actually write a
  plugin. It doesn't seem like there are any GOOD plugins out there.
  Shelve is one option but I don't trust it.

- Using a cache server and then tunneling all your browser activity
  through a proxy provided by that server. I think [Squid][squid] is the dominant
  player here, but I haven't much experience with this strategy in
  general. One advantage of this is, you can set it up once, and it will
  work for all browsers (that can tunnel through a proxy).

- Browser cache? Firefox and Chrome both maintain a cache of pages.
  The question is, does this count as a cache server, or serialized browser
  DOM, or a completely different solution?

Here is a table summarizing the strategies in more detail.
The "Type" column is defined as follows:

External
:   A process external to the browser is run, and fetches pages separately.
    The advantages of this approach are that it is guaranteed to run
    asynchronously and it is easy to automate.
    One disadvantage is that all content must be downloaded twice (once when
    viewing the page in the browser, and once when archiving the page through
    the external process).
    Another is that the effects of scripting are generally not present.

Browser DOM
:   The browser fetches the pages, and internally represents it as a DOM.
    This is a serialized form of the DOM.
    The advantages of this approach are that the content need only be
    downloaded once, and the effects of scripting are generally(?) present.

Raw
:   The browser fetches the pages, but a process intercepts the streams
    reaching it to store it for the long-term.
    One advantage: theoretically, every bit that is transmitted is captured.
    Disadvantages: the way things are cached may be different from how the
    browser represents the page as a DOM(?); effects of client-side scripting
    are not present(?).


|Strategy|Type|Browser support|Completeness|Appearance|Speed|Coverage of external resources|Automated?|Pages that require authentication?|
|:-------|:---|:--------------|:-----------|:---------|:----|:-----------------------------|:---------|:---------------------------------|
|wget/curl|External|Works for all browsers because downloads happen outside of the browser|Difficulty downloading sites that require JavaScript|Possibly bad|Fast, but requires downloading content twice (because it runs outside of the browser)|Yes|Yes, it's pretty easy to set up a pipeline to export browser history and automatically fetch the URLs|Yes, if cookies are exported|
|[PhantomJS][phantomjs]|External|Works for all browsers because downloads happen outside of the browser|Runs a headless browser so can support most/all JavaScript|Should be pretty good if external resources are also downloaded|Should be fine, but downloads content twice (because it runs outside of the browser)|Yes, but you have to script it yourself?|Yes, but you need to know JavaScript|Yes?
|View source|Raw|Most browsers have a "View Source" menu option|This is usually the raw HTML of the page *without* the effects of DOM scripting, so content that is loaded through scripts may not be present|Depends on whether you also fetch external resources, and also on how much scripting the page uses|Fast enough for most pages|Most browsers can do this|No|Yes|
|`document`|Browser DOM|Most modern browsers support this, though the representation and serialization might vary|Good, but doesn't include external resources, although these could be fetched as well (see ScrapBook)|Generally bad unless external resources are downloaded|Fast|Yes, if you script it|Yes; both Firefox and Chrome provide [`content_scripts`][cont_scr] that can run on matched URLs|Yes|
|[DOM Inspector][domi]|Browser DOM|Firefox|Good, but doesn't include external resources|Generally bad unless external resources are downloaded|Fast|No?|No?|Yes|
|[Web Developer][webdev] plugin's "view generated source"|Browser DOM|Firefox, but Chrome probably has something similar|Good, but doesn't include external resources|Generally bad unless external resources are downloaded|Pretty slow on sites like Facebook|No|No|Yes|
|[ScrapBook][sb], [ScrapBook X][sb_x]|Browser DOM|Firefox|Good|Good|Slow|Yes|With corresponding autosave plugin|No|Yes|
|Shelve| | | | | | |Yes|Yes|
|[WarcProxy][warcproxy]|Raw?|Works via HTTP proxy, so supports any browser|[Apparently good][wp_comp]|[Apparently good][wp_comp]|
|[Squid][squid]|Raw|
|Browser cache|Raw?|Each browser maintains its own cache|Depends on implementation by browser|Depends on implementation by browser|Depends on implementation by browser|Depends on implementation by browser| |Yes, since the browser controls it|

# Source HTML vs generated HTML

Thanks to JavaScript and other client-side scripting, naively saving the
source HTML of a webpage is sometimes *not enough to save all the
content*.

There is a concept of "generated HTML", which is the HTML that results
from applying scripts to the source HTML.

Is there a reliable way to access this generated HTML?

Separately (?) there is the concept of the browser DOM, which is the
object-oriented representation of the page, as interpreted by the browser.
The DOM acts as an API that languages like JavaScript can use.
The browser DOM differs from the source HTML is at least two respects:

-   It corrects for "in the wild" HTML by e.g. completing tags that were not
    closed in the original HTML.
-   It applies scripts to the original HTML.

Does the DOM differ from the "generated HTML"?

This is a good read: [Best Way to View Generated Source of Webpage?](https://stackoverflow.com/questions/1750865/best-way-to-view-generated-source-of-webpage).

# What are various things that can go wrong?

-   JavaScript alters source HTML
-   JavaScript loads more content as you interact with the page (e.g. "See
    more" and replies in Facebook, Quora, etc.)
-   Login required

See <https://exp.issarice.com/archive_test/> for several tests to run on
archival programs.

# Facebook.com DOM

I downloaded <https://facebook.com> while logged in, after scrolling down on my
newsfeed a couple of times and expanding some things.
I downloaded the page using three methods:

-   `document.documentElement.outerHTML`
-   DOM Inspector plugin
-   The Web Developers plugin's "generated HTML" feature

To diff the files, I first pre-processed the files using `fmt -w 40` and `tidy
-utf8` and then did the actual comparison using `gvimdiff`.
Passing `-w 40` to `fmt` is so that three files could comfortably sit
side-by-side on my screen.
`gvimdiff` is convenient in that it allows for three files to be compared at
once.

DOM Inspector uses things like

    <a class="see_more_link" onclick='var func = function(e) {
    e.preventDefault(); }; var parent = Parent.byClass(this,
    "text_exposed_root") ...' ...>...</a>

On the other hand, the bookmarklet and Web Developer Tools "generated HTML" do
things like

    <a class="see_more_link" onclick="var func = function(e) {
    e.preventDefault(); }; var parent = Parent.byClass(this,
    &quot;text_exposed_root&quot;) ..." ...>...</a>

The bookmarklet also compresses contiguous spaces into a single space, and
breaks lines on its own.

In other words, some differences are merely due to different ways of
serializing the same underlying structure.

Here is another.
On the bookmarklet and Web Dev tools:

    <abbr class="livetimestamp"
    title="Monday, October 31, 2016 at
    2:55am" data-utime="1477907708"
    data-shorten="true">8 hrs</abbr>

On the DOM Inspector:

    <abbr class="livetimestamp"
    title="Monday, October 31, 2016 at
    2:55am" data-utime="1477907708"
    data-shorten="true"><span class="timestampContent">8 hrs</span></abbr>

Note that here, the structure itself is different.
There is no span tag with class `timestampContent` in the former.

There are also some positional stuff that is different, e.g. chat contact list?
Some of it could be because the pages were not captured at exactly the same
time.

Some div tags corresponding to people (in the chat bar?) were also missing in
one or more of the dumps.

The Web Dev tools version also didn't have some script tags that referenced
external scripts.

However, as far as I can tell, the actual content on the page is stored in all
versions.
Indeed, `du -h *` shows the same size (1.2M) for all versions so the
differences are a rounding error.
Given this, it *seems* like the easiest way to programmatically access the
current browser DOM is through `document.documentElement.outerHTML`.

# Various bookmarklets

You will have to run these through a JavaScript compressor like
`yui-compressor`.

    // Open a new window and dump the current DOM. This can then be saved with
    // "Save Page As".
    javascript:(function() {
      var para = document.createElement('p');
      var t = document.createTextNode(document.documentElement.outerHTML.toString());
      para.appendChild(t);
      var win = window.open();
      win.document.body.appendChild(para);
    })();

There is a variant to the above that uses `win.document.write()` and
`win.document.close()` instead of manipulating the DOM with methods like
`appendChild()`.
However, I found that this fails on some sites for some unknown reason.
One page it fails on is
<https://developer.mozilla.org/en-US/docs/Using_files_from_web_applications>.
Another is <http://www.tecmint.com/best-linux-file-diff-tools-comparison/>.

From a [Stack Overflow answer][ans]:

> `document.write` is one of the oldest vestiges of ancient JavaScript, and
> should generally be avoided. Instead, you probably want to use DOM
> \[manipulation\] methods to update the document.

I don't know enough about JavaScript or its history to know if this is true,
but it's parsimonious.

For small pages, doing

    // Pick one
    copy(document.documentElement.outerHTML);
    copy(document.body.innerHTML);

is another option.
This copies the DOM to your clipboard.
I found that with very large sites, the clipboard seems to get full and not
update.
See <http://stackoverflow.com/a/20023875/3422337>.

# Dissecting ScrapBook X

[Git tree that I am using][sb_tree].

ScrapBook X seems to improve ScrapBook, and is apparently based on it.
I couldn't find the source for the original ScrapBook, so I can't really see if
this is true.

Anyway, my general intent is to get an idea of the high-level strategy it uses,
and then see if there is a way to save things without blocking the browser.

Some notes follow.

`chrome/content/scrapbook/` seems to be where the meat of the plugin is stored.
Here, I first noticed `capture.js`, but there is actually also a `saver.js`,
which turned out to be where the actual work is being done.

Reading `capture.js`, I see `var sbCaptureTask`.
Reading in, I see `_captureWindow: function(aWindow, aAllowPartial)` on line
470.
This calls

    var ret = gContentSaver.captureWindow(aWindow, aAllowPartial, gShowDetail, gResName, gResIdx, preset, gContext, gTitles[this.index]);

on line 491.
But line 2 defines `var gContentSaver = new sbContentSaverClass();`.
This is the only occurrence of `sbContentSaverClass` in this file.
No worry, I run

    :vimgrep /sbContentSaverClass/ **/*.js

and find

    chrome/content/scrapbook/capture.js|2 col 25| var gContentSaver = new sbContentSaverClass();
    chrome/content/scrapbook/saver.js|4 col 25| var saver = new sbContentSaverClass();
    chrome/content/scrapbook/saver.js|9 col 25| var saver = new sbContentSaverClass();
    chrome/content/scrapbook/saver.js|42 col 10| function sbContentSaverClass() {
    chrome/content/scrapbook/saver.js|88 col 1| sbContentSaverClass.prototype = {

So the class is in `saver.js`.
Line 42 looks promising (the fourth result above).
We want `captureWindow`, so search downward.
Lines 214--216:

    // save the document content to ScrapBook
    this.contentDir = sbCommonUtils.getContentDir(this.item.id);
    var newName = this.saveDocumentInternal(aRootWindow.document, this.documentName);

So now we want `saveDocumentInternal`, and it looks like `aRootWindow.document`
is what is being saved, which should be analogous to `document` if the entire
page is sought.
In Vim `[I` looks for all occurrences of the keyword under the cursor, so with
the cursor in `saveDocumentInternal`, I hit `[I`.
The definition is on line 272.

Several interesting things here. First off,

    if ( ["text/html", "application/xhtml+xml"].indexOf(contentType) < 0 ) {
        if ( !(aDocument.documentElement.nodeName.toUpperCase() == "HTML" && this.option["fileAsHtml"]) ) {
            captureType = "file";
        }
    }
    if ( captureType ) {
        var newLeafName = this.saveFileInternal(aDocument.location.href, aFileKey, captureType, charset);
        return newLeafName;
    }

So it looks like if the root node is HTML, we call `saveFileInternal`.
But this looks confusing because we're only passing `aDocument.location.href`
rather than `aDocument` or `aDocument.documentElement`, which contains the DOM!
But the test

    if ( ["text/html", "application/xhtml+xml"].indexOf(contentType) < 0 ) {

seems to be checking whether the content type is in the list.
Regular HTML files should have `text/html` as the content type, so it seems
that this capture only happens when the content type is not HTML yet the root
element is HTML.
I'm not sure why we would make this a special case.

Going past the block and reading down, line 316 has:

    var htmlNode = aDocument.documentElement;

And then line 394:

    if ( !this.selection ) {
        rootNode = htmlNode.cloneNode(true);

So `rootNode` is now a copy of `htmlNode`; tracking both and scrolling down,
line 525 has:

    myHTML += sbCommonUtils.surroundByTags(rootNode, rootNode.innerHTML + "\n");

And finally line 535:

    sbCommonUtils.writeFile(myHTMLFile, myHTML, charset);

So it is `myHTML` that gets written in the end.
But `myHTML` takes from `rootNode.innerHTML`, which is `htmlNode.innerHTML`,
which is `aDocument.documentElement.innerHTML`.

To summarize, it seems that ScrapBook X (and hence probably ScrapBook also)
saves the browser DOM by accessing `document.documentElement.innerHTML`.
Of course, the plugin does a lot more because it also tries to fetch
dependencies like stylesheets and various media.

I'm still not sure why ScrapBook X blocks Firefox while it saves a page.
I think plugins are allowed to fork separate processes, so it should be
possible to run the archival in the background while the user is free to do
whatever else with Firefox.

# Naming archives

How do you name archives?
In general, using the URL is not possible, because there is around a
2000-character limit to URLs but file systems like ext4 have a 255-byte limit.

# Solution in ELinks

ELinks comes with Lua scripting support.
Since it provides a hook that runs when the page loads and gives you the URL
and HTML, the solution is pretty simple:

    -- From http://stackoverflow.com/a/4991602
    function file_exists(name)
        local f = io.open(name, "r")
        if f ~= nil then
            io.close(f)
            return true
        else
            return false
        end
    end

    function pre_format_html_hook(url, html)
        local timestamp = os.date("%Y-%m-%dT%H-%M-%S%z")
        -- Increment i until we get a fresh location we can write to. This is
        -- necessary not because someone can open multiple pages in the same
        -- second, but rather because ELinks occasionally downloads auxiliary
        -- files, such as CSS files, as it fetches the page.
        local i = 0
        while file_exists(timestamp .. "." .. i .. ".html") do
            i = i + 1
        end
        local name = timestamp .. "." .. i .. ".html"
        -- After obtaining the HTML page, save a copy of it timestamped
        local index = io.open("index.txt", "a")
        index:write(name .. "\t" .. url .. "\n")
        index:close()
        local file = io.open(name, "w")
        file:write(html)
        file:close()
        -- Return the HTML page unmodified
        return nil
    end

Just save it in `~/.elinks/hooks.lua`.

Question: Does this capture everything that can be seen in ELinks?
In other words, is there a one-to-one correspondence between 'things that can
be see when browsing the page' and 'things that are saved on disk'?
Since Elinks doesn't support JavaScript, this seems possible, but I do wonder
if e.g. the content of iframes are saved (not that many sites I browse use
these).
Periodically grepping around the archived content is probably a good idea to
see if anything is missing.

Also the ELinks handling of HTTPS connections (as of version 0.12pre6 on
Ubuntu) is a bit concerning.

# Inactive account policy of various services

I'd like to do something similar for other services to what I [did for Dropbox
in a Quora answer](https://www.quora.com/Will-all-Dropbox-URLs-become-link-rot-December-2016).

The internet is so young that inactive accounts due to death has not been that
big of a deal yet.
Legal deposit laws, libraries, etc., have kept old books from disappearing, but
what can we say about internet content?

# Requirements for good data archiving solutions


Some ideas for now:

-   Pandoc-flavored markdown
-   LaTeX, then use LaTeX2WP or LaTeX–HTML converters (the benefit of
    this is that printing is covered, as long as your LaTeX skills are
    decent)
-   raw HTML (no)
-   using different formats for different content may be possible, e.g.
    using markdown for most content, but switching to LaTeX for
    math-heavy content.




# Static page generation

-   [Static Site Generators](http://staticsitegenerators.net/) —complete(?) list
-   [Static site generators](https://web.archive.org/web/20140921123610/http://www.mzlinux.org/?q=node/415)
-   [Jekyll • Simple, blog-aware, static sites](http://jekyllrb.com/)
-   [Hakyll - Home](http://jaspervdj.be/hakyll/)
-   [Switching from Jekyll to Hakyll](http://mark.reid.name/blog/switching-to-hakyll.html)
-   [The Switch to Hakyll](http://www.blaenkdenum.com/posts/the-switch-to-hakyll/)


Best Jekyll doc seems to be the video available from here:
[algonquindesign/jekyll](https://github.com/algonquindesign/jekyll).
Okay, so I've finally figured out how to use jekyll in conjunction with
Github. My test website is up on [Hello world](http://riceissa.github.io/abc/index.html).
See [riceissa/abc](https://github.com/riceissa/abc/tree/gh-pages)
for the source. The trickiest part was modifying all of jekyll's default
internal links (e.g. automatically generated links to blog posts) to use
`{{site.baseurl}}`, so that it worked both locally and
through Github pages.

I'm still trying to figure out how to do math properly through jekyll,
because at the moment I must use two backslashes, since one gets eaten
up by Markdown (pandoc can prevent this, so either switch to hakyll or
use a plugin for jekyll?—does Github even allow plugins for jekyll?)


# More on link rot and the Internet Archive (EDIT: found the speech!!)

Ones with a star (\*) are more useful.

-   [Why URL shorteners suck](http://boingboing.net/2009/04/04/why-url-shorteners-s.html)
-   [URL shorteners suck less, thanks to the Internet Archive and 301Works](http://boingboing.net/2009/11/13/url-shorteners-suck.html)
-   [URLTeam - Archiveteam](https://web.archive.org/web/20131105102512/http://archiveteam.org/index.php?title=TinyURL)
-   [URLTE.AM](http://urlte.am/)
-   [Learn From History: Why The Internet Archive Is So Important](http://flippa.com/blog/learn-from-history-why-the-internet-archive-is-so-important/)
-   [Brewster's trillions: Internet Archive strives to keep web history alive](http://www.theguardian.com/technology/2013/apr/26/brewster-kahle-internet-archive)
-   [on url shorteners](https://web.archive.org/web/20131016131625/http://joshua.schachter.org/2009/04/on-url-shorteners.html)
-   [301works-faq : Free Download & Streaming : Internet Archive](https://archive.org/details/301works-faq)


I'm still trying to find that speech about link rot and URL shorteners.

EDIT: I found the speech: [The Splendiferous Story of Archive Team](http://ascii.textfiles.com/archives/3029).
The guy's name is [Jason Scott Sadofsky](https://en.wikipedia.org/wiki/Jason_Scott_Sadofsky) and
he seems to have a lot of stuff e.g. [T E X T F I L E S](http://textfiles.com/jason/). He actually seems to be part
of the [Archiveteam](http://archiveteam.org/index.php?title=Main_Page),
which makes him even cooler. (How did I find the speech again after two
days of trying? [So that I can get better at finding old things.]
Through this article: [This Group Is Saving The Web From Itself (And Rescuing Your Stuff)](http://www.huffingtonpost.com/2013/03/27/jason-scott-archive-team_n_2965368.html),
where I got his name. My search terms on Google to find that article
were "saving the internet archive"; after I recognized the name, I just
Googled "jason scott", and found his Wikipedia page and website, whose
design I remembered from when I read the speech before.)

The relevant bit on URL shorteners is:


> URL shorteners may be one of the worst ideas, one of the most backward
> ideas, to come out of the last five years. In very recent times,
> per-site shorteners, where a website registers a smaller version of
> its hostname and provides a single small link for a more complicated
> piece of content within it.. those are fine. But these general-purpose
> URL shorteners, with their shady or fragile setups and utter
> dependence upon them, well. If we lose TinyURL or
> [bit.ly](http://bit.ly), millions of weblogs,
> essays, and non-archived tweets lose their meaning. Instantly.


# Terminally Incoherent

from Luke.

-   [Personal Backups](http://www.terminally-incoherent.com/blog/2012/06/04/personal-backups/)
-   [Putting your Vim files under version control](http://www.terminally-incoherent.com/blog/2012/03/12/putting-your-vim-files-under-version-control/)
-   [You Need Backups](http://www.terminally-incoherent.com/blog/2013/10/02/you-need-backups/)
-   [Backing up your work: Common Sense 101](http://www.terminally-incoherent.com/blog/2010/09/06/backing-up-your-work-common-sense-101/)
-   [Maybe the Backup Problem Will Resolve Itself In Time](http://www.terminally-incoherent.com/blog/2008/11/11/maybe-the-backup-problem-will-resolve-itself-in-time/)
-   [Backup is not just for geeks](http://www.terminally-incoherent.com/blog/2007/10/24/backup-is-not-just-for-geeks/)


The message is clear.

Also example of backing up dotfiles: [maciakl/.dotfiles](https://github.com/maciakl/.dotfiles).
Somewhere I remember reading a post about how to set this up nicely (by
Luke), but can't seem to locate it at the moment.


# Gwern on archiving

[Archiving URLs](http://www.gwern.net/Archiving%20URLs) see also
<http://www.gwern.net/About#long-content>. I can't
believe I had forgotten about this! Okay and linked on the first page is
this:
<https://web.archive.org/web/20141208192153/http://www.gwern.net/docs/2011-muflax-backup.pdf>
(from muflax).


# URL shortening

where is the speech that
someone at [Digital Library of Free Books, Movies, Music & Wayback Machine](http://archive.org) made about how URL
shortening sites cause a lot of link rot?

EDIT: Okay I found this at least:
<http://www.archiveteam.org/index.php?title=URLTeam>
and this links to [Why URL shorteners are bad](http://web.archive.org/web/20131025182943/http://rield.com/faq/why-url-shorteners-are-bad).
Not bad.

EDIT2: Okay finally found it. See [More on link rot and the Internet Archive (EDIT: found the speech!!)](http://www.quora.com/Issa-Rice/Data-Archiving/More-on-link-rot-and-the-Internet-Archive-EDIT-found-the-speech).


# What do people do about archiving information that they don't own?

e.g. a journal article that
you didn't write. This sort of thing could be very useful for people to
have access to. Storing them locally wouldn't be a problem, and putting
them up online shouldn't cause too much trouble either. Websites like
<http://archive.org> always just archive
whatever they can find anyway.

Actually, how does [Digital Library of Free Books, Movies, Music & Wayback Machine](http://archive.org) deal with
copyright issues?


# Git/GitHub

See [What are some unconventional and unique uses of Git?](http://www.quora.com/What-are-some-unconventional-and-unique-uses-of-Git)
and also the article linked in the description of the question (<http://www.wired.com/wiredenterprise/2012/02/github-revisited/>).

Git in particular is excellent in terms of having a local mirror as well
as one online (e.g. by using Github/Bitbucket), along with all of the
changes that have been made. This makes the data redundant/safe. It
doesn't seem to be bad either in terms of sharing, since everything will
be in plaintext. Posting on Quora might be a problem though, since it
doesn't use Markdown or the like.

I suppose the other big problem with using source-control is the
question of storing binary data. Use a different place to store those?
(e.g. putting all plaintext on Github but uploading photos to Wordpress,
and linking them?) Deal with binaries in git as well, and make many
small projects so that it doesn't slow down git?


# Random questions (not Quora-quality yet)

Some of these have
probably already been asked, so.

-   Is single-sourcing worth one's time for most things?
    For some things?
-   How important is grammar/capitalization for recording most thoughts?
    (cf AKC's post [on wordpress?] about grammar not being important)
-   Is Evernote reliable?
-   How do I easily create multiple mirrors of my data, both locally and online?
-   How do I reliable backup online data?
-   How do I keep a revision list of online data?—version control it somehow?
    how?
-   Why is Quora's search feature unreliable at finding the information I want?
    e.g. it can't find comments.
-   Why does Quora make everything so hard to find?
    —e.g. there are no chronological lists of all posts of a user, no place to find all the posts I've upvoted, and so on.
-   How do I make sharing easier between Quora and other sites?


# External mirroring

The way I see it, external page savers like the Internet Archive and WebCite shouldn't be trusted; rather, they're a convenient way to avoid copyright violations (since they're hosting the files, not you); and they provide a time buffer for you to get local copies.

I don't think I should be surprised at all by this, but I was quite impressed with [Perma.cc](http://perma.cc)'s [contingency plan](https://perma.cc/contingency-plan), which seems like an obvious improvement over standard web services that simply shut down and give no notice[^quora].

# Archive buttons

On Firefox, I have the following archive buttons:

![](archive-buttons.png)

From left to right, these are [Pinboard](https://pinboard.in/), Zotero,
archive.is, and Archive.org. The Archive.org button is a bookmarklet with the
code:

```
javascript:void(window.open('https://web.archive.org/save/'+location.href))
```

I also have the Scrapbook plugin for Firefox.
This allows me to quickly create copies that are local (Scrapbook and Zotero), private network (Pinboard), and public network (Archive.org).

# See also

-  [[Archiving Facebook]]

[^quora]: In the case of Quora, private blogs were almost immediately disabled and deleted after announcement (though archives were emailed out to owners); Google reader gave [under three months](https://en.wikipedia.org/wiki/Google_Reader#Discontinuation) to backup data.

[ans]: http://stackoverflow.com/a/10873999/3422337
[cont_scr]: https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/content_scripts
[domi]: https://addons.mozilla.org/en-Us/firefox/addon/dom-inspector-6622/ "“DOM Inspector”. SeaMonkey Council."
[phantomjs]: http://phantomjs.org/
[sb]: https://addons.mozilla.org/en-US/firefox/addon/scrapbook/
[sb_tree]: https://github.com/danny0838/firefox-scrapbook/tree/f77539c020e30d4235ab647934e72459056ce479
[sb_x]: https://addons.mozilla.org/en-US/firefox/addon/scrapbook-x/
[squid]: http://www.squid-cache.org/
[warcproxy]: https://github.com/odie5533/WarcProxy
[webdev]: https://addons.mozilla.org/en-US/firefox/addon/web-developer/
[wp_comp]: https://github.com/odie5533/WarcProxy#comparison

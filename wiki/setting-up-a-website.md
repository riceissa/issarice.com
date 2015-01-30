---
title: Setting up a website
tags: linux, site-info
status: notes
belief: possible
aliases: setting-up-a-webserver
---

More to come.

some things I need to talk about:

- how to set up domains with linode and hover.
- how to set up hakyll to work.
- how to set up the apache server on linode.
- decent workflow for how to go about editing a page, pushing changes, and then deploying. show all automation.


# Setting up a subdomain

on *Linode* go to A/AAAA Records, and add the following:

- Hostname: "blog" (or whatever you want in blog.example.com)
- IP Address: 192.xy.hij.ab WHATEVER. Just go to your Linode dashboard and find it.
- TLL: "Default" is fine

Then: **be patient**; it takes a bit of time for this to work.
But also in Apache, you need to set up a VirtualHost so this subdomain actually goes somewhere.
Do something like

~~~ bash
<VirtualHost *:80>
  DocumentRoot /var/www/blog/public_html
  ServerName blog.example.com

  DirectoryIndex index index.html index.php
#  LogLevel warn
#  ErrorLog /var/www/wp-blog/log/error.log
#  CustomLog /var/www/wp-blog/log/access.log combined
</VirtualHost>
~~~

but remember, `/var/www/blog/public_html` must be a valid location on your server.
Remember also to restart Apache using `sudo service apache2 restart`.

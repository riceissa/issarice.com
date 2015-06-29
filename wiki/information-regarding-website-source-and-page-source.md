---
title: Information regarding website source and page source
last-major-revision-date: 2015-01-18
tags: site-info
license: CC0
---

I like to be transparent about what I do, so I publish all the source
files used to compile this site. The source code repository on GitHub
can be seen by clicking on "[website source]" on any page.  In addition,
for any page that was written in Pandoc markdown, it's also possible to
click "page source" to view that page's source.  Note that some pages,
such as the [tags index], are automatically generated during
compilation, so there is no "page source" other than the code that was
used to build the site (along with templates), which can already be
viewed using "website source".

[website source]: https://github.com/riceissa/issarice.com
[tags index]: _tags/index

I push changes to GitHub more often than I deploy the site.
Therefore, clicking on "website source" or "page source" at the top of a page may or may not reveal the actual source (markdown) file used to generate the HTML---it may instead give you a newer version.
Of course, it's possible to hunt inside the git repository and look for the exact source file, but I figure this is unnecessary except in very exceptional cases.

In the future, I might add the option of linking each deployment with the commit from which it is generated.

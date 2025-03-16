---
title: Newsbeuter
author: Issa Rice
date: 2016-10-26
---

I use [Newsboat](https://newsboat.org/) (formerly called [Newsbeuter](https://web.archive.org/web/20161013081017/http://newsbeuter.org/)) to read RSS and Atom feeds.
On my local machine, I have a [smaller list of
URLs](https://issarice.com/urls.txt) that I regularly check.

My [dotfiles repository contains my `~/.newsbeuter/config`][config].

I have found that after the cache file reaches about 20MB, starting up newsbeuter becomes incredibly slow. To work around this, I create a new cache as follows:

1. I rename the old cache to `cache-YYYY-MM-DD.db`
2. I open newsbeuter and refresh all feeds. This will be stored in a new cache called `cache.db`.
3. This will also give a chance to notice if any feeds are broken (e.g. new URL or the site doesn't exist anymore, which is difficult to tell from simply inactive sites), because those will not have downloaded any articles.
4. I mark all feeds as read in this new cache.
5. I open newsbeuter with the old cache, using the `-c` flag to newsbeuter to select the old cache.
6. I refresh all feeds. Then I process any new articles here. This will be the last time I use this old cache.

Doing step (4) before step (6) is important. Otherwise, in the time between when you process the feeds and when you reload all the feeds again with the new cache, some site may post a new article, which you would erroneously mark as read.

# See also

* [[software I use]] for more about the software I use
* [[Feed]] for this site's feed and feeds for my other online activity

[config]: https://github.com/riceissa/dotfiles/blob/master/.newsbeuter/config

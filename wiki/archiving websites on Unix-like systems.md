---
title: Archiving websites on Unix-like systems
author: Issa Rice
created: 2015-09-22
date: 2015-09-22
status: notes
---

*Note: this page was originally written for the wikiHow article "[How to Archive Websites on Unix Like Systems](http://www.wikihow.com/Archive-Websites-on-Unix-Like-Systems)".
The writing of this page was sponsored by [Vipul Naik](http://vipulnaik.com).*

Link rot (the phenomenon where old websites and pages disappear, making links useless) is a huge problem on the internet.^[See for instance "Archiving URLs" by gwern, [§ Link rot](http://www.gwern.net/Archiving%20URLs#link-rot).]
For readers, it is disappointing when old websites no longer exist.
For writers whose writing on the web is extensively hyperlinked, there is the problem of not being able to verify information when links die.
Whatever the motivation, it is important to be able to archive information on the internet.

## Steps

1. **Understand your motivations for archiving the site.**
It is important to know what you are trying to do in archiving the site.
There are several reasons one might want to archive a website, and these influence your strategy:

    - You may just want an archive of the site to exist, without necessarily caring about who maintains it.
    If this is the case, refer to the step "Check if there are recent archives of the website."
    - You may want to maintain a personal copy (i.e. have the archive locally).
    This might be the case if you can't trust others to keep archives online (e.g. if the site content is copyrighted or illegal, then it may be subject to takedowns, in which case it is safer to have local copies).
    - You may want only the snapshot of the site at a certain point in time.
    This might be the case if you are writing something and want to your citations to be durable; you can just take a snapshot of the site at the time when you used the site as a resource.
    - You may want to continually make snapshots of the site.
    This might be the case if you have an unseemly obsession with the site's content or its owners.
    - You may want only parts of the site (e.g. the pages you cite).

    Note that the above points aren't mutually exclusive (although some are contradictory, like wanting parts of a site versus the whole site); in other words, you may want someone to have an archive, you yourself to keep an archive, and for continual snapshots to be made, all at the same time.

1. **Consider contacting the site owners to obtain dumps.**
It's possible the site owners will oblige by for instance giving you their backups of the site.
However also keep in mind that this will make transparent to them your intentions, so they may react in an unfavorable way (e.g. by password-protecting parts of the site).

1. **Check if there are recent archives of the website.**
It is important to remember that doing work isn't inherently valuable; believing so would be to commit the make-work bias.^[See Wikipedia's "*The Myth of the Rational Voter*", [§ Make-work bias](https://en.wikipedia.org/wiki/The_Myth_of_the_Rational_Voter#Make-work_bias).]
Archiving large websites can often take a lot of time and effort.
If someone else has already done the bulk of the work for you, then there is no need to feel compelled to repeat the task all over again.

    If someone else has made a recent backup of the site, then you might be done (if you just wanted someone else to have a copy) or close to being done (if you just wanted one local snapshot; your task reduces to that of mirroring their backup, which is likely substantially easier than the original task).

    There are several places one should check before proceeding with one's own archiving solution (which is presented in the rest of the steps):

    - [The Archiveteam wiki](http://www.archiveteam.org/index.php?title=Main_Page).
    The Archiveteam is a group of volunteers specializing in archiving websites.
    Their wiki has information on a variety of websites and the progress that has been made toward archiving them.
    Try searching around on the wiki to see what work (if any) has been done.
    The Archiveteam also has [public logs of their IRC (internet relay chat) channels](http://archive.fart.website/bin/irclogger_logs).
    In particular, try searching [\#archiveteam](http://archive.fart.website/bin/irclogger_log_search/archiveteam) and [\#archiveteam-bs](http://archive.fart.website/bin/irclogger_log_search/archiveteam-bs).
    - [The Internet Archive](https://archive.org/).
    The Internet Archive has a massive store of cached versions of various websites.
    See [the guide on Archiveteam's wiki](http://www.archiveteam.org/index.php?title=Internet_Archive#Downloading_from_archive.org) for more information on how to access this.
    - Search [Google](https://www.google.com/).
    Search for the site's name followed by words like "archive" and "mirror".

1. **Check to see if there are any specialized tools to download the site.**
There are sometimes special tools for downloading particular content.
For instance, if you want to download many YouTube videos, there is a tool called [`youtube-dl`](https://github.com/rg3/youtube-dl/).
Many sites also have an API (application programming interface) that allows you to easily programmatically access content.
This is the case with for example reddit, which as [a well-documented API](https://www.reddit.com/dev/api) (though also note that there is already [a fairly comprehensive archive of reddit](http://www.archiveteam.org/index.php?title=Reddit), which was itself created using reddit's API).

1. **Figure out if the site has limit to how many requests you can make in a certain amount of time.**
If no one else has recently archived the site and if there are no specialized tools to archive the site, then you are on your own.
It is good practice to figure out if the site you are targeting has any special rules on how much or how quickly you can download content.
Many sites have clearly-defined rules, which are frequently listed under their terms of service/use.
Even if you don't personally care whether the site wants to limit your access, this is still good to keep in mind, since they may have automatic IP banning (and other measures) in place to prevent people from overloading their servers or "stealing" their content.

    See the step "Use multiple computers or IP addresses to speed up archival" for ways to get around this limit.

1. **Try running a wget command on the site.**
Wget is a program that can download content from the internet, and is included by default on many Unix-like systems.
Sometimes, a single wget command can download all or most of the site.^[See also "[Downloading an Entire Web Site with wget](http://www.linuxjournal.com/content/downloading-entire-web-site-wget)" and "[How can I download an entire website?](https://superuser.com/questions/14403/how-can-i-download-an-entire-website)", which suggest similar flags for wget.]
If this is the case, the task becomes trivial.
However, it is still important to start out the crawl on a page that is likely to link to many other pages, since wget begins at the starting page (called the "seed") and recursively follows internal links.
Locating a sitemap page is ideal, if the site has one.

    Here is a sample command with many useful flags turned on:

    ```{.bash}
    wget --mirror --page-requisites --adjust-extension --convert-links \
        --wait=1 --random-wait --no-clobber -e robots=off \
        http://example.com/sitemap.html
    ```
    
    Be sure to change `http://example.com/sitemap.html` as well as any flags to suit your needs.
    Here are the meanings of the flags, although you should also consult [the official wget documentation](https://www.gnu.org/software/wget/manual/wget.html) (or `info wget`) as well as its manual (type `man wget`):

    - `--mirror` turns on several options favorable to mirroring the site, including recursively following links.
    - `--page-requisites` makes wget download images, stylesheets, and other files that help to produce an appearance faithful to the original.
    - `--adjust-extension` adds the suffix `.html` to HTML files to make them easier to browse locally.
    - `--convert-links` alters linking in downloaded files so they are suitable for local browsing.
    - `--wait=1` forces wget to wait for 1 second between requests (however, see the next option as well).
    - `--random-wait` randomly multiplies the constant from `--wait` for each request so that the download pattern is less suspicious; this plausibly helps prevent being IP banned.
    - `--no-clobber` will preserve local copies of a file instead of overwriting or downloading new copies.
    This is something to consider if the download was stopped in the middle.
    - `-e robots=off` turns off obeying the `robots.txt` file of a site.
    Some people consider it respectful to follow the rules in `robots.txt`, but sometimes whole sites are excluded by `robots.txt` (if the owners put `Disallow: /`).
    The Archiveteam, for one, considers `robots.txt` "[a suicide note](http://www.archiveteam.org/index.php?title=Robots.txt)" and ignores it.

    Consider also using the following options:

    - `--user-agent='Mozilla/5.0 Firefox/40.0'` will set your user agent to appear as if you are using Firefox to access the site.
    This is useful since some sites disallow crawler-like user agents or else display different pages depending on the user agent.
    - `--restrict-file-names=nocontrol` will prevent wget from touching special characters in the URL.
    This often is useful if you are downloading from a site with filenames containing many Unicode characters.^[Brouwer, Andries E. "[wget failure to handle UTF-8 filenames](https://www.win.tue.nl/~aeb/linux/misc/wget.html)".]

    cURL is a similar utility to wget that has similar features.
    On Mac OS X and many BSD systems, cURL is the default downloader instead of wget.
    You may also be interested in finding other programs that are intended for mirroring sites, such as HTTrack.

1. **Examine the website to see if there are any patterns or structure to it.**
If a site cannot be mirrored easily using wget (or similar utility), then it is time for another strategy.
Many sites, such as web forums, have explicit patterns in the URL, such as numbered threads.

    To take an example, we can look at AutoAdmit, a notorious discussion board.
    One of the threads on the site has the URL <http://autoadmit.com/thread.php?thread_id=2993725&mc=12&forum_id=2>.
    However, we might notice that the only crucial number here is the `thread_id`; indeed, navigating to just <http://autoadmit.com/thread.php?thread_id=2993725> shows an essentially identical page.
    We might now try to deduce that the general AutoAdmit URL structure is `http://autoadmit.com/thread.php?thread_id=N`, where *N* is some number; trying several URLs that are instances of this general pattern confirms this.
    After this, it is a matter of looping through all the threads and downloading them; in bash:

    ~~~{.bash}
    for i in {1..2993725}
    do 
        wget -A 'Mozilla/5.0 Firefox/40.0' \
            "http://xoxohth.com/thread.php?thread_id=$i"
        sleep 0.3s
    done
    ~~~

    Of course, the URL structure of AutoAdmit is one of the simplest.
    Other sites, like WordPress blogs, may require e.g. looping through the archive pages after calculating how many pages of posts are in each month (though WordPress blogs also tend to be quite amenable to a naïve crawl).
    There is no general way to go about this, so you might be on your own; searching around on Google can often be very helpful.

1. **If the site has a lot of JavaScript, consider more advanced or tedious techniques for downloading the site.**
In recent times, the web has shifted increasingly toward the heavy use of JavaScript and other interactive elements (sometimes called [DOM scripting](https://en.wikipedia.org/wiki/DOM_scripting)).
While this shift has allowed the web to "rival native applications without a hefty initial download, without an install process, and do so across devices old and new"^[Archibald, Jake. "[Progressive enhancement is still important](https://jakearchibald.com/2013/progressive-enhancement-still-important/)". 2013-07-03.], it is still often the subject of ridicule^[Zawinski, Jamie. "[design](https://www.jwz.org/gruntle/design.html)". 2001.] and criticism^[*cat -v*. "[Everyone has JavaScript, right?](http://harmful.cat-v.org/Blog/2015/04/24/0/)" 2015-04-24.].
In terms of archiving websites, JavaScript and interactive elements are almost always bad news.
There are several strategies of trying to deal with archiving a JavaScript-heavy site.

    One approach is to try to avoid JavaScript entirely.
    Many sites make available RSS or Atom feeds that readers can use to keep up with new content.
    For archivers, web feeds are useful because it is static XML, which makes downloading and processing easy.
    This is especially useful if you want to continue making snapshots of the site: just follow the relevant feeds and you will automatically have what you want (if you're lucky; many sites only show previews on feeds, or the authors may edit the content afterwards, etc., which complicates matters).
    A caveat here is that most web feeds only contain the newest several posts or articles, so retroactively archiving a site may not be possible.

    Other things to look into:

    - In-browser JavaScript to e.g. automatically click on elements
    - PhantomJS and other headless browsers
    - Websites frequently change their UI so keeping up can be hard

1. **If a site is password-protected or otherwise requires authentication, export cookies.**
Sites that require authentication are tricky to access through tools like wget.
However, it is possible to export cookies from graphical browsers like Firefox, then use the cookies to access the sites on wget.
Firefox as the plugin [Export Cookies](https://addons.mozilla.org/en-US/firefox/addon/export-cookies/), which works well.^[gwern. "Archiving URLs", [§ Local caching](http://www.gwern.net/Archiving%20URLs#local-caching). 2015-08-12.]

1. **Use multiple computers or IP addresses to speed up archival.**
If a website can relatively quickly detect crawlers and ban them, one option (besides slowing down) is to connect to the site using multiple IP addresses.
There are multiple ways to do this; here are two: one simple form of having multiple IP addresses is to change your physical location by for instance visiting several cafés or libraries; at each new location, you will have a fresh IP address with which to download from the site.
Another option is to obtain access to multiple computers, by for instance purchasing access to [virtual private servers](https://en.wikipedia.org/wiki/Virtual_private_server).
An advantage of the latter option is that you can have multiple IP addresses that can download *simultaneously*, which will speed up the downloading process instead of simply allowing you to continue the download.
However, note that the latter option often involves spending money, although this can be as low as \$15 per year.
The latter form of downloading is in addition [of questionable legality](https://en.wikipedia.org/wiki/Denial-of-service_attack#Legality).

    It is also possible to use the anonymity network [Tor](https://en.wikipedia.org/wiki/Tor_%28anonymity_network%29) to continually alter your IP by changing exit nodes.
    However, it is highly discouraged to abuse Tor in this way.^[Note, however, that if you want to crawl sites that require Tor (such as certain black-market sites), then the legality of network abuse is probably not a problem, although the legality of the content might be.
    For the curious, a highly detailed guide to using Tor to archive sites is available at gwern's "Black-market archives", [§ How to crawl markets](http://www.gwern.net/Black-market%20archives#how-to-crawl-markets).]

1. **Automate as much as possible.**
If you expect to continue making archives of the site or if the target site is enormous, then it becomes very important to automate as much of the process as possible.

1. **Consider releasing your archives.**
There are several reasons you might want to release your archives to the public.
For one, you have now gone through a time-consuming process of archiving the site; if others also want local copies, then it's likely they would be gratified to find that someone else has done the work for them.
In addition, "lots of copies keep stuff safe", so allowing others to mirror your archives ensures that it is safer against threats like disk failure.
See for instance [the Internet Archive's upload page](https://archive.org/create/) for more.

## Warnings

- Some sites have special links that are meant to be "honeypots" for bots.
These come in several forms, but are usually links that are disguised such that regular users of a site do not click on them, but such that a crawler recursively following all links would follow through on them.
One type of honeypot will blacklist people who click on a particular link^[Manu Chandra Prasad. [Answer to "What are some Web crawler tips to avoid crawler traps?"](https://www.quora.com/What-are-some-Web-crawler-tips-to-avoid-crawler-traps/answer/Manu-Chandra-Prasad-1) 2014-08-22.], while others will trick the crawler into following an infinite loop^[*Stack Overflow*. "[Interview question: Honeypots and web crawlers](https://stackoverflow.com/questions/6780461/interview-question-honeypots-and-web-crawlers)". 2011.] (also called a [spider trap](https://en.wikipedia.org/wiki/Spider_trap)).
- Be careful about sites that link to different query links, so that you might end up with, say, multiple copies of the same page sorted in a different way or using different queries.
- Some sites implement [CAPTCHAs](https://en.wikipedia.org/wiki/CAPTCHA), which make archiving exceedingly difficult.
If you have to solve a lot of CAPTCHAs, consider trying to set up a solver or paying people to solve them for you (there are online services for this).
Doing this, however, is outside the scope of this guide.
- You might run into network issues at home if you download too much.
- You might also cause problems for the site you are targeting (and might even bring it down) if you download too much or too quickly.
This is especially an issue if you use more questionable methods like using multiple computers to conduct downloads or not following the suggested limits for downloading.
- Some sites are bigger than they might at first seem.
One problem you might run into is running out of disk space on your computer.
It is thus important to consider estimating beforehand how large the archive will end up being and to also take steps to minimize the archive size by compressing files.

    The average size of web pages has steadily been increasing^[See for instance [a graph of total transfer size from November 2010 to September 2015](http://httparchive.org/trends.php?s=All&minlabel=Nov+15+2010&maxlabel=Sep+1+2015#bytesTotal&reqTotal).], with the average size being 1600kB in July 2014^[*Website Optimization*. "[Average Web Page Breaks 1600K](http://www.websiteoptimization.com/speed/tweak/average-web-page/)". 2014-07-18.].
    Of course, if you are targeting a specific website, then the sizes of pages on that site could deviate significantly from the figure given above.
    Therefore it is useful look more closely at the specific site in hand.
    In the browser Firefox, you can press `Ctrl`-`Shift`-`q` to bring up the network monitor; you can then press "Reload" to reload the page, after which you can see the total network transfer size.
    (Other browsers may have a similar functionality.)
    Doing this for several pages will give you a good idea of how much space individual pages will occupy.
    The other important information is the total number of pages one expects to download, which also depends a lot on the site.
    Many blogs for instance list the number of posts for each month, so summing these will give a good idea; for more complex sites, this is more difficult.

    As for file compression, [data deduplication](https://en.wikipedia.org/wiki/Data_deduplication) programs like [bup](https://github.com/bup/bup) are excellent especially if you want to continue making snapshots of the site indefinitely.
    Even simply using file compression programs like [xz](https://en.wikipedia.org/wiki/Xz) can dramatically cut disk space since many websites tend to contain a lot of text, which compresses well.
    You may even want to write a script that filters out the site template so you are left with just the content.
    Such a script [exists for Quora](https://github.com/t3nsor/quora-backup#what-the-converter-does), to give one example.


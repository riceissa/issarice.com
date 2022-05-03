---
title: Having a personal website
author: Issa Rice
created: 2014-12-26
date: 2015-08-30
status: notes
belief: possible
---

This page describes my thoughts on having a personal website.
Having a personal website is part of [maintaining one's online presence](http://info.cognitomentoring.org/wiki/Maintaining_your_online_presence).

# Advantages

- Having a single place to store all of one's writings, social media profiles, etc., seems like a good idea
- Helps with being transparent to the world
- Gives a place to write one's opinions that don't fit anywhere else
- Practice with managing a website alone
- May be useful in terms of dating, because here the individual is much more important than the topic.

# Disadvantages

- Inherently egoistic
- Cost (good ones tend to have their own domain names, for instance)
- In general it seems like a bad idea to organize content by author than by topic; liking someone's writing about cooking doesn't say much about liking someone's writing about programming, for instance.
Having, say, one website about cooking (written by various people) and a separate one about programming (written by various people, some of whom may overlap with the cooking website) is much more likely to produce relevant results for everybody.

    Compare the following organizations:

    ````
    .
    ├── A
    │   ├── cook
    │   └── prog
    ├── B
    │   ├── cook1
    │   └── cook2
    └── C
        └── prog
    ````

    versus

    ````
    .
    ├── cook
    │   ├── A
    │   ├── B1
    │   └── B2
    └── prog
        ├── A
        └── C
    ````

    Ceteris paribus, the second organization is preferable because people are more likely to be interested in a topic than a person (?).

    On the other hand there may be some individuals with such compelling personality and such high aesthetic discernment that reading what they write is more important than reading what other people write in the same topic (or rather, such an individual can act as an intellectual guide for showing one what is important).

# Compromise?

One thing to note is that, even given the disadvantages of having one's own website, one can still have a website but primarily post in places other than one's own website, for instance in Facebook groups or on topic-specific websites.
For instance, I post all of my research relevant to [[cause prioritization]] on the [Cause Prioritization Wiki](http://causeprioritization.org/).

In addition, there is often information that cannot fit in other places.
For instance, where does one put information about the account names one uses on various sites, or one's contact information?
Or if one wanted to write monthly or quarterly updates on the progress one makes on various projects, like [gwern](http://www.gwern.net/Changelog) and [Vipul Naik](http://vipulnaik.com/blog/tag/month-in-review/).


# Notes on having mine

- I expect to fairly often rename pages when I'm starting out, since I want pages to use [[canonical naming]] but sometimes I'm careless or don't know what the standard name of a topic is.
Fixing is cheap, though.
For instance, I recently changed the page "Openness and availability of content" to the much simpler "[[Content availability]]".
After the obvious `git mv` and changing of the title in the file itself, I had to look for all the references I made to that page throughout.
This is achieved by:

    ```{.bash}
    egrep -i --color -n "*openness.and.avail*" pages/*
    ```

    The periods are helpful because they catch both the hyphenated links (explicit) or the spaces (used for implicit internal linking).

    Note that in [[Vim]] it's also possible to do `:vim /openness.and.avail/ wiki/*` instead, and then cycle through the matches with `:cn`.

- What are the "essential" parts of a personal website?
In terms of topics, it seems that the following are good to have: a short biography, links to one's work, and contact information.
Indeed, a CV could take care of all three in a sense.

    But what about a more "functional" and engaging site?
    Here are some ideas that I've thought of and have implemented to some degree on this site:

    Search
    :   I've outsourced this to Google since I prefer a static site and cannot implement a better search mechanism on my own anyway.
    By using a plain HTML form, I avoid unnecessary Javascript, which means even people using test-only browsers like ELinks can search directly on this site.

        One trick to making this work is to have a proper sitemap so that search engines can index the whole site.

    Feed
    :   For a site that hopes to continue updating itself over the course of months or years, it seems important to have a standard way to tell people of new content.
    Of course, now there are other ways besides RSS/Atom feeds, like sharing on Facebook or sending out a monthly newsletter (like what gwern does).
    I have also considered that, since this site is already version-controlled through git, that I could simply generate a feed through git; in fact, [GitHub already does this](https://github.com/riceissa/issarice.com/commits/master.atom) (although it is somewhat uninformative since it only includes the commit messages).
    However, it is unclear to me how many people would actually care about the feed; it's not as if they are very useful on a static site like mine anyway.
    On a blog that puts out full posts it is more important to have a feed, but a static site like mine adds content slowly across many pages.
    I *could* treat the site like a software project---and to some extent I already do this---with separate "versions" for each page; then I can call the state of a page a "new major version" once it crosses some threshold.

    List of pages
    :   This comes in two forms: for machines, there is a [sitemap.xml](sitemap.xml) that records all the pages on this site.
    This seems important mostly for search engines.
    It could also aid people trying to scrape the site for whatever use, but considering that I already publish the source files for everything on GitHub, that would probably be easier to deal with than scraping the HTML and then parsing it.

    Redirection
    :   This may just be characteristic of how I write, or perhaps indicative of how much I care about long-term content, but I like to aim for [[canonical naming]] of pages, which means that pages (especially older ones) are renamed, so implementing redirection is very important.
    I often get frustrated when links to pages on personal websites don't work just because the page had moved.
    One question is whether it is better to implement this at the server level or the HTML level.
    I currently use an HTML redirection, which has the advantage of working even on a local machine (for the moment, this is mostly useful for myself when I use the local version as my personal wiki, since the public version on [issarice.com](http://issarice.com) becomes out-of-date over the course of one month---the usual time interval with which I deploy this site).
    I do think server-level redirection is more elegant, however, since the user need not see the redirection page.
    In addition, with server-level redirection even a HEAD request will be able to determine the new location (whereas with HTML redirection a user obtains a 200 response).
    Ideally I would have both so redirection works locally and is elegant once deployed, but I haven't gotten around to this.

    Tag/category organization
    :   I used to have a tags page, as well as pages for individual tags, on this site.
    It works reasonably well for organizing all the content here, although I don't get the sense that it's being used.
    Or to put it another way: since I have to manually tag pages, it isn't clear to me that I'm doing less work by tagging than by creating special "root pages" for certain topics like computing and math and content creation.^[This question also surfaces in redirection: is it better to specify redirection in the pages' metadata (as on this site currently) or have separate pages that contain redirection (as on gitit or MediaWiki)?]
    With the latter, I would have more freedom to organize the structure of the "root page" and add summaries or order by importance (though I can already change the ordering using tags if I implement an `importance:` metadata tag in the YAML header---but this is more work).

        Another phrasing: the question is whether organization should be internal or external to content pages.
        Basically for content that a single individual produces for their personal website, things like the semantic web are probably overkill.
        Categories are also unsatisfying because one always wants to know the most important pages *within* categories.

- In terms of generating the site and as part of one's workflow, here are some other points.

    Automatic generation
    :   Using a static site generator or makefile to generate the site seems essential (if one wants a static site) since it's cumbersome to manually manage everything if the site is larger than a handful of pages.

    Partial generation
    :   When the site grows, it becomes slow to generate the whole site each time.
    Either caching results or using a makefile to determine dependencies is important, especially when writing pages (since I often like to view the output as I write so as to ensure there are no syntax errors in the markdown source^[Using a [lint](!w Lint (software)) could also be useful here.]).

    A single layer of processing
    :   There are static sites that use two layers of processing e.g. writing an m4 file that contains a "body" portion that is written in markdown.
    This seems unnecessarily complicated and reasoning about two layers of character escapes is painful.[^layers]

    Templating
    :   Manually writing and looking at HTML is painful, so write in markdown and use templating to convert to HTML.
    When using templates, having metadata in a YAML header is useful.

[^layers]: This is the case with many things, such as two layers of escaped backslashes when matching a single literal backslash using a regular expression in Python (i.e. the regular expression is `"\\\\"` because Python sees this as `\\` and to match a literal backslash one must escape it---but thankfully Python has raw strings so `r"\\"` also works).
Or consider the case of two nested tmux sessions, where one session is running locally, from which one uses ssh to connect to a remote machine and attaches to a remote tmux session.
If the prefix keys are identical in both sessions, say, `C`-`b`, then one must type *four* instances of `C`-`b` to send a literal `C`-`b` to the remote shell: two to send a literal `C`-`b` to the *local* tmux session, which turns into a prefix on the *remote* session, then two more to make *that* literal.

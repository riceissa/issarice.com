---
title: Project ideas
author: Issa Rice
created: 2017-11-20
date: 2017-11-20
bigtable: yes
# documentkind:
# status:
# belief:
---

This page catalogs some project ideas I have that have not been implemented yet.
My hope is that I or somebody else can eventually complete these.

I am writing this page for various reasons. Some of these are to:

* Give people a better idea of what I might work on next. I like to make myself
  predictable so others can plan according to a good model of how I will act.
* Tell the world the things I want to see. I think the things in this list are
  useful to the world, and it doesn't need to be me who does it. It would be
  great to find out that somebody saw a sufficient need based partly on this
  page and decided to make something. This is similar to [request for startups](https://www.ycombinator.com/rfs/ "“Requests for Startups”. Y Combinator. September 2016. Retrieved November 26, 2017.") or
  [charities](https://blog.givewell.org/2015/10/15/charities-wed-like-to-see/ "Elie Hassenfeld. “Charities we'd like to see”. GiveWell. March 1, 2017. Retrieved November 26, 2017.").
* Track the things I want to work on. I often think of things I'd like to work on while daydreaming
  or working on something else. If I don't put an effort into recording things
  to work on (and training myself to notice needs that exist in the world), I
  might forget.
* Clean out some tasks from [orgmode](emacs). I have a backlog of tasks in orgmode. A
  lot of these aren't for me to immediately work on, and they kind of clutter
  up my orgmode file. If the tasks can be done by somebody that isn't me, why not keep that portion of the todo list public?
* Give potential funders an idea of what they can fund. If I already want to
  see something in the world, a modest amount of funding can shift my
  priorities to work on that thing.
* Find potential collaborators. Especially for the larger projects, it can be
  helpful to have other interested parties on board to divide up the work.
* Give people a better idea of where I'm coming from. This is a broader point
  that applies to other efforts I have made to be more [transparent](individual-transparency).

The information in the table is intended
to be helpful in scanning the list and orienting oneself, but is only
suggestive; it is often the case that as a project proceeds, details become
clearer or change.

Effort can be rated on the following scale. In each case I assume I am the one
performing the task (skill-sets vary considerably across people so it would be difficult to provide a good estimate for the general population). I have a good programming and writing ability but I am not
exceptional by any means and I expect many people can perform at a comparable
level or even better depending on their expertise. (As a side note, even on the
project idea generation front I don't think I am exceptional -- in fact this
page so far is quite rudimentary and biased toward things I find personally
interesting rather than most useful to the world -- so I think other people can
and should also be more transparent about projects they want to see.) Days here
refer to work days, so 8 hour periods. Of course, [planning fallacy](https://en.wikipedia.org/wiki/Planning_fallacy "“Planning fallacy”. English Wikipedia. Retrieved November 26, 2017.") makes it difficult to estimate how long a project will take,
but I list some things I have actually produced in the past to ground myself on
the kinds of tasks and their timescales.

0
:   Up to one day (8 hours) of effort. These are relatively quick things that can be
done. Examples are [Timeline of Carl Shulman publications](https://timelines.issarice.com/index.php?title=Timeline_of_Carl_Shulman_publications&oldid=15618) as of July 13, 2017 (about 7 hours of work) and some
global health pages like Amanda Glassman (I think).

1
:   More than one day and up to two weeks (8--80 hours) of effort. Examples on this level are
[timeline of MIRI](https://timelines.issarice.com/index.php?title=Timeline_of_Machine_Intelligence_Research_Institute&oldid=15715) as of July 15, 2017 (75 hours) at the upper end. I think [timeline of AMF](https://timelines.issarice.com/index.php?title=Timeline_of_Against_Malaria_Foundation&oldid=13553) (33 hours) around the middle.

2
:   More than two weeks (80 hours) of effort. Examples here are my total work so far on
the [donations list site](https://donations.vipulnaik.com/) (as of November 2017) and my total work on [Devec wiki](https://devec.subwiki.org/wiki/Main_Page) (as of November 2017).

This is not an exhaustive list of project ideas. In particular if I have
already done some work on a project and just want to make general improvements
to it, I won't usually list it here (*all* projects can be improved to varying
extents, and it would be tedious to list them all). If I have specific
improvements, I will try to list them here.

# Table

|Project|Description|Effort|Venue|Format|
|----------------|------------------------------------|-----:|--------|--------|
|Pandoc scripting guide|A guide to scripting with Pandoc. Probably with Lua filters now that Pandoc 2.0 is out. It would be good to cover common frustrations like how to debug your filter, some common real-life filters, and so on.|1||Prose with code samples|
|Naturalism table|A table summarizing naturalistic worldviews. The columns can be "author", "view on consciousness", "view on free will", "view on time", etc. In other words, the "[mysterious questions](http://lesswrong.com/lw/iu/mysterious_answers_to_mysterious_questions/ "Eliezer Yudkowsky. “Mysterious Answers to Mysterious Questions”. LessWrong. August 25, 2007. Retrieved November 20, 2017.")". The authors that I would like to be covered are Yudkowsky, Tomasik, Gary Drescher, and Dennett. The cells of the table can contain the works by the author that discusses the views.|0||Table|
|Table on multiverses/Big World theories|Rows could be the multiverses: many worlds interpretation, modal realism, etc. See [Tegmark's classification](https://en.wikipedia.org/wiki/Multiverse#Max_Tegmark.27s_four_levels) for example. The columns could be things like "how big?", "implications for altruism", "proponents".|1|No particular venue in mind|Table|
|Timeline of felicifia|I think quite a few EAs came from felicifia-related online presence, including Brian Tomasik, Pablo Stafforini, Ryan Carey, and Peter Hurford. Carl Shulman also has an account on the forums. It would be interesting to document its rise and decline.|1|Timelines Wiki|Timeline|
|Guide to working on wiki-like pages with Vim|I've developed some ideas about how to work on wiki-like pages in [Vim](), which is distinct from working on related program source code. Some useful options for this are `'isfname'`, `'includeexpr'`, and `'suffixesadd'`. Setting these to good values will allow for traveling between related pages on the wiki more easily. As a case study, MediaWiki could be used. Also see the [wikilink script](https://github.com/riceissa/contentcreation/blob/master/wikilink.vim) I use on one wiki.|0|Vim Tips Wiki|Prose with code samples|
|List of mysterious answers to mysterious questions|I think one reason I like the {Yudkowsky, Tomasik, Drescher, Dennett} approach to dealing with philosophy is that they treat all of the "big questions" or "mysterious questions" at once, rather than just treating one thing in isolation. But it seems like Drescher doesn't talk much about the problem of personal identity, and Yudkowsky's blog posts only pose it as a *question* (about the anthropic trilemma) rather than as an answer. I think having these all in one table would be nice, since I am tabulating a bunch these days. The columns could be "mysterious question", "mysterious answer", "resolution/dissolved answer".|1||Table|
|Timeline of web analytics|There is a stub for this [here](https://timelines.issarice.com/wiki/Timeline_of_web_analytics).|1|Timelines Wiki|Timeline|
|Improve the [Staycation § Benefits](https://en.wikipedia.org/wiki/Staycation#Benefits)|Some benefits can be framed as ways to avoid the downsides of international travel (jet lag, illness, and so on). I think Bryan Caplan discusses staycation in his kids book.|0|Wikipedia|Prose|
|A consciousness wiki|A wiki systematically exploring issues related to consciousness. See more ideas [here](https://github.com/riceissa/issarice.com/tree/master/external/consciousness.issarice.com). The wiki can have an altruism/crucial considerations bent like [Luke Muehlhauser's moral patienthood report](https://www.openphilanthropy.org/2017-report-consciousness-and-moral-patienthood "Luke Muehlhauser. “2017 Report on Consciousness and Moral Patienthood”. Open Philanthropy Project. August 5, 2017. Retrieved November 20, 2017."). It can also apply the ideas to e.g. cryonics.|2|Separate wiki|Prose and tables|
|Improve [pdftextfmt](https://github.com/riceissa/pdftextfmt) to handle more PDF madness|It's already fine for simple linebreaks and hyphens, but "word breaks" need to be handled manually (i.e. when there's a space within a word that's not supposed to be there). MuPDF also inserts strange lines containing just the character "f". Ligatures also often mess up the output.|2|GitHub|Code|
|Improve [Timeline of online dating services](https://timelines.issarice.com/wiki/Timeline_of_online_dating_services)|For example add info from [this piece](https://www.huffingtonpost.com/susie-lee/timeline-online-dating-fr_b_9228040.html). I also have a private discussion about more columns to add to the timeline (so find that before starting on this).|1|Timelines Wiki|Timeline|
|Research some trends in font usage|For instance, both Lato and Merriweather have become very popular in recent years. It seems like Minion Pro has supplanted Times New Roman as the new "boring default font". Default fonts for MS Word etc. have changed as well.|1|No particular venue in mind|Prose with maybe tables or graphs|
|Rationality blogroll graph|A graph showing which rationality community blogs have which blogs in their blogroll. To see if any patterns in e.g. subcommunities can be observed, and to uncover potentially interesting blogs.|1|GitHub for the code, no particular venue in mind for a writeup|Code with figures and maybe a writeup|
|Some sort of program to check for arbitrary web page updates|There is [urlwatch](https://github.com/thp/urlwatch), which seems fine, but I would like the diff in the form of an RSS or Atom feed so that I can look over the updates in the same way I look over new blog post updates. A hack can probably be created fairly easily.|0|GitHub|Code|
|Timeline of Eliezer Yudkowsky publications|See [Timeline of Carl Shulman publications](https://timelines.issarice.com/wiki/Timeline_of_Carl_Shulman_publications) for a similar timeline that could be used as a model.|0|Timelines Wiki|Timeline|
|Robin Hanson summary|A summary of Robin Hanson's "key ideas" like *homo hypocritus*, "X is not about Y", signaling, great filter, etc., would be nice. This would allow people to "catch up" on his thinking without having to spend a ton of time reading through poorly organized blog posts. Each of these might also need pages on the LessWrong Wiki, but that's a separate task.|1|LessWrong Wiki?|Structured prose|
|Inadequate equilibria|A wiki page summarizing the concept and giving a list of examples.|0|LessWrong Wiki|Prose|
|Hostile wife phenomenon|A wiki page describing hostile wife phenomenon and summarizing what has been said about it. There are quite a few articles out there about this, but no summary as far as I can tell.|0|LessWrong Wiki|Prose|
|Amazon Lightsail|Similar pages exist for e.g. [AWS Lambda](https://en.wikipedia.org/wiki/AWS_Lambda).|0|Wikipedia|Prose|
|Guide on choosing data storage formats|I have especially small-to-medium scales in mind. When should one use a CSV/TSV file? When should one store data as a SQL file or dump? There's a lot of intuition one would need to transmit.|1|wikiHow?|Prose|
|Wikipedia pages for AGI projects|Specifically those AGI projects listed in [Seth Baum's paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3070741). Some of these projects already have Wikipedia pages but many do not. Writing each page should take less than a day of work, so each page would be a '0' in terms of effort, but since I don't want to list each page here, I'll record the effort as a '2'.|2|Wikipedia|Prose|
|Research Japanese input method engines|This might just be my ignorance, but in my experience there is no really good free software Japanese IME. All of the ones I have tried work reasonably well but a lot of their kanji suggestions are way off or not present in their dictionaries. Even mozc, developed by Google, seems to be some inferior free software version of the actual IME they use for Google's keyboard. Is there really nothing really good out there? Could one of the existing engines fairly easily brought to a higher quality by assembling better dictionaries?|1|No particular venue in mind|Prose|
|Timelines of machine learning pedagogy|This timeline wouldn't cover cutting-edge research, but rather learning resources dedicated to machine learning. Some things to cover: various subreddits, Ng's ML courses, Distill, various textbooks.|1|Timelines Wiki|Timeline|
|DeWitt clause|A page explaining DeWitt clauses, some examples, its history, etc. There is a tiny amount of info on [David DeWitt's page](https://en.wikipedia.org/wiki/David_DeWitt).|0|Wikipedia|Prose|
|Better conversion from MediaWiki to Markdown|I think Pandoc is the best converter at the moment, but it doesn't handle templates, which are used a lot in MediaWiki documents. Maybe writing a Pandoc filter to handle templates can get decent output. Or maybe some method involving going from MediaWiki to some intermediate format, then to Markdown would work.|1|No particular venue in mind|Prose/code|
|Mapping out EA/impact-focused projects|Two projects that were released in 2017 are [EA Work Club](http://www.eawork.club/) (announced [December 2017](http://effective-altruism.com/ea/1i7/introducing_ea_work_club_highimpact_jobs_and_side/)) and the [Diaspora Project Map](https://namespace.obormot.net/Main/DiasporaProjectMap) (announced [December 2017](https://www.lesserwrong.com/posts/fDhy3PXvJ6sjBJQB8/show-lw-diaspora-project-map-and-preregistration-database)). However, I think both of these suffer from the "make it and they will come" mindset. While the tools look decent, without data, I think people are unwilling to contribute their own data. So the idea would be to go out and find more projects and add them to one of these or add them to some other list of projects (I think .impact also had a hackpad containing a bunch of projects at one point).|1|EA Work Club/Diaspora Project Map/Other|Structured data|
|Various contributions to [Cause Prioritization Wiki](https://causeprioritization.org/)|The wiki has been mostly dormant for a few years, and at some point I would like to return to writing more pages for it. I might list some specific area for improvement in this list at some point|2|Cause Prioritization Wiki|Various|
|Magical reality fluid|A page about what it is and any progress made on understanding it. Some links: [1](https://www.facebook.com/alyssamvance/posts/10205442165803261), [1](https://www.google.com/search?q=%22magical%20reality%20fluid%22), [3](http://lesswrong.com/lw/ua/the_level_above_mine/8bww).|1|LessWrong Wiki|Prose|
|Psycho-conservatism|A wiki page about the topic, covering proponents, major beliefs, books, blogs, groups within the broader [rationality community]() that discuss it, etc.|0|LessWrong Wiki|Prose|

# External links

- [My Quora questions](https://www.quora.com/profile/Issa-Rice/questions "“Issa Rice's Questions”. Quora. Retrieved November 26, 2017.").
  Not all of my questions are "serious" questions, but they are things I
  have wondered about or think others have wondered about, so I would
  appreciate responses.
- [New article pool](https://github.com/vipulnaik/contractwork/blob/master/new-article-pool.mediawiki)
  by Vipul Naik lists article ideas
- [Luke Muehlhauser's 2011 list of posts he would like to write](http://lesswrong.com/lw/85d/11_less_wrong_articles_i_probably_will_never_have/)
- [orthonormal's 2012 list of posts they would like to write](http://lesswrong.com/lw/cnl/posts_id_like_to_write_includes_poll/)

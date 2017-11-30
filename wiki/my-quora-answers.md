---
title: My Quora answers
author: Issa Rice
date: 2017-11-30
---

# Introduction

My main contributions to [Quora]() are through my questions, but I don't think my answers are especially bad, so here they are.

Starting in November 2017, I have begun storing my answers as separate text
files in a [directory on my website repository](https://github.com/riceissa/issarice.com/tree/master/external/quora.com).
The answer text there is produced by copy-pasting from Quora's rich text editor
(i.e. the editor automatically converts the rich text formatting to a plain
text equivalent, which I can place in a text file).
This change means I don't have to manually convert each answer to Markdown,
which is good because it means less work for me.

Reverse chronological order

# How many edits have been made to Wikipedia?

[Mirror](https://www.quora.com/How-many-edits-have-been-made-to-Wikipedia/answer/Issa-Rice)

For **total edits**, see [Special:Statistics](https://en.wikipedia.org/wiki/Special:Statistics).

For the **current month**, I recommend Erik Zachte’s [“English Wikipedia at a glance”](https://stats.wikimedia.org/EN/SummaryEN.htm)page, which has pretty plots for other metrics as well.

For **edits by month**, see the [Wikipedia Statistics table for this](https://stats.wikimedia.org/EN/TablesDatabaseEdits.htm). (Warning: large page that might take a while to load.)

# Does MediaWiki have a git-bisect equivalent?

[Mirror](https://www.quora.com/Does-MediaWiki-have-a-git-bisect-equivalent/answer/Issa-Rice)

MediaWiki itself does not have a git-bisect equivalent, but there are various web-based tools with varying amounts of flexibility that implement the most important parts of git-bisect. The two that seem to work are:

-   [User:Flominator/WikiBlame - Wikipedia](https://en.wikipedia.org/wiki/User:Flominator/WikiBlame), which is available from the “Revision history search” link of the revision history page of each article. This tools does both linear and binary search. The source seems to be available on GitHub: [FlominatorTM/wikiblame](https://github.com/FlominatorTM/wikiblame).
-   [Article blamer](https://tools.wmflabs.org/xtools/blame/), which is part of X!’s tools. This tool seems to do a linear search [x-tools/xtools](https://github.com/x-tools/xtools-legacy/blob/c49a5e3db99b941393564a0a2f6a37c0e7d49f34/public_html/blame/index.php#L53-L82).

See also [Wikipedia:Tools § Finding the responsible user](https://en.wikipedia.org/wiki/Wikipedia:Tools#Finding_the_responsible_user).

# Will all Dropbox URLs become link rot? (December 2016)

[Mirror](https://www.quora.com/Will-all-Dropbox-URLs-become-link-rot-December-2016/answer/Issa-Rice)

“All” is too strong of a quantifier, but something close to it can happen.

As far as I can tell, a Dropbox link can stop working for any of the following reasons:

-   Dropbox goes out of business (remember [Ubuntu One](http://archiveteam.org/index.php?title=Ubuntu_One)?).
-   The sharing link uses [db.tt](http://db.tt/) (Dropbox’s own URL shortener) and Dropbox somehow drops support for it.
-   The file associated with the link is copyrighted, the person who shared the file isn’t legally allowed to distribute it, and Dropbox decides to delete the file or prevent sharing ([Can I share files with non-Dropbox users?](https://www.dropbox.com/en/help/20)).
-   The person who shared the file deleted the file or folder containing the file ([Why did my shared link stop working?](https://www.dropbox.com/en/help/45)).
-   The person who shared the file set an expiration date for the shared link ([How can I set an expiration for a shared link?](https://www.dropbox.com/help/5888)).
-   Dropbox bans the link for generating too much traffic ([Banned links or file requests](https://www.dropbox.com/help/4204)), though this is temporary.
-   The account of the person who shared the file becomes inactive. Dropbox considers an account inactive after 12 months of no sign-ins, and deletes files 90 days after that ([I received an email about an inactive Dropbox account—what do I need to do?](https://www.dropbox.com/en/help/9080)).
-   A subset of the cases in the above bullet point is if the user dies and nobody claims the account afterwards ([Can I access the Dropbox account of someone who has passed away?](https://www.dropbox.com/en/help/488)).

In other words, unless a user takes special steps to keep the shared file available, to ensure the account is preserved after death, and so forth, the link will eventually stop working.

I’m not aware of any studies of link rot that are specific to Dropbox.

# Why isn't effective altruism called effective utilitarianism?

[Mirror](https://www.quora.com/Why-isnt-effective-altruism-called-effective-utilitarianism/answer/Issa-Rice)

[Linchuan](https://www.quora.com/profile/Linchuan-Zhang) is quite right about point 1. The 2014 EA survey [https://eahub.org/sites/effectiv...](https://eahub.org/sites/effectivealtruismhub.com/files/survey/2014/results-and-analysis.pdf) shows that about 70% of respondents hold consequentialist moral philosophies. The 2015 EA survey [https://eahub.org/sites/eahub.or...](https://eahub.org/sites/eahub.org/files/SurveyReport2015.pdf) breaks down consequentialism into utilitarian and non-utilitarian types, and finds that 56% of respondents are utilitarian. It would therefore be strange to call the movement “effective utilitarianism”.

# Is there anyone else "like Gwern"?

[Mirror](https://www.quora.com/Is-there-anyone-else-like-Gwern/answer/Issa-Rice)

A2A.

It depends on what qualities you are interested in, but some people who are similar in various ways are:

-   muflax
-   Carl Shulman (see my comment on this question)
-   Scott Alexander (also listed in the answer by Anonymous)

# What should someone do if their dog develops romantic feelings towards them?

[Mirror](https://www.quora.com/What-should-someone-do-if-their-dog-develops-romantic-feelings-towards-them/answer/Issa-Rice)

Nothing.

# What is your review of University of Washington?

[Mirror](https://www.quora.com/What-is-your-review-of-University-of-Washington/answer/Issa-Rice)

★

My experience at UW has been worse than my experience at my high school, which you can read here: [Issa Rice's answer to What is your review of Inglemoor High School?](https://www.quora.com/What-is-your-review-of-Inglemoor-High-School/answer/Issa-Rice)

About 99.99% of the positive value I derived from UW came from befriending Ethan Bashkansky. And yes, I really do mean it in the sense that if you divide all of the positive value I derived from UW into 10,000 equal parts, then all but one is due to Ethan.

# How common is it for people to check Alex K. Chen's questions page after they talk to him (to see if he asked q’s in response to their interaction)?

[Mirror](https://www.quora.com/How-common-is-it-for-people-to-check-Alex-K-Chens-questions-page-after-they-talk-to-him-to-see-if-he-asked-q%E2%80%99s-in-response-to-their-interaction/answer/Issa-Rice)

I have done this a few times (say, between 2 and 10 times). Given that I’ve known Alex for over two years (and have interacted with him frequently over those years), this isn’t a very common occurrence.

# Are there URLs one cannot send over Facebook messenger due to its broken URL parsing?

[Mirror](https://www.quora.com/Are-there-URLs-one-cannot-send-over-Facebook-messenger-due-to-its-broken-URL-parsing/answer/Issa-Rice)

This answer has moved to [URL parsing]().

# What is epistemic soundness?

[Mirror](https://www.quora.com/What-is-epistemic-soundness/answer/Issa-Rice)

In LessWrong/rationality parlance, “epistemic soundness” means the same
thing as “epistemic rationality”. To quote the LW Wiki:

> Epistemic rationality is that part of rationality which involves
> achieving accurate beliefs about the world. It involves
> [updating](https://wiki.lesswrong.com/wiki/Updating)
> on receiving new
> [evidence](https://wiki.lesswrong.com/wiki/Evidence),
> mitigating cognitive biases, and examining why you believe what you
> believe. It can be seen as a form of instrumental rationality in which
> knowledge and truth are goals in themselves, whereas in other forms of
> instrumental rationality, knowledge and truth are only potential aids
> to achieving goals. Someone practising instrumental rationality might
> even find falsehood useful.

([Rationality -
Lesswrongwiki](https://wiki.lesswrong.com/wiki/Rationality#Epistemic_rationality))

Further, Eliezer Yudkowsky says:

> **Epistemic rationality**: believing, and updating on evidence, so as
> to systematically improve the correspondence between [your map and the
> territory](http://yudkowsky.net/rational/the-simple-truth).
> The art of obtaining beliefs that correspond to reality as closely as
> possible. This correspondence is commonly termed "truth" or
> "accuracy", and we're happy to call it that.

([What Do We Mean By
"Rationality"?](http://lesswrong.com/lw/31/what_do_we_mean_by_rationality/))

The idea of “epistemic soundness” has over time become associated with
certain other ideas like betting on beliefs and having good calibration
([Calibrated probability
assessment](https://en.wikipedia.org/wiki/Calibrated_probability_assessment)).

# Does Alex K. Chen come off as socially awkward when he asks people too many questions IRL?

[Mirror](https://www.quora.com/Does-Alex-K-Chen-come-off-as-socially-awkward-when-he-asks-people-too-many-questions-IRL/answer/Issa-Rice)

Yes (though I’ve only met Alex a few times in person).

This isn’t to say it’s a bad thing (in fact, I very much enjoy watching Alex ask people questions).

# If I incorrectly included my failure-to-file penalty on line 79 of Form 1040, how should I amend this?

[Mirror](https://www.quora.com/If-I-incorrectly-included-my-failure-to-file-penalty-on-line-79-of-Form-1040-how-should-I-amend-this/answer/Issa-Rice)

You should fill in Form 843, as described here: [How should Form 1040 be
amended if error was introduced on lines 78 and
79?](http://money.stackexchange.com/a/66829/44690)

# What are all of the websites Vipul Naik has created or contributed significantly to?

[Mirror](https://www.quora.com/What-are-all-of-the-websites-Vipul-Naik-has-created-or-contributed-significantly-to/answer/Issa-Rice)

Here are the ones I know about:

-   [What Is Research?](https://whatisresearch.wordpress.com/), his old math
    research blog
-   [Olympiads and I](http://olympiadsandi.blogspot.com/), his old Olympiads
    blog
-   [The Web Crawler](http://spideroftheweb.blogspot.com/), another old Blogger
    blog that only has one post
-   [Vipul Naik](http://vipulnaik.com/), his current personal site
-   [Vipul Naik's Home Page: Main
    Page](https://web.archive.org/web/20130518071716/http://www.cmi.ac.in/%7Evipul/),
    his old personal/academic site from CMI
-   [Vipul Naik's Home Page -- University of
    Chicago](https://web.archive.org/web/20120516191221/http://math.uchicago.edu/%7Evipul),
    his academic site from UChicago
-   [Thinking Beyond
    Competition](https://thinkingbeyondcompetition.wordpress.com/), his old
    ethics/philosophy/econ blog
-   [Wikipedia Views](http://wikipediaviews.org/), a site to tabulate pageviews
    of Wikipedia pages
-   [Vipul’s Classroom](http://www.vipulsclassroom.org/), the site for his math
    YouTube videos
-   [Open Borders: The Case](http://openborders.info/), the open borders
    advocacy site he started
-   [Subwiki](http://subwiki.org/wiki/Main_Page), the site where he puts all of
    his subject-specific wikis. Out of these, the most developed is
    [Groupprops](http://groupprops.subwiki.org/wiki/Main_Page), the group
    theory wiki
-   [Cognito Mentoring](http://cognitomentoring.org/), an experimental
    mentoring service he started with Jonah Sinick, which also has the [Cognito
    Mentoring Info Wiki](http://info.cognitomentoring.org/wiki/Main_Page)
-   [Wikipedia](http://vipulnaik.com/wikipedia/) (various topics)
-   See also [Service](http://vipulnaik.com/service/) for his various online
    profiles

# I'm now 18 and heading into my senior year of high school next year and still a virgin. Should I be worried?

[Mirror](https://www.quora.com/Im-now-18-and-heading-into-my-senior-year-of-high-school-next-year-and-still-a-virgin-Should-I-be-worried/answer/Issa-Rice)

No.

# What are Issa Rice's favorite tvtropes articles?

[Mirror](https://www.quora.com/What-are-Issa-Rices-favorite-tvtropes-articles/answer/Issa-Rice)

I haven’t explored TV Tropes that much so it’s hard to say. Here are
some articles I’ve referred to that I liked:

-   [Ordinary High-School Student - TV
    Tropes](http://tvtropes.org/pmwiki/pmwiki.php/Main/OrdinaryHighSchoolStudent)
-   [Tempting Fate - TV
    Tropes](http://tvtropes.org/pmwiki/pmwiki.php/Main/TemptingFate)
-   [Tsundere - TV
    Tropes](http://tvtropes.org/pmwiki/pmwiki.php/Main/Tsundere)
-   [Harem Genre - TV
    Tropes](http://tvtropes.org/pmwiki/pmwiki.php/Main/HaremGenre)
-   [Love Tropes - TV
    Tropes](http://tvtropes.org/pmwiki/pmwiki.php/Main/LoveTropes)
    (not an article, but I found it fascinating to look through)

I find TV Tropes useful because while each idea is quite obvious in
hindsight, I often hadn’t verbalized it until I encountered the term and
article for it.

# Is IRS Form 1040 a one-pass form?

[Mirror](https://www.quora.com/Is-IRS-Form-1040-a-one-pass-form/answer/Issa-Rice)

As of the 2015 tax year, no, Form 1040 is not a one-pass form. Indeed,
the instructions for line 78 contain the following:

> Include any estimated tax penalty from line 79 in the amount you enter
> on line 78.

[https://www.irs.gov/pub/irs-pdf/...](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf)

Line 78 is calculated using lines 63 and 74. Then line 79 is entered.
However, if the amount on line 79 is nonzero, line 78 must now be
updated, so the form cannot be one-pass. Of course, one might still
anticipate this and fill in line 79 first and then use lines 63, 74, and
79 to arrive at line 78, but now this breaks the usual flow of the form
(although it's possible that this is precisely what the instructions
suggest, and I think IRS forms in general don't have linear flow anyway;
so you have at least an undocumented line dependency on the form itself,
and then at least one of nonlinear flow or multiple-pass).

# What are some good essays about computer science and programming?

[Mirror](https://www.quora.com/What-are-some-good-essays-about-computer-science-and-programming/answer/Issa-Rice)

[https://dl.dropboxusercontent.co...](https://web.archive.org/web/20150109054504/https://dl.dropboxusercontent.com/u/85192141/1996-hoare.pdf)
("How Did Software Get So Reliable Without Proof?")

# What are the best books to learn Vim in a month?

[Mirror](https://www.quora.com/What-are-the-best-books-to-learn-Vim-in-a-month/answer/Issa-Rice)

My recommendation would be to start with vimtutor, then do a combination
of the following as you see fit (which might take more than a month):

-   Watch some [Vimcasts](http://vimcasts.org/).
-   As you discover things you wish you could do in Vim, try googling
    for keywords; this will usually lead you to relevant [Vim Tips
    Wiki](http://vim.wikia.com/wiki/Vim_Tips_Wiki) or
    StackOverflow pages.
-   Read *Practical Vim* by Drew Neil (who coincidentally also does
    Vimcasts); I think this book does an excellent job of getting people
    to think in a "Vim mindset". I especially like the realistic
    examples and multiple approaches presented for solving a single
    editing problem. However, I should warn you that there is a high
    degree of references to future points in the book, i.e. if you read
    the book straight through, you may encounter a lot of things that
    have not been explicitly covered in the book yet. In other words
    this book might be more useful at a more advanced stage in one's
    Vim learning.
-   Read the help pages. I don't necessarily find a lot of Unix manual
    pages helpful (often googling provides a better explanation), but I
    really like Vim's help pages. They don't cover everything in the
    best way, but often invoking the help page on a topic is faster than
    going to one's browser and looking an answer up, especially if one
    has already encountered the material before and is only looking for
    a quick memory jog.

# What would Issa Rice do if he were a millionaire?

[Mirror](https://www.quora.com/What-would-Issa-Rice-do-if-he-were-a-millionaire/answer/Issa-Rice)

This would largely depend on where on the millionaire spectrum I was. A
single million dollars isn't very much money, and wouldn't influence my
actions very much (for instance, I would still complete my undergraduate
degree, get a job, etc.). Most likely I would just save it and invest it
accordingly so as to have a comfortable financial buffer. Having a large
financial buffer, in turn, will allow me to take on bigger and riskier
bets (e.g. quitting a typical programming job in order to do [cause
prioritization research](http://causeprioritization.org/) full-time \[disclosure: I run the site\]).

In terms of selfish investments, [What would Alex K. Chen do if he were
a
millionaire?](https://www.quora.com/What-would-Alex-K-Chen-do-if-he-were-a-millionaire)
has some good ideas. In general, I would lean toward spending money on
ergonomics and longevity-related purchases. In addition to the points in
Alex's answer, I might in addition consider more strongly cryonics, for
example.

I would also probably donate more; [GiveWell](http://www.givewell.org/)'s
recommendations are a good start.

With even more money, see [A Long-run perspective on strategic cause selection
and
philanthropy](http://www.effective-altruism.com/ea/5g/a_longrun_perspective_on_strategic_cause/).

# How does gwern manage his backups?

[Mirror](https://www.quora.com/How-does-gwern-manage-his-backups/answer/Issa-Rice)

He explains this in a footnote ([Page on
gwern.net](http://www.gwern.net/Archiving%20URLs#fn1)):


> I use [duplicity](http://duplicity.nongnu.org/) &
> [rdiff-backup](http://www.nongnu.org/rdiff-backup/) to
> backup my entire home directory to a cheap 1.5TB hard drive (bought
> from Newegg using forre.st’s [“Storage Analysis - GB/\$ for different
> sizes and media”](http://forre.st/storage#hdd)
> price-chart); a limited selection of folders are backed up to
> [Tarsnap](http://www.tarsnap.com/).
> 
> I used to semiannually tar up my important folders, add
> [PAR2](http://en.wikipedia.org/wiki/PAR2) redundancy,
> and burn them to DVD, but that’s no longer really feasible; if I ever
> get a Blu-ray burner, I’ll resume WORM backups. (Magnetic media
> doesn’t strike me as reliable over many decades, and it would ease my
> mind to have optical backups.)

# What makes so many aspies attracted to effective altruism?

[Mirror](https://www.quora.com/What-makes-so-many-aspies-attracted-to-effective-altruism/answer/Issa-Rice)

I'm not sure it's the case that there are a lot of people with Asperger
syndrome in effective altruism (EA); this would be the case in any
movement of sufficient size. I think the burden of proof is on the
person asking the question to provide evidence for what they are seeing.
Having interacted with the EA community for over a year, I don't get
this impression, though I haven't actually gone out and surveyed how
many people with Asperger syndrome are associated with EA. I would also
note that "Asperger syndrome" gets slapped onto movements on occasion
without evidence. Libertarianism and in particular the open borders
movement has had this happen; see [Asperger’s syndrome at Open Borders:
The Case](http://openborders.info/aspergers-syndrome/)
for more. As Evan at Open Borders: The Case writes (in [Autism Can’t
Explain Away Open Borders
Arguments](http://openborders.info/blog/autism-cant-explain-away-open-borders-arguments/)),
"the project of associating political positions \[or social movements!\]
with mental disorders is probably not a wise undertaking in the first
place".

To the extent that people with Asperger syndrome seem over-represented
in EA, I offer several reasons. Note that I have a low level of
confidence in these explanations, which are more akin to
rationalizations (which might still be useful to verbalize). One is that
people involved with the tech industry are over-represented in EA (see
[What happened to all the
non-programmers?](http://www.benkuhn.net/nonprog)), and
if we grant that people involved in tech are more likely to have
Asperger syndrome (see for instance [Peter Thiel on the Future of
Innovation — Conversations with
Tyler](https://medium.com/conversations-with-tyler/peter-thiel-on-the-future-of-innovation-77628a43c0dd)),
then it might seem like many people with Asperger syndrome are also in
EA.

Another related idea is that both people with Asperger syndrome and
those in effective altruism compartmentalize less relative to the
general population. Effective altruism is well-known for preferring
quantitative measures of effectiveness as well as explicit verbal
reasoning of actions (so they might be more likely to change their
beliefs when faced with new evidence). This is also a stereotype of
people with Asperger syndrome (who are thought to be bad at nonverbal
communication, are thought to be savants who are good at quantitative
subjects, and so on).

# What do people think of the ticket price of EA Global?

[Mirror](https://www.quora.com/What-do-people-think-of-the-ticket-price-of-EA-Global/answer/Issa-Rice)

The price of the ticket seems reasonable. Some high school clubs force
students to pay about the same price for conferences for what I think is
much less valuable (in terms of the long-term impact on one's life and
the world), not that one should be basing one's decisions on a
comparison with high school club conferences.

One thing that I think the effective altruism movement and the EA Global
people in particular don't do a good job of is explaining exactly why
it's a good idea to spend several hundred dollars to meet each other in
person. Posts like [Why you should attend EA Global and (some) other
conferences](http://lesswrong.com/lw/mhf/why_you_should_attend_ea_global_and_some_other/)
seem like an excuse to advertise the event, not an actual argument (and
I think does a disservice to LessWrong, which prides itself on being
rational).

I'd guess that some people are dissuaded from attending by the ticket
price. In my case, this wasn't the biggest factor: as a student, I might
have been able to obtain one of the EA Global scholarships, and even if
I hadn't I had some people offer to pay for some of the cost. (I chose
not to attend this year mostly to work on some personal projects and
because travelling is stressful for me.)

# What scraping software does gwern use to web-scrape forums?

[Mirror](https://www.quora.com/What-scraping-software-does-gwern-use-to-web-scrape-forums/answer/Issa-Rice)

I think he just uses wget; see e.g. [Evolution forums mirror/scrapes torrent
released •
/r/DarkNetMarkets](https://www.reddit.com/r/DarkNetMarkets/comments/2zps7q/evolution_forums_mirrorscrapes_torrent_released/).
For more details, see [Page on
gwern.net](http://www.gwern.net/Black-market%20archives#how-to-crawl-markets).

For why he doesn't use something more advanced, see [I once tried using
HTTrack, but I found it was doing too much magic under the
ho...](https://news.ycombinator.com/item?id=9899286).

# Why do some people use Hakyll to generate webpages?

[Mirror](https://www.quora.com/Why-do-some-people-use-Hakyll-to-generate-webpages/answer/Issa-Rice)

I suspect this is because Hakyll is the flagship static site generator
that uses Haskell. On the one hand, there are many reasons people prefer
static site generators to more complex content management systems like
WordPress and MediaWiki (security, speed, etc.). On the other hand,
there are people who are enthusiastic about using Haskell to do many
things (in fact, Quora seems to have many such Haskell programmers). If
one is at the intersection of these two things and wants a website or
blog, it's relatively natural to use Hakyll.

From what I've read, many people often start out using another static
site generator like Jekyll (i.e. they're already sold on the benefits of
static site generators) but then move on to Hakyll, usually because they
want to experiment with Haskell. See [Switching from Jekyll to
Hakyll](http://mark.reid.name/blog/switching-to-hakyll.html),
[The Switch to
Hakyll](http://www.blaenkdenum.com/posts/the-switch-to-hakyll/),
[Switching this site from Jekyll to
Hakyll](http://cliffle.com/article/2015/05/09/hakyll/),
[Blog now powered by
Hakyll](http://dannysu.com/2012/07/26/hakyll-blog/), and
so on.

# If gwern.net could be turned into a book, how many pages would it contain altogether?

[Mirror](https://www.quora.com/If-gwern-net-could-be-turned-into-a-book-how-many-pages-would-it-contain-altogether/answer/Issa-Rice)

Using his [source repo](https://github.com/gwern/gwern.net) as of today, I'm
getting:

```bash
$ cat *.page | wc -w | sed 's/$/\/500\*1.1/' | bc3747.7
```

pages based on the [assumption](http://wordstopages.com/) that there are 500
words per 1.1 pages.

There are a few things to keep in mind, however:

-   The above does not capture the pages gwern deleted.
-   The unix command wc cannot distinguish actual (prose) words from
    everything else (like equations, source code, tables, metadata,
    other hidden markup, etc.). So for instance tables would probably
    take up even more space than what was calculated above.
-   gwern quotes others extensively when writing, which might result in
    copyright issues if he were to actually publish.
-   The words-to-pages conversion is just for paragraphs, so if we
    account for all the headings, blank spaces (after each page when
    printed), etc., then the page count could be even higher.
-   There might be something else I haven't thought of that could skew
    the result (since 4000 pages seems like *a lot*).

# What has a higher chance of lasting into the 2030s-2040s: LessWrong or gwern.net?

[Mirror](https://www.quora.com/What-has-a-higher-chance-of-lasting-into-the-2030s-2040s-LessWrong-or-gwern-net/answer/Issa-Rice)

In terms of the existence of the website (domain name and all), I would
agree with [Vipul](https://www.quora.com/profile/Vipul-Naik) that
LessWrong has a better chance of lasting. However in terms of the
survival of the content, I'd say gwern's site has a *much better shot*.
Everything on the site, along with all the changes, are up on GitHub for
anyone to clone. Indeed, at the moment there are 7 forks on GitHub
already:
[gwern/gwern.net](https://github.com/gwern/gwern.net).
If it ever goes down, all one would need to do is use the cloned repo
and compile the site using Hakyll (which is free software).

Take the content that's been produced so far. What percent of LessWrong
content is available now, out of everything that's been produced so far?
Definitely not 100%, for comments and even whole posts have been
deleted. And if we take into account *usability* of the site, then it's
*even lower*, because some external links no longer exist. In contrast,
I'd say just about everything that's ever been on gwern's site (sans
Disqus comments, which are not too substantial anyway) is still
available today; even his deleted pages (like those on homelessness and
masturbation) are still available today, as long as you know where to
look. Moreover, gwern is good about backing up external sources (he
includes PDFs he links to in the git repo, for instance, and also runs
scripts to save pages he links to), so usability in the future should be
higher as well.

Now, there's also the size of the site that we have to consider. gwern's
site is much smaller, so it's easier for projects like the Internet
Archive to keep a copy of everything. In contrast, LessWrong is a much
larger site with more pages (which are also dynamic, unlike gwern's
static pages), so I doubt the Internet Archive has a full copy.

Dynamic content (mentioned above) is indeed *much* harder to backup, and
in any case the only way to fully do that would be if the LessWrong
sysadmins released database dumps (very unlikely).

Now, the word "lasting" in the question is a bit ambiguous. So far I've
talked about "lasting" in terms of readable content, site usability, and
so on. But another important aspect of "lasting" for a long time is the
community aspect. And here it's a no brainer: LessWrong has already
steadily been dying due to all the most prolific contributors leaving
the site. In contrast, gwern's site didn't really have any "community"
to begin with, so not much is lost even if gwern stops adding to the
site (I mean, gwern still slowly adds to the site, but all the most
notable pages were already written years back), whereas with LessWrong,
interacting with other readers is a fundamental aspect of the site.

# What is Gwern's personality type (MBTI, Big 5, etc.)?

[Mirror](https://www.quora.com/What-is-Gwerns-personality-type-MBTI-Big-5-etc/answer/Issa-Rice)

MBTI:


> No \[I don't know mine\], and I don't care. MBTI is not founded on any
> data, is unreliable, has little predictive value, exists because it
> is so lucrative, and is ignored by mainstream psychology because of
> all its problems in favor of Big Five (which I do provide).


(From [Page on
gwern.net](http://www.gwern.net/Links#comment-853463775))

Big 5:


> My scores on the “Big 5 Personality Inventory”,
> [short](http://www.gwern.net/docs/personal/2011-gwern-yourmorals.org/bigfive_process.html)/long
> [1](http://www.gwern.net/docs/personal/2012-gwern-personalityproject.html)/[2](http://www.gwern.net/docs/personal/2012-gwern-personalityproject-2.html)/[3](http://www.gwern.net/docs/personal/2013-gwern-personalityproject.html):
>
> 1.  [Openness to
>     Experience](http://en.wikipedia.org/wiki/Openness%20to%20Experience):
>     high (short) or 87/87th
>     [percentile](http://en.wikipedia.org/wiki/percentile) (long)
> 2.  [Conscientiousness](http://en.wikipedia.org/wiki/Conscientiousness%23Personality%20models):
>     medium or 64/69th
> 3.  [Extraversion](http://en.wikipedia.org/wiki/Extraversion):
>     low or 6/7th percentile
> 4.  [Agreeableness](http://en.wikipedia.org/wiki/Agreeableness):
>     medium-low or 3/3rd percentile
> 5.  [Neuroticism](http://en.wikipedia.org/wiki/Neuroticism):
>     medium-low or 16/13th percentile


(From [Page on
gwern.net](http://www.gwern.net/Links#personality))

# What is your review of Inglemoor High School?

[Mirror](https://www.quora.com/What-is-your-review-of-Inglemoor-High-School/answer/Issa-Rice)

★

My experience at Inglemoor (especially the first two years) was much
worse than my experience at Northshore Junior High, probably because of
my increased self-awareness (i.e. objectively it was probably better
than junior high, as [Anonymous' answer](https://www.quora.com/What-is-your-review-of-Inglemoor-High-School/answers/13780648)
states). Having moved to the US from Japan at the beginning of 4th
grade, it was finally in 10th grade at Inglemoor that my level of
English caught up to that of my peers and surpassed it; because of this
(and in general being essentially at the top of my class academically
all through high school), I was finally able to comprehend how little
academic success in high school means, how little self-awareness my
peers had, how poor of an environment Inglemoor is for personal growth,
and so on. In other words, my
[isolation](http://info.cognitomentoring.org/wiki/Dealing_with_intellectual_isolation)
and alienation from my peers (despite interacting more with them than
during junior high), as well as my [anger at the
world](https://en.wikipedia.org/wiki/The_Catcher_in_the_Rye),
probably peaked during 10th and 11th grade.

Either at the end of junior high or the beginning of high school, I
discovered some of my early intellectual heroes like Bertrand Russell
and Noam Chomsky, whose works and biographical information I read
throughout high school. I also discovered
[LessWrong](http://lesswrong.com/), which really opened
my imagination to what sorts of ideas and intellectual conversations are
possible. Both in high school and in retrospect, I think these sources
of ideas and information have had a much bigger impact on my
intellectual ability and growth as a person than anything I learned in
high school. In fact, it seems like in high school there is in general a
tendency to stifle intellectual and personal growth \[1\]. So I think I
was really lucky that my propensity for spending large amounts of time
on the internet allowed me to discover these.

I'm glad I read some of the works of literature we read in IB English
(especially Joyce's *Dubliners*), though I don't think the amount of
time spent on them was justified. I also think the two-year IB History
was a particularly good class; see [Anonymous' answer to What are the
best classes at
Inglemoor?](https://www.quora.com/What-are-the-best-classes-at-Inglemoor/answers/4315032)
for more.

It's important to keep in mind though, that Inglemoor is probably much
better than the average high school in the US, and in particular is
probably indistinguishable from other IB high schools located in
Liberal, upper-middle class areas in the US.

\=\=\=\=\=

\[1\] See for instance [College Observations: Freshman, Quarter
1](http://michael0x2a.com/blog/college-observations-freshman-quarter-1):


> There’s a lot more religious/political people at UW, passing out
> pamphlets and such. This is in stark contrast to high school, where
> religion and politics (religion, especially) were almost taboo and
> were confined mostly to the Christian/debate clubs and a few
> discussions in history classes.
>
> Similarly, people are much more frank about sex and sexuality, and
> seem to take it as a fact of life.


Also in general the infantilization of teens combined with the
uninspiring students and teachers (for the most part), means few
opportunities for growth.

# How does Gwern from http://gwern.net manage his website?

[Mirror](https://www.quora.com/How-does-Gwern-from-http-gwern-net-manage-his-website/answer/Issa-Rice)

This is explained at length on his site's [About
page](http://www.gwern.net/About). The most relevant bits are in his
[Colophon](http://www.gwern.net/About#colophon).  Essentially, he writes
everything in Pandoc markdown and compiles the site using Hakyll, a static site
generator.

# What is your review of Northshore Junior High School?

[Mirror](https://www.quora.com/What-is-your-review-of-Northshore-Junior-High-School/answer/Issa-Rice)

★

I agree with much of [Anonymous' answer to What is your review of
Northshore Junior High
School?](https://www.quora.com/What-is-your-review-of-Northshore-Junior-High-School/answers/9520496),
though my experience probably wasn't as bad.

I made exactly zero friends at NJH, though I had friends at the [Seattle
Japanese School](https://www.quora.com/topic/Seattle-Japanese-School)
(and my friends from the Japanese school used to tease me all the time
about how I had no friends at NJH). Yeah, it was lonely, but probably
not as bad as having to interact with a lot of the kids that attended
the school. I only later found out about some of the crazy drama that
occurred during my time there—and I'm extremely glad I wasn't involved
in any of it (this also applies to high school, though I had one close
friend in high school).

The teachers at NJH are extremely uninspiring, and I actually struggle
to come up with examples of teachers I liked. Even my high school had a
few good teachers.

Probably the thing I remember most from my time in junior high is
reading alone at the library every day after lunch. For a while I
repeatedly read *Ender's Game* and *Ender's Shadow*. I also remember
just thinking alone.

I didn't place into honors English and social studies coming into 7th
grade, but at the end of 8th grade, the principal (probably at the
suggestion of my English and history teachers at the time) invited me to
apply to join honors English and social studies for 9th grade, so for
one year I got to sit in with the honors humanities kids. They were
probably smarter kids, but I don't recall noticing a huge difference.
(And now I just laugh at the anti-intellectualism of almost everyone
from junior high and high school, to the point where it's just comical
that I wasn't in those honors classes the first two years.)

As for math, I placed into honors math in 7th grade, but then took an
accelerated course in the summer after 7th grade to skip one more year
\[1\]. So in 8th grade I was in 9th grade honors math, and by 9th grade
I got to go to Inglemoor High School in the mornings for math. Going to
high school in 9th grade was somewhat interesting because due to some
scheduling problem, we got to miss an hour of class (in my case science)
at the junior high on one day while also having an hour to do nothing
\[2\] on another day (or something like this; I forget the details).

As for learning, it's hard to say. NJH taught "form writing" in English,
which is basically a really formulaic version of 5 paragraph essays, so
I probably didn't learn to write very well in junior high. I probably
did pick up a lot of random stuff though. In general the learning
experience seemed very inefficient due to all the social competitions
(including inane comparisons about who is smarter, etc.) that were going
on.

\=\=\=\=\=

\[1\]: This actually turned out to be a really interesting experience.
Until I took the math 13X honors calculus sequence at University of
Washington in my first year of college, this summer class was the *only*
time I was ever challenged in math in school.

\[2\]: We were actually supposed to TA for some teachers who had their
prep time during this hour, but I just didn't go.

# How many Taylor Swift songs are about breakups?

[Mirror](https://www.quora.com/How-many-Taylor-Swift-songs-are-about-breakups/answer/Issa-Rice)

See also [\[SELF\] How many of Taylor Swift's songs are about heartbreak.. •
/r/theydidthemath](https://www.reddit.com/r/theydidthemath/comments/2gdvle/self_how_many_of_taylor_swifts_songs_are_about/)

# Where can I find archives of the LessWrong IRC?

[Mirror](https://www.quora.com/Where-can-I-find-archives-of-the-LessWrong-IRC/answer/Issa-Rice)

The LessWrong IRC has no public logs. Therefore you'll have to find someone who
is willing to give you logs. I know that gwern, for one, has been keeping
extensive logs, but I doubt he's willing to give them out (seeing that he's a
moderator of the channel).

# What do University of Washington students think of By George?

[Mirror](https://www.quora.com/What-do-University-of-Washington-students-think-of-By-George/answer/Issa-Rice)

I really like studying here at night since it's open very late (you can
get food until 1am on most nights, but the periphery is open 24/7) and
is much less crowded than Odegaard (except for maybe Monday and Tuesday
night of finals week). As [Andrew J.
Ho](https://www.quora.com/profile/Andrew-J-Ho) mentioned, the chairs are
rather uncomfortable though. Also there aren't very many power sockets.
However all things considered, it's a decent place. I usually like to
come here around 10pm and then move to Odegaard when it gets less
crowded.

# What is the "anonymity problem" in online dating?

[Mirror](https://www.quora.com/What-is-the-anonymity-problem-in-online-dating/answer/Issa-Rice)

I originally asked this question because [Vipul
Naik](https://www.quora.com/profile/Vipul-Naik) used the phrase in a
conversation. It turns out he may just have invented the phrase himself,
so there may not be a well-known "anonymity problem". In any case, I'll
try to explain what he seemed to be getting at.

He quoted [my answer to Why has LinkedIn had substantially greater
success and impact than
OKCupid?](https://www.quora.com/Why-has-LinkedIn-had-substantially-greater-success-and-impact-than-OkCupid/answer/Issa-Rice):


> The anonymity on OKCupid, in contrast to people using their real names
> on LinkedIn, could also be a factor \[of difference in success\]:
> information on LinkedIn has the ability to be reused elsewhere or have
> a better chance of having an impact in other places (whereas with
> OKCupid, only your (potential) partners will ever care about the
> information, and it won't be linked to your real identity). (Thanks to
> Vipul Naik for this idea.)


In other words, online dating may suffer in various respects because it
is often conducted anonymously. We can even see this in articles like
[Anonymity: The Joker in Online
Dating](http://mariashriver.com/blog/2014/10/anonymity-the-joker-in-online-dating-ken-solin/):


> Anonymity contributes disproportionately to boomer dating
> dissatisfaction. While integrity may top most boomers’ lists of
> desirable qualities, it’s at odds with some boomers’ online dating
> behavior. *“If I don’t really know this man or woman I’m contacting,
> why should I be on my best behavior? If I meet a person who’s a
> stranger  and I’m disappointed, why should I care about how I treat
> that person?  I’ll never see this person again, so what difference
> does it make if I’m  rude?”* This myopia is reminiscent of Internet
> tough guys who use anonymity as a shield.


In general, using one's real identity does tend to mean there will be
consequences for one's actions, and this can promote more long-term
thinking, which may be desirable; see my [Long-term
thinking](http://issarice.com/long-term-thinking) for
more. The fact that online dating often doesn't have this means people
can be short-sighted.

# Can Google Photos automatically detect (and delete) photos I upload that might have nudity in them?

[Mirror](https://www.quora.com/Can-Google-Photos-automatically-detect-and-delete-photos-I-upload-that-might-have-nudity-in-them/answer/Issa-Rice)

Maybe in the future, but I don't think that's the case at the moment.
From their content policy page:


> We depend heavily upon users to let us know about content that may
> violate our policies. After we are notified of a potential policy
> violation, we may review the content and take action, including
> restricting access to the content, removing the content, and limiting
> or terminating a user’s access to Google products. Note that we may
> make exceptions to these policies based on artistic, educational, or
> documentary considerations, or when there are other substantial
> benefits to the public from not taking action.


([Policies for Google+, Hangouts &
Photos](https://www.google.com/intl/en-US/+/policy/content.html))

Also do note that some sexually explicit material is allowed (bolding
mine):


> Do not distribute sexually explicit or pornographic material. Do not
> drive traffic to commercial pornography sites.
>
> **We do allow naturalistic and documentary depictions of nudity (such
> as an image of a breastfeeding infant), as well as depictions of
> nudity that serve a clear educational, scientific, or artistic
> purpose.**
>
> Note that your profile photo cannot include mature or offensive
> content. For example, do not use a photo that is a close-up of a
> person’s buttocks or cleavage.

# What do University of Washington students think of the "Impeach Obama" people near the quad, red square, etc.?

[Mirror](https://www.quora.com/What-do-University-of-Washington-students-think-of-the-Impeach-Obama-people-near-the-quad-red-square-etc/answer/Issa-Rice)

I don't think of them, and try to avoid them. Once I was wearing a sunhat and
sunglasses (to protect myself from the sun), when one of them spoke at me,
"Hey, you from the FBI or what?" or something similar.

# What would Andrew J. Ho do if he were a millionaire?

[Mirror](https://www.quora.com/What-would-Andrew-J-Ho-do-if-he-were-a-millionaire/answer/Issa-Rice)

Hard to say, but he has made references to ruling over certain populations (not
sure if this is possible for a mere millionaire), funding certain types of
people to do work, and not having to do tedious work himself. In addition,
given his interest in a variety of intellectual activies including writing,
mathematics, and reading literature, I would presume he'd pursue those to a
greater extent than has been possible for him so far.

# I've completed my freshman year of university with a 4.0 GPA, yet I feel something is missing. How do I make college the most fulfilling, enlightening experience possible?

[Mirror](https://www.quora.com/Ive-completed-my-freshman-year-of-university-with-a-4-0-GPA-yet-I-feel-something-is-missing-How-do-I-make-college-the-most-fulfilling-enlightening-experience-possible/answer/Issa-Rice)

*This answer is quoted in full at [Some thoughts on college education]().*

# Is it secure for me to log into my Internet accounts on the KCLS library computers?

[Mirror](https://www.quora.com/Is-it-secure-for-me-to-log-into-my-Internet-accounts-on-the-KCLS-library-computers/answer/Issa-Rice)

Possibly (but why risk it?). In general it's bad practice to log into
internet accounts from a device you do not own (since you never know
what software/hardware keyloggers they could be running). With public
library computers, it's even worse than, say, a friend's computer,
because anyone could have physical access to the machine. Moreover last
time I was at a KCLS library, they were still running something like
Windows XP, which makes me trust those machines even less.

If you need to be scared away from logging in, read something like
[Hardware keyloggers discovered at public
libraries](https://nakedsecurity.sophos.com/2011/02/14/hardware-keyloggers-discovered-public-libraries/)
or [Page on
mit.edu](http://tech.mit.edu/V125/PDF/V125-N20.pdf).

But if you must log in, enable something like two-factor authentication
(for services that have this), and change your password immediately
afterwards. Also most people have smartphones now so it's better to just
use the Wi-Fi network from your own device instead of touching any of
the public machines (and if you have a VPN, then that's even better).

# What is a list of questions that could be asked about any Nobel laureate on Quora?

[Mirror](https://www.quora.com/What-is-a-list-of-questions-that-could-be-asked-about-any-Nobel-laureate-on-Quora/answer/Issa-Rice)

Here are some:

-   Was the decision to give X the Nobel prize justified?
-   Who were the other people being considered for the Nobel prize
    during the year X was selected?
-   How many times was X considered for the Nobel prize before getting
    it?
-   Did X auction off their Nobel prize medal only to have it returned
    to them for free?
-   What is the most controversial thing X has said?
-   Did X produce their best work before or after getting the Nobel
    prize?
-   When should I put X in my dead pool?
-   To what extent does X have a cult following?
-   How many books have been written about X?
-   Is X mostly just known in their home country, or are they famous
    internationally?
-   Does X use Quora?
-   Is X on any social media sites?
-   What is it like to do marijuana/MDMA/psilocybin/LSD with X?
-   What is it like to watch a lecture by X while on
    marijuana/MDMA/psilocybin/LSD?
-   Is [Alex K. Chen](https://www.quora.com/profile/Alex-K-Chen)
    obsessed with X?
-   How well does X speak English?
-   Is X a good role-model?
-   How would X approach grad school admissions?
-   If X were born today, would they have a shot at getting the Nobel
    prize again?
-   What are the best anecdotes about X?
-   How many views does the Wikipedia page for X have?
-   How many followers would X have if they were on Quora?
-   What do experts in the field in which X got the Nobel prize think of
    X?
-   What would people think of X if X had the opposite gender?

# Why hasn't Issa Rice posted to Quora of late?

[Mirror](https://www.quora.com/Why-hasnt-Issa-Rice-posted-to-Quora-of-late/answer/Issa-Rice)

I was edit-banned for a month for asking "[What is it like to rape each
member of your
family?](https://www.quora.com/unanswered/What-is-it-like-to-rape-each-member-of-your-family)",
which was marked as "possibly insincere". The ban actually lasted for a
full two weeks after the one-month period, for reasons I'm not sure
about.

# How do I cope with losing a long-time friend who I love?

[Mirror](https://www.quora.com/How-do-I-cope-with-losing-a-long-time-friend-who-I-love/answer/Issa-Rice); the version here has since been edited

It's unprofessional of them to refuse communication, but there isn't
anything you can do about that. Their refusal to communicate is a sign
that you shouldn't bother with them. In general, I find loneliness
preferable to interaction with unprofessional, immoral, uninteresting,
or otherwise unfit people. Finding the right people is difficult, but
until then, grit your teeth and march on. The sooner your learn this,
the better.

See also [Raman Shah's answer to What are the most difficult things people have to learn in their 20s?](https://www.quora.com/What-are-the-most-difficult-and-useful-things-people-have-to-learn-in-their-20s/answer/Raman-Shah):

> How little most former friends, significant others, bosses, students,
> and colleagues care about you once they've gotten what they want.
> Conversely, how precious the few people are who still care once you
> can't give them anything.

Also, although the situation here doesn't directly mirror what Caplan
describes in “[The Futility of Quarreling When There Is No Surplus to Divide](http://econlog.econlib.org/archives/2014/02/the_futility_of.html)”,
read that post and in particular this quote:

> The only way out is to calm down and admit that bad matches aren't
> anyone's fault. When two people want incompatible things, they should
> politely say goodbye and move on with their lives.

See also this quote from *[The 7 Habits of Highly Effective People](!w)*, which isn't about romance but is still relevant:

> So let’s work for a Win/Win. Let’s really hammer it out. And if we
> can’t find it, then let’s agree that we won’t make a deal at all. It
> would be better not to deal than to live with a decision that wasn’t
> right for us both.

# One year on, how has Cognito Mentoring benefited you?

[Mirror](https://www.quora.com/One-year-on-how-has-Cognito-Mentoring-benefited-you/answer/Issa-Rice)

[This answer is mostly a quote from my [Cognito Mentoring]() page, so it's easier just to look at that.
If you're curious about how the page was when I quoted it in the answer, have a look at [the exact commit](https://raw.githubusercontent.com/riceissa/issarice.com/9ff14ea008aa49cba8db6e2459cdf9150fcd2a0c/pages/cognito-mentoring.md).]

# Are the Vipul Naik-related questions on Quora cultish?

[Mirror](https://www.quora.com/Are-the-Vipul-Naik-related-questions-on-Quora-cultish/answer/Issa-Rice)

I don't think so.
I think I've asked a lot of the questions about Vipul, but I do this for some others like Alex K. Chen and Andrew Ho as well.
See also [You're Calling \*Who\* A Cult Leader?](http://lesswrong.com/lw/4d/youre_calling_who_a_cult_leader/)

# What are some good questions that could be asked on Quora for any animal species?

[Mirror](https://www.quora.com/What-are-some-good-questions-that-could-be-asked-on-Quora-for-any-animal-species/answer/Issa-Rice)

Some others:

-   What is it like to have sex with X?
-   What is it like to give X marijuana
    edibles/MDMA/ketamine/psilocybin/LSD (or any combination thereof)?
-   What is it like to be on marijuana/MDMA/ketamine/psilocybin/LSD (or
    any combination thereof) while holding/petting/having sex with/being
    eaten by/eating X?
-   What is it like to use X as a verb?
-   What is it like to watch X mate/reproduce?
-   What is it like to work with X in a lab environment (as peers)?
-   What is it like to work with X in a lab environment (where X is the
    subject)?
-   What is it like to fall in love with X?
-   What is it like to marry X?
-   Do kakapo and X get along?
-   Can X cry?
-   What is it like to watch a movie where X is a main character?
-   Why hasn't [Alex K.  Chen](https://www.quora.com/Alex-K-Chen) asked questions
    about X yet?
-   What does it mean if X is your spirit animal?
-   What is it like to talk to X?
-   What are the funniest YouTube videos about X?
-   What does it mean if X is your best friend?
-   Do stuffed animals of X tend to be cute?
-   Does X make you go eeeeeee?
-   What is it like to pet X?
-   What can X do that humans can't?
-   What should everybody know about X?
-   Can I convince X to go vegan and wear sunglasses and a wide-brimmed
    hat?
-   What does Alex K. Chen think of X?
-   What does [Vipul Naik](https://www.quora.com/Vipul-Naik) think of X?
-   What does [Andrew J.  Ho](https://www.quora.com/Andrew-J-Ho) think of X?
-   What does X think of [Marc Bodnick](https://www.quora.com/Marc-Bodnick) "always" being
    on Quora?
-   What is it like to cuddle with X?
-   What Disney characters are X?
-   How many X does it take to screw in a lightbulb?
-   Why did X cross the road?
-   My daughter wants X for her Christmas present, but I don't know
    where to find one. I've also heard things like Y about X, which
    worries me. I'm also Z years old and feel like I've wasted all my
    life, and would really just like to give my daughter something she
    wants. What do I do?


# Why has LinkedIn had substantially greater success and impact than OKCupid?

[Mirror](https://www.quora.com/Why-has-LinkedIn-had-substantially-greater-success-and-impact-than-OKCupid/answer/Issa-Rice)

I think it's helpful to consider (1) whether the business-oriented
nature of LinkedIn has given it an edge over OKCupid, a dating site; and
(2) if there is anything specifically LinkedIn has been doing right that
OKCupid hasn't.

It's not too hard to find evidence that online dating has a lot of
stigma attached to it. Here is just one article on the topic: [Online dating still stigmatized despite popularity, success](http://thegazette.com/2014/03/16/online-dating-still-stigmatized-despite-popularity-sucess/).

Online dating still stigmatized despite popularity, success. In general,
social networking sites tend to have many more users and much higher
Alexa rankings than dating sites (see [List of social networking websites](https://en.wikipedia.org/wiki/List_of_social_networking_websites)
and [Comparison of online dating websites](https://en.wikipedia.org/wiki/Comparison_of_online_dating_websites)).
If we restrict the social networking sites to just business-oriented
sites, then we find that LinkedIn has 300 million users (2013), Viadeo
has 55 million users (2013), and XING about 11 million users. In
contrast, some of the more popular online dating-focused sites like
Badoo, Match.com, and Zoosk have as many as 197 million (2013), 96
million (2010), and 50 million users (2011), respectively. So the
numbers seem rather comparable, which means LinkedIn may just be
particularly good, and OKCupid, with only 5.6 million active users
(2010), may just be particularly bad, in this respect. (Though note here
that OKCupid is the only site reporting in terms of *active* users, and
not registered users. I'm also not an expert on the other dating sites
so I can't say if OKCupid is doing something wrong.)

Other heuristics besides the stigma that one might come up with:

-   After a suitable match has been found on a dating website, the users
    may delete their profiles. I remember reading about an unfortunate
    couple who had met on OKCupid, deleted their profiles, and now
    wished to look at them again, for a sense of nostalgia -- but hadn't
    made backups of their profiles. Businesses, on the other hand, do
    not care if you have a LinkedIn profile even while you are working
    for them. (Thanks to Vipul Naik for clarifying this point with me.)
-   I get the impression that many people are officially (e.g. schools)
    or unofficially (e.g. peer pressure) *encouraged* to create LinkedIn
    profiles, which probably leads to more users, which just doesn't
    happen for dating sites (although in some social circles, creating
    online dating profiles may be encouraged somewhat).
-   The anonymity on OKCupid, in contrast to people using their real
    names on LinkedIn, could also be a factor: information on LinkedIn
    has the ability to be reused elsewhere or have a better chance of
    having an impact in other places (whereas with OKCupid, only your
    (potential) partners will ever care about the information, and it
    won't be linked to your real identity). (Thanks to Vipul Naik for
    this idea.)


# How did you discover Cognito Mentoring?

[Mirror](https://www.quora.com/How-did-you-discover-Cognito-Mentoring/answer/Issa-Rice)

I saw Jonah's original post on Less Wrong. I was a bit scared to contact them on my own so I had a friend also contact them.

# Who is interested in a December 2014 Quora meetup in Seattle?

[Mirror](https://www.quora.com/Who-is-interested-in-a-December-2014-Quora-meetup-in-Seattle/answer/Issa-Rice)

Sure, I'd be interested.

# What does Issa Rice think of Andrew J. Ho's recent questions as of 4 November 2014?

[Mirror](https://www.quora.com/What-does-Issa-Rice-think-of-Quora-Users-recent-questions-as-of-4-November-2014/answer/Issa-Rice)

I find them all to be very amusing. [What is it like to secretly mix in small amounts of your own blood with cookie dough that you intend on baking into cookies for your significant other?](https://www.quora.com/What-is-it-like-to-secretly-mix-in-small-amounts-of-your-own-blood-with-cookie-dough-that-you-intend-on-baking-into-cookies-for-your-significant-other)
in particular seems especially creative, and is giving me ideas about
other questions I could ask.

I can never tell whether your relationship questions are completely
serious or a deliberate attempt to be humorous and mocking of similar
Quora questions.

Your Asian-American questions are also highly relevant to my own
situation so I appreciate you asking those.


# What would Noam Chomsky think of unschooling?

[Mirror](https://www.quora.com/What-would-Noam-Chomsky-think-of-unschooling/answer/Issa-Rice)

Chomsky hated high school, so presumably his opinion of unschooling is
more positive (though it's not quite clear what type of education he
considers ideal; I suppose that he will in general support any education
system that promotes creative thinking, which includes the Deweyite
school he attended, which is mentioned in the quotes below). Some quotes
will illustrate his thinking (all emphasis mine):

> I had friends but **I hated high school**. [...] My parents worked, so
> from about 18 months I’ve been in school. But up until 8th  grade I
> was in an experimental school run by Temple University.  Progressive
> school, and that was great. But in high school I had to go  to an
> actual ‘high school’. There was one academic high school were I  was,
> one for boys, one for girls, and it was very rigid. For the  teachers
> it was a dream because the kids there wanted to go to college,  so the
> teachers could sit back and relax. But it was very rigid, you  know,
> tests, grades. I had never had grades before, never knew I was a  good
> student, nothing. And it was a bore. **It was a black hole**.

(From [The Secret of Noam: A Chomsky Interview](http://brightestyoungthings.com/articles/the-secret-of-noam-a-chomsky-interview.htm))

> There are huge efforts that do go into making people, to borrow Adam
> Smith's phrase, "as stupid and ignorant as it is possible for a human
> being to be." **A lot of the educational system is designed for that,
> if you think about it, it's designed for obedience and passivity**.
> From childhood, a lot of it is designed to prevent people from being
> independent and creative. **If you're independent-minded in school,
> you're probably going to get into trouble very early on**. That's not
> the trait that's being preferred or cultivated.

(From [Education is Ignorance](http://www.chomsky.info/books/warfare02.htm))

> For example, it wasn't until I was in high school that I knew I was a
> good student. The question had never arisen. I was very surprised when
> I got into high school and discovered that I was getting all A's and
> that was supposed to be a big deal. That question had never arisen in
> my entire education. In fact, every student in the school I had
> previously attended was regarded as somehow being a very successful
> student. There was no sense of competition, no ranking of students. It
> was never anything even to think about. It just never came up that
> there was a question of how you were ranked relative to other
> students. Well, anyway, at **this particular school, which was
> essentially a Deweyite school and I think a very good one, judging
> from my experience, there was a tremendous premium on personal
> creativity, not in the sense of slapping paints on paper, but doing
> the kind of work and thinking that you were interested in**. Interests
> were encouraged and children were encouraged to pursue their
> interests. They worked jointly with others or by themselves. It was a
> lively atmosphere, and the sense was that everyone was doing something
> important.
> 
> [...]
> 
> Well, then I got to high school, the academic high school in the
> public school system, which was supposed to be a very good high
> school, and it was a real shocker. For one thing, as I said, there
> was  the shock of discovering that I was a good student, which had
> never occurred to me before. And then there was the whole system of
> prestige and value that went along with that. And the intense
> competitiveness and regimentation. In fact, I can remember a lot about
> elementary school, the work I did, what I studied and so on. **I
> remember virtually nothing about high school. It's almost an absolute
> blank in my memory  apart from the emotional tone, which was quite
> negative**.
> 
> If I think back about my experience, there's a dark spot there. 
> That's what schooling generally is, I suppose. It's a period of 
> regimentation and control, part of which involves direct
> indoctrination, providing a system of false beliefs. But more
> importantly, I think, is the manner and style of **preventing and
> blocking independent and creative thinking and imposing hierarchies
> and competitiveness and the need to excel, not in the sense of doing
> as well as you can, but doing better than the next person**. Schools
> vary, of course, but I think that those features are commonplace. **I
> know that they're not necessary, because, for example, the school I
> went to as a child wasn't like that at all**.
> 
> I think schools could be run quite differently. That would be very
> important, but I really don't think that any society based on
> authoritarian hierarchic institutions would tolerate such a school
> system for long. As Sam Bowles and Herb Gintis have pointed out, it 
> might be tolerated for the elite, because they would have to learn how
> to think and create and so on, but not for the mass of the
> population.   There are roles that the public schools play in society
> that can be very destructive.

(From [Personal influences](http://www.chomsky.info/books/reader01.htm))


# What was it like to attend the Seattle Quora meetup on October 24, 2014?

[Mirror](https://www.quora.com/What-was-it-like-to-attend-the-Seattle-Quora-meetup-on-October-24-2014)

I think the conversations that happened at
the meetup this time were a lot like those of past meetups. What made
this meetup unique was that we couldn't agree on a good place to meet,
so ended up talking outside of the RAM from 6:00pm to around 7:30(?)pm.
We ended up waiting in line for the RAM but there was difficulty
acquiring a table (the restaurant wanted to split the group into two
tables). I eventually had to leave before the group even got a table.

Some other notable points:

-   Everyone did manage to get the new Quora shirt.
-   There were several new people attending the meetup.
-   The group again did seem to mostly be people associated with UW.


# Is anyone interested in a study partner system at the University of Washington?

[Mirror](https://www.quora.com/Is-anyone-interested-in-a-study-partner-system-at-the-University-of-Washington/answer/Issa-Rice)

As the asker of this question, I am highly interested.

# Who is interested in an effective altruism group/club at the University of Washington?

[Mirror](https://www.quora.com/Who-is-interested-in-an-effective-altruism-group-club-at-the-University-of-Washington/answer/Issa-Rice)


As the asker of this question, I am highly interested in such a group. I
don't have a lot of experience with effective altruism yet though. I
also don't have experience with typical leadership positions like in
high school clubs, so I'm not sure about trying to start it just on my
own—although I'd definitely be willing to give it a try. (But in any
case, if very few people are interested, then it might not be worth the
effort to attempt to start a group).

# How has the way Vipul Naik uses Facebook changed the way you think about social media?

[Mirror](https://www.quora.com/How-has-the-way-Vipul-Naik-uses-Facebook-changed-the-way-you-think-about-social-media/answer/Issa-Rice)

Please see [Facebook](), where this answer has been incorporated.

# How can I implement cool URIs with Hakyll?

[Mirror](https://www.quora.com/How-can-I-implement-cool-URIs-with-Hakyll/answer/Issa-Rice)


In the Hakyll configuration file, do something like `route $ setExtension ""`, which will remove the `.html` extension from the generated file.
See also the discussion at [Google Groups](https://groups.google.com/forum/#%21msg/hakyll/XewxMLIjRIw/hBDnD3iXLMwJ).

Really, the main thing is to have the server set the default MIME type
to `text/html` so that these extensionless files are seen as valid HTML files by browsers.
Note that if you're hosting on something like GitHub pages, then this is not possible (see [Can MIME types of Github Pages files be configured?](http://stackoverflow.com/questions/15951012/can-mime-types-of-github-pages-files-be-configured)), which is why many people set up Jekyll/Hakyll to make separate directories for each page with an `index.html` in each so that the URLs will still look pretty (so you can go to both `example.com/page-name/` and `example.com/page-name/index.html`).


# What music does Issa Rice listen to?

[Mirror](https://www.quora.com/What-music-does-Issa-Rice-listen-to/answer/Issa-Rice)

See [Music I like to listen to]().

# Does Issa Rice watch anime?

[Mirror](https://www.quora.com/Does-Issa-Rice-watch-anime/answer/Issa-Rice)


Not anymore. When I was younger and lived in Japan, I used to watch
quite a bit (there are usually evening anime around 5pm–7pm in Japan,
and I used to watch several of those). I also remember being obsessed about [Digimon](https://en.wikipedia.org/wiki/Digimon),
which used to (not sure if this is still true) come on around 9am 
on Sundays. In fact I was so obsessed that I got my parents to record
it onto videotapes every week (might still have those somewhere). I
remember being very upset once when we forgot to record it.

Other anime I remember watching: [Pokémon](https://en.wikipedia.org/wiki/Pok%C3%A9mon),
[Yakitate!! Japan](http://en.wikipedia.org/wiki/Yakitate%21%21_Japan), [Doraemon](https://en.wikipedia.org/wiki/Doraemon),
[Chibi Maruko-chan](https://en.wikipedia.org/wiki/Chibi_Maruko-chan),
学校の怪談, 名探偵コナン, あたしンち,
and [Sazae-san](https://en.wikipedia.org/wiki/Sazae-san).
(There probably are more.)

When I got older and moved to the US, I briefly got excited about [笑ゥせぇるすまん -
Wikipedia](https://ja.wikipedia.org/wiki/%E7%AC%91%E3%82%A5%E3%81%9B%E3%81%87%E3%82%8B%E3%81%99%E3%81%BE%E3%82%93)
(Laughing Salesman), which has a fantastic depiction of a hedonistic
Japan.

I also remember liking [The Girl Who Leapt
Through Time (2006
film)](https://en.wikipedia.org/wiki/The_Girl_Who_Leapt_Through_Time_%282006_film%29).

Interestingly I never liked reading manga, and only ever watched anime.

# How often do you check the edit history to see the author of a question?

[Mirror](https://www.quora.com/How-often-do-you-check-the-edit-history-to-see-the-author-of-a-question/answer/Issa-Rice)

If the question is about someone on Quora, then I like to check who asked it. (This helps me build a better mental model of which Quora users like asking personal questions, like receiving them, etc., as well as letting me see which users interact with each other.)

If a question is particularly interesting or elaborately formulated, then I'm more inclined to check as well.

I'm less likely to check when I'm on the mobile app since I have to open an external browser to check.

As for how often this actually happens, I'd guess maybe once or twice a day.

# What are the Dungeons & Dragons alignment types of prominent Quora users?

[Mirror](https://www.quora.com/What-are-the-Dungeons-Dragons-alignment-types-of-prominent-Quora-users/answer/Issa-Rice)

See my [profile]() page.

# How does your Quora all time views/upvotes ratio compare to your questions/answers (public) ratio?

[Mirror](https://www.quora.com/How-does-your-Quora-all-time-views-upvotes-ratio-compare-to-your-questions-answers-public-ratio/answer/Issa-Rice)

My all time views:upvotes ratio is 5135, and my questions:answers ratio is 27.



# What is the difference between the markdown implementations kramdown, maruku, and rdiscount?

[Mirror](https://www.quora.com/What-is-the-difference-between-the-markdown-implementations-kramdown-maruku-and-rdiscount/answer/Issa-Rice)


You can compare the
different implementations using [Babelmark
2 - Compare markdown
implementations](http://johnmacfarlane.net/babelmark2/); simply
enter a Markdown document and observe the differing HTML outputs.


# How can I write messages in Gmail using Markdown?

[Mirror](https://www.quora.com/How-can-I-write-messages-in-Gmail-using-Markdown/answer/Issa-Rice)

See my page on [Pandoc]().

# Why does only the first item of a list show up when using pandoc and YAML headers?

[Mirror](https://www.quora.com/Why-does-only-the-first-item-of-a-list-show-up-when-using-pandoc-and-YAML-headers/answer/Issa-Rice)


Answering my own question since I figured it out. Indeed only the first
item seems to be bound to the variable, but using for-loops we can
obtain the other values as well. See [Listing tags using pandoc and YAML
header](http://stackoverflow.com/questions/25559469/listing-tags-using-pandoc-and-yaml-header)
[1] for more on how to do this for the specific case of listing tags.

=\=\=\=\=\
[1]\: Note: I asked and answered my own question on there as well.



# Is there a service or program that lets you copy text from a website directly into Markdown, retaining all formatting?

[Mirror](https://www.quora.com/Is-there-a-service-or-program-that-lets-you-copy-text-from-a-website-directly-into-Markdown-retaining-all-formatting/answer/Issa-Rice)

See my page on [Pandoc]().

# Are there translations websites of Quora content?

[Mirror](https://www.quora.com/Are-there-translations-websites-of-Quora-content/answer/Issa-Rice)


For Japanese, there is [Knoh (ノウ) | The
Knowledge Hub](https://web.archive.org/web/20170510103004/http://knoh.jp), which, as of August 2014, seems
to have around 60 answers on Quora translated (with the original answer
side-by-side, like [初めて起業するアントレプレナーたちが、もっともよくやってしまう過ちはなんですか？
| Knoh (ノウ)](https://web.archive.org/web/20161028104543/http://knoh.jp/answers/289014)). It seems to be
the efforts of a small group of people, and there doesn't seem to be a
sign up feature, so I'm not sure how much it will expand. They do say on
[Knoh について | Knoh
(ノウ)](https://web.archive.org/web/20131210152438/http://knoh.jp:80/about) that in the future they're planning
to publicly allow transaltions through the cloud. Also there does seem
to be a fairly active hashtag devoted to it on Twitter at [Twitter / Search -
\#knoh](https://twitter.com/hashtag/knoh) as well as an official
account at [Knoh (公式) (knoh\_jp) on
Twitter](https://twitter.com/knoh_jp).



# Has gwern ever considered enrolling in a massive personal genomics project such as the Personal Genome Project or the 100K Wellness Project?

[Mirror](https://www.quora.com/Has-gwern-ever-considered-enrolling-in-a-massive-personal-genomics-project-such-as-the-Personal-Genome-Project-or-the-100K-Wellness-Project/answer/Issa-Rice)


Here is his response:

> I didn't make the cutoffs for Hsu's BGI project, and I signed up for
> one  such project whose name I forget but wasn't selected (probably
> because I  am in a deeply uninteresting demographic). Personal
> genomics hasn't  been a priority for me: I'm not sure what I'd do with
> my genome if I had  it, and the declining costs are a deterrent to
> buying one myself  (Illumina is claiming a \$1k genome right now, and
> at that rate, it could  be \$100 in another decade).

(From [Page on
gwern.net](http://www.gwern.net/Links#comment-1562662493))


# What does Issa Rice think of Andrew J. Ho's post-graduation plans?

[Mirror](https://www.quora.com/What-does-Issa-Rice-think-of-Andrew-J-Hos-post-graduation-plans/answer/Issa-Rice)


I'm not an expert on the subject, so I hope [Vipul
Naik](https://www.quora.com/Vipul-Naik) can provide a better
answer, but here are some thoughts.

-   Admittedly my first reaction was one of bewilderment, mostly because
    I don't know anyone (smart) who is even remotely interested in
    pursuing personal tutoring. I suppose I just hadn't considered this
    at all until now, which probably shows in this answer.
-   In general I seem to associate the test prep industry with
    compulsory schooling in the US in general, and my impression isn't
    very positive [1, 2]. I'm still split on the question of time
    allocation for high school students. [3] In general I'm a lot more
    interested in extremely long-term goals rather than relatively
    short-term ones, and I think test prep falls under the latter. I
    suppose if the opportunity is lucrative enough, then it might be
    worth it. [4]
-   I am however very much interested when you mention teaching more
    advanced topics. I sometimes wish there were local groups that
    extended Cognito Mentoring, and if your plan could evolve to
    accomplish that (while, say, paying for maintenance/development with
    donations and the money earned from doing test prep), then I'd be
    very interested.
-   Your description [5] of the local area is consistent with what I
    have observed, but again I'm not an expert.
-   I suppose I can evaluate your plans personally, and consider whether
    I would take a similar path, although even this is a bit difficult
    since I haven't even begun college yet: for myself, my relative lack
    of experience with standardized tests makes the prospect fall apart
    immediately, though I would consider helping high school students
    per the Cognito Mentoring plan given above.

=\=\=\=\=\
[1]\: See for example [Education
Disruption](http://education-disruption.quora.com). From what
I've observed, you seem to have similar views.

[2]\: On the other hand, Cognito Mentoring, for instance, takes a neutral
stance regarding [Standardized
tests](http://info.cognitomentoring.org/wiki/Standardized_tests).

[3]\: See for instance [High school extracurricular activities: factors to consider](http://info.cognitomentoring.org/wiki/High_school_extracurricular_activities:_factors_to_consider) and [High school extracurricular activities: suggestions](http://info.cognitomentoring.org/wiki/High_school_extracurricular_activities:_suggestions).
During my own high school career, I tended to eschew studying for
standardized tests altogether. Still, one can ask whether, given that
students shouldn't spend time on test prep, whether one should still
seek a career in it to "extort money from the oblivious", or similar.

[4]\: Though with money, I now just think of it in terms of effective
altruism and earning-to-give.

[5]\: Specifically,

> In  the local area, there are a lot of affluent Asian immigrants with
> lots  of disposable income. There's also no private/boarding school
> culture  (indeed, the reported strength of the local high schools is
> why many  people decide to live here), but the public high schools
> here also  aren't that good



# Why has the Cognito Mentoring blog on Quora been dormant recently?

[Mirror](https://www.quora.com/Why-has-the-Cognito-Mentoring-blog-on-Quora-been-dormant-recently/answer/Issa-Rice)


Cognito Mentoring is now in "maintenance mode"; see [Moving on from Cognito
Mentoring](http://lesswrong.com/lw/k8q/moving_on_from_cognito_mentoring/)
for more. Specifically (taken from the post),


> **Existing blog posts will remain**, but we probably won't be making
> many new blog posts. New blog posts will happen only if one of us has
> an idea that really seems worth sharing and for which the Cognito
> Mentoring blog is an ideal forum.


As for why it is in "maintenance mode", the conclusion puts it
concisely:


> We (*qua* Cognito Mentoring) are grateful to LessWrong for being
> welcoming of our posts, offering constructive criticism, and providing
> us with some advisees we've enjoyed working with. We think that the
> work we've done has value, but don't think that there's enough
> marginal value from full-time work on Cognito Mentoring. We think we
> can do more good for ourselves and the world by switching Cognito
> Mentoring to maintenance mode and freeing our time currently spent on
> Cognito Mentoring for other pursuits. The material that we have
> already produced will continue to remain in the public domain and we
> hope that people will benefit from it. We may revisit our "maintenance
> mode" decision if new evidence changes our view regarding traction,
> impact, and long-run financial viability.



# For high school and early college (or equivalent) students, how has regular casual interaction with people in their mid-to-late 20s influenced you?

[Mirror](https://www.quora.com/For-high-school-and-early-college-or-equivalent-students-how-has-regular-casual-interaction-with-people-in-their-mid-to-late-20s-influenced-you/answer/Issa-Rice)

My thoughts are [here](importance-of-having-differently-aged-peers).

# Who is interested in an October 2014 Quora meetup in Seattle?

[Mirror](https://www.quora.com/Who-is-interested-in-an-October-2014-Quora-meetup-in-Seattle/answer/Issa-Rice)

Interested.

# Who is interested in a September 2014 Quora meetup in Seattle?

[Mirror](https://www.quora.com/Who-is-interested-in-a-September-2014-Quora-meetup-in-Seattle/answer/Issa-Rice)

I'm interested.

# How does Quora deal with question URLs if a question is edited but then a new question is added with the exact wording of the old question?

[Mirror](https://www.quora.com/How-does-Quora-deal-with-question-URLs-if-a-question-is-edited-but-then-a-new-question-is-added-with-the-exact-wording-of-the-old-question/answer/Issa-Rice)


Both the old and new URLs for the original question go to the original
question; the new question gets its own URL entirely.

Here's what I did. I asked "What is Quora's policy on test questions?",
which first created [https://www.quora.com/What-is-Quoras-policy-on-test-questions](https://www.quora.com/What-is-the-Quora-policy-on-test-questions).
Then I changed that wording to "What is the Quora policy on test
questions?", which generated a new URL for that question, <https://www.quora.com/What-is-the-Quora-policy-on-test-questions>.
Then I added a new question with the exact wording of the old question,
"What is Quora's policy on test questions?". This new question got the
URL <https://www.quora.com/What-is-Quoras-policy-on-test-questions-1>.
Meanwhile, both of the first two links go to the first question.


# What are some of the best questions and answers you have come across recently (July 2014) on Quora?

[Mirror](https://www.quora.com/What-are-some-of-the-best-questions-and-answers-you-have-come-across-recently-July-2014-on-Quora/answer/Issa-Rice)


Over the course of two days I looked through all of Jessica Su's
questions. They aren't "recent" in terms of when they were produced, but
they are certainly worth checking out if you haven't already. See for
example:

-   [What is a good approach to learn
    mathematics having a programming
    background?](https://www.quora.com/What-is-a-good-approach-to-learn-mathematics-having-a-programming-background)
-   [In college, is it better to expose
    yourself to a broad swath of material, or delve deeply into a narrow
    topic of
    interest?](https://www.quora.com/In-college-is-it-better-to-expose-yourself-to-a-broad-swath-of-material-or-delve-deeply-into-a-narrow-topic-of-interest)
-   [How can I become your
    friend?](https://www.quora.com/How-can-I-become-your-friend)</span>
-   [Do professors ever get bored of their
    university?](https://www.quora.com/Do-professors-ever-get-bored-of-their-university)
-   [How long does it take you to read
    journal papers in your
    field?](https://www.quora.com/How-long-does-it-take-you-to-read-journal-papers-in-your-field)


# What is the best way to read library books in bed without any part of the book cover touching the sheets?

[Mirror](https://www.quora.com/What-is-the-best-way-to-read-library-books-in-bed-without-any-part-of-the-book-cover-touching-the-sheets/answer/Issa-Rice)


There are also [Prism
glasses](http://www.amazon.com/Prism-Glasses-Eye-Bed-Spectacles/dp/B000RZNBF4)


![](https://qph.is.quoracdn.net/main-qimg-57c2efa7f8c28c14da5d97f6defb05f4?convert_to_webp=true)


(Image from Amazon link above.)

They're a bit odd to wear, since one can usually see more than just the
page from the book reflected (i.e. near the top and bottom, one sees
different angles of reflection).

See also [D\_Malik comments on Post
ridiculous munchkin ideas! - Less
Wrong](http://lesswrong.com/lw/h9b/post_ridiculous_munchkin_ideas/8yb9).


# What is it like to attend the Friday pizza lunch on the astronomy floor at the University of Washington?

[Mirror](https://www.quora.com/What-is-it-like-to-attend-the-Friday-pizza-lunch-on-the-astronomy-floor-at-the-University-of-Washington/answer/Issa-Rice)


I went to one during the summer, so I'm not quite sure if the atmosphere
I experienced was usual. Essentially, someone goes out to buy three(?)
large pizzas[2] and some drinks (canned Coca Cola) and everyone else
pays \$2.50 a slice to eat.[1] Everyone sits or stands around in the
lounge (which is sort of more like a hallway with chairs), and chats a
bit. I think most of the people there were professors/researchers or
graduate students. I felt a bit out of place as I was one of the only
undergraduates/prefrosh. What I ended up doing was standing in the room
next to the lounge/hallway with [Kristin
Lie](https://www.quora.com/Kristin-Lie) and [Lilian
Liang](https://www.quora.com/Lilian-Liang).

If I end up going again, I'd like to (1) try talking to people about
astronomy/the astronomy major at UW/the astronomy research at UW; (2) go
during the regular school year to see if the summertime was unique; (3)
update this answer accordingly.


=\=\=\=\=\
[1]\: Although, for myself, I had brought lunch so I ate that instead of
the pizza.

[2]\: I did hear someone say that the pizza slices tend to run out fast,
although when I went there seemed to be (just) enough for everyone.



# Is it true that preschoolers in Japan are starting to wear wide brimmed hats and sunglasses to protect from sunlight?

[Mirror](https://www.quora.com/Is-it-true-that-preschoolers-in-Japan-are-starting-to-wear-wide-brimmed-hats-and-sunglasses-to-protect-from-sunlight/answer/Issa-Rice)


As [Sed
Chapman](https://www.quora.com/Sed-Chapman) mentioned, this isn't
widely adopted, but one school at least has adopted this[1], and was
recently on the news for it. Observe:


[The video was made private since I first posted the answer...]

\
Rough transcript[2]\:

> [Female narrator:] The rainy season has been ending starting in the
> south, and we are entering the hottest season of the year. What
> measure against this season do we tend to forget?
>
> [Man enters:] At this preschool, in order to protect from UV rays, the
> preschoolers wear sunglasses while walking to the preschool.
>
> [Female narrator:] Protecting your eyes from UV rays:
>
> [Principal:] Since the sun is situated lower in the sky, it's easier
> for the light to enter the eye, and thus it's said that wearing
> sunglasses in the mornings and evenings is important.
>
> [Parent 1:] I'm concerned about my child's eye working properly in the
> future, so that's why we wear these when coming to the preschool.
>
> [Parent 2:] I think that it's because they are children that we are
> supposed to care for them.

The school does seem to be a private school: [埼玉県さいたま市緑区 学校法人古里学園 大古里
育ちの森幼稚園](http://www.chikyu-go.ed.jp/index.html)
(Japanese).

=====\
[1]\: I suppose I should also note that most of the hats aren't quite
regular wide brimmed ones, so [Alex K.  Chen](https://www.quora.com/Alex-K-Chen) may be disappointed.

[2]\: By me, so there are possibly errors.


# What is it like to go to the UW A&O (for freshmen)?

[Mirror](https://www.quora.com/What-is-it-like-to-go-to-the-UW-A-O-for-freshmen/answer/Issa-Rice)


Some thoughts (from the 2014 A&O):

-   I am not convinced that the A&O required two days. The total time
    required to attend fully is 16.5 hours, and I felt that the
    important parts (getting one's Husky Card, signing up for classes,
    asking questions, getting to know some students) didn't really
    require this entire time. It almost felt like the university itself
    was not confident that students would stay, so had to implement
    measures to force students to stay the full time. (To illustrate,
    they didn't tell you the schedule for the second day on the first
    day, they scared students into coming on time on the second day[1],
    course registration was during the second day, and they didn't hand
    out the Husky Cards until the very end of the second day, even
    though photos were taken much earlier during that day.) One student
    in my particular group actually left after dinner on the first day.
-   I thought that a lot of the information could simply have been
    placed on the UW website for students to read[2], especially
    considering that most of the videos that were shown during the
    orientation are available on YouTube already.
-   Even though the A&O required so much time, I still felt that I
    didn't get enough time/support to register for courses. They
    allocated around 1–1.5 hours for registration, but I still felt
    rushed and actually didn't end up registering for any courses during
    the alloted time[3], mostly due to questions about prerequisites for
    majors, which math course to take, IB credits, honors courses, and
    so on. At least in the very beginning, I would have appreciated more
    extended individualized help. My wish would be that they had
    concentrated their efforts more into making sure each student got
    help instead of setting up some sort of "Husky experience" with a
    chain of presentations.[4]
-   The food/eating experience was pleasant, and much better than what I
    got during high school orientation. I appreciated the
    vegetarian/vegan accommodations.
-   The orientation leaders were extremely helpful. My particular
    orientation leader was a rising senior, so seemed to know a lot of
    things about UW. His anecdotes were rather helpful, and I was able
    to ask about e.g. taking graduate level courses and even what the
    conditions were for getting a free replacement for the Husky Card
    (in case it broke).[5]
-   I was in an honors group during the orientation, so was able to
    spend some time with peers who tended to be more high-achieving (on
    average), which perhaps helped me regarding socialization (e.g.
    having more common topics to discuss). I don't know if I was able to
    construct any "lasting friendships", but it was nonetheless pleasant
    to be in my group (of 17 people). I should mention that the
    university didn't bother to filter out students who were accepted
    into UW honors but declined; these students were forced to sit in
    for the honors presentations, and I felt bad for them.


=\=\=\=\=\
[1]\: The schedule pamphlet states "8:00am - Don't be late! Meet your
Orientation Leader at your group's designated location. Failure to
arrive on-time and check-in by 8:05am will result in a block on Autumn
course registration." In reality, they were pretty lax about this
requirement, staying until around 8:15am at the meeting spot.

[2]\: Perhaps included as part of the pre-registration screens, to force
students to read through them?

[3]\: I don't think this was usual; most people seemed to be able to get
their registration done/almost done.

[4]\: Perhaps I am being too bitter.

[5]\: I suppose one thing to keep in mind is that the orientation leaders
are paid, so they may be acting extremely helpfully to make people feel
welcomed. I personally did not mind their helpfulness/cheerfulness, and
thought they did a very good job.


# What is the dinner/lunch like at the UW freshmen A&O?

[Mirror](https://www.quora.com/What-is-the-dinner-lunch-like-at-the-UW-freshmen-A-O/answer/Issa-Rice)


From 2014:

-   Dinner (Day 1): A salad (from a huge salad bowl, so one can get an
    arbitrary amount), (canned?) oranges, some sort of stir fry (there
    was a vegetarian stir fry as well, which one could ask for at the
    kitchen), rice. We ate at the ball room in the HUB.
-   Lunch (Day 2): I think all the groups split off into different
    locations (possibly because of the problem Jennifer mentioned),
    although there were multiple groups in my location. Our group ate at
    [Local Point in Lander
    Hall](https://www.hfs.washington.edu/localpoint/), where it
    was, as Jennifer noted, a buffet-style lunch. (Vegetarian options
    were available; I had a salad and a vegetarian plate with random
    food on it.)


# What is it like to have Vipul Naik as a teacher?

[Mirror](https://www.quora.com/What-is-it-like-to-have-Vipul-Naik-as-a-teacher/answer/Issa-Rice)


I'm answering because Vipul asked me to, but I don't primarily consider him a teacher.
I first contacted him when he began Cognito Mentoring with
Jonah Sinick, so I still think of our relation as being one of
mentor–mentee.

On Quora, he helpfully answers some of my questions like [What are the common frustrations of Vipul Naik?](https://www.quora.com/What-are-the-common-frustrations-of-Vipul-Naik)
(which I asked because I was feeling curious after I saw one that was
asked of Alex K. Chen) and [Does Vipul Naik cook?](https://www.quora.com/Does-Vipul-Naik-cook) (which I asked because I became curious about vegetarianism/veganism).
However this is rather typical of Quora in general (e.g. I ask more questions about Alex K. Chen than about Vipul).

On Facebook, I know him as the most sedulous article collector and
discussion initiator/moderator. I suppose this is somewhat the role
teachers usually fill, by introducing material to the class. He seems to
do this better in some sense, then, by mostly bringing up discussion
topics that are of interest to me, and also by not forcing people to
contribute (which is what a traditional teacher does through verbal
remarks and grades).

He also personally tells me things e.g. to join LinkedIn or to check out
Power Smoothies, but again this applies to a greater class of people
than that of just teachers.

\

I was reminded (by Vipul) that I have also watched some of his math videos on YouTube.
I thought these were high quality, and especially interesting
since they went into more abstract topics than the typical math videos
one finds online (e.g. Khan academy).
More recently, I watched his videos on proving limits using the epsilon–delta definition (available as a playlist [here](https://www.youtube.com/watch?v=smP5NIYsvPc&list=PLC0bHnWu122lmEcvTXAnTbb33-faiCY1E)).
I thought the videos were good, and more detailed than what my math class did in college (at the same level).
I didn't like that he already had the delta beforehand instead of using "scratch work" like many others do (although the algebraic computations do make it rather obvious what to choose for delta).
When I asked about this, he was also willing to point out a few more things, like how the choice of delta was related to the derivative of the function.
I wish he had another video explaining this, though it's understandable that at the introductory stage this sort of thing isn't discussed.


# University of Washington: Why do the computers in the undergrad astro lab only have Scientific Linux with Python 2.4?

[Mirror](https://www.quora.com/University-of-Washington/Why-do-the-computers-in-the-undergrad-astro-lab-only-have-Scientific-Linux-with-Python-2-4/answer/Issa-Rice)


The astro lab recently updated to Scientific Linux 6, along with Python
2.6 and Vim 7.2, so some more features may be working.

\=\=\=\=\=

**Update**: Actually if you use something like `/astro/apps6/anaconda2.0/bin/python` instead of the default installation of Python (`/usr/bin/python`), [1] then you can use Python 2.7.8 as of August 2014. The other
advantage of using the Python on Anaconda is that you get software like
[Astropy](http://www.astropy.org/)
and [Matplotlib](http://matplotlib.org/)
without having to install them yourself.

[1]\: Since the astro admins install [Anaconda Scientific Python
Distribution](https://store.continuum.io/cshop/anaconda/) on the
servers for you.

# What was it like to attend the Seattle Quora meetup on June 27th, 2014?

[Mirror](https://www.quora.com/What-was-it-like-to-attend-the-Seattle-Quora-meetup-on-June-27th-2014/answer/Issa-Rice)


Some thoughts:

-   In terms of the venue, Tutta Bella had good food (although I felt
    bad for Alex K. Chen) but was a bit too noisy for conversing
    comfortably. I often found myself leaning toward whoever was
    speaking just so I could hear them.
-   It was really nice to have Hao there, because he would be able to
    give insight to things that only someone at Quora would know (e.g.
    that Quora is considering revising its "walled-garden" approach, and
    that this issue is somewhat contentious). I had been to two previous
    meet ups, and these tended to be more decentralized, but since Hao
    was there he in some sense took the role of "leader" e.g. by
    introducing himself to anyone who came later, or by managing the
    payment at the end.
-   I felt that the conversation topics were more varied, probably due
    to the higher turnout (compared to the other meetups I have been
    to). For instance there was a conversation near the end about the
    "Seattle freeze", and it was nice to see that the conversation could
    transition to even local things.
-   There were quite a few top writers there, so hearing some stories
    about the top writers' conference was fun (e.g. everyone clapping
    for Alex K. Chen before he asked a question).


# How can I combine an AND and a NOT in Liquid?

[Mirror](https://www.quora.com/How-can-I-combine-an-AND-and-a-NOT-in-Liquid/answer/Issa-Rice)

I'm answering my own question because I figured out a hack. I've been looking at some documentation, but it seems that Liquid does not have a NOT operator, and instead uses the "unless" construction along with conditions... So I ended up doing:

```
{% unless page.tags contains "japanese" %}
  {% if page.tags contains "math" %}
    for math and not japanese
  {% endif %}
{% endunless %}

{% unless page.tags contains "math" %}
  for not math, japanese or no japanese
{% endunless %}

{% if page.tags contains "math" and page.tags contains "japanese" %}
  for math and japanese
{% endif %}
```

#  What are all of Vipul Naik's acronyms?

[Mirror](https://www.quora.com/What-are-all-of-Vipul-Naiks-acronyms/answer/Issa-Rice)


I've created an Anki
deck for this for people who want to learn such Vipulous Vipulisms:
[Vipul Naik's acronyms](https://ankiweb.net/shared/info/1023766037)

# Who is going to the Quora dinner meetup on Friday, June 27th in Seattle?

[Mirror](https://www.quora.com/Who-is-going-to-the-Quora-dinner-meetup-on-Friday-June-27th-in-Seattle/answer/Issa-Rice)


I'm interested.

# How long has Issa Rice used Linux for?

[Mirror](https://www.quora.com/How-long-has-Issa-Rice-used-Linux-for/answer/Issa-Rice)


**\~5 years.**

I started with Ubuntu (either Intrepid (Oct 2008) or Jaunty (Apr 2009))
after I got my own computer (a very old Gateway machine); at first I
dual-booted with Windows XP. Even as far back as 2005/2006, however, I
remember playing around on Ubuntu (mostly just the pre-installed games)
because my father had it installed on his computer.

After a while I found [K.Mandla's blog
(Motho ke motho ka botho)](http://kmandla.wordpress.com/), which
I found really inspiring. I very much enjoy their antagonism toward
buying newer and newer hardware just to keep up with software bloat.[1]
So after reading posts like [Things to do
with an old
computer](http://kmandla.wordpress.com/2007/09/14/things-to-do-with-an-old-computer/),
[Ten things you can do keep an old
computer
useful](http://kmandla.wordpress.com/2007/03/16/ten-things-you-can-do-keep-an-old-computer-useful/),
[More reasons to learn from old
computers](http://kmandla.wordpress.com/2010/10/27/more-reasons-to-learn-from-old-computers/),
[Software](http://kmandla.wordpress.com/software/),
[Maximalism is a better
word](http://kmandla.wordpress.com/2010/05/05/maximalism-is-a-better-word/),
[Three reasons to buy an old
computer](http://kmandla.wordpress.com/2009/04/11/three-reasons-to-buy-an-old-computer/),
[Twenty-ten: The picks of the
litter](http://kmandla.wordpress.com/2010/12/13/twenty-ten-the-picks-of-the-litter/),
and countless others, I distro-hopped quite a bit before coming to like
Arch Linux and Debian best. At the moment I use Debian exclusively on
all my computers (I still use the default Android installation on my
phone, but I hate it).

\=\=\=\=\=

[1] K.Mandla is also very opposed to cloud computing in general (mostly
due to privacy concerns; see [The cloud is
a
lie](http://kmandla.wordpress.com/2009/07/07/the-cloud-is-a-lie/);
sort of like [What does Richard Stallman
think of
Quora?](https://www.quora.com/What-does-Richard-Stallman-think-of-Quora)),
and I used to agree more with this, but after discovering Quora I've
become more open to sacrificing some privacy for the sake of obtaining
useful information.


# How do I paste from the clipboard into vim when I type commands into the vim terminal?

[Mirror](https://www.quora.com/How-do-I-paste-from-the-clipboard-into-vim-when-I-type-commands-into-the-vim-terminal/answer/Issa-Rice)


Use `<C-r>"` or `<C-r>*`. The former will paste from Vim's internal clipboard, and the latter
will use the system's clipboard.
See [How to copy yanked text to VI command prompt](http://stackoverflow.com/questions/906535/how-to-copy-yanked-text-to-vi-command-prompt) for more.


# How can I use Vim UltiSnips to compute the sha1 hash of the current file?

[Mirror](https://www.quora.com/How-can-I-use-Vim-UltiSnips-to-compute-the-sha1-hash-of-the-current-file/answer/Issa-Rice)


Here is an approach using Vimscript interpolation:

```vimscript
snippet sha1 "insert sha1 hash of the current file"
`!v strpart(system("sha1sum ".expand("%")), 0, 40)`
endsnippet
```

(Note that the system must have sha1sum as a command, which is true for
e.g. Debian.)

# How did you discover Quora?

[Mirror](https://www.quora.com/How-did-you-discover-Quora-2/answer/Issa-Rice)


-   [Tim Gowers's
    Weblog](http://gowers.wordpress.com/) has a sidebar that
    links to [What is it like to
    understand advanced
    mathematics?](https://www.quora.com/What-is-it-like-to-understand-advanced-mathematics),
    which is where I first found Quora. I didn't stay on the site for
    long, however (probably because of the sign-in policy).
-   Later [Vipul
    Naik](https://www.quora.com/Vipul-Naik) and [Jonah Sinick](https://www.quora.com/Jonah-Sinick) (as part of [Cognito
    Mentoring](http://cognitomentoring.quora.com)) pointed me to
    Quora for getting information mainly on colleges. I signed up but
    didn't really become active (I did read the Weekly Digests though).
    I think [Alex K.
    Chen](https://www.quora.com/Alex-K-Chen)'s questions/answers
    convinced me to stay and become active on Quora.


# How did you discover LessWrong?

[Mirror](https://www.quora.com/How-did-you-discover-LessWrong/answer/Issa-Rice)


-   Originally through the xkcd forums. I think Vaniver was the one who
    linked to Less Wrong. Searching 'site:[forums.xkcd.com](http://forums.xkcd.com)
    "less wrong" vaniver' on Google seems to bring many results up.
-   That wasn't enough for me to stay on the site, however. At some
    point later (maybe 1 year later), I found lukeprog's [The Best Textbooks on Every
    Subject](http://lesswrong.com/lw/3gu/the_best_textbooks_on_every_subject/)
    through a Google search (I can't remember the keywords now). This
    time I stayed, and I've continued to lurk on the site for several
    years now.


# Should you use Anki flashcards for memorizing and in what cases?

[Mirror](https://www.quora.com/Should-you-use-Anki-flashcards-for-memorizing-and-in-what-cases/answer/Issa-Rice)


Using Anki for memorization is good because it incorporates both testing
(i.e. one is actively recalling information instead of just reading) and
spacing (i.e. not cramming, but rather spreading reviews out).

To copy what I wrote elsewhere:


> The best source to learn about spaced repetition in general is Gwern's
> article at [Spaced
> repetition](http://www.gwern.net/Spaced%20repetition).
>
> Also read [A vote against spaced
> repetition (Less
> Wrong)](http://lesswrong.com/lw/juq/a_vote_against_spaced_repetition/)
> for why using flashcards may not be the best way to study. (The title 
> is somewhat misleading, and one comment points this out, saying 'This
> is  really more "a vote against flashcards" than "a vote against
> spaced  repetition", though, at least given your concrete issues with 
> flashcards.')
>
> For  myself, I've been using it and like it a lot, but it probably
> works  best for language learning/vocabulary study. I've tried using
> it to  memorize e.g. trigonometric identities/integrals before, but
> couldn't  figure out a good way to break apart the information (since
> some  identities are too long to be recited quickly). The hardest part
> is  motivating myself to keep up the daily reviews; Beeminder is only 
> helping somewhat.

\
See [A brief summary of effective study
methods](http://lesswrong.com/lw/k4n/a_brief_summary_of_effective_study_methods/)
for more.


# Who is interested in a May 2014 Quora meetup in Seattle?

[Mirror](https://www.quora.com/Who-is-interested-in-a-May-2014-Quora-meetup-in-Seattle/answer/Issa-Rice)


Yes I'm
interested.

# As a high school student, how have you found reading and participating on Quora useful?

[Mirror](https://www.quora.com/As-a-high-school-student-how-have-you-found-reading-and-participating-on-Quora-useful/answer/Issa-Rice)


Some thoughts:

-   Reading about people's experiences in college has been immensely
    useful, especially since there don't seem to be other good
    systematic ways to elicit such information and make it public. Quora
    seems particularly good at spreading everything from random
    anecdotes about a teacher to general opinion about a major at a
    university to study habits, and so on. I'm also lucky that the
    school I will be attending already has a lot of questions/answers on
    Quora, so I get a "head start", in a way. See [Vipul Naik's answer to For what
    universities does Quora have the most information and
    why?](https://www.quora.com/For-what-universities-does-Quora-have-the-most-information-and-why/answer/Vipul-Naik)
    for more.
-   This is more general, but there are some amazing answers on Quora,
    which I am unsure I can find anywhere else. See e.g. [Mark Eichenlaub's answer to Do grad school
    students remember everything they were taught in college all the
    time?](https://www.quora.com/Do-grad-school-students-remember-everything-they-were-taught-in-college-all-the-time/answer/Mark-Eichenlaub)
-   Other websites I tend to be interested in (e.g. Less Wrong) are more
    intimidating, which makes contribution more difficult for high
    school students like me. Quora is more tolerant of my random
    interests. (See e.g. [Is the
    popularity of multi-colored carrots proportional to the diversity of
    ethnicities of a
    country?](https://www.quora.com/Is-the-popularity-of-multi-colored-carrots-proportional-to-the-diversity-of-ethnicities-of-a-country))
    I don't see the Stack Exchange network ever allowing me to ask that.
-   It's also probably easier to get upvotes on Quora than on Less
    Wrong, so there is perhaps more motivation to post here because of
    that.
-   See also [Join Quora -
    Cognito](http://info.cognitomentoring.org/wiki/Join_Quora).


# What are some examples of censorship on Quora?

[Mirror](https://www.quora.com/What-are-some-examples-of-censorship-on-Quora/answer/Issa-Rice)


See also [Brian Fey's answer to What are some cases of questions for which the tag "Possibly Insincere Question" seems to be misapplied to censor content?](https://www.quora.com/What-are-some-cases-of-questions-for-which-the-tag-Possibly-Insincere-Question-seems-to-be-misapplied-to-censor-content/answer/Brian-Fey)
where he says that


> **In  many cases, this tag is just used as one more tool for censoring
> Quora  to remove thoughts that culturally narrow people don't like.**
> 
> **As soon as the tag is applied, nobody can see the question unless
> they follow the "Possibly Insincere Question" topic."**

(Be sure the read the comments to the answer as well.)


# What are good command line alternatives to popular GUI apps?

[Mirror](https://www.quora.com/What-are-good-command-line-alternatives-to-popular-GUI-apps/answer/Issa-Rice)


[Kmandla's page on Software](https://kmandla.wordpress.com/software/) has many good
ideas.

# How long does it take for DuckDuckGo to process a new bang expression?

[Mirror](https://www.quora.com/How-long-does-it-take-for-DuckDuckGo-to-process-a-new-bang-expression/answer/Issa-Rice)


In one instance, around three months.

I think I suggested one (`!gooj) 2 January, and it got added on 24 March. I'm not sure if my date of
suggestion is correct, though. (I got an email notification when it got
added, so the latter date should be pretty precise.)


# How should I properly pronounce your name?

See [Name]().

# Does anyone want a Seattle Quora Meetup for April 2014?

[Mirror](https://www.quora.com/Does-anyone-want-a-Seattle-Quora-Meetup-for-April-2014/answer/Issa-Rice)


Interested.

# What is the longest question on Quora?

[Mirror](https://www.quora.com/What-is-the-longest-question-on-Quora/answer/Issa-Rice)

I just found [In today’s hyper-fast
business world, we watch startups like Groupon go from zero to billions
seemingly overnight.  It’s tempting to measure ourselves by these
examples and to feel wholly inadequate. Personally, I have to wonder:
Why isn’t my businesses growing as fast as these new-age juggernauts?
What am I doing wrong? Why the 'New Normal' Isn't  The truth is,
Groupon-style growth is neither normal nor sustainable, and no “normal”
company should worry about emulating it. The reason for this is
two-fold:  Without VC money to flush down the toilet, you must fund you
own growth  Your funding is mathematically limited by actual profits.
Let'stake a closer look at this simple logic. Calculating Sustainable
Growth  Normal companies are profitable, not venture-funded. Not all
businesses are venture funded (thank God), and not all entrepreneurs
want to sell their souls to a VC. Although VC money powers rapid growth,
99.9% of companies will never see a dime of VC investment.  I’m guessing
that your “normal” company is not funded by VC and instead relies on
profits to fuel growth. (Groupon, meanwhile, has burned through almost a
billion dollars of venture capital.) Profitable companies have limits...
Believe it or not, growth is naturally limited in a profitable company
that is not venture-funded. Big companies figured this out decades ago.
In fact, Hewlett Packard pioneered the term “Affordable Growth Rate” to
describe the maximum speed of growth at HP in the 1950s. HP's Affordable
Growth Rate formula is a good (and easy to calculate) method that any
profitable company can use. ...And that limit is the Affordable Growth
Rate. Your Affordable Growth Rate (AGR) is the percentage that your
sales can grow year over year. If your sales doubled, that’s 100 percent
growth – that much is simple. But sales growth is limited by your
ability to fund new sales.  So -- how fast can your business grow?
Calculate your maximum AGR by dividing this year’s net profits by last
year's equity. [More specifically, AGR = (this year’s after tax retained
profits) / (Stockholders' tangible equity at the end of last year).]
Hewlett  Packard used this equation to limit its own growth. Yes, that’s
right, they wanted to limit growth.  Why?Because growing sales faster
than the rest of your business is a sure way toget yourself into
financial trouble. HP knew that sales have to be financed(computers have
to be built, sales people paid, etc.), and financing comeseither from
your own assets (cash) or what you can borrow against those assets
(loans). Sustainable Growth Is Good Growth  There’s no magic formula for
unlimited growth in a normal company. In fact, just the opposite. Your
AGR is a rather good formula (perhaps not magic) to show why growth
should be limited. You can only grow as fast as your profits (and equity
growth) allow. Not even Groupon can change the fundamentals of
sustainable growth. (And a few rational investors have seen this in
their analysis of the Groupon IPO.) So whether you make lunch boxes or
machine tools, websites or weed-whackers, take note. Make your best
effort to grow – just be sure that the growth is sustainable by sticking
to your AGR limits. Dedicated to your (Growing!) profits,  David  By:
David Worrell Growing Like Groupon: How NOT to Grow Too Fast, read more
http://markintelbd.com/view\_1/latestresearch/blog/2011/11/03/growing-like-groupon-how-not-to-grow-too-fast/](https://www.quora.com/In-today%E2%80%99s-hyper-fast-business-world-we-watch-startups-like-Groupon-go-from-zero-to-billions-seemingly-overnight-It%E2%80%99s-tempting-to-measure-ourselves-by-these-examples-and-to-feel-wholly-inadequate-Personally-I-have-to-wonder-Why-isn%E2%80%99t-my-businesses-growing-as-fast-as-these-new-age-juggernauts-What-am)

Admittedly it's not a single question, and I haven't even read the
entire question. The question details for this question, on the other
hand, are very short.

# When does the UW CSE direct admit mail go out?

[Mirror](https://www.quora.com/When-does-the-UW-CSE-direct-admit-mail-go-out/answer/Issa-Rice)


From the [High School Direct
Admission](https://web.archive.org/web/20170625104812/http://www.cs.washington.edu/prospective_students/undergrad/admissions/direct_admission)
page:


> Students who are admitted to the university will get a letter from UW 
> between March 15 and 31. UW Admissions then sends a Welcome Packet 
> containing an "enrollment confirmation" slip that lists your major.
> For *most* DA students, the enrollment confirmation slip will be
> updated to show  the major as Computer Science or Computer
> Engineering. For students who  have not been selected for DA, the
> major will be listed as Pre-Major,  Pre-Science, or another pre-major
> status.
>
> Official Direct Admission offers from CSE will arrive a little
> later  -- roughly two weeks after the Admissions office sends its
> notifications  of general university admission.  In April, CSE will
> email all DAs to  announce our offer of admission to the department.
> We will follow this  email with a letter from our chair, sent via
> postal mail. We will then  communicate directly with our new DA
> students to answer any questions  about our program, and to confirm
> enrollment.


# What are some creative ways to use Quora?

[Mirror](https://www.quora.com/What-are-some-creative-ways-to-use-Quora/answer/Issa-Rice)


Some active Quora users like Alex K Chen use Quora as a **"personal web
assistant"**. See [Alex K. Chen's answer
to Why are some Quora answers so
long?](https://www.quora.com/Why-are-some-Quora-answers-so-long/answer/Alex-K-Chen)

Some other posts that elaborate on this:

-   [Dave Cheng's answer to Why are some
    Quora answers so
    long?](https://www.quora.com/Why-are-some-Quora-answers-so-long/answer/Dave-Cheng)
-   [Alex K. Chen's answer to Where does
    Alex K. Chen find time to post hundreds of questions all
    day?](https://www.quora.com/Where-does-Alex-K-Chen-find-time-to-post-hundreds-of-questions-all-day/answer/Alex-K-Chen)


# Is LessWrong a cult-like group?

[Mirror](https://www.quora.com/Is-LessWrong-a-cult-like-group/answer/Issa-Rice)


Here are some resources that might help.

-   To their credit, Less Wrong has discussed its cult impressions in [Cult impressions of Less Wrong/Singularity Institute](http://lesswrong.com/lw/atm/cult_impressions_of_less_wrongsingularity/)
-   There is also the post [You're Calling \*Who\* A Cult Leader?](http://lesswrong.com/lw/4d/youre_calling_who_a_cult_leader/) by Eliezer Yudkowsky.
-   This one is clearly a joke, but there are [Eliezer Yudkowsky Facts](http://lesswrong.com/lw/4g/eliezer_yudkowsky_facts/)
-   Less Wrong also conducts annual surveys; the most recent one is [2013 Survey Results](http://lesswrong.com/lw/jj0/2013_survey_results/)
-   Some relevant articles that aren't strictly from Less Wrong: [The Cult of Bayes' Theorem](https://web.archive.org/web/20131203234424/http://plover.net/~bonds/cultofbayes.html) ([archive.today](https://archive.today/V4xK9)) and [LessWrong - RationalWiki](http://rationalwiki.org/wiki/LessWrong)


# What is the best way to treat or prevent acne?

[Mirror](https://www.quora.com/What-is-the-best-way-to-treat-or-prevent-acne/answer/Issa-Rice)


There are some resources on Reddit that seem useful. In particular see

- [The Redditor's Guide to Acne 2013](http://www.reddit.com/r/acne/comments/1bs7nv/the_redditors_guide_to_acne_2013/) (old version: [The Redditor's Guide to Acne, Version 2](http://www.reddit.com/r/acne/comments/nrkg2/the_redditors_guide_to_acne_version_2))
- [I've had acne for a long time and finally cured it. Here's a huge post of guidelines to follow that will probably cure yours too.](http://www.reddit.com/r/acne/comments/188mha/ive_had_acne_for_a_long_time_and_finally_cured_it/)

via [phonypapercut comments on Open Thread, August 1-15, 2012 - Less Wrong](http://lesswrong.com/lw/dwb/open_thread_august_115_2012/74w4).


# Longevity and Life Extension: What can I do to live as long as possible?
[Mirror](https://www.quora.com/Longevity-and-Life-Extension/What-can-I-do-to-live-as-long-as-possible/answer/Issa-Rice)


There is a recent (28 Feb. 2014) post on Less Wrong that discusses
longevity, which is worth checking out.

See [Lifestyle interventions to increase longevity](http://lesswrong.com/lw/jrt/lifestyle_interventions_to_increase_longevity/).
(The post is licensed CC-BY, so someone may want to attempt to extend it.)

The comments discuss sleep apnea: [Yvain comments on Lifestyle interventions to increase longevity - Less Wrong](http://lesswrong.com/lw/jrt/lifestyle_interventions_to_increase_longevity/amp8).
On Quora, there is [What is it like to have sleep apnea?](https://www.quora.com/What-is-it-like-to-have-sleep-apnea)


# Why do Quora blogs have URLs that are subdomains and subdirectories?

[Mirror](https://www.quora.com/Why-do-Quora-blogs-have-URLs-that-are-subdomains-and-subdirectories/answer/Issa-Rice)

**For blogs with a subdomain URL**

1.  Go to the corner (on full web version) of the page with your name.
    (Hover over your name.)
2.  Click on "Create Blog".
3.  The URL will automatically assume the style http://blogname.quora.com.

Interestingly, going to either http://quora.com/yourusername/blogname or http://quora.com/blogname will redirect you to the same blog.
However the blog identifier here must be unique in all of Quora, so one does not have the freedom to choose an arbitrary name.

**For blogs with subdirectory URL**

(I actually haven't found a direct way to do this, and the current
method seems like a hack...)

1. Go to a random Quora post/answer/question.
2. Click on "Share" at the bottom of the post/answer/question.
3. Check the box that says "Post to Blog".
4. Type in any name for a blog.
5. Click on "Create Blog". (This assumes that you don't already have a
    blog with this name.)
6. Now the URL assumes the style http://quora.com/yourusername/blogname.
7. Now one can post to this blog like any other blog.



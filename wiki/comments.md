---
title: Comments
author: Issa Rice
created: 2014-12-30
date: 2015-10-10
status: notes
belief: possible
---

I've been interested in commenting systems, comment [spam in blogs](!w), and whether it's a good idea to have comments on this site.
I [once asked on Facebook](https://www.facebook.com/riceissa/posts/1477764832502469):

> What are the advantages and disadvantages of the various commenting
> systems used on websites? Some qualities one can pick out: whether to
> have nested comments, the size of the unit of language on which one
> can comment (e.g. comments for a whole article versus comments for
> each paragraph, or even smaller units), voting (and whether to display
> who voted), displaying who has seen the comments, which markup
> language to use, and so on.

It's rather interesting how many different commenting systems one can find, and is natural to ask which one works best.
And if that is an ill-defined question, then one can at least try to ask what one should use on one's own website.

It might be worthwhile to list all the possible parameters (i.e. to
extend the list I came up with in the Facebook post).

- Nesting/threading: [Web Discussions: Flat by Design](http://blog.codinghorror.com/web-discussions-flat-by-design/),
  [Mark New Comments](https://www.jefftk.com/p/mark-new-comments).
    There are several choices here.
    On sites like Reddit, Quora, and Hacker News, discussions both *have* a
    tree structure and are *presented* as a tree.
    On 4chan, discussions *have* a DAG structure but are *presented* as a flat
    list that is chronologically sorted.
    Facebook used to have comments that had a flat structure and were presented
    as such.
    In general the underlying data structure has to be more "complicated" than
    the format in which the discussion is presented.
- Unit of language relevant for replies
    - talk about [Comment Press](http://futureofthebook.org/commentpress/)
    - Medium also has paragraph-level comments
- Voting
- Location of downvoted content.
[John\_Maxwell\_IV writes](http://lesswrong.com/lw/mbd/lesswrong_effective_altruism_forum_and_slate_star/cghw):

    > On reddit, if your submission is downvoted, it's downvoted in to
    > obscurity. On Less Wrong, downvoted posts remain on the Discussion
    > page, creating a sort of public humiliation for people who are
    > downvoted.

    This is also true of a site like Quora, where heavily downvoted
    answers are hidden.
    (And in fact, only highly upvoted content is widely circulated through people's feeds.)

- User accounts
    - Anonymity/pseudonymity
- Markup language
- Permissions (e.g. ability to edit others' comments)
    - Version control (though I've never seen this before)
- Timestamp
- Quotation (as on bulletin boards); see [Web Discussions: Flat by Design](http://blog.codinghorror.com/web-discussions-flat-by-design/) again.
- Independence (i.e., each comment to a post could become a post itself, to which others could comment)
- Length (some sites restrict the length of comments; this is most extreme on Twitter)
- Reference style: hyperlink, hover-over with some JavaScript, positionally
  apparent on the page (e.g. reddit-style threading).

Some questions to ask:

- Can a greedy selection (in the sense that, for each bullet point, one
  chooses the most preferable option) of the features optimize for the
  "best" commenting system?
- What patterns might we find if we classify many of the existing
  commenting systems (e.g. on Facebook, Quora, Wikipedia discussions,
  reddit, WordPress, Disqus, Discourse, etc.)?


# Comments for personal sites

## Cons

On social media like Facebook and Quora, and even on WordPress blogs, it
is not necessary to think too much on commenting, since this is all
provided upstream.  When I first started using a static site generator
to make my website, I followed gwern and used [Disqus](!w).  However,
currently this site has no comments.  My reasoning is that, ever since
I've become active on Facebook, I've realized that most of the useful
discussions about an article happen there, instead of on the original
article's comments section.  More directly, in his answer to "[Why are
people more willing to comment on a Facebook post sharing an article
rather than in the comments section of the article itself?][andrew]",
Andrew Ho writes:

[andrew]: https://www.quora.com/Why-are-people-more-willing-to-comment-on-a-Facebook-post-sharing-an-article-rather-than-in-the-comments-section-of-the-article-itself/answer/Andrew-J-Ho

> To answer the question directly, it is because the comments section of
> the article is full of <u>inane and worthless chatter</u> that has
> zero intellectual value whatsoever. However, my Facebook friends are
> mostly fairly intelligent people, so usually they have something
> insightful to say about the article and/or participating in the
> discussion that they prompt is enjoyable and interesting.

This obviously does not happen on every site.  In fact, I get the
impression that small personal sites tend to have the highest-quality
comments, while large news sites tend to have the worst, with blogs
somewhere in the middle.

The other issue is with having to moderate the comments.  Quora and
Facebook are convenient because they require real names, and thus are
able to keep out non-human spam (for the most part).  Disqus does seem
to have anti-spam measures, but verifying the identities of commenters
may be more difficult since people can choose to post anonymously (and
also because Disqus isn't as widely-used as Facebook).

It's probably worth thinking about why we have comments in the first
place.  Comments are useful chiefly because they are a means to provide
feedback for the author.  But this can be done via email or messaging
(see my [contact information](contact) for how); better yet,
for minor things like pointing out typos, I have an "edit page" link at
the top of each page that will allow people with GitHub accounts to fork
the site repo and submit a pull request.

There is also the problem of security.  Since it's not possible to
support native comments using purely static HTML, one must rely on
something like PHP or Javascript.  PHP can be [unsafe to use][php sec],
and relying on some external Javascript like Disqus means that it won't
work for people with Javascript disabled and comments might suddenly
disappear (if Disqus goes away).

[php sec]: http://www.networkworld.com/article/2345518/data-center/firewall-pioneer-wanted-a--super-secure--blogging-service-----so-he-s-built-his-own.html

Another idea: having comments could mean more flame.
When people on a site see that others are complaining about something, they might jump on that and add more flame^[I wouldn't compare this site to [Slate Star Codex](http://slatestarcodex.com/), but just look at any post there to see the problem of unending arguments.].
(This, of course, relates to the problem of the burden of moderation.)
Even seemingly innocuous content on an otherwise unknown site could become the target of a torrent of verbal attacks, and dealing with this seems highly stressful.
Forcing people to email in their attacks could have a dampening effect.
Of course, this doesn't prevent public attacks happening on Twitter, Tumblr, and elsewhere.

## Pros

One idea in favor of having comments is so criticisms are out in the
open.  But there are other ways to do this[^otherways], and in any case,
how can one trust a site owner to be honest about the comments posted on
their own site (since they usually have the power to delete any comment,
or even edit them in the case of sites using WordPress)?

[^otherways]: gwern has an "[External
links](http://www.gwern.net/On%20Stress#external-links)" section for his
page *On Stress* that links to a reddit discussion of the page.  I can
do the same with Facebook discussions or when I crosspost to Quora.


Another idea is that there is a natural presumption that commenting on a
site is enabled.  This site itself is the most natural place to have a
discussion about the content on the site, and also provides an obvious
place for readers to interact with each other; who am I to take this
zone of exchange away?


Some convincing ideas for me are:

- Site-native comments are potentially easier to backup than comments
  posted to Facebook or Quora.  Even Disqus does not allow the site
  owner to backup the comments for a site (only their own comments, last
  time I checked); [gwern seems to backup Disqus comments
  though](http://www.gwern.net/Archiving%20URLs#comment-886147303)[^disquscomments].

[^disquscomments]: In response to "What about [archiving] the comments
here?", gwern writes:

    > Likely to die, I'm afraid. I do back up my Disqus comments on a
    > regular basis, but there's no guarantee that I'll migrate them to
    > the next commenting system. (On the plus side, I try to address
    > any issues comments bring up, quote ones which add to the article,
    > etc, so the losses won't be too great.)

- Some people don't have an account on Facebook or Quora, and even
  emailing may be inconvenient.  For this, I do have an [anonymous
  feedback form][feedback] (which works even with text-only browsers
  like Elinks), as advertised on my contacts section of the about page.

[feedback]: https://docs.google.com/forms/d/1AbwmuMIyzB5X7P4ysL71vGD4WnMxsCKsAZULLc0X7V0/viewform?usp=send_form

- Having a comments section might be a good idea for an outsider (say,
  if they want to recruit bloggers).  Vipul Naik writes in [his answer
  to "How do you recruit writers for a group blog?"][recruit] that he
  searched on Bryan Caplan's EconLog when looking for bloggers to
  recruit to Open Borders:

    [recruit]: https://www.quora.com/How-do-you-recruit-writers-for-a-group-blog/answer/Vipul-Naik

    > I looked at the comment thread on Bryan's
    > migration posts on EconLog. I looked carefully for people who wrote
    > long, detailed comments on migration issues, whose philosophy seemed
    > broadly similar to what was being conveyed on the site, who were
    > eloquent, *and* who didn't seem to already have a very active blog
    > presence of their own.

I also do have a GitHub repository for this site, where anyone can open
an issue, which is viewable publicly.

# External links

A variety of people have discussed whether to have comments on their
site.  Here are some of the better ones.

- Matt Gemmell has:
    - [Comments Off](http://mattgemmell.com/comments-off/)<!-- ([Perma.cc](http://perma.cc/AP2L-32XU))-->
    - [Comments Still Off](http://mattgemmell.com/comments-still-off/)<!-- ([Perma.cc](http://perma.cc/6C7U-GL4W))-->
    - [Comments Commentary](http://mattgemmell.com/comments-commentary/)<!-- ([Perma.cc](http://perma.cc/D84U-WUX2), [archive.today](https://archive.today/hI4i1))-->, a collation of other writers' take on comments

- [Darren Steadman](https://web.archive.org/web/20140829044846/http://darrensteadman.com/2012/01/06/re-comments-off/) (through Gemmell)

- [MG Siegler](http://parislemon.com/post/15288210624/comments-still-off) (also through Gemmell):

    > Let’s be totally honest here: anyone worthwhile leaving a comment
    > should do so on their own blog. Very few read blog comments
    > anyway. I’m sorry, but it’s true. Commenting is a facade. It makes
    > you think you have a voice. You don’t. Get your own blog and write
    > how you really feel on your own site.

    This is related to my idea of treating comments as their own post.

    However, with this, it's important to consider the counterfactual:
    by removing a place to rapidly provide thoughts, readers may *never*
    end up providing their thoughts. In other words, I suspect that for
    many, it's comments or nothing; making one's own site or blog
    isn't an option (too much activation energy required).

- [Copyblogger](http://www.copyblogger.com/removing-blog-comments/):

    > If you’re going to put the work in to articulate your thoughts, to
    > make an intelligent argument, and to bring something fresh to the
    > conversation … you should be [putting that work into *your*
    > site][sharecrop], not ours.

    [sharecrop]: http://www.copyblogger.com/digital-sharecropping/


- The notorious [John Gruber](http://daringfireball.net/2010/06/whats_fair)

- [No Comment](http://prog21.dadgum.com/57.html) by James Hague:

    > I think that initial knee-jerk "I've been looking at this for ten
    > seconds and now let me explain the critical flaws" reaction is a
    > common one among people with engineering mindsets. And that's not
    > a good thing.  I've seen this repeatedly, from people putting down
    > programming languages for silly, superficial reasons (Perl's
    > sigils, Python's enforced indentation), to ridiculous off-the-cuff
    > put downs of new products (such as the predictions of doom in the
    > [Slashdot announcement](http://apple.slashdot.org/article.pl?sid=01/10/23/1816257)
    > of the original iPod in 2001).

- From "[A Brief History of the End of the Comments](http://www.wired.com/2015/10/brief-history-of-the-demise-of-the-comments-timeline)":

    > For years, comment boxes have been a staple of the online
    > experience. You’ll find them everywhere, from The New York Times
    > to Fox News to The Economist. But as online audiences have grown,
    > the pain of moderating conversations on the web has grown, too.
    > And in many cases, the most vibrant coversations about a
    > particular article or topic are happening on sites like Facebook
    > and Twitter. So many media companies are giving up on comments, at
    > least for now. So far this year, Bloomberg, The Verge, The Daily
    > Beast and now Motherboard have all dropped their comments feature.

    The article links to "[Why we're killing our comments section](http://www.dailydot.com/company/comments-section-dead/)", which has:

    > [W]e suspect that many publishers will soon find that their
    > existing commenting systems do not serve their readers as the
    > conversation continues to move off websites to social media, where
    > most of our content is discovered and consumed.

- "[So that took a while](https://www.peterkrautzberger.org/0181/)":

    > Jekyll can’t provide comments (obviously) and I am not interested in
    > going back to Disqus (for various reasons). I also had the impression
    > that comments were not doing it for me anymore. The ratio spam / useful
    > comment was about 1000 to 1. Sure, Akismet took care of this and Disqus
    > could, too. In addition, I’d get comments from other places (twitter, g+
    > or plain email) and since ~~I’m not a cool indieweb dev~~ it’s never
    > that many, I manually added them to posts.
    >
    > In other words, I started to feel like comments are just not that useful
    > anymore (caveat lector: see below) and that having a special technology
    > for it seems overkill.

- "[The internet has made defensive writers of us all](https://pchiusano.github.io/2014-10-11/defensive-writing.html)":

    > At times I’ve been tempted to just turn off comments entirely on my blog,
    > and just flat out avoid participating in comment threads on the web, but
    > this feels like throwing the baby out with the bathwater. Despite the
    > signal to noise ratio, there are conversations and exchanges that make
    > talking about things on the web worth it to me.

-   [Brian Tomasik](http://reducing-suffering.org/history-of-this-website/#Blog_comments "Brian Tomasik. “History of This Website”. Essays on Reducing Suffering. Retrieved October 23, 2017."):

    > I prefer to incorporate feedback into the original piece and acknowledge
    > people for their contributions, similar to what's done during peer review
    > of an academic paper. [...]
    >
    > Finally, a lot of discussion of my pieces happens on Facebook, Reddit, or
    > other places, which makes on-blog comments less crucial.

    I don't agree with the reasoning that having comments makes a site look
    less academic.

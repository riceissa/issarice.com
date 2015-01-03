---
title: Comments
#description: none
author: Issa Rice
creation-date: 2014-12-30
last-major-revision-date: 2014-12-30
language: English
# accepts "notes", "draft", "in progress", or "mostly finished"
status: notes
# accepts "certain", "highly likely", "likely", "possible", "unlikely", "highly unlikely", "remote", "impossible", "log", "emotional", or "fiction"
belief: possible
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
tags: content creation, comments
...

I've been interested in commenting systems, comment [spam in blogs](!w), and whether it's a good idea to have comments on this site.
[I once asked on Facebook](https://www.facebook.com/riceissa/posts/1477764832502469):

> What are the advantages and disadvantages of the various commenting systems used on websites? Some qualities one can pick out: whether to have nested comments, the size of the unit of language on which one can comment (e.g. comments for a whole article versus comments for each paragraph, or even smaller units), voting (and whether to display who voted), displaying who has seen the comments, which markup language to use, and so on.

It's rather interesting how many different commenting systems one can find, and is natural to ask: "Well, which one works best?"
And if that is an ill-defined question, then one can at least try to ask, "What should I use for *my* site?"

It might be worthwhile to list all the possible parameters (i.e. to extend the list I came up with).

- Nesting
- Unit of language relevant for replies
    - talk about [Comment Press](http://futureofthebook.org/commentpress/)
    - Medium also has paragraph-level comments
- Voting
- User accounts
    - Anonymity/pseudonymity
- Markup language
- Permissions (e.g. ability to edit others' comments)
    - Version control (though I've never seen this before)
- Timestamp
- Quotation (as on bulletin boards)
- Independence (i.e., each comment to a post could become a post itself, to which others could comment)

Some questions to ask:

- Can a greedy selection (in the sense that, for each bullet point, one chooses the most preferable option) of the features optimize for the "best" commenting system?
- What patterns might we find if we classify many of the existing commenting systems (e.g. on Facebook, Quora, Wikipedia discussions, reddit, WordPress, Disqus, Discourse, etc.)?


# Comments on this site

On social media like Facebook and Quora, and even on WordPress blogs, it is not necessary to think too much on commenting, since this is all provided upstream.
When I first started using a static site generator to make my website, I followed gwern and used [Disqus](!w).
However, currently this site has no comments.
My reasoning is that, ever since I've become active on Facebook, I've realized that most of the useful discussions about an article happen there, instead of on the original article's comments section.
More directly, in his answer to "[Why are people more willing to comment on a Facebook post sharing an article rather than in the comments section of the article itself?](https://www.quora.com/Why-are-people-more-willing-to-comment-on-a-Facebook-post-sharing-an-article-rather-than-in-the-comments-section-of-the-article-itself/answer/Andrew-J-Ho)", Andrew Ho writes:

> To answer the question directly, it is because the comments section of the article is full of <u>inane and worthless chatter</u> that has zero intellectual value whatsoever. However, my Facebook friends are mostly fairly intelligent people, so usually they have something insightful to say about the article and/or participating in the discussion that they prompt is enjoyable and interesting.

This obviously does not happen on every site.
In fact, I get the impression that small personal sites tend to have the highest-quality comments, while large news sites tend to have the worst, with blogs somewhere in the middle.

The other issue is with having to moderate the comments.
Quora and Facebook are convenient because they require real names, and thus are able to keep out non-human spam (for the most part).
Disqus does seem to have anti-spam measures, but verifying the identities of commenters may be more difficult since people can choose to post anonymously (and also because Disqus isn't as widely-used as Facebook).

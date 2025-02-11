---
title: Adaptive typography
author: Issa Rice
created: 2023-04-12
date: 2023-04-12
---

# tl;dr

Typographers focus almost exclusively on designing texts that are meant to be read linearly (and typography guidelines follow this as well, telling writers to limit line length, use a certain font size, etc.). But if you look at the actual stuff happening in the reader's mind as they interact with a book or webpage, linear reading is only one of many possible ways of interacting with a text. In particular, searching for things, flipping around, cross-referencing, and other "movement" tasks are quite common. For such movement tasks, the standard typographic advice seems like a poor choice. So the idea of _adaptive_ typography is to alter the typography of a page as the reader is reading to fit the current task. (This is to be distinguished from "responsive typography": adaptive typography is adapting to the reader's *mental state*, while responsive typography is responding to the reader's *device*.) I don't have a great idea for how to implement adaptive typography in practice, but one naïve idea is to have a button at the corner of the page that can toggle between "absorbing/linear mode" and "movement mode" (and possibly other modes).

# stuff

(this page used to be called "List of cognitive processes that happen as one interacts with a text".)

(Motivation: when people read things, they're not just linearly processing the words and then storing each word in their head. They might be jumping around in the text to find the "interesting" parts or might be searching for something specific. This makes typography tricky: you can't just say "this is a book. so we use the typography of a book"; as the reader's mental activity changes, the "best" typography also changes. And that's just for a single reader! If we consider all the possible readers who might get value from a text, that's a lot of different purposes and mental activities going on. So. The goal here is to list out a bunch of mental activities and then see how design/typography decisions can improve the experience of each activity.)

"responsive typography" is a pre-existing term, but for some reason it's only used to point to the concept of a page layout changing to match the size of the screen, essentially just the idea of "make sure you can read the page on both a laptop and a smartphone". this is like.. such a limited conception of what the term could mean! i'm just going to call my own thing "adaptive typography" for now so there is no confusion: i want typography that changes as the reader's mental state/goals/intentions change.  i am actually against responsive typography since i don't really want people to be reading my works on a smartphone. so you could say i am interested here in adaptive anti-responsive typography :D

# List of cognitive processes that happen as one interacts with a text

Things you do when "reading" something. Or: distinct cognitive processes that happen as you interact with a text.

For each thing below, I want to figure out how it maps onto design decisions. How can a better designed page cater to each activity/process? Some of it will be best-addressed at the "explanation level" or "writing style level" rather than the typography/design level, but I'm still interested in seeing if there are easy design tweaks that can be made to improve reading experience.

- reading the words in order, trying to transfer ink to your mental scratchpad/verbal word-recognizer/sentence-parser
	- this is where the standard typography advice works well: legible font, [[text width]] that is not too wide, etc. You're just trying to make the job as easy as possible for the eyes. I would also add things like a color scheme that does not hurt the eyes (see [[some thoughts on website design]] where I elaborated on this idea).
	- there's a kind of contrarian point here where typographers tend to really hate on "boring" typefaces, but actually, the more a font is used in the world, the more readers are used to seeing it, and so the more readable it is... there is a pressure toward using fonts that everyone else is using, contrary to what professional typographers want us to believe.
- scanning around to see if anything catches your eye
	- this is where the standard typography advice is *harmful*! It's the first sign that maybe, just maybe, something is severely wrong with how people usually even talk about typography and design... To elaborate more on why the standard advice is harmful: when you're scanning around, you want as much text to fit on the screen as possible, so you can cover more ground. This means you want long lines, smaller text, a font that isn't perhaps the most legible but just works really well even if the font is small, that sort of thing. We kinda want the "opposite" of what the standard advice is.
	- i often get the sense that a website feels "cramped" somehow, like i'm trying to do something but i have very low visibility of the overall structure. or like, there aren't enough affordances to navigate around the site in the way i want?
		- there's a question of like "how ADHD do you want the reader to be?" or "how ADHD should the reader be allowed to be?"  Sometimes you want to kind of force the reader to stick along to what you want to say, because you know you have a good point to make and you don't want them to miss it. But also, if you're not producing enough insight, the reader should be free to move along (possibly to another page on the site, possibly to some other site altogether) until they find something of interest.
		- see also [this video](https://twitter.com/andy_matuschak/status/1656118011168964608) and the quote-tweeted thread by andy matuschak (especially the [tweet](https://twitter.com/andy_matuschak/status/1202663258827542529) "If I read an old digital note, I get the unnerving sense that it’s part of some 'whole' that I can’t see at all—no matter how much hypertext is involved. Working with physical notes, I’d shuffle notes around to make sense of the structure. There isn’t a digital equivalent." For some reason andy doesn't talk about peripheral vision for a *single website* or peripheral vision for a *book*). potential keywords: robert spence, bifocal display. There's something great about a physical space, which is that most of the time you can stay on your desk, which can be a small space. but if you ever need more space, you can kind of cheaply acquire more space -- e.g. by using your floor or something. with a computer screen, you're hard-limited to the size of your screen. like, sure, i guess you could keep a giant external monitor around that you only rarely use, but it's not a *cheap* solution, and what if you want even more space than that?
	- [link styling](https://practicaltypography.com/how-to-use.html) is another place where you want it to be subtle if you're trying to create an immersive reading experience, but you want it to be easily spottable if you're trying to create a "surfing" or "exploration" experience.
- scanning to find a particular thing you have in mind. This may require using an index or search bar.
	- similar to previous point. but really, this is more something that's best handled by a good index or search bar.
- trying to find a thing that you know is somewhere here but you can't remember what exactly it's called or what page it was on
	- same as previous point, but even more emphasis on "good" index, e.g. one that has all the synonyms and near-misses included so that the reader doesn't need to exactly know what the thing is called.
- verbalizing a particular question in your head, hoping the text will answer it.
	- is this even a task for design? i think it's a matter of having several beta readers or something and have them note down their questions, so that questions can be addressed, possibly by linking out to something or in a footnote.
- verbalizing a particular reaction/opinion to the text, hoping the author could respond to your point.
	- same as above?
- something clicks. you highlight/underline, maybe.
	- probably something that is best left to the reader... like, you would hope the reader has their own note-taking system in place. but perhaps something like orbit cards (that pop up when you select some text) or something like [readwise](https://readwise.io/) would work nicely.
- scanning because you just want the *point*. You're skeptical you have to read *so many words* to understand the point. You wish the point could just be given to you, somehow.
	- another thing that beta readers could catch. but once pointed out, how should it be presented? some sort of abstract or tl;dr that's easily noticeable should perhaps be added to the top of the page.
- You feel vaguely bored, bounce off, you think "tl;dr".
	- maybe a really good design could artificially keep a reader around, just to marvel at the design. but that feels like an illegitimate use of design. if the content feels boring, it's probably the fault of the ideas or the explanation. is there anything design can do here?
- You're excited. You've been waiting a long time for this piece to come out, or it's by your favorite writer. You want to absorb every word, every insight.
- You just *finished* "reading". You wish there was something more. You feel fooled. You feel the text did not deliver on what it implicitly or explicitly promised.
- You're not sure you're absorbing the text. You wish someone could test you on the knowledge. You wish you could practice, apply, the knowledge, so that you know you're not just overfitting on the particular example given in the text.
	- orbit-style cards maybe. beta readers. maybe not something to address with design.
- You wish for a goddamned example.
- The idea is interesting, but it's just not written in a style you like engaging with. Maybe it's too illegible/murky, maybe it's not [technical](https://www.readthesequences.com/A-Technical-Explanation-Of-Technical-Explanation) enough.
- You see clarification on the meaning of a particular word, or the relevance of the statement just made, more elaboration of something. You want to "click through" on something. You wish it were a hyperlink.
- you know most of the content, but you want to see if there's anything new in here that you have not seen already.
	- if the "new pieces" are predictable, then having a special section addressed to experts or something would be one option. if it's clearly just an exposition piece and there's no new ideas, that's also something worth being explicit about.

i think the two big "modes" are "**absorbing**" (linear reading, engaging with the *local content*) and "**moving**" (includes e.g. scanning and searching; interacting with the *global structure*).

possibly another framing: instead of "adaptive typography", it can be "modal reader", like how vim is a "modal text editor". the reader goes between different modes as they interact with the text, just as a programmer goes between e.g. edit, visual, normal modes as they write code.

reading goes through several stages:

- figuring out whether this is what you want to read -- e.g. reading the abstract, quickly scrolling to see the section names, reading the TOC, etc
- committed: if you didn't bounce at the first step, you have committed. there's _something_ in here that you want to absorb. but at this stage you might still not be sure exactly where the info you want is located. so you still want some sort of intra-page navigation features
- you've found your spot. now you just want to read linearly.

another thought i had about all of this: i think that this sort of mode switching is more helpful at the level of an entire website rather than just a single paper or webpage. with a single page you're more likely to just want to sit down and absorb it. with a website, you want to navigate around to find the thing you're looking for.

# External links

- [here](https://www.greaterwrong.com/posts/X4nYiTLGxAkR2KLAP/open-and-welcome-thread-december-2019/comment/89tQRcqPkRKrPFJ3S) is a discussion i started on LessWrong back in 2019.

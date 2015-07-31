---
title: UW CSE application
#description: 
#feed_description: 
author: Issa Rice
creation_date: 2015-07-31
last_major_revision_date: 2015-07-31
language: English
# Possible values are "notes", "draft", "in progress", and
# "mostly finished"
status: notes
# Possible values are "certain", "highly likely", "likely", "possible",
# "unlikely", "highly unlikely", "remote", "impossible", "fiction", and
# "emotional"
#belief: possible
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
tags: uw, uw cse
#aliases: 
---

This page contains information about my UW CSE application.
I applied after one full year at the University of Washington, for the July 1, 2015 deadline.
I was admitted to the major (on my first attempt) on July 24.

The main purpose of this page is to be transparent about my academic situation, and also so that people interested in applying to CSE have one more data point they can use.
Before I was admitted, I would often stress out over whether I was good enough to be admitted, and so on.
Moreover, when people posted their grades online, they would often only list their overall GPA (not very useful, since prerequisite classes matter much more), their prerequisite GPA (more useful, but still doesn't provide a full picture), or even just their CSE 142/3 grades (and my CSE 143 grade wasn't as high as I had hoped it would be, so I was quite worried hearing almost everyone had gotten a 3.9 or 4.0 in that course)!
In light of this, I'd like to provide my "full stats" so people have more information.
Note that in many ways, this page is a lot like my UW transcript after the first year (just arranged differently, and with essays).

I'd like to note that while I don't think I was one of the strongest applicants, I certainly don't think I was one of the weakest either (even among those admitted).

One last note: during the new CSE admit orientation, one of the CSE advisors said that this admissions cycle was a "particularly brutal" one.

# General numbers

- Credits: 111
- GPA: 3.85
- Prerequisite GPA: 3.85 or 3.87, depending on whether you count the MATH 134 grade.[^p_gpa]

[^p_gpa]: Not counting MATH 134, in Python:

    ```python
    >>> import numpy as np
    >>> grades = np.matrix("3.9, 3.7, 3.9, 4.0, 3.8, 3.8")
    >>> credits = np.matrix("4; 5; 5; 5; 5; 5")
    >>> float(grades*credits)
    111.6
    >>> float(grades*credits/sum(credits))
    3.848275862068965
    ```

    Counting the 4.0 in MATH 134 (as my MATH 124) grade:

    ```python
    >>> import numpy as np
    >>> grades = np.matrix("3.9, 3.7, 3.9, 4.0, 4.0, 3.8, 3.8")
    >>> credits = np.matrix("4; 5; 5; 5; 5; 5; 5")
    >>> float(grades*credits/sum(credits))
    3.8705882352941177
    ```

# Employment

I listed no work experience (as I had none).

# Courses

## Prerequisites

- [CSE 142](): 3.9
- [CSE 143](): 3.7
- [ENGL 131](): 3.9
- MATH 124: AP^[The application lists "AP", but I actually took an IB test (IB Math HL, getting a 7/7) to satisfy this requirement.]
- [MATH 135](): 4.0
- [MATH 136](): 3.8
- [PHYS 121](): 3.8

## Recommended courses

The CSE application lists "represents recommended courses that this department would like to see", which as far as I can tell are simply courses that aren't a prerequisite that are nonetheless in CSE, ENGL, or MATH.

- [CSE 190](): CR
- [CSE 390 (for CSE 142)](): CR
- [CSE 390 (for CSE 143)](): CR
- ENGL 193: AP^[Again, from IB English HL.]
- [ENGL 478](): 4.0
- [MATH 134](): 4.0
- PHYS 114: AP^[All physics from IB Physics HL.]
- PHYS 115: AP
- PHYS 116: AP
- PHYS 117: AP
- PHYS 118: AP
- PHYS 119: AP

## Other courses

- [HONORS 100](): 4.0
- [HONORS 394](): 3.5
- [ATM S 559](): S^[That's right, I S/NSed a course and still got into CSE!]

# Department rank

I put "Computer Science: 1", i.e. I only applied to CSE.

# Essays

The following were my essays as submitted.
Note that the application asked not to use special characters, so I refrained from using smart quotes (i.e. curly quotes) in the submission form, but the essays below use smart quotes (since I think they look better).
You can check out the page source (see link at the top navigation bar) to see the source form, which still has the straight quotes.

I don't think my essays are that great.
I hope the message you get out of them is something like "Oh, I guess you don't need to write a very good essay to get in!"

## Short answer

**Prompt**: \[FIXME\]

In terms of diversity, I bring my cosmopolitan views, which can be seen in many different ways.

For instance, I grew up in Japan so have a fair amount of awareness of other cultures. Japan is especially interesting in computing because of its unique writing system that requires three different sets of characters. Being fluent in Japanese gives me sensitivity to the problems one can face in character input, dealing with character sets, translating software and websites, typography, and so on, which are all important considerations in computing.

I also love prying into people's minds in order to understand their psychology. To this end, I ask a lot of questions when I interact with people to understand and clarify their thinking. I have also asked nearly 3,000 questions on the question and answer site Quora about a huge array of topics. Many of them have the form "What is it like to do X?" or "What does X think about Y?", which allows me to consult the "hivemind".

In the past year, I've also become involved with a movement called effective altruism, which attempts to figure out how best to have a positive impact on the world. In particular, the movement is international, both in terms of supporters and those that the movement helps. Interacting with the people in this movement (both online and at local meetups) has allowed me to absorb their styles of thinking, which I can then incorporate into my own worldview.

## Personal statement

**Prompt**: \[FIXME\]

For a huge variety of reasons computer science has always intensely fascinated me. Roughly, these can be categorized in terms of impact on the world, the types of problems in the field, and the ethics (or social side) of the field.

In terms of impact on the world, I think computer science currently has the best shot at staying relevant in the coming years. The ongoing growth of technology companies like Google and Facebook means computer science will stay relevant. In addition, the huge applicability of computer science in for instance natural science research means that there is huge potential to apply one's computer science knowledge even in other domains. In other words, computer science allows one to be very versatile for the future. This flexibility is extremely important for me, since one of my goals is have the most positive impact I can have on the world (cf. effective altruism), which requires me to become continually productive.

Even in small ways, my current knowledge of computer science has already helped me in many (sometimes subtle) ways. My knowledge of regular expressions and web scraping, for example, allows me to effortlessly extract relevant information that I need instead of wasting time manually copying data. Or knowing about recursion has allowed me to reason about complicated problems in elegant ways. This relevance of computer science to solving real human needs, I think, is important: it means that what I learn is always connected to something tangible. This also means that when I help others with their computing tasks, the benefits will be visible in clear ways.

Computer science is also intellectually fascinating to me. Its brand of discrete and combinatorial problems are among those in mathematics that I find most satisfying to think about. For instance a while ago I was thinking with a friend about an exercise in an algorithms textbook that asked to devise a method to produce unbiased random numbers given a consistently-biased random number generator. Problems like these pique my interest because they make me think, "Wait, is this even possible?" There is also the eerie feeling that one can prove a fact about random number generation without even knowing that the biased random number generator exists!

I also think computer science has been the scene of some of the most interesting ethical debates. I'm insanely obsessed about free software and the freedom of information in general. My interest in computer science as a field extends into the past: I'm fascinated by the historical development of the free software movement, software patents, copyright law, and so on. Equally, I'm obsessed with how these ethical considerations are relevant today: information freedom, digital surveillance, online anonymity, and so forth. Ideally, I'd like to promote discussions on these topics within the CSE community to stimulate people's thinking.

Thus computer science is an exciting field for me in multiple ways. I've been fortunate to already experience some highly interesting aspects of the field. I only wish to continue this endeavor at UW CSE.

# Additional comments

I entered no additional comments on the application.

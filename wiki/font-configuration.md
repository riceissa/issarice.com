---
title: Font configuration
#description: none
author: Issa Rice
creation_date: 2015-01-01
last_major_revision_date: 2015-01-01
language: English
# accepts "notes", "draft", "in progress", or "mostly finished"
status: notes
# accepts "certain", "highly likely", "likely", "possible", "unlikely", "highly unlikely", "remote", "impossible", "log", "emotional", or "fiction"
#belief: 
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
tags: linux, debian, computing, font, tinkering, aesthetics
---

This is for Linux.
(I am using Debian GNU/Linux, but should work on other distros as well.)

The problem originally surfaced[^f] when I was trying to get Baskerville working on my Debian machine; on an iPad the Baskerville font rendered beautifully---and this was *not* just because of its greater pixel density.

[^f]: Or rather, the problem always existed, but I just didn't know that it *was* a problem\ ...\ .

On the other hand, on Debian, even when I had the correct Baskerville font installed
<!--
    Perhaps I should talk about all the fake Baskerville fonts out there!
-->(read: the identical one), I could not get text to display well.
Eventually I found [an ArchLinux forum thread about font rendering in Firefox](https://bbs.archlinux.org/viewtopic.php?pid=1260113).
This led me to [a post on the Gentoo forums](http://forums.gentoo.org/viewtopic-p-7273876.html#7273876), which had [a very good `/etc/fonts/local.conf` example file](https://dl.dropboxusercontent.com/u/18371907/local.conf).
I simply copied, it---after glancing at it; it seemed good---and now Baskerville essentially renders the same as on an iPad.
If you search inside the file for "Baskerville" you will find the relevant lines:

```{.xml}
<!-- Make these fonts use autohint slight hinting -->
<!-- Makes only horizontal stems align to pixels.  Truer to glyph -->
<match target="font">
    <test name="family"><string>Baskerville</string></test>
    <edit mode="assign" name="autohint"><bool>true</bool></edit>
    <edit mode="assign" name="hintstyle"><const>hintslight</const></edit>
</match>
```

In fact, Baskerville is not the only font to be helped by this: Computer Modern, which till now had only behaved well under LaTeX, now works rather well as well!
Even Linux Libertine (which I like very much; I regard it below only Computer Modern and Baskerville) looks much better; the problem I used to have with uneven open- and end-quotes has disappeared.

---I only wonder, why is this not the default on all Linux machines?

# Setting default font

Some notes:

- Setting on Firefox the default serif and sans fonts is a good idea.
Now even very plain websites like [WikiWikiWeb](http://c2.com/cgi/wiki?FrontPage) have Baskerville for me.
- For Japanese, IPAMincho and IPAGothic used to work best for me.
For some reason IPAexMincho and IPAexGothic used to produce awful thin lines---but following the font config described above, they are even prettier than IPAMincho and IPAGothic.

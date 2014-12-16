---
title: Playing with Pandoc
description: 
author: Issa Rice
creation-date: 2014-10-31
last-major-revision-date: 2014-10-31
language: English
status: draft
license: CC BY
tags: linux, pandoc
...

# Going from markdown to HTML

Answering "How can I write messages in Gmail using Markdown?" on Quora.

If you are on Linux and use a combination of tools like Vim, `xclip` , and `pandoc` [1], then this can easily be achieved. After composing the email in Vim, simply write the buffer directly into `pandoc` , convert the Markdown to HTML, and send that into the clipboard with `xclip`:

```bash
:w !pandoc -f markdown -t html | xclip -sel clip
```

Then just paste the results into Gmail using Control-V (or similar).\

This procedure can then be bound to a command or a keyboard shortcut for
repeated use.

If you in addition choose to write the Markdown buffer to a file, the
message will be locally backed up, as well as being on the Gmail servers
(which is good).

=\=\=\=\=\
[1]\: Of course, these can all be replaced in part or entirely with other
tools, as long as they have the necessary features. The editor must
either support Markdown–HTML conversion and be able to use the
clipboard, or else be able to interact with the shell, for instance.

# Going from HTML to markdown

Answering "Is there a service or program that lets you copy text from a website directly into Markdown, retaining all formatting?" on Quora.

This is possible using a combination of something like xclip and `pandoc`.
After copying the HTML text from a website, one can do `xclip -t text/html -o | pandoc -f html -t markdown` (or turn on the `-selection clip` flag on `xclip` if that doesn't work).

The other option, which is slighly more tedious, is to use something
like the online editor on WordPress and to paste in the HTML on the
"Visual" side and then go to the "Text" side to retrieve the converted
source for the HTML; then, place the source into a local HTML file (e.g.  `temp.html`) and run `pandoc` on it using something like `pandoc -o temp.md temp.html`.

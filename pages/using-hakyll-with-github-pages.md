---
layout: default
title: Using Hakyll with GitHub Pages
comments: ""
disqus-id:
math: ""
last-major-revision-date: 2014-08-28
license: "CC-BY"
tags: computing
...

- Hakyll doesn't seem to work well with Debian stable (Wheezy) since cabal and everything else (including pandoc) is out of date.  I had success upgrading to Debian unstable (sid).
- Installed pandoc using Debian repositories, but did `cabal install hakyll` for obtaining Hakyll itself.
- Add the cabal path to your `PATH` variable in bash: `PATH+=':$HOME/.cabal/bin`; do `echo $PATH` to make sure everything looks right.
- Everything compiled according to the tutorials given on the official website.
- problem with YAML headers: pandoc already has a fairly intelligent way of dealing with YAML headers, but hakyll will actually consume it on its own without allowing pandoc to see it (or so it seems to me).
hakyll, on the other hand, *doesn't* know what to do with more complex things like YAML lists.
Therefore, any time you want to do something intelligent with what is in the header (instead of just displaying it), you must write Haskell code to interpret it.
This is the case with tags.
This is irritating, but in the end it may be worth it. With tags, for instance, one would hope to do a lot more intelligent things with it than simply looping over and displaying them, so forcing it through Haskell may be better.
- author lists may be more interesting, since they are usually a list with dictionaries as items; writing this as a compressed YAML string will make it look ugly...

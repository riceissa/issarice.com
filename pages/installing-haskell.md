---
title: Installing Haskell (on Debian)
description: steps for installing the lastest version of Haskell on Debian Stable
tags: debian, haskell, cs
author: 
creation-date: 2014-09-14
last-major-revision-date: 2014-09-14
license: CC0
...

- [Chris Done](http://chrisdone.com/) pointed me to <https://github.com/bitemyapp/learnhaskell#debian>
- to get cabal, use <https://www.haskell.org/cabal/download.html>.
I had an older version of cabal already on my machine (1.20.0.0), so just deleted that from `~/.cabal/lib/i386-linux-ghc-7.4.1/` and then installed the new library. This way, `cabal-install` will use the new library (you can verify this with `cabal --version` once `cabal-install` is installed).

## Pandoc

Doing

```bash
# this is a test
cabal update
cabal install --force pandoc pandoc-citeproc
```

seemed to work. When I just did `cabal install hakyll` (since that is why I wanted Pandoc), the install failed with

```
pandoc-1.13.1 failed during the building phase. The exception was:
ExitFailure 1
```

(See <https://groups.google.com/forum/#!topic/pandoc-discuss/NbredqPHVCg>, which may or may not be relevant.)


Since I had some really old versions of Pandoc and cabal on my machine (from the Debian repositories), I just redefined my path with `$HOME/.cabal/bin` as the first item, so that the newer programs in there would take priority.

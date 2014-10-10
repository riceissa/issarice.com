---
title: Installing Haskell (on Debian)
description: steps for installing the lastest version of Haskell on Debian Stable
tags: debian, haskell, cs
creation-date: 2014-09-14
last-major-revision-date: 2014-09-14
license: CC0
...

- [Chris Done](http://chrisdone.com/) pointed me to [this page](https://github.com/bitemyapp/learnhaskell#debian)
- to get cabal, use [this](https://www.haskell.org/cabal/download.html).
I had an older version of cabal already on my machine (1.20.0.0), so just deleted that from `~/.cabal/lib/i386-linux-ghc-7.4.1/` and then installed the new library. This way, `cabal-install` will use the new library (you can verify this with `cabal --version` once `cabal-install` is installed).

## On a new machine

This is how I would do it given a new Debian stable machine with no previous installations of Haskell.
It's easy to just install `haskell-platform`, but this introduces an older version of cabal, which may or may not be annoying.
The following is the minimal way to get things installed.

```bash
sudo aptitude install ghc ghc-haddock zlib1g-dev # or maybe libghc-zlib will work too; actually, "libghc-zlib-dev" will pull "zlib1g-dev" so it doesn't really matter
wget https://www.haskell.org/cabal/release/cabal-install-1.20.0.3/cabal-install-1.20.0.3.tar.gz
tar -zxf cabal-install-1.20.0.3.tar.gz && rm cabal-install-1.20.0.3.tar.gz
./bootstrap.sh
echo "PATH+=':$HOME/.cabal/bin'" >> ~/.bashrc
cabal update && cabal install cabal cabal-install alex happy
```



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

(See the [discussion here](https://groups.google.com/forum/#!topic/pandoc-discuss/NbredqPHVCg), which may or may not be relevant.)


Since I had some really old versions of Pandoc and cabal on my machine (from the Debian repositories), I just redefined my path with `$HOME/.cabal/bin` as the first item, so that the newer programs in there would take priority.


## Hakyll

did not work when I just did `cabal install hakyll`. I had to force install Pandoc again and then do `cabal install hakyll` once more. Strange...

2014-10-10: I had to do `cabal --force-reinstall install hakyll`. waiting to see if it works...

---
title: Installing Haskell
created: 2014-09-14
date: 2014-09-14
---

- [Chris Done](http://chrisdone.com/) pointed me to [this page](https://github.com/bitemyapp/learnhaskell#debian)
- to get cabal, use [this](https://www.haskell.org/cabal/download.html).
I had an older version of cabal already on my machine (1.20.0.0), so just deleted that from `~/.cabal/lib/i386-linux-ghc-7.4.1/` and then installed the new library. This way, `cabal-install` will use the new library (you can verify this with `cabal --version` once `cabal-install` is installed).

# On a new machine

This is how I would do it given a new Debian stable machine with no previous installations of Haskell.
It's easy to just install `haskell-platform`, but this introduces an older version of cabal, which may or may not be annoying.
The following is the minimal way to get things installed.

There might be some unexpected problems when executing the commands below.
On Linux Mint (either 17.1 or 17.3), I couldn't install `cabal-install-1.22.9.0` because `bootstrap.sh` complained about not having `transformers` version 0.4 (the Linux Mint repositories have 0.3).
However, installing from the older `cabal-install-1.22.4.0` seems to work.
On the other hand, Ubuntu MATE 16.04 seems to have no problem with version 1.22.9.0 (but had documenting issues with 1.24.0.0).
(This is intended as an example of a problem one might run into, and not as an exhaustive list of issues.)

```bash
sudo aptitude install ghc ghc-haddock zlib1g-dev # or maybe libghc-zlib
                                    # will work too; actually, 
                                    # "libghc-zlib-dev" will pull
                                    # "zlib1g-dev" so it doesn't really
                                    # matter
wget https://www.haskell.org/cabal/release/cabal-install-1.20.0.3/cabal-install-1.20.0.3.tar.gz
tar -zxf cabal-install-1.20.0.3.tar.gz && rm cabal-install-1.20.0.3.tar.gz
# on Linux Mint using cabal-install-1.22.4.0.tar.gz, I also had to install ghc-prof and ghc-dynamic for this to work.
./bootstrap.sh
echo "PATH+=':$HOME/.cabal/bin'" >> ~/.bashrc
cabal update && cabal install cabal cabal-install alex happy
```



# Pandoc

Doing

```bash
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
See also the article about [avoiding "Cabal hell"](http://softwaresimply.blogspot.com/2014/07/haskell-best-practices-for-avoiding.html).

To update Pandoc to the latest version on Debian, I recently (2015-11-27) did:

```{.bash}
cabal update
cabal install cabal
cabal install --max-backjumps=-1 --reorder-goals --force-reinstalls pandoc
```

# Hakyll

did not work when I just did `cabal install hakyll`. I had to force install Pandoc again and then do `cabal install hakyll` once more. Strange...

2014-10-10: I had to do `cabal --force-reinstall install hakyll`. waiting to see if it works...

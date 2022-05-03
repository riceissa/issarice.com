---
title: Debian installation notes
tags: linux, debian
---

We start from a base system.
Most of these steps can actually now be automated using my [dotfiles](https://github.com/riceissa/dotfiles); the software, in particular, can all be found in [`debian_packages.py`](https://github.com/riceissa/dotfiles/blob/master/debian_packages.py).

# Basic utilities

~~~bash
su
aptitude install sudo
update-alternatives --config editor # set to vi
visudo # add user
# Ctrl-D to exit
~~~

~~~bash

sudo aptitude install iceweasel
sudo aptitude install keepassx
sudo aptitude install iceweasel-adblock-plus
~~~


## Audio

```
sudo aptitude install pulseaudio pavucontrol
```

Just make sure to log out or reboot; then audio should be working.


## Installing Haskell

See [this page](http://riceissa.com/installing-haskell).

TODO:



- how to get it so that i can easily switch between versions of python? (but this isn't necessary, since even debian has decent versions)
- dropbox?
- Java?
- non-free packages
- evernote?
- flash?
- surfraw config
- vim /etc/apt/sources.list
- sudo aptitude install flashplugin-nonfree
- install duckduckgo plugin

- for getting Source Code Pro on LXDE:
I extracted the archive from [here](https://github.com/adobe-fonts/source-code-pro/releases/latest), then did the following from the directory containing the `.otf` files:

~~~bash
sudo mkdir /usr/share/fonts/SourceCodePro
sudo cp * /usr/share/fonts/SourceCodePro/
mkfontscale
mkfontdir
fc-cache
~~~

(as shown [here](http://forum.lxde.org/viewtopic.php?f=8&t=1914#p5573))
I'm not exactly sure which steps are required.
`mkfontdir` seemed to create a `fonts.dir` in the current directory, so perhaps that was unnecessary considering that I had already moved all my fonts to the system directory.)

For finding pages for my website repository:

```bash
findAllPagesWith() {
    find ~/projects/riceissa.com/pages -iname "*$1*"
}

alias fp=findAllPagesWith
```

# Website compilation

- get all the prerequisites; just install `python-pip` and then do

```
pip install --user jinja2
pip install --user pyyaml
pip install --user pandocfilters
pip install --user awesome-slugify
sudo aptitude install ruby-sass
```

which should take care of most problems.
Make sure you have the latest Pandoc version (at least 1.13) though.

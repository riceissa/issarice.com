---
title: Debian installation notes
...

We start from a base system.

## Basic utilities

~~~bash
su
aptitude install sudo
update-alternatives --config editor # set to vi
visudo # add user
# Ctrl-D to exit
~~~

~~~bash
sudo aptitude install vim git python htop python3 pandoc elinks

# I did this one first, but then couldn't get the login screen to show up for LXDE (couldn't get X to start up...). I probably could have done it this way though, so that I would have an even more minimal setup.
sudo aptitude install lxde-core
# Doing this worked
sudo aptitude install lxde

sudo aptitude install iceweasel
sudo aptitude install keepassx
sudo aptitude install iceweasel-adblock-plus
~~~

get vim config from here: https://github.com/riceissa/vim

## Setting your Git info

~~~bash
git config --global user.name "First Last"
git config --global user.email "name@example.com"
~~~

### Audio

```
sudo aptitude install pulseaudio pavucontrol
```

Just make sure to log out or reboot; then audio should be working.


### Installing Haskell

See [this page](http://riceissa.com/installing-haskell).

TODO:



- how to get it so that i can easily switch between versions of python? (but this isn't necessary, since even debian has decent versions)
- dropbox?
- Java?
- non-free packages
- evernote?
- flash?
- surfraw config
- tmux config
vim /etc/apt/sources.list
sudo aptitude install flashplugin-nonfree
- install duckduckgo plugin
- set up MOC config file

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

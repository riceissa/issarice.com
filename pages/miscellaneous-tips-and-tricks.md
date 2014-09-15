---
layout: default
title: Miscellaneous Tips and Tricks
comments: "yes"
disqus-id: 71ad5a09b2dff55d25260e2918efb896b82ce578
math: ""
last-major-revision-date:
license: "CC-BY"
tags: computing
---


## Changing the Default Editor

To change the default editor on Debian, run:

    $ sudo update-alternatives --config editor

On other systems, the `$EDITOR` variable can be set:

    $ echo $EDITOR
    
    $ which vim
    /usr/bin/vim
    $ export EDITOR=/usr/bin/vim
    $ echo $EDITOR
    /usr/bin/vim

## Convert from HTML to Plain Text

To convert from HTML to plain text, just type:

    $ cat filename.html | sed 's/<[^>]*>//g' | tr -s '\n'

## Wget (Recursive Download)

Recursively download all text files to the current directory:

    $ wget --no-directories --no-host-directories --recursive --no-parent --accept txt ⟨URL⟩

Or equivalently:

    $ wget -nd -nH -r -np -A txt ⟨URL⟩

## Disable Bluetooth

To disable Bluetooth, use [`rfkill`](http://linuxwireless.org/en/users/Documentation/rfkill).

[On Debian, the package is called `rfkill`](http://packages.debian.org/squeeze/rfkill).
Once the package is installed, Bluetooth may be disabled by running:

    $ sudo rfkill block bluetooth

This command may also be placed in `/etc/rc.local` (or an alternative startup script) so that the command executes each time at boot.
For example:

~~~~
$ which rfkill
/usr/sbin/rfkill
$ sudo vim /etc/rc.local
(add the following line before 'exit 0')
/usr/sbin/rfkill block bluetooth
$ sudo reboot # to see if it works
~~~~

Running `which rfkill` is important because `rfkill` may be located elsewhere on your system.
Using the absolute path is recommended to avoid confusion.

Source: <http://unix.stackexchange.com/questions/4761/how-to-ensure-the-bluetooth-is-switched-off-after-boot-up>

## Hard Disk Drive Formatting (command line)

Partitioning through the command line is split into two steps:

1. partitioning the drive (with `fdisk`), and
1. creating the file system (with `mkfs`).

~~~~
$ man fdisk # read this before blindly following
$ sudo fdisk -l /dev/⟨xyz⟩ # this lists the current file systems on this drive; make sure you change ⟨xyz⟩ for your drive
$ sudo fdisk /dev/⟨xyz⟩
(type these into fdisk's prompt:)
m
d
n
defaults
w
$ man mkfs # read this too
$ sudo mkfs /dev/⟨xyzn⟩ # n is the partition number; most likely 1.
$ sudo fsck
$ sudo vim /etc/fstab
(add the following line to mount the disk at boot)
/dev/xyzn /mnt/point auto defaults 0 0
~~~~

If you have it, [gparted](http://gparted.sourceforge.net/) also works well.

## Formatting Text

You can use a pager like `less`, but if you want a better output, you can try the following commands.
(You can even pipe the output to `less`!)

### Using `fold`

    $ cat ⟨filename⟩ | fold --spaces --width=72 | sed 's/\(.\)/    \1/' # four spaces

The `--spaces` option makes the text split on spaces so words will not be cut off at the edge of the screen.
`--width=72` allows for 8 characters of margin space; we will use 4 on each side.

Original text using `cat` or `less`:

~~~~
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostr
ud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis au
te irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qu
i officia deserunt mollit anim id est laborum.
~~~~

After using the above command (note that words are no longer cut off):

~~~~
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do 
    eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad 
    minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip 
    ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
    voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur 
    sint occaecat cupidatat non proident, sunt in culpa qui officia 
    deserunt mollit anim id est laborum.
~~~~

### Using `par`

If you have `par` you can use it instead:

    $ cat ⟨filename⟩ | par -j -w 72 | sed 's/\(.\)/    \1/' # four spaces again

The `-j` option justifies the text, and `-w 72` sets the width to 72 characters.

After using `par`:

~~~~
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt  ut labore et  dolore magna  aliqua. Ut enim  ad minim
    veniam, quis nostrud exercitation ullamco  laboris nisi ut aliquip ex ea
    commodo consequat. Duis  aute irure dolor in  reprehenderit in voluptate
    velit  esse  cillum dolore  eu  fugiat  nulla pariatur.  Excepteur  sint
    occaecat  cupidatat non  proident, sunt  in culpa  qui officia  deserunt
    mollit anim id est laborum.
~~~~

## How to Tell If You’re in a Git Directory

    $ git branch >/dev/null 2>/dev/null || echo not git; git branch >/dev/null 2>/dev/null && echo git

## Debian Networking

To start a network in Debian, run:

    $ sudo dhclient eth0

## Configure WiFi (command line)

For more information, please see the [Arch Linux Wiki](https://wiki.archlinux.org/index.php/Wireless_Setup).

~~~~
# /etc/network/interfaces
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug eth0
iface eth0 inet dhcp

# Custom setting below
auto wlan0
iface wlan0 inet dhcp
wpa-ssid ⟨NETWORKNAME⟩
wpa-psk ⟨PASSWORD⟩
~~~~

## Scan for WiFi Networks

    $ iwlist wlan0 scan

## Sound Card Configuration

Here is how to change the default sound card on Debian 6 “Squeeze”:

    $ echo 'options snd slots=snd-emu10k1,snd-via82xx' | sudo tee -a /etc/modprobe.d/alsa-base.conf

Or, more generically:

    $ echo 'options snd slots=snd-⟨NEW_DEFAULT⟩,snd-⟨OLD_DEFAULT⟩' | sudo tee -a ⟨/path/to/configuration/file⟩

Try `alsaconf` if you don't know which sound card you have.

Source: <http://alsa.opensrc.org/MultipleCards#The_newer_.22slots.3D.22_method>

## `ww.sh`

`ww.sh` is a small shell script that can be used to keep a log.

Here’s the script.
The script depends on Vim and Bash:

~~~~
#!/bin/bash
echo 'Title:'
read x
y="$(date "+%d %b %Y") @ $(date "+%H:%M:%S"): $x"
echo -e "\n$y\n" >> ~/⟨some text file⟩
vim + ~/⟨some text file⟩
~~~~

Make sure you modify permissions to allow execution:

    $ chmod u+x ww.sh

Run the script by typing:

    $ ./ww.sh

You can also alias the scipt to allow quick access:

    $ alias ww='⟨/path/to/ww.sh⟩'

## OpenBSD Configuration Files

`rc.local`:

    wsconsctl keyboard.map+="keysym Caps_Lock = Escape"

`.xinitrc`:

    exec xmodmap ~/.disable_caps_lock_x &
    exec openbox-session

`.profile`:

~~~~
# $OpenBSD: dot.profile,v 1.4 2005/02/16 06:56:57 matthieu Exp $
#
# sh/ksh initialization

PATH=$HOME/bin:/bin:/sbin:/usr/bin:/usr/sbin:/usr/X11R6/bin:/usr/local/bin:/usr/local/sbin:/usr/games:.
export PATH HOME TERM
export PKG_PATH=ftp://ftp.openbsd.org/pub/OpenBSD/4.9/packages/i386/
export ENV=$HOME/.kshrc

.disable_caps_lock
remove Lock = Caps_Lock
keysym Caps_Lock = Escape
~~~~

## Change urxvt Font

    $ urxvt -fn "xft:Terminus:pixelsize=15"

## Configure Mutt

Make sure the file is not readable by anyone except you:

    $ chmod 600 ~/.muttrc

~~~~
# ~/.muttrc
set imap_user = "⟨USERNAME@gmail.com⟩"
set imap_pass = "⟨PASSWORD⟩"

set folder = "imaps://imap.gmail.com:993"
set spoolfile = "imaps://imap.gmail.com:993/INBOX"
set postponed="imaps://imap.gmail.com/[Gmail]/Drafts"

# for more information about different ports, see this page:
# http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
set smtp_url = "smtp://⟨USERNAME⟩@smtp.gmail.com:587/"
set smtp_pass = "⟨PASSWORD⟩"
set from = "⟨USERNAME⟩@gmail.com"
set realname = "⟨First Last⟩"

set message_cachedir="~/.mutt/cache/bodies"
set certificate_file="~/.mutt/certificates"
~~~~

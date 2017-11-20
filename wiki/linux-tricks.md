---
title: Linux tricks
date: 2016-06-20
---


# Changing the Default Editor

To change the default editor on Debian, run:

    $ sudo update-alternatives --config editor

On other systems, the `$EDITOR` variable can be set:

    $ echo $EDITOR
    
    $ which vim
    /usr/bin/vim
    $ export EDITOR=/usr/bin/vim
    $ echo $EDITOR
    /usr/bin/vim

# Convert from HTML to Plain Text

To convert from HTML to plain text, just type:

    $ cat filename.html | sed 's/<[^>]*>//g' | tr -s '\n'

# Wget (Recursive Download)

Recursively download all text files to the current directory:

    $ wget --no-directories --no-host-directories --recursive --no-parent --accept txt ⟨URL⟩

Or equivalently:

    $ wget -nd -nH -r -np -A txt ⟨URL⟩

# Disable Bluetooth

To disable Bluetooth, use [`rfkill`](https://web.archive.org/web/20170407083428/http://www.linuxwireless.org:80/en/users/Documentation/rfkill/).

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

[Source](http://unix.stackexchange.com/questions/4761/how-to-ensure-the-bluetooth-is-switched-off-after-boot-up).

# Hard Disk Drive Formatting (command line)

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

# Formatting Text

You can use a pager like `less`, but if you want a better output, you can try the following commands.
(You can even pipe the output to `less`!)

## Using `fold`

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

## Using `par`

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

# How to Tell If You’re in a Git Directory

    $ git branch >/dev/null 2>/dev/null || echo not git; git branch >/dev/null 2>/dev/null && echo git

# Debian Networking

To start a network in Debian, run:

    $ sudo dhclient eth0

# Configure WiFi (command line)

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

# Scan for WiFi Networks

    $ iwlist wlan0 scan

# Sound Card Configuration

Here is how to change the default sound card on Debian 6 “Squeeze”:

    $ echo 'options snd slots=snd-emu10k1,snd-via82xx' | sudo tee -a /etc/modprobe.d/alsa-base.conf

Or, more generically:

    $ echo 'options snd slots=snd-⟨NEW_DEFAULT⟩,snd-⟨OLD_DEFAULT⟩' | sudo tee -a ⟨/path/to/configuration/file⟩

Try `alsaconf` if you don't know which sound card you have.

[Source](http://alsa.opensrc.org/MultipleCards#The_newer_.22slots.3D.22_method)

# `ww.sh`

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

# OpenBSD Configuration Files

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

# Change urxvt Font

    $ urxvt -fn "xft:Terminus:pixelsize=15"

# Configure Mutt

Moved to [Mutt]().

# Other commandline notes

```bash
fbterm --font-names="Source Code Pro" --font-size=14
```

```bash
alias fb='fbterm --font-names="Source Code Pro" --font-size=14'
```


See [here](https://github.com/sigurdga/gnome-terminal-colors-solarized)
and [here](http://www.webupd8.org/2011/04/solarized-must-have-color-paletter-for.html)
for getting Solarized to work with Gnome Terminal.
also cf. [this post](http://www.terminally-incoherent.com/blog/2013/12/30/tools-you-need/)

Updating Flash player (Debian):

```
sudo update-flashplugin-nonfree --install
```

# Fixing permissions

- Reinstall packages (e.g. lightdm) to get fresh copies of certain configs
- see <http://stackoverflow.com/questions/21716426/cant-apt-get-remove-or-apt-get-install-fopen-permission-denied> also

# Changing swappiness

On Debian/Ubuntu/Linux Mint:

```bash
# check swappiness value
$ cat /proc/sys/vm/swappiness 
60
# change to a lower value, which means RAM will more aggressively be
# used
$ sudo sysctl vm.swappiness=10
$ cat /proc/sys/vm/swappiness 
10
```

See also [here](http://unix.stackexchange.com/a/2664) for how to change it permanently by editing `/etc/sysctl.conf` to include the line `vm.swappiness=10`.

# Check font aliases

```bash
$ fc-match "Charter"
DejaVuSans.ttf: "DejaVu Sans" "Book"
$ fc-match "Arial"
Arial.ttf: "Arial" "Normal"
```

Also try `fc-list` for the exact locations.

# Audio glitches/stuttering/repeating

Upgrading on Ubuntu/Linux Mint caused odd audio glitches while playing music.
As is often the case, the [Arch Wiki](https://wiki.archlinux.org/index.php/PulseAudio/Troubleshooting#Glitches.2C_skips_or_crackling) was most helpful.
Open `/etc/pulse/default.pa` and add the following line at the end:

```
load-module module-udev-detect tsched=0
```

The following *might* work:

```bash
$ pulseaudio -k
$ pulseaudio --start
```

On my machine, Pulseaudio failed to restart after being killed, but rebooting fixed one of the problems, namely the stuttering.
Now I get strange popping sounds once in a while, especially when both MOC and Facebook try to produce a sound simultaneously.
I added the line

```
options snd-hda-intel vid=8086 pid=8ca0 snoop=0
```

to `/etc/modprobe.d/sound.conf` (as in the Arch Wiki, which was originally empty), but that didn't seem to fix it.
Seeing [this thread](http://ubuntuforums.org/showthread.php?t=2230750), I have now placed the same line in `/etc/modprobe.d/alsa-base.conf` (which was not empty).

Note though that while the stuttering was so annoying as to make the computer unusable (since I like listening to music while I work), the occasional popping is much less annoying, and I can probably live with it for now.

It might also possibly be some sort of power saving option kicking in.
See [here](http://www.howtoeverything.net/linux/issues/remove-whistling-and-popping-sounds-intel-hda) if nothing works.

# Use less like `tail -f`

Instead of

```
tail -f filename
```

to continuously monitor the end of a file, it is possible to issue

```
less +F filename
```

One can then hit `Ctrl`-`c` to return to regular less, and hit `F` to return to the `tail -f` mode again.

# `tee /dev/tty`

Piping output through `tee /dev/tty` allows you to print to stdout as well as pass it along to another process.
I find it useful to pass output to xclip while also seeing what was copied.
For instance

```bash
$ cat somefile | tee /dev/tty | xclip -sel clip
```

allows you to copy the contents of `somefile` into your clipboard while also seeing what is in the file.

# sponge

sponge (from moreutils) allows you to pipe something to a file while also reading from it first.
So for instance:

```bash
$ cat somefile | grep keyword | sponge somefile
```

Without sponge, you would first have to redirect the output of `cat somefile | grep keyword` to a temporary file, because simply doing

```bash
$ cat somefile | grep keyword > somefile
```

would blank `somefile`.

# System free on excessive RAM usage

This is probably the single most annoying thing on Linux for me right now.
Just some links for now:

- [How to Configure the Linux Out of Memory Killer](http://www.oracle.com/technetwork/articles/servers-storage-dev/oom-killer-1911807.html)
- [What to do when a linux desktop freezes?](https://unix.stackexchange.com/questions/31818/what-to-do-when-a-linux-desktop-freezes)
- [How do I prevent Linux from freezing when out of memory?](https://serverfault.com/questions/390623/how-do-i-prevent-linux-from-freezing-when-out-of-memory)
- [Bug \#1504914 “System freeze/restart on high memory usage” : Bugs : linux package : Ubuntu](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1504914)
- [Computer freezing on almost full RAM, possibly disk cache problem](https://askubuntu.com/questions/41778/computer-freezing-on-almost-full-ram-possibly-disk-cache-problem)

Things that work for me:

- `SysRq`-`f` (on my X220, this is pressed as `Alt`-`PrtSc`-`f`)

Things that don't work for me:

- Setting aside memory
- Setting the swappiness

Things that I haven't tried:

- Using `ulimit` to limit the memory per process

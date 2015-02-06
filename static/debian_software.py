#!/bin/python


# This script installs some common tools used on a Debian GNU/Linux
# system.  Comment or uncomment to select the programs that you want to
# install.  Since this script needs Python to run, it might be necessary
# to do (assuming you have sudo) `sudo aptitude install python` or `sudo
# apt-get install python` first.  In addition, this program uses
# aptitude to install software instead of apt-get, so if you only have
# apt-get, either change all instances of "aptitude" to "apt-get" or
# else do `sudo apt-get install aptitude`.

from subprocess import call

# List of programs to install.
programs = [
# "Essential" utilities:
"vim",
"vim-gtk", # for gundo, which requires python
"python3",
"python-pip",
"python-dev", # for website
"htop",
"pandoc",
"elinks",
"git",
#"mercurial",

#"lynx-cur",

"python-gpgme", # for Dropbox
"ruby-sass", # for website

# More advanced utilities:
"surfraw",
"par",
"detox",
"xclip",
"wodim",
"gparted",

# Tmux and screen ... and byobu
"tmux",
#"screen",
#"byobu",

# Programming-related:
"build-essential",
"flex",
"bison",
"gcc",
r"g\+\+",
"ruby",
"openjdk-7-jre",
"openjdk-7-jdk",

# For Haskell, it's a good idea to get GHC, Haddock, and zlib, but
# getting the entire Haskell platform is not a good idea since the one
# in Debian is outdated.  Instead, use the notes provided here:
# http://riceissa.com/installing-haskell to get an up-to-date version of
# the Haskell platform.
"ghc",
"ghc-haddock",
"libghc-zlib-dev",

# Music On Console is a lightweight and easy-to-use commandline audio
# player.
#"moc", # Run using 'mocp'.
#"moc-ffmpeg-plugin", # Extra plugins.

# Support for Japanese:
#"ibus-anthy",
#"fonts-ipafont",
# On the command line, type 'ibus-setup' to bring up the IBus
# preferences.  Under "Input Method" > "Select an input method" >
# "Japanese", find "Anthy" and click.  Click "Add" to add it to the list
# of input methods.  You can now close the window.  You must logout once
# in order to enable Japanese input.  To switch to Japanese input, hit
# <Ctrl>-<Space> while in a text-field.

# For Japanese on the commandline, see http://riceissa.com/japanese-input-on-the-command-line-framebuffer

# LaTeX (warning: large download):
#"texlive-full",

"gdebi",

# For the Acer laptop; Wi-Fi driver and bluetooth diabler.
# Make sure to enable 'non-free' and 'contrib' for the driver.
#"firmware-iwlwifi",
#"rfkill",

# For the PowerBook Mac
#"firmware-b43-installer",

# Some media-related tools:
#"cdparanoia",
#"flac",
#"vlc",
#"vorbis-tools",

#"bsdgames",

# note you might have to install the oxygen theme for this to work
"okular", # essentially the best PDF viewer, even if it drags in all the KDE dependencies...


# Openbox
#"xorg",
#"openbox",
#"obconf",
#"obmenu",
#"rxvt-unicode",
#"iceweasel",
#"gtkchtheme",
#"emelfm2",
#"leafpad",
#"mirage",
#"epdfview",

#"gnupg",
#"virtualbox-ose",
#"wine",

# These are packages (or in some cases non-packages) that still have not
# been sorted.
#"hexer",
#"mc",
#"flashplugin-nonfree",
#"alsaequal",
#"antiword",
#"aspell",
#"detox",
#"dict",
#"fbgrab",
#"fim",
#"mplayer",
#"o3read",
#"odt2txt",
#"renameutils",
#"rtorrent",
#"recorder",
#"eatdoc",
#"catppt",
#"espeak",
#"vlock",
#"dtrx",
#"cmatrix",
#"openssl",
#"docx2txt",

# gitosis, gitolite?
# openssl-server?
# get scheme! keepass(X)
]

# Update sources and upgrade system:
#call("sudo aptitude update && sudo aptitude upgrade", shell=True)

# Install programs:
#call("sudo aptitude install {programs}".format(programs=' '.join(programs)), shell=True)


# Some commands for Bash:
call('''echo "PS1='[\u:\W]> '" >> ~/.bashrc''', shell=True)
call('''echo "alias {upgrade,update}='sudo aptitude update && sudo aptitude -y upgrade'" >> ~/.bashrc''', shell=True)
#call('''echo "alias ls='ls --color'" > ~/.bashrc''', shell=True)

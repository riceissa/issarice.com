---
title: Music On Console
author: Issa Rice
created: 2016-12-15
date: 2016-12-15
---

For my music player, I use Music On Console (MOC). (May 2022: This is old. Ever since I switched to Windows in April 2021, I've just been using YouTube and VLC for music, not even a dedicated music player.)

To avoid keeping system-specific paths in the configuration file, one can pass
certain options when invoking the program:

    mocp -O MusicDir=/home/issa/Music -O FastDir1=/media/issa/wd1/Music

The above allows me to press `m` to visit the `Music` folder in my home
directory, and `!` to visit the `Music` folder on an external drive.

My configuration files are [available on
GitHub](https://github.com/riceissa/dotfiles/tree/master/.moc).

# See also

* [[software I use]] for more about the software I use

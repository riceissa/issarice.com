---
title: Export Chrome history
author: Issa Rice
created: 2016-12-25
date: 2016-12-25
---

# Introduction

This page explains how to export one's Google Chrome history on Ubuntu.
Parts of this page should work for Chromium and for other operating systems as
well but I don't make any guarantees.

# Locating the history file

The history database is located at `~/.config/google-chrome/Default/History`
for Google Chrome.

For Chromium, it is located at `~/.config/chromium/Default/History`.

The locations may differ if you have multiple Chrome profiles.

Neither file has an extension, but they are databases that can be queried using
SQLite.

# Creating the dump

I recommend the following before continuing:

* Close Chrome
* Make a copy of the history file and work with this copy instead of the actual
  history file

Then run the following commands:

    $ sqlite3 History
    sqlite> .headers on
    sqlite> .mode csv
    sqlite> .output out.csv
    sqlite> SELECT datetime(last_visit_time/1000000-11644473600,
       ...> 'unixepoch', 'localtime') as 'date',url FROM urls
       ...> ORDER BY last_visit_time DESC;
    sqlite>

Press `CTRL`-`D` to exit sqlite3 after the final prompt.

Chrome seems to use FILETIME for representing time, whose [epoch][epoch] and
unit length both differ from those of Unix time; hence the dividing and
subtracting.

# External links

* [Answer to "Can Chrome browser history be exported to an HTML
  file?"](http://superuser.com/a/602274); the sqlite3 commands are from this
  answer.

[epoch]: https://en.wikipedia.org/wiki/Epoch_(reference_date)

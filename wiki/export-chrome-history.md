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

Then run the following command in a shell to get a list of visited URLs, sorted
by last visit date:

    sqlite3 -header -csv History "SELECT \
        datetime(last_visit_time/1000000-11644473600, 'unixepoch', \
        'localtime') as 'date',url FROM urls ORDER BY \
        last_visit_time DESC;" > out.csv

Chrome seems to use FILETIME for representing time, whose [epoch][epoch] and
unit length both differ from those of Unix time; hence the dividing and
subtracting.
Then the `'unixepoch'` converts the Unix time to a date and time, and
`'localtime'` adjusts for timezone differences ([see the
documentation](https://www.sqlite.org/lang_datefunc.html)).

The above limits output to a single line for each URL.
To obtain a more complete browsing history, one must combine the `urls` table
with the `visits` table.
Run the following command to obtain a history of visits, where each URL can
occur multiple times:

    sqlite3 -header -csv History "SELECT \
        datetime(visits.visit_time/1000000-11644473600, 'unixepoch', \
        'localtime') as 'visit_time',urls.url from urls,visits \
        WHERE urls.id = visits.url ORDER BY visit_time DESC" > out.csv

# External links

* [Answer to "Can Chrome browser history be exported to an HTML
  file?"](http://superuser.com/a/602274); the sqlite3 commands are from this
  answer.

[epoch]: https://en.wikipedia.org/wiki/Epoch_(reference_date)

---
title: Durable link
#description: none
author: Issa Rice
creation-date: 2015-01-01
last-major-revision-date: 2015-01-01
language: English
# accepts "notes", "draft", "in progress", or "mostly finished"
status: notes
# accepts "certain", "highly likely", "likely", "possible", "unlikely", "highly unlikely", "remote", "impossible", "log", "emotional", or "fiction"
#belief: 
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
tags: untagged
...

A durable link is one that is not susceptible to [link rot](http://www.gwern.net/Archiving%20URLs#link-rot).
gwern already does a good job of summarizing the issue, with his corrections.
But for this website, I've written a custom URL filter that takes links of the form `[test](!STRING)` and converts them into a [DuckDuckGo bang expression](https://duckduckgo.com/bang.html).
For instance, writing `[Fishmans](!w)` will search Wikipedia for the string "Fishmans", and will take you to the page for the band [Fishmans](music-i-like-to-listen-to).
In a sense, I think this will make more of my links robust.
I have, for instance, the choice to link to a Google query of the coding project's name or to its actual website.
One may then ask: "Which link would be more robust?"
Given that many projects suffer from link rot (moving location, being deleted, etc.), I would suppose that a Google query would be much more robust in the long term.
Even if a project has been taken down, search results would presumably contain hints to that effect.
Of course, having the actual link will be most useful if one wants to use Archive.org or a similar online archive...

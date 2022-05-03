---
title: URL parsing
author: Issa Rice
created: 2016-07-30
date: 2016-07-30
---

*Note: this was originally written as an answer to the Quora question ["Are
there URLs one cannot send over Facebook messenger due to its broken URL
parsing?"][question].*

Yes, at least if you want the URL to be clickable. One instance where this
happens is if a URL ends with `*` (a star or asterisk). Facebook interprets a
star followed by a space to be the end of a URL (and does not include the star
in the URL), so one cannot click to navigate to `http://exp.issarice.com/lol/*`,
since it will go instead to `http://exp.issarice.com/lol/`. Percent-encoding the
URL results in `http://exp.issarice.com/lol/%2A`, but this displays a different
page in this demo. (Try going to both the version with the `*` and with the
`%2A`.)

Here’s what I get using curl:

    % curl 'http://exp.issarice.com/lol/*'
    You cannot access this by clicking on Facebook!
    % curl 'http://exp.issarice.com/lol/%2A'
    This URL was URL-encoded so can be clicked on Facebook.

This demo was created on nginx with the following:

    location = /lol/* {
        if ($request_uri = "/lol/*") {
            return 200 "You cannot access this by clicking on Facebook!";
        }
        if ($request_uri = "/lol/%2A") {
            return 200 "This URL was URL-encoded so can be clicked on Facebook.";
        }
    }

One might feel this is quite contrived, but I actually first encountered it when
trying to send an [archive.org](http://archive.org) link to a friend. The URL
ending with `*` (which Facebook cannot send) was interpreted to mean “search all
the URLs in this domain”, whereas the percent-encoded URL ending in `%2A` was
interpreted to mean “find the URL in this domain containing just `%2A`”.

I also encountered a problem once when I sent a series of long URLs in a single
message (I’ll have to dig that example up).

[question]: https://www.quora.com/Are-there-URLs-one-cannot-send-over-Facebook-messenger-due-to-its-broken-URL-parsing

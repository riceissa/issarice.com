---
title: Revisiting the “great decline” in Wikipedia pageviews
date: 2016-09-21
---

# Introduction

In March 2015 one of us (Vipul Naik) wrote "The great decline in Wikipedia
pageviews".
This post is intended as an update to some of the points from that article,
along with some graphs.

Data sources:

  * Wikipedia Views (stats.grok.se and Wikimedia Pageview API)
  * Google Trends (for musicians)
  * comScore data, WMF overall numbers
  * Google Consumer Survey and Survey Monkey Audience

See also the [timeline of Wikipedia analytics][ana] that was created as part of
this process.

# Plots

Things we plotted:

  * Log pageviews, for each of {desktop, mobile, desktop + mobile}
  * Mobile:desktop ratio vs 95% quantile
  * $\log(\mathrm{WV}) - \log(k)$

We also found the [peaks for desktop][peak_gist] and [peaks overall][peak_ov]
using different windows.

To visualize the "decline" in pageviews we plotted the pageviews from Wikipedia
Views, which now includes mobile data since July 2015.

Example:

![](http://23.226.229.10/~issa/pageview_plots/musicians_total_top_6.png)

# Surveys

Two surveys:

  * A Google Consumer Survey asking people to compare how much their Wikipedia
    usage has changed since 2011.
  * (Not yet launched) A Survey Monkey Audience survey asking the same question
    as the Google Consumer Survey, plus some other background and follow-up
    questions.

# Questions

  * Are pageviews even declining?
    It seems that desktop pageviews are declining, but is this still the case
    if we add in mobile views?
    Another difficulty here is that stats.grok.se seems to have used a
    different exclusion method for bots/spiders (evidenced by the stats.grok.se
    pageviews not matching up with the pageviews from the Wikimedia Pageview
    API even on months where they both have data), so it's not totally clear if
    even desktop is declining.

# License

Most permissive license Vipul Naik allows.

[ana]: https://en.wikipedia.org/wiki/User:Riceissa/Timeline_of_Wikipedia_analytics "“User:Riceissa/Timeline of Wikipedia analytics - Wikipedia, the free encyclopedia”."
[peak_gist]: https://gist.github.com/riceissa/c47656af388120f4b5bbc4eba1ffc5ab
[peak_ov]: https://gist.github.com/riceissa/213c5b0cb31f12746d713f6ec0790257

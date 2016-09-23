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
  * $\log\mathrm{WV} - \log\mathrm{GT}$

We also found the [peaks for desktop][peak_gist] and [peaks overall][peak_ov]
using different windows.

To visualize the "decline" in pageviews we plotted the pageviews from Wikipedia
Views, which now includes mobile data since July 2015.

Example:

![](http://23.226.229.10/~issa/pageview_plots/musicians_total_top_6.png)

The full list of plots for this can be found [here][plots_all].
The plots generally show that desktop pageviews according to stats.grok.se fell
from around 2011 or 2013 (depending on the class of pages examined) to 2015.
Adding on the Wikimedia Pageview API data for desktop from January 2016 to the
present shows that this trend seems to continue, but we think the Pageview API
imposes a stricter filter on bots/spiders.

On the other hand, if we add in the mobile data, we see that predictably there
is a "bump" starting in July 2015, when the mobile data started.
However, for some classes of pages, even adding in the mobile data -- while
causing the desktop "decline" to become mostly flat -- did not cause the
pageviews to increase back to the level of 2011--2013 pageviews.

# Surveys

Two surveys:

  * A Google Consumer Survey of a US audience (without any demographic filters)
    asking people to compare how much their Wikipedia
    usage has changed since 2011.
  * A Survey Monkey US Audience survey (again, no demographic filters) asking
    the same question
    as the Google Consumer Survey, plus some other background and follow-up
    questions.

# Questions/thought process

  * Are pageviews even declining?
    It seems that desktop pageviews are declining, but is this still the case
    if we add in mobile views?
    Another difficulty here is that stats.grok.se seems to have used a
    different exclusion method for bots/spiders (evidenced by the stats.grok.se
    pageviews not matching up with the pageviews from the Wikimedia Pageview
    API even on months where they both have data), so it's not totally clear if
    even desktop is declining.
  * What are the possible reasons?

      * Shift to mobile → Check by adding the mobile views and by asking people
        on Survey Monkey
      * Language substitution → Check the same tag using different languages
        (we did colors in English, French, and German)
      * Google Knowledge cards? → Ask people about this in SM survey
      * Siri? → Ask people
      * Wikipedia showing up less in SERPs? → Try to get access to historical
        SERPs for some search queries.
        This actually seems harder to obtain than we first thought.
      * People somehow preferring Wikipedia less? → Ask people.
      * Is Wikipedia's popularity in general decreasing? → Can we see that in
        the $\log \mathrm{WV} - \log \mathrm{GT}$ graph?
        Apparently not well.

      * Could a change in redirects have anything to do with this?
        For instance see ["Consider the Redirect"][ctr]:

        > Because viewers don't see redirects, viewing a redirect is
        > substantively different from viewing a normal page. For example, if a
        > user visits the article on "Seattle, Washington", this will be
        > recorded as a view to the redirect even though the target article
        > "Seattle" is displayed. In this sense, views of redirects will tend
        > to be overcounted while views of target articles will tend to be
        > undercounted.

# License

Most permissive license Vipul Naik allows.

[ana]: https://en.wikipedia.org/wiki/User:Riceissa/Timeline_of_Wikipedia_analytics "“User:Riceissa/Timeline of Wikipedia analytics - Wikipedia, the free encyclopedia”."
[ctr]: http://dl.acm.org/citation.cfm?doid=2641580.2641616 "Benjamin Mako Hill and Aaron Shaw. “Consider the Redirect: A Missing Dimension of Wikipedia Research”. 2014."
[peak_gist]: https://gist.github.com/riceissa/c47656af388120f4b5bbc4eba1ffc5ab
[peak_ov]: https://gist.github.com/riceissa/213c5b0cb31f12746d713f6ec0790257
[plots_all]: http://23.226.229.10/~issa/pageview_plots/

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

  * Log pageviews, for each of {desktop, mobile, desktop + mobile,
    desktop + mobile + spiders}
  * Mobile:desktop ratio vs 95% quantile
  * $\log\mathrm{WV} - \log\mathrm{GT}$

We also found the [peaks for desktop][peak_gist] and [peaks overall][peak_ov]
using different windows.

To visualize the "decline" in pageviews we plotted the pageviews from Wikipedia
Views, which now includes mobile data since July 2015.

Example:

![Plot for top 10 musicians, total access](http://ram.issarice.com/~issa/pageview_plots/musicians_total_top_6.png)

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

We also plotted the same plot with the addition of spiders.
Note that the Wikimedia Pageview API makes the distinction between "bot" and
"spider", but we couldn't find pages for which the "bot" traffic was nonzero,
so we simply excluded the pageviews identified as "bot"; as far as we know,
"spider" means "not human".
These were only included from January 2016, because stats.grok.se did its own
filtering for bot traffic; we looked at a few pages, and our impression is that
the aggressiveness of non-human traffic filtering of stats.grok.se is
below that of the current Wikimedia Pageview API.
In other words, had stats.grok.se continued to report their pageviews in the
same way, we suspect its values would be somewhere between what the Wikimedia
Pageview API would report for desktop user (lower bound, aggressive filtering)
and desktop user + desktop spider (upper bound, no filtering).

Here is a classification of the tags we looked at based on whether there was
a rebound to 75th percentile or higher July 2015 or later:

Tag                                   Rebound?
---                                   --------
American pundits                      Yes
Cities                                Yes
Colors                                No
Compiler theory                       Yes
Countries                             Yes
Eggplant dishes                       Yes
French colors                         No
German colors                         No
Musicians                             Yes
Philanthropic foundations             Yes
Programming languages                 Yes
Sex organs                            No
Shooting-related                      Yes
Spanish colors                        Yes
US politicians                        Yes
US presidents                         Yes

As can be seen, the colors (in languages besides Spanish) and the sex organs
tag did not have a rebound.
However, this doesn't mean the other tags had increasing traffic; many simply
kept up with the 2011--2013 values.
We think the table above gives a way to tell the tags for which the pageviews
have *definitely* gone down since the 2011--2013 period.

# Surveys

Several surveys:

  * A Google Consumer Survey of a US audience (without any demographic filters)
    asking people to compare how much their Wikipedia
    usage has changed since 2011.
    This was answered by 1036 people.
    You can see the [results page][gcs_results].
  * A Survey Monkey US Audience survey (again, no demographic filters) asking
    the same question
    as the Google Consumer Survey, plus some other background and follow-up
    questions.
    We ran this for 50 people and TODO answered.
    After this, we changed the order of the questions to ask about Wikipedia
    first, then about general internet use and use of search engines.
    We ran this second version for 50 people and TODO answered.
  * Vipul's timeline (first version)
  * UW audience (which version?)
  * More audiences?

## Survey Monkey first survey



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
        >
        > [...]
        >
        > Because redirects are edited infrequently but "viewed" as often as
        > millions of times per month each, redirects may be contributing to
        > the surprisingly low correlation between edits and views noted by
        > Priedhorsky et al. and others.

        See also ["Analytics/Data/Redirects - Wikitech"][redirect_spelling]

        Could people somehow be viewing redirects more than the actual pages,
        compared to 2011--2013?
        To give one recent example (too recent to matter), the Wikipedia
        article [New York][ny] is about the state, not the city.
        However there is a [recent shift][ny_disc] to change all wikilinks
        \[\[New York\]\] to go through the redirect page [New York
        (state)][ny_state], with the wikilink \[\[New York (state)|New
        York\]\].
        This means that less pageviews will be recorded for the New York page,
        and more will be recorded for the redirect page.
        One idea is that if a sufficiently large number of highly popular pages
        have similar sorts of redirection manipulation, the pageviews for the
        article itself could be going down even while people are reading the
        page more -- the pageview is just being distributed more between the
        main article and its redirect pages.

        However my impression is that most pageviews come from search engine
        results pages, and that wikilinks are not used very much.
        See for instance the pageviews on redirects to [Red][red_redirects] and
        [Black][black_redirects] (though one complication here is that
        redirects might not be static, though in this case I wouldn't expect
        the redirects to be changing much).
        Likewise there are some effects that should push pageviews *less*
        toward redirects.
        For instance, presumably Google and other search engines have gotten
        better at showing the link to the main article rather than a link to
        the redirect page.

      * Could views be going to the Simple English Wikipedia?
        This does not seem to be the case, at least for colors; see the
        [tabulation on Wikipedia Views][simple_colors].

      * Could browsers like Opera Mini be adding pageviews as bots?
        See the ["analytics and proxy/remote browsers"][opera] thread on the
        Analytics mailing list.
        Probably not.

      * See also [pageview definition changes][pageview_defn].
        I don't think this is a big cause of pageview change.
        It's also not clear whether pageview definitions are applied
        retroactively.

# License

Most permissive license Vipul Naik allows.

[ana]: https://en.wikipedia.org/wiki/User:Riceissa/Timeline_of_Wikipedia_analytics "“User:Riceissa/Timeline of Wikipedia analytics - Wikipedia, the free encyclopedia”."
[black_redirects]: http://wikipediaviews.org/displayviewsformultipleyears.php?tag=Pages%20that%20redirect%20to%20Black&language=en&device=desktop&allyears=allyears
[ctr]: http://dl.acm.org/citation.cfm?doid=2641580.2641616 "Benjamin Mako Hill and Aaron Shaw. “Consider the Redirect: A Missing Dimension of Wikipedia Research”. 2014."
[gcs_results]: https://www.google.com/insights/consumersurveys/view?survey=2l5h5cssu4am3oferd32zcxaai&question=1&filter=&rw=1 "Vipul Naik and Issa Rice. “How does your use of Wikipedia, the online encyclopedia, compare to your use 5 years ago (2011)?” Google Consumer Surveys. September 20, 2016."
[ny]: https://en.wikipedia.org/wiki/New_York
[ny_disc]: https://en.wikipedia.org/wiki/Talk:New_York#Proposed_action_to_resolve_incorrect_incoming_links
[ny_state]: https://en.wikipedia.org/w/index.php?title=New_York_(state)&redirect=no
[opera]: https://lists.wikimedia.org/pipermail/analytics/2016-June/005247.html
[pageview_defn]: https://meta.wikimedia.org/wiki/Research:Page_view#Change_log
[peak_gist]: https://gist.github.com/riceissa/c47656af388120f4b5bbc4eba1ffc5ab
[peak_ov]: https://gist.github.com/riceissa/213c5b0cb31f12746d713f6ec0790257
[plots_all]: http://ram.issarice.com/~issa/pageview_plots/
[red_redirects]: http://wikipediaviews.org/displayviewsformultipleyears.php?tag=Pages%20that%20redirect%20to%20Red&language=en&device=desktop&allyears=allyears
[redirect_spelling]: https://wikitech.wikimedia.org/wiki/Analytics/Data/Redirects#Other_spellings_covered_by_a_redirect_page "“Analytics/Data/Redirects - Wikitech”."
[simple_colors]: http://wikipediaviews.org/displayviewsformultipleyears.php?tag=Colors&language=simple&device=desktop&allyears=allyears

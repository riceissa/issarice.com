---
title: uBlock Origin filters for Tao Analysis Solutions
author: Issa Rice
created: 2023-05-02
date: 2023-05-02
---

It probably goes against wordpress.com's terms of service to give instructions on how to have an ad-free experience on my blog, [Tao Analysis Solutions](https://taoanalysis.wordpress.com/). But what happens outside of the blog is outside of WordPress's control. So here's my recommended uBlock Origin filters:

```
taoanalysis.wordpress.com##.noskim.marketing-bar
taoanalysis.wordpress.com##.site-header:style(position: relative !important; top: -48px !important;)
taoanalysis.wordpress.com###infinite-footer
```

The first line removes the "Design a site like this with WordPress.com" bar at the top of the page. If you just have the first line, there will be a blank space the exact same size as the bar that was just removed. So the second line adjusts the actual site header bar upwards to fill the empty space. I've only tested this on a desktop browser. The third line I believe gets rid of some sort of footer that only appears on certain pages (I am forgetting the details).

To add these lines to your filter rules, [install uBlock Origin](https://github.com/gorhill/uBlock#readme) for your browser. Then click on the uBlock Origin icon, click the gears ("Open the dashboard"), click the "My filters" tab, paste the lines above, and finally click "Apply changes".
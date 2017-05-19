---
title: GitHub punch card exploration
author: Issa Rice
created: 2017-05-18
date: 2017-05-18
---

Each repository on GitHub has a punch card graph under `/graphs/punch-card`.
This page looks at the punch card graphs of some projects.

Note that contribution graphs on GitHub are [only timezone-aware after
2014-03-10](https://github.com/blog/1793-timezone-aware-contribution-graphs):

> When counting commits, we use the timezone information present in the
> timestamps for those commits. Pull requests and issues opened on the web will
> use the timezone of your browser. If you use the API you can also specify
> your timezone.
>
> We don't want to mess up your current contribution streaks, so only
> contributions after Monday 10 March 2014 (Temps Universel Coordonné) will be
> timezone-aware.

So for projects with the bulk of commits in the past, it would be better to
filter out the older commits.
However, even for older projects a weekday/weekend split should be observable.

[Neovim](https://github.com/neovim/neovim/graphs/punch-card):

[![](punch-card-neovim-neovim.png)](punch-card-neovim-neovim.png)

[mod_pagespeed](https://github.com/pagespeed/mod_pagespeed/graphs/punch-card):

[![](punch-card-pagespeed-mod_pagespeed.png)](punch-card-pagespeed-mod_pagespeed.png)

[Linux kernel](https://github.com/torvalds/linux/graphs/punch-card):

[![](punch-card-torvalds-linux.png)](punch-card-torvalds-linux.png)

[Bootstrap](https://github.com/twbs/bootstrap/graphs/punch-card):

[![](punch-card-twbs-bootstrap.png)](punch-card-twbs-bootstrap.png)

[React](https://github.com/facebook/react/graphs/punch-card):

[![](punch-card-facebook-react.png)](punch-card-facebook-react.png)

[Redis](https://github.com/antirez/redis/graphs/punch-card):

[![](punch-card-antirez-redis.png)](punch-card-antirez-redis.png)

# External links

- Similar graphs are available for Wikipedia contributions,
  e.g. [my account](https://tools.wmflabs.org/xtools-ec/?user=Riceissa&project=en.wikipedia.org#timecard)

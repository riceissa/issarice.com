---
title: GitHub punch card exploration
author: Issa Rice
created: 2017-05-18
date: 2017-05-19
---

# Summary

Each repository on GitHub has a punch card graph under `/graphs/punch-card`.
This page looks at the punch card graphs of some projects.

# Timezone issues

Note that apparently contribution graphs on GitHub are [only timezone-aware after
2014-03-10](https://github.com/blog/1793-timezone-aware-contribution-graphs):

> When counting commits, we use the timezone information present in the
> timestamps for those commits. Pull requests and issues opened on the web will
> use the timezone of your browser. If you use the API you can also specify
> your timezone.
>
> We don't want to mess up your current contribution streaks, so only
> contributions after Monday 10 March 2014 (Temps Universel Coordonné) will be
> timezone-aware.

However since timezone-awareness is so important to punch cards, and since the
display of punch card graphs does not interfere with GitHub's stated reason for
not implementing timezone-awareness for earlier periods (i.e. using timezone
data on the punch card doesn't mess up contribution streaks), it seems
plausible that GitHub would be using the timezone data just for the punch cards
anyway.
So for projects with the bulk of commits in the past, it would be better to
filter out the older commits, just to be sure that timezone nonsense does
not affect the results (or to use something like [Git-Pandas](https://github.com/wdm0006/git-pandas)
to generate the punch cards oneself).
However, even for older projects a weekday/weekend split should be observable.

# Plots

The images below are screenshots that I took from the respective repositories;
credit goes to GitHub for producing them.
The screenshots were taken on 2017-05-18 and 2017-05-19.

[Neovim](https://github.com/neovim/neovim/graphs/punch-card)
(~9,000 commits):

[![](punch-card-neovim-neovim.png)](punch-card-neovim-neovim.png)

[Vim](https://github.com/vim/vim/graphs/punch-card)
(~7,000 commits; only Bram Moolenaar seems to have commit privileges, so this provides a
contrast with the Neovim graph):

[![](punch-card-vim-vim.png)](punch-card-vim-vim.png)

[mod_pagespeed](https://github.com/pagespeed/mod_pagespeed/graphs/punch-card)
(~5,000 commits):

[![](punch-card-pagespeed-mod_pagespeed.png)](punch-card-pagespeed-mod_pagespeed.png)

[Linux kernel](https://github.com/torvalds/linux/graphs/punch-card)
(~678,000 commits):

[![](punch-card-torvalds-linux.png)](punch-card-torvalds-linux.png)

[Git](https://github.com/git/git/graphs/punch-card)
(~47,000 commits):

[![](punch-card-git-git.png)](punch-card-git-git.png)

[Bootstrap](https://github.com/twbs/bootstrap/graphs/punch-card)
(~16,000 commits):

[![](punch-card-twbs-bootstrap.png)](punch-card-twbs-bootstrap.png)

[React](https://github.com/facebook/react/graphs/punch-card)
(~9,000 commits):

[![](punch-card-facebook-react.png)](punch-card-facebook-react.png)

[Redis](https://github.com/antirez/redis/graphs/punch-card)
(~6,000 commits; Salvatore Sanfilippo's commits [dominate the repository by far](https://github.com/antirez/redis/graphs/contributors),
and he [works on Redis as his day job][antirez], so a clear 9am--6pm "box" appears on
weekdays):

[![](punch-card-antirez-redis.png)](punch-card-antirez-redis.png)

[Lua](https://github.com/lua/lua/graphs/punch-card)
(~5,000 commits):

[![](punch-card-lua-lua.png)](punch-card-lua-lua.png)

[Go](https://github.com/golang/go/graphs/punch-card)
(~33,000 commits):

[![](punch-card-golang-go.png)](punch-card-golang-go.png)

[Tim Pope dotfiles](https://github.com/tpope/tpope/graphs/punch-card)
(~900 commits):

[![](punch-card-tpope-tpope.png)](punch-card-tpope-tpope.png)

[Justin M. Keyes dotfiles](https://github.com/justinmk/config/graphs/punch-card)
(~900 commits):

[![](punch-card-justinmk-config.png)](punch-card-justinmk-config.png)

[Drew Neil dotfiles](https://github.com/nelstrom/dotfiles/graphs/punch-card)
(~500 commits):

[![](punch-card-nelstrom-dotfiles.png)](punch-card-nelstrom-dotfiles.png)

[gwern.net](https://github.com/gwern/gwern.net/graphs/punch-card)
(~11,000 commits):

[![](punch-card-gwern-gwern-net.png)](punch-card-gwern-gwern-net.png)

[Eevee's website](https://github.com/eevee/eev.ee/graphs/punch-card)
(~400 commits):

[![](punch-card-eevee-eev-ee.png)](punch-card-eevee-eev-ee.png)

[vimtex](https://github.com/lervag/vimtex/graphs/punch-card)
(~1,700 commits):

[![](punch-card-lervag-vimtex.png)](punch-card-lervag-vimtex.png)

[wikipediaviews](https://github.com/vipulnaik/wikipediaviews/graphs/punch-card)
(~400 commits):

[![](punch-card-vipulnaik-wikipediaviews.png)](punch-card-vipulnaik-wikipediaviews.png)

[Vipul Naik's contract work repo](https://github.com/vipulnaik/contractwork/graphs/punch-card)
(~1,000 commits):

[![](punch-card-vipulnaik-contractwork.png)](punch-card-vipulnaik-contractwork.png)

[Vipul Naik's working drafts](https://github.com/vipulnaik/working-drafts/graphs/punch-card):

[![](punch-card-vipulnaik-working-drafts.png)](punch-card-vipulnaik-working-drafts.png)

[Vipul Naik's donations site](https://github.com/vipulnaik/donations/graphs/punch-card)
(~300 commits):

[![](punch-card-vipulnaik-donations.png)](punch-card-vipulnaik-donations.png)

# Acknowledgments

Thanks to [Vipul Naik](https://vipulnaik.com/) for suggesting that I write
something up about GitHub punch cards.
He also allowed me to count the time I spent on this page toward my work hours,
for which I receive a [stipend](https://github.com/vipulnaik/contractwork/blob/master/contributor-lists/issa-list.mediawiki#Stipends)
(however he did not provide task payment beyond this stipend).

# External links

- Similar graphs are available for Wikipedia contributions,
  e.g. [my account](https://tools.wmflabs.org/xtools-ec/?user=Riceissa&project=en.wikipedia.org#timecard)

[antirez]: http://invece.org/ "Salvatore Sanfilippo. “Salvatore Sanfilippo aka antirez”. Retrieved May 19, 2017. “Currently my main project is Redis, and thanks to Redis Labs sponsoring the development of Redis, it is also my work.”"

---
title: GitHub punch card exploration
author: Issa Rice
created: 2017-05-18
date: 2017-05-18
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

[Neovim](https://github.com/neovim/neovim/graphs/punch-card):

[![](punch-card-neovim-neovim.png)](punch-card-neovim-neovim.png)

[Vim](https://github.com/vim/vim/graphs/punch-card)
(only Bram Moolenaar seems to have commit privileges, so this provides a
contrast with the Neovim graph):

[![](punch-card-vim-vim.png)](punch-card-vim-vim.png)

[mod_pagespeed](https://github.com/pagespeed/mod_pagespeed/graphs/punch-card):

[![](punch-card-pagespeed-mod_pagespeed.png)](punch-card-pagespeed-mod_pagespeed.png)

[Linux kernel](https://github.com/torvalds/linux/graphs/punch-card):

[![](punch-card-torvalds-linux.png)](punch-card-torvalds-linux.png)

[Git](https://github.com/git/git/graphs/punch-card):

[![](punch-card-git-git.png)](punch-card-git-git.png)

[Bootstrap](https://github.com/twbs/bootstrap/graphs/punch-card):

[![](punch-card-twbs-bootstrap.png)](punch-card-twbs-bootstrap.png)

[React](https://github.com/facebook/react/graphs/punch-card):

[![](punch-card-facebook-react.png)](punch-card-facebook-react.png)

[Redis](https://github.com/antirez/redis/graphs/punch-card):

[![](punch-card-antirez-redis.png)](punch-card-antirez-redis.png)

[Lua](https://github.com/lua/lua/graphs/punch-card):

[![](punch-card-lua-lua.png)](punch-card-lua-lua.png)

[Go](https://github.com/golang/go/graphs/punch-card):

[![](punch-card-golang-go.png)](punch-card-golang-go.png)

[Tim Pope dotfiles](https://github.com/tpope/tpope/graphs/punch-card):

[![](punch-card-tpope-tpope.png)](punch-card-tpope-tpope.png)

[Justin M. Keyes dotfiles](https://github.com/justinmk/config/graphs/punch-card):

[![](punch-card-justinmk-config.png)](punch-card-justinmk-config.png)

[Drew Neil dotfiles](https://github.com/nelstrom/dotfiles/graphs/punch-card):

[![](punch-card-nelstrom-dotfiles.png)](punch-card-nelstrom-dotfiles.png)

# Acknowledgments

Thanks to Vipul Naik for suggesting that I write something up about GitHub
punch cards.
He also allowed me to count the time I spent on this page toward my work hours,
for which I receive a [stipend](https://github.com/vipulnaik/contractwork/blob/master/contributor-lists/issa-list.mediawiki#Stipends)
(however he did not provide task payment beyond this stipend).

# External links

- Similar graphs are available for Wikipedia contributions,
  e.g. [my account](https://tools.wmflabs.org/xtools-ec/?user=Riceissa&project=en.wikipedia.org#timecard)

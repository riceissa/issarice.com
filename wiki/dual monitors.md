---
title: Dual monitors
date: 2015-12-27
---

This worked in Openbox, where my second monitor is placed above the laptop screen:

```bash
xrandr --auto --output LVDS1 --mode 1366x768 --below VGA1
```

Help from "[Dual monitors with Openbox and Xrandr](https://web.archive.org/web/20151214195159/https://travisred.github.io/dual-monitors-with-openbox-and-xrandr/)".

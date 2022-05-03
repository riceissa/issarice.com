---
title: Regular screenshots
author: Issa Rice
created: 2015-09-09
date: 2015-09-09
status: notes
---

In Linux Mint MATE^[See also [How to check if screen saver is running?](https://stackoverflow.com/questions/4327187/how-to-check-if-screen-saver-is-running) for other desktops.]:

```bash
sleep 5s; qdbus org.mate.ScreenSaver /ScreenSaver org.mate.ScreenSaver.GetActive
```

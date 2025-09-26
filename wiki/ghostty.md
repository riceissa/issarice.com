---
title: "Things that bug me about Ghostty's user experience"
author: Issa Rice
created: 2025-09-26
date: 2025-09-26
---

When Ghostty first came out, I was still using Windows, so I couldn't use it. I
recently heard about the project again, and now that I'm back on Linux, I can
use it, so I decided to give it a try.

This page isn't meant to be a bashing of Ghostty. It's still a new project, so
I don't think it should be judged according to the standards of a mature
application. I really respect what Mitchell Hashimoto is doing, and as a fellow
"recreational programmer", I think it's super cool that he went from doing a
company to going back to just hacking on his own projects. Instead, this list
is a personal checklist of things that I want to remember to check back on so
that I know when Ghostty has matured to the point where I can use it as a daily
driver. I did a similar thing with Neovim when it was new.

So here's my list of things I don't like about Ghostty at the moment, based on
roughly an hour of using it. These things bug me enough that I am going to
stick with Gnome terminal for now. This was on `Ghostty-1.2.0-x86_64.AppImage`
under Fedora 42 running a Gnome desktop environment:

- When I ssh into a server and do `tmux a`, it just says "missing or unsuitable
  terminal: xterm-ghostty" which is unacceptable to me. Kitty does this too,
  which is why I don't use Kitty either.
- The popup messages like "Copied to clipboard" just keep getting sent at a
  certain interval of delay, even if I did the action many times very quickly,
  so if I repeatedly copy some text, like 10 times (this is not some
  unrealistic example; I sometimes repeatedly do something as a tic/fidgeting
  thing), then for the next minute or so I just see the "Copied to clipboard"
  popup repeatedly coming up every 5 seconds or whatever, which is the most
  annoying thing ever. Gnome terminal has the same problem, but actually I
  never noticed this before because I think it sends way fewer things to the
  popup message. (e.g. Ghostty copies all tmux selections to the system
  clipboard, whereas Gnome terminal doesn't do that. So Ghostty sends a popup
  message whenever I select anything in tmux.)
- Installation is a pain. The easiest way to install in Fedora is the AppImage
  (I didn't want to use some random third party repo), which I download, then I
  have to make it executable, put it in the right place (`~/.local/bin`) and
  then I need to add a shortcut so that Gnome shell can find it (in
  `~/.local/share/applications`), which of course means I need to look up what
  text to put in the `.desktop` file. And it still doesn't have an icon -- by
  that point, I got tired of looking up how to do it.
- I use CTRL+Enter to mean just Enter all the time when I'm using a terminal,
  e.g. I do CTRL+p to go up a command in bash, and without letting go of the
  finger on the CTRL key, I just press enter; it's much more ergonomic to type
  that way, as it's one fewer finger coordination. But in Ghostty, CTRL+Enter
  is a mapping for full-screen toggle, so this doesn't work and does something
  I don't want. The more general point is, just because a terminal can't accept
  certain key combos (like CTRL+Enter), it shouldn't just map it to whatever it
  wants, thinking it's helping the user by adding a "feature". The user may
  have gotten used to certain key combos _not_ being mapped, and instead having
  the "fall-through" behavior, and when the terminal application maps those
  keys in the GUI, it steals those key combos from the user.
- Font rendering is weird. DejaVu Sans Mono, the font I am using now on the
  terminal, has hyphens that render differently depending on the vertical
  height of the glyph on the terminal window, which should _never ever_ happen.
  The font also looks very weird in general on Ghostty (hard to describe what
  feels off about it), whereas on Gnome terminal it looks just fine. Other
  fonts look fine on Ghostty, but I want to use DejaVu Sans Mono! On the other
  hand, it _does_ render Consolas better than Gnome terminal. Consolas was my
  favorite font on Windows and I was very disappointed when I discovered it
  renders so horribly on Gnome terminal (it is vertically shifted so the glyphs
  aren't centered on the line they are on) that it meant I couldn't use it
  anymore.
- It has a cool theme picker, but I like to use different themes depending on
  the time of day (light during the day, dark at night). I really love how
  Gnome terminal just has an auto mode right there in the menu that lets you
  pick that option. In Ghostty there was no obvious way to do this and I didn't
  even look into how to do it.
- I don't like the bell emoji that shows up in the title bar when a terminal
  bell rings. Gnome terminal changes the window title bar color background,
  which is a much better, less visually intrusive way of signaling a bell. (I
  honestly don't like bells in general, and e.g. on Vim I just have `set
  belloff=all`.)
- The cursor shape is a vertical bar, but it's way too thin -- I can barely see
  it. I'm sure I can go in the settings to change it to a block just like in
  Gnome terminal, but I shouldn't have to do that, in an application that touts
  sane defaults.
- Even though there are a thousand themes in the theme picker, none of them
  look right. I really like the palette called "GNOME" in Gnome terminal, but I
  don't think Ghostty has it. I decided to go with Tango light, which is still
  a decent theme.
- The theme picker really should separate out the dark themes from the light
  ones, rather than mixing them all in one list; it's visually jarring to keep
  flipping back and forth and forcing my eyes to have to adjust. Ideally, I
  could pick a theme for light mode and a theme for dark mode, and then say
  "toggle automatically based on the OS theme".
- Has the same problem as Gnome terminal where the green tmux bar at the bottom
  gets "lifted up" as I change the height of the terminal, because it's trying
  to do smooth resizing to be cool. But I don't want that. I would much rather
  have the Emacs GUI (at least on Gnome Linux) way of snapping to glyphs, so
  that no matter what the size window is, the borders near the text are sharp
  and don't have any "wasted" space.
- The mouse scroll wheel by default scrolls way too much under tmux. I can
  change `mouse-scroll-multiplier = 0.25` in the settings but then it skips
  every other scroll, and I can set it to 0.5 instead, but then it's still
  feels like it's scrolling more than in Gnome terminal.

Looking at this list, I have the thought that the thing that's important in a
GUI application is not that it's the fastest or that it has the most features,
but more that it doesn't have a bunch of little annoyances. I can get used to
little annoyances, but if I have already gotten used to the little annoyances
of one application (Gnome terminal, in this case), then I am not going to
switch to another application (Ghostty) unless it is better in some way and
either has the _same_ little annoyances or fixes some of those annoyances. But
if the new application has _different_ little annoyances, then that's a
problem.

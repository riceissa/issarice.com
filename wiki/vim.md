---
title: Vim
#description: 
author: Issa Rice
creation_date: 2015-02-28
last_major_revision_date: 2015-08-10
language: English
# accepts "notes", "draft", "in progress", or "mostly finished"
status: notes
# accepts "certain", "highly likely", "likely", "possible", "unlikely", "highly unlikely", "remote", "impossible", "log", "emotional", or "fiction"
belief: possible
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC0
tags: vim, computing
#aliases: 
---

**Vim** is my text editor of choice.
I started using it in 2011 (or even before that---I can't quite remember).
It was the first "serious" text editor I tried to learn, and although I've experimented some with a few others (e.g. I downloaded emacs and went through its tutorial, I downloaded and played around with Sublime), I haven't really felt a desire to switch.

This page documents some of my musings from using Vim; most of it has probably already been said elsewhere. 

I probably spend too much time configuring Vim---something I've been trying to cut down on.

# Ex mode

One thing I learned really recently is that Vim has very sophisticated ex mode features.
I had always been frustrated by the fact that ex mode seemed way too limited, since I couldn't even get bash-style keys like `<C-a>` to go to the beginning of the line to work.
But it turns out I was wrong; see `:h cmdline.txt` for more, as well as `:h usr_20.txt`, which is referenced in the first help page.
But for instance, you can type `q:` to enter essentially insert mode within ex mode, which allows you to do regular Vi keys to edit commands.
I also learned that `<C-b>` is the right way to go to the beginning of a line in ex mode; you can change this with `cnoremap <C-a> <C-b>` too though; also see `:h emacs-keys` to make keybindings more "sane".

# Poor-man's folding

It's certainly possible to use something like [nelstrom/vim\-markdown\-folding](https://github.com/nelstrom/vim-markdown-folding) to get proper folding in Vim.
But what if one is on a remote machine, for instance?
It's always useful to know efficient ways to work in Vim even when one does not have access to one's accustomed plugins.
Here's a cool way to navigate a long markdown document, assuming all headers begin with `#`.
It's possible to use `:g/pattern` to search for an expression in the current buffer and print the results.
For markdown files, just type `:g/^#` to see all headers, for instance.
Then, once one has found the heading one was looking for, note the line number (say, 10) and then type `:10<CR>` to get there.

# Plugins or not?

*Note, this section isn't balanced.*

Lately I've been thinking that it's perhaps more desirable to simply learn Vim well instead of trying to customize Vim "needlessly"; are many plugins merely distractions?
In other words, maybe relying so heavily on some Vim plugins might just be an indication that you don’t know Vim well.
See for instance [Kevin Beckford's answer to Vim: How can I learn to write a vimrc?](https://www.quora.com/Vim/How-can-I-learn-to-write-a-vimrc/answer/Kevin-Beckford):

> Preferentially, waste time reading how vim works, rather than
> scripting it.  Vimscript is an interesting language, but I feel
> learning the options that would go into a .vimrc is more important.

Something like a "Unix philosophy for text editing":

- a text editor should just let you efficiently input text. if you want version control, then that should be an external command, not a plugin to vim (or something). or how YCM actually does linting stuff for you, but that something like [Valgrind](http://valgrind.org/) or other linting software should *externally* be run
- “convention over configuration” (a phrase from [What can I do in Vim that I can't do in a Jetbrains IDE?](https://www.quora.com/What-can-I-do-in-Vim-that-I-cant-do-in-a-Jetbrains-IDE))

Or as [roel\_v points out](https://news.ycombinator.com/item?id=3566062) on Hacker News:

> I've used vim for coming on 15 years now, so I feel that I may qualify
> as 'experienced'. My biggest productivity gain was giving up on
> endless customization after I had reached a certain proficiency (e.g.,
> everything in the original article is rather basic vim usage) and
> comfortable workflow for specific development purposes (e.g. when
> switching to a new language, I spend some time setting vim up to solve
> the most glaring pain points and once it feels comfortable, I stop
> customizing). All the mucking about with various baroque plugins and
> ever-more-marginal keystroke-saving key mappings costs a lot more time
> than what can be gained from it. For example, I used to have a bunch
> of mappings that would insert documentation blocks in various forms.
> Just misremembering the mapping once a day causes enough workflow
> disruption to undo any gains from having them in the first place.
> Nowadays I just type comments / docblocks by hand. It's a few more
> keystrokes, but a lot more natural and flexible.
> 
> Also, staying as close as possible to the default settings makes it a
> lot easier to move to other environments and/or upgrade. Although now
> that I have my .vimrc in my Dropbox it doesn't matter as much as it
> used to.

Another "essence" of Vim, as [Tim Pope says](https://www.reddit.com/r/vim/comments/267vrv/i_am_tim_pope_crafter_of_plugins_ama/chooack):

> Don't use a map when a command will do. Vim doesn't even have a map
> for `:write`.

Though maybe the most important metric is: if adding a new feature slows down your text editor, you have to think: does having this feature speed me up enough that the slower editor is still better than not having that feature?
I do think that having some mappings (like `jj` and `kk` to escape from insert mode) really do increase my editing speed.
The same argument could be made for some plugins like vim-fugitive.

See also the "light" versus "dark" distinction explained in [Sharpen your Vim with snippets](https://medium.com/brigade-engineering/sharpen-your-vim-with-snippets-767b693886db).

# Small things

- `:windo diffthis` and then `:windo diffoff` when done
- `Ctrl`-`f` in command mode to edit using regular Vim options (one can also access this with `q:`)
- `:only` after `:sp` or `:vsp`
- Editing with Vim under sudo or su: use `vim -X` to disable X so that there are no strange "No protocol specified" or grabled text/reordered lines.
- Visual selection followed by `:'<,'>normal.` is really powerful (see *Practical Vim*).
- Also see this enlightening quote by Drew Neil in *Practical Vim*:

    > The start and end of the last visual selection are both recorded
    > automatically as marks, so we might even consider Visual mode to be a
    > fancy interface to the underlying marks feature.

- Modelines: Secure Vim by disabling modelines; see "[Securing
  Vim](http://usevim.com/2012/03/28/modelines/)" and "[Turn off modeline
  support in Vim -
  TechRepublic](http://www.techrepublic.com/blog/it-security/turn-off-modeline-support-in-vim/)"
  for more information.

# Moving in long lines

I've always found it frustrating that Vim by default acts on physical lines instead of "display lines".
Of course, mapping `j` and `k` to `gj` and `gk`, respectively (and conversely; though `Ctrl`-`n` and `Ctrl`-`p` also work for navigating physical lines), partly solves this, but page-wide navigation like `Ctrl`-`f` still act according to physical lines, and it isn't possible to sanely display partial lines (in the way that even simple editors like gedit are able to do).
One solution, of course, is to force the burden upon the markup language: both LaTeX and Markdown allow for hard linebreaks, which means one can set `:set tw=72` and not have to think about long lines.
But I don't consider this a very satisfactory solution, especially since I like to have each sentence on its own line in markup, which means there is the occasional long sentence and hence long line.
Worse yet, Wikipedia source files tend to have entire paragraphs on single lines, so even if I write my markup one way, there is no way to avoid *others* from writing *their* markup a certain way.---Hence, the problem must be solved within Vim.

I think something like `9j`, etc., can work as a replacement for `Ctrl`-`d`.

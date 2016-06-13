---
title: Vim
creation_date: 2015-02-28
date: 2015-08-10
---

**Vim** is my text editor of choice.
I started using it in 2011 (or even before that---I can't quite remember).
It was the first "serious" text editor I tried to learn, and although I've experimented some with a few others (e.g. I downloaded emacs and went through its tutorial, I downloaded and played around with Sublime), I haven't really felt a desire to switch.

This page documents some of my musings from using Vim; most of it has probably already been said elsewhere.

I probably spend too much time configuring Vim---something I've been trying to cut down on.

You can see my [current vimrc](https://github.com/riceissa/dotfiles/blob/master/.vimrc) and [Vim directory](https://github.com/riceissa/dotfiles/tree/master/.vim) in my dotfiles repository.

You can also see [my contributions to the Vim Tips Wiki](http://vim.wikia.com/wiki/Special:Contributions/IssaRice?useskin=monobook).

# Ex mode

One thing I learned really recently is that Vim has very sophisticated ex mode features.
I had always been frustrated by the fact that ex mode seemed way too limited, since I couldn't even get bash-style keys like `<C-a>` to go to the beginning of the line to work.
But it turns out I was wrong; see `:h cmdline.txt` for more, as well as `:h usr_20.txt`, which is referenced in the first help page.
But for instance, you can type `q:` to enter essentially insert mode within ex mode, which allows you to do regular Vi keys to edit commands.
I also learned that `<C-b>` is the right way to go to the beginning of a line in ex mode; you can change this with `cnoremap <C-a> <C-b>` too though; also see `:h emacs-keys` to make keybindings more "sane".

# `:g`-based folding

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

- Use Python's `ord()` to obtain the integer value of a character. Hit
  `<C-k>` in insert mode then type the characters following `'dig'` to
  produce the special character.

- Filtering span tags from Quora's HTML, assuming the HTML is in its own
  buffer; modify as necessary for parts of a buffer:

    ```vim
    " paste the raw HTML
    :r !xclip -sel clip -t text/html -o
    " remove span tags; may need to repeat with @: if these are nested
    :%!pandoc -f html -t html -F ./despan.py
    " finally convert to markdown; use gq for further formatting as
    " necessary
    :%!pandoc -f html -t markdown
    ```

    Here `despan.py` is the following:

    ```python
    #!/usr/bin/python3

    # modified from https://github.com/jgm/pandoc/issues/1893

    from pandocfilters import toJSONFilter, Str

    def despan(key, value, format, meta):
        if key == 'Span':
            return value[1]

    if __name__ == "__main__":
        toJSONFilter(despan)
    ```

- [This answer](http://superuser.com/a/716269) for setting the omnifunc even for languages that aren't well-supported by Vim. In particular, `:h ft-syntax-omni` contains a useful snippet:

    ```vim
    if has("autocmd") && exists("+omnifunc")
    autocmd Filetype *
            \    if &omnifunc == "" |
            \        setlocal omnifunc=syntaxcomplete#Complete |
            \    endif
    endif
    ```

- When writing prose, it's rather convenient to load up similar files with `:args` all into the current buffer so that word completion using `C-n` and `C-p` are more relevant (as in, the top results are usually what I expect).
- Deciding between `C-n` and `C-p` is sometimes challenging. If the completion one wants is more likely to have been just typed, then `C-p` is better, but if appears just below the current line, then `C-n` is better. But if it's unclear where in the file the completion one wants is, then it's harder to tell which to use.

- Using `C-l` to escape from insert mode: this has been rather convenient so
  far.  I used to use `jj` and `kk`, which are useful since they don't appear
  in English often, but I still ran into awkward problems in e.g. UltiSnips
  when using LaTeX when the final character before a "jump" turned out to be a
  `j` or `k`, in which case the jump would proceed in a half-hearted way (in
  math mode, the cursor would end up on the `)` in `\)`). Also I had to be more
  careful about setting `paste` before pasting long lines of text into the
  buffer with `C-S-v`, since the pasted text could accidentally get me out of
  insert mode and start executing normal mode commands (I now use just `C-r+`
  in insert mode though, or `"+P` in normal mode). `C-l` is actually the
  default escape in evim, so it's somewhat strange that the mapping doesn't
  also exist in Vim itself (edit: I actually just found out why. Apparently vim can't keep track of separate key mappings for vim and evim, so if one maps `C-l` to `<esc>`, then, since escape is disabled in evim, one can never escape easy mode! Luckily I don't ever use easy mode---I think Neovim removes it, in fact---so I have the luxury of leaving Vim in this broken state). One problem I've had so far though: in linewise
  insert completion mode with `C-x` `C-l`, hitting `C-l` again will just shift
  through the completions instead of escaping. To break out, one must use `C-[`
  or `C-e` as usual.

- Another thing that took me too long to discover: keyword completion using `Ctrl`-`x` `Ctrl`-`p` and `Ctrl`-`x` `Ctrl`-`n`; see [the Vim help section](http://vimdoc.sourceforge.net/htmldoc/insert.html#compl-current).
However, rather than describing it as "keyword completion", I would say it is more like "predictive completion" (like on a smartphone keyboard).

# Moving in long lines

I've always found it frustrating that Vim by default acts on physical lines instead of "display lines".
Of course, mapping `j` and `k` to `gj` and `gk`, respectively (and conversely; though `Ctrl`-`n` and `Ctrl`-`p` also work for navigating physical lines), partly solves this, but page-wide navigation like `Ctrl`-`f` still act according to physical lines, and it isn't possible to sanely display partial lines (in the way that even simple editors like gedit are able to do).
One solution, of course, is to force the burden upon the markup language: both LaTeX and Markdown allow for hard linebreaks, which means one can set `:set tw=72` and not have to think about long lines.
But I don't consider this a very satisfactory solution, especially since I like to have each sentence on its own line in markup, which means there is the occasional long sentence and hence long line.
Worse yet, Wikipedia source files tend to have entire paragraphs on single lines, so even if I write my markup one way, there is no way to avoid *others* from writing *their* markup a certain way---hence, the problem must be solved within Vim.

I think something like `9j`, etc., can work as a replacement for `Ctrl`-`d`.

One hack: use the following series of custom commands (optionally
replacing '↵' with another rare character):

```vim
command! ShortLines :%s/.\{71}/&↵\r/g | 0
command! ShortLinesAtSpace :%s/.\{,70} /&↵\r/g | 0
command! LongLines :%s/↵\n// | 0
```

Use `:ShortLines` or `:ShortLinesAtSpace` to convert the document to use
short hard linebreaks, and use `:LongLines` to convert back.  I'm not
certain if this won't corrupt the file somehow, but it seems to work...
This was inspired by the [JpFormat plugin](
https://github.com/fuenor/JpFormat.vim ), which actually probably does
something rather different, but I didn't bother using it (I only took
inspiration from the [screenshot](
https://cca8f41b-a-62cb3a1a-s-sites.googlegroups.com/site/fudist/Home/jpformat/JpFormat.jpg)).
Anyway, the file you are editing shouldn't have any '↵' characters in
it, because those could interfere with the regex replacement, and when
restoring the file, a newline may be added at the very end, so the file
might not be identical when restored.  Other than that, I haven't
experienced any problems.

For specific cases, like really long CSS or JSON lines, one can pass it
through a pretty filter, like ` :%!python -m json.tool` (from [here](
http://blog.realnitro.be/2010/12/20/format-json-in-vim-using-pythons-jsontool-module/
)) in the case of JSON.

Another hack: set `:set scrolloff=99999`. This will at least make for
a somewhat more pleasant scrolling experience when the file is just one
enormous line; `j` sort of replaces `Ctrl`-`e` and so forth.

In any case, it seems that the way Vim treats long lines is
fundamentally broken, in the sense that the way it thinks of lines is
[stuck in the days of line-based text processing](http://doc.cat-v.org/bell_labs/structural_regexps/se.pdf).  I really would like
display-line versions of `Ctrl`-`e`, `Ctrl`-`d`, and `Ctrl`-`f`, in the
same way that we have `gj` and `g$`. It might be worth noting that when using `:vim`, vim uses some pager like `more`, which can display partial lines even when using `j` and `k`.

In editing Wikipedia, I've also found it useful to learn [CUA keybindings](https://en.wikipedia.org/wiki/IBM_Common_User_Access) like `Ctrl`-`→`, `Ctrl`-`Backspace`, and so forth, which can be used directly on browsers like Firefox.
This suffices for most editing tasks, and I have [It's All Text!](https://addons.mozilla.org/en-US/firefox/addon/its-all-text/) installed and set up to open GVim for more complicated tasks (like search-and-replace), where dealing with long lines in Vim is preferable to dealing with such tasks in the browser's text field.
I've also found Emacs useful (with a bit of practice[^evil]) if I am dealing with a file that neither Vim nor a CUA editor can easily deal with.

See also [this Neovim discussion](https://github.com/neovim/neovim/issues/4232).

# From my old .vimrc

It's sometimes interesting to read my old .vimrc to note things that I
used to accomplish in a really convoluted manner (and which sometimes
Vim did natively!).  Here I want to list some of these.

```vim
set list listchars=eol:$,extends:>,precedes:<,nbsp:_,tab:>-,trail:@
```

I used to have `extends` and `precedes`, although I later realized I
didn't really like them for the following reason: When editing long
lines, these hide the first character of each visual line, making the
text difficult to read. I also switched `tab` to `>\ ` (i.e. greater
than, backslash, space), which, when combined with a `ctermbg` highlight
color, makes it possible to see the spaces.

Next, I used to have several lines like the following to help automate
LateX document compilation:

```viml
autocmd filetype tex nnoremap <buffer> <silent> <localleader><localleader> :!latexmk -pdf %<CR>
```

But Vim already has `:make`, which is more versatile anyway, and doesn't
require configuration for each filetype.

I used to set manual abbreviations like the following to help with
typos:

```vi
iabbrev adn and
iabbrev nad and
iabbrev teh the
iabbrev het the
iabbrev ehty they
iabbrev hety they
iabbrev tehn then
iabbrev waht what
iabbrev THen Then
```

But Vim has the much more general `<C-x>s`, which, combined with other
types of autocompletion, becomes incredibly powerful.

Also in general I used to have a lot more lines in my .vimrc, many of
which I couldn't be bothered to memorize.

I used to also have:

```vim
nnoremap <silent> <C-n> :tabn<CR>
nnoremap <silent> <C-p> :tabp<CR>
```

This is fine, but I mostly needed to quickly switch between tabs because
I was using them *instead of buffers*.  In other words, I was unable to
think of editing buffers in a "Vim mindset", which caused me to treat
tabs in a naive manner.  See [this
answer](http://stackoverflow.com/a/103590) as well as [this
question](https://stackoverflow.com/questions/26708822/why-do-vim-experts-prefer-buffers-over-tabs)
for more.

Also mappings like:

```vim
nnoremap <silent> <leader>nh :nohlsearch<CR>
nnoremap <silent> <leader>I :set list!<CR>
nnoremap <silent> <leader>N :set number!<CR>
nnoremap <leader>p :set paste! paste?<CR>
```

These show that I was unaware of
[unimpaired.vim](https://github.com/tpope/vim-unimpaired).

I also had a habit of adding new plugins almost by whim, which may have
been a positive thing (in that I was able to experiment with more
possible editing workflows) but ended up not really being necessary, and
also *discouraged me from actually learning Vim*---because why read
through the help pages when a flashy plugin will solve my problem?

Right now my approach consists of (1) not creating new mappings to solve
problems for me (cf. the Tim Pope quote above); (2) not making any
changes to my configuration that would require different "muscle memory"
from the default Vim/Neovim configuration---to quote Tim Pope again, I
want to keep my changes in configuration to those which are a "[cosmetic
improvement with no impact on muscle memory](
https://github.com/tpope/vim-sensible/issues/81 )".  In fact both (1)
and (2) have a lot in common, and (2) might be construed as a more
general formulation of (1).

I used to do ` gg"+yG`` `, when the ex-mode `:%y +` is much simpler.

# Other problems

Despite using Vim for almost everything, I still have some problems with
it:

- The way Vim treats long lines (see section above)
- The fact that I have to press `Enter` twice after compiling something (note
  that Neovim fixes this problem).
- Using eclim for Java completion (along with YCM) results in a strange error
  when running `:make`, even on projects that have nothing to do with Java.
  Specifically, the first line of the quickfix list is always `error: ...`, and
  `:cwindow` is populated with the command output. Adding `@` to each line of
  the makefile gets rid of this error, but that's just a hack. Removing the
  directory `~/.vim/eclim` gets rid of this issue, but then obviously I can't
  use eclim for completions.
- Strange "bug" (not sure if intended behavior): with `incsearch` on, searching
  for text on a long line makes the found search term disappear sometimes, but
  only on gvim. Take the raw text on [this
  page](https://en.wikipedia.org/w/index.php?title=Fiduciary&action=edit). Then
  turn `incsearch` on, then type `/incl` to try to search for "including".
  After the "c" is typed, the match disappears and typing "l" brings it back,
  and so forth. Hitting enter at any point completes the search, *but not on
  gvim, where it just fails*. (Actually trying it again now, it seems to fail everwhere, even on Neovim...). Make sure your window height is also small relative to the line length.

[^evil]: Emacs Evil mode is also an option (it's a fairly good emulation of Vim).

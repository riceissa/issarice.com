---
title: Vim
author: Issa Rice
created: 2015-02-28
date: 2016-08-27
---

**Vim** is my text editor of choice.
I started using it in 2011 (or even before that---I can't quite remember).
It was the first "serious" text editor I tried to learn, and although I've experimented some with a few others (e.g. I downloaded emacs and went through its tutorial, I downloaded and played around with Sublime), I haven't really felt a desire to switch.

This page documents some of my musings from using Vim; most of it has probably already been said elsewhere.

I probably spend too much time configuring Vim---something I've been trying to cut down on.

You can see my [current vimrc](https://github.com/riceissa/dotfiles/blob/master/.vimrc) and [Vim directory](https://github.com/riceissa/dotfiles/tree/master/.vim) in my dotfiles repository.

You can also see [my contributions to the Vim Tips Wiki](http://vim.wikia.com/wiki/Special:Contributions/IssaRice?useskin=monobook).

# Command-line mode

In the past I had always been frustrated by the fact that command-line mode
seemed way too limited, since I couldn't even use bash-style keys like `<C-a>`
to go to the beginning of the line to work. But it turns out I was wrong; see
`:h cmdline.txt` for more, as well as `:h usr_20.txt`, which is referenced in
the first help page. But for instance, you can type `q:` to enter essentially
insert mode within ex mode, which allows you to do regular Vi keys to edit
commands. I also learned that `<C-b>` is the right way to go to the beginning
of a line in ex mode; you can change this with `cnoremap <C-a> <C-b>` too
though; also see `:h emacs-keys` to make keybindings more "sane". Note that I
now just use Tim Pope's [rsi.vim](https://github.com/tpope/vim-rsi).

# `:g`-based folding

It's certainly possible to use something like [nelstrom/vim\-markdown\-folding](https://github.com/nelstrom/vim-markdown-folding) to get proper folding in Vim.
But what if one is on a remote machine, for instance?
It's always useful to know efficient ways to work in Vim even when one does not have access to one's accustomed plugins.
Here's a cool way to navigate a long markdown document, assuming all headers begin with `#`.
It's possible to use `:g/pattern` to search for an expression in the current buffer and print the results.
For markdown files, just type `:g/^#` to see all headers, for instance.
Then, once one has found the heading one was looking for, note the line number (say, 10) and then type `:10<CR>` to get there.

To generate the headings in a new split window, do something like this:

    :redir @a
    :silent global/^#/print
    :redir END
    :vnew | put a
    :g/^$/d

Then save it in a file and `:source` it, or yank it and execute with `@"`.
You can also view the output at any time without putting it in a new window
using `:echo @a`.
For some reason, chaining the above commands like

    :redir @a | silent global/^#/print | redir END

only captures the first line of output from the `:global` command.
I think it's because `:global` tries to use everything after it as the ex
command it executes.
Doing

    :redir @a | silent global/^#/print \| redir END

seems to work.

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

See also ["On sharpening the saw"][saw], which pushes for learning the base Vim
really well, but also accepting plugins that extend Vim in a way Vim was "meant
to be" (e.g. surround.vim, fugitive.vim, etc., are all "Vimlike" plugins).

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

    See also [Filtering out messy HTML](pandoc#filtering-out-messy-html).

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
  also exist in Vim itself (edit: I actually just found out why. Apparently vim
  can't keep track of separate key mappings for vim and evim, so if one maps
  `C-l` to `<esc>`, then, since escape is disabled in evim, one can never escape
  easy mode! Luckily I don't ever use easy mode---I think Neovim removes it, in
  fact---so I have the luxury of leaving Vim in this broken state). One problem
  I've had so far though: in linewise
  insert completion mode with `C-x` `C-l`, hitting `C-l` again will just shift
  through the completions instead of escaping. To break out, one must use `C-[`
  or `C-e` as usual.

- Another thing that took me too long to discover: keyword completion using `Ctrl`-`x` `Ctrl`-`p` and `Ctrl`-`x` `Ctrl`-`n`; see [the Vim help section](http://vimdoc.sourceforge.net/htmldoc/insert.html#compl-current).
However, rather than describing it as "keyword completion", I would say it is more like "predictive completion" (like on a smartphone keyboard).
- In a Markdown document with reference-style links at the end of the file, add
  the current line to the list and sort it:

        :+1kl | m$ | $?^$?,$sort | 'l

    This won't work if the file has footnotes at the end instead.
    Additionally, each reference must be on its own line, and
    the references must be contained in a single paragraph (since we search
    backward from the end of the buffer with `$?^$?`).

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

For something more complicated, the following might work:

    function! FShortLines(break_at_space, line_end_chars)
      for c in a:line_end_chars
        let use_this = 1
        for line in getline("1", "$")
          if match(line, c) >= 0
            " This char was in the file originally, so we can't use it as the line
            " separator.
            let use_this = 0
            break
          endif
          " echom "got one more"
        endfor
        if use_this
          if exists('b:end_char_stack')
            call add(b:end_char_stack, c)
          else
            let b:end_char_stack = [c]
          endif
          if a:break_at_space
            exe 'silent %s/.\{,70} /&' . c . '\r/g | 0'
          else
            exe 'silent %s/.\{71}/&' . c . '\r/g | 0'
          endif
          return 0
        endif
      endfor
      " We couldn't use any of the a:line_end_chars.
      return -1
    endfunction

    function! FLongLines()
      if exists('b:end_char_stack')
        if len(b:end_char_stack) > 0
          let c = remove(b:end_char_stack, -1)
          exe 'silent %s/' . c . '\n//e | 0'
          return 0
        endif
      else
        let b:end_char_stack = []
      endif
      return -1
    endfunction

    command! ShortLines :call FShortLines(0, ['↵', '↲', '⤶', '↩'])
    command! ShortLinesAtSpace :call FShortLines(1, ['↵', '↲', '⤶', '↩'])
    command! LongLines :call FLongLines()

This will create a stack of artificial line-end characters,
so that the mapping can be used repeatedly.
Doing `:LongLines` will pop values off the stack.
The function will also check the buffer first to make sure that
the line-end character is not present.
At the moment this is still pretty slow for very large files,
because of the substitute command.
I'm not sure if it might be better to use an external filter,
and pipe the buffer in and out.
If you are wondering about the list `['↵', '↲', '⤶', '↩']`,
I decided to pick four Unicode characters that looked like a linebreak;
you might find that confusing and prefer something more visually
distinctive.

For specific cases, like really long CSS or JSON lines, one can pass it
through a pretty filter, like ` :%!python -m json.tool` (from [here](
http://blog.realnitro.be/2010/12/20/format-json-in-vim-using-pythons-jsontool-module/
)) in the case of JSON.
For HTML or XML files, there is `:%!tidy -xml -utf8 -i` once one installs tidy.

Another hack: set `:set scrolloff=99999`. This will at least make for
a somewhat more pleasant scrolling experience when the file is just one
enormous line; `j` sort of replaces `Ctrl`-`e` and so forth.

In any case, it seems that the way Vim treats long lines is
fundamentally broken, in the sense that the way it thinks of lines is
[stuck in the days of line-based text processing](http://doc.cat-v.org/bell_labs/structural_regexps/se.pdf).
I really would like
display-line versions of `Ctrl`-`e`, `Ctrl`-`d`, and `Ctrl`-`f`, in the
same way that we have `gj` and `g$`, as well as an option that will allow one to display a partial line at the top of the current view (currently, unless a line is extremely long, Vim will show a line at the top of the current view so as to expose the beginning of the line). It might be worth noting that when using commands like `:vim` and `:cl`, vim uses some pager like `more`, which can display partial lines even when using `j` and `k`.

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

# Syntax files

Vim syntax files seem to have the problem of either coloring things incorrectly
(often happens with complicated or nested structures in Markdown or LaTeX), or,
even when syntactically correct, overzealously. There isn't much point in
coloring *most* things on the screen because that just makes it difficult to
distinguish parts.

In markup languages, the two most important parts of syntax coloring are the
following:

- Disabling spell-checking in regions where it doesn't make sense (URLs,
  reference variables, etc.)
- Distinguishing "hidden" parts from the visible parts. Example: when editing
  MediaWiki files, the parts inside `<ref>` tags should be colored differently
  so that one can read a sentence without constantly having to track where the
  references end.

I take some inspiration from Vim's own mail.vim, which is both helpful (in
coloring URLs and not spell-checking within them) and unobtrusive (by not even
distinguishing common markup for e.g. \*emphasis\*).

Note that Hacker News also has a [very minimal markup][hn] that only converts
code blocks (but not inline code!), italics, and URLs. Facebook messaging and
posts also have limited formatting options, where URLs and certain other text
(phone numbers, dollar amounts, `@dailycute`, `@fbchess`, names of people, etc.)
are detected.

Do we see this trend only in markup languages, or also in programming languages?
One point to consider is that in programming, indentation either does not matter
(e.g. C) or it does not affect the highlighting (e.g. with Python, indentation
matters, but one can always ignore all the current level of indentation and
color as if the text is at the outermost level of indentation (?)). In contrast,
Markdown makes heavy use of indentation to affect meaning *and* the coloring
must be aware of this (e.g. to understand that one is *in* or *not in* a
codeblock or blockquote); indeed, some markup languages like TeX allow the user
to arbitrarily redefine the language (commonly seen with `\makeatletter` and
`\makeatother`). Another difficulty with Markdown is the lack of
standardization, which makes the coloring correct under some implementations but
not others. Escaping methods might also be worth considering. Markdown code can
take $n$ backticks to include $n-1$ backticks inside the code. This makes the
source easier to read for a human, but for syntax highlighting, it's easier to
deal with one-off backslash escapes favored in languages like Python (since
there is less context to maintain).

# Using alternative Vim setups

Sometimes when I am editing a quick file, I don't want to load all my plugins
and custom setup (especially YCM -- although vim-plug might have a way to speed
this up that I'm not aware of), as that results in a slow startup that I don't
want to bother to wait for. I also like to experiment with radically different
Vim configurations sometimes In these cases, it can be useful to have an
alternative Vim setup, sort of like a second `~/.vim` path, or an option like
`-u` that also changes the `.vim` directory to something else. Here I change it
to `~/.alt-vim`.

First, from
<http://superuser.com/questions/561434/telling-vim-to-use-custom-vimrc-is-easy-but-how-to-tell-it-to-use-alternative>,
I have the following in my `~/.zshrc`:

    alias avim='vim --cmd '"'"'let &rtp = substitute(&rtp, $HOME."/\\.vim", $HOME."/.alt-vim", "g")'"'"' -Nu /home/issa/.alt-vim/init.vim'

I might change it to a shell script later, so I don't have to deal with the
nested quotes. The basic idea is to invoke Vim with:

    vim --cmd 'let &rtp = substitute(&rtp, $HOME."/\\.vim", $HOME."/.alt-vim", "g")' -Nu $HOME/.alt-vim/init.vim

This sets both the `vimrc` as well as the runtime path, which controls where Vim
searches for plugins. (Question: Does this use the same or different `viminfo`?)
I'm also not sure why the above expression uses `\.` instead of just `.` (this
is because in `substitute`, Vim interprets the second argument as a pattern
rather than a verbatim string; note that because we are using double quote
strings, we must use two backslashes to escape the dot).

Then I have in `init.vim` (after installing vim-plug -- see below):

    call plug#begin('~/.alt-vim/plugged')
    Plug 'nelstrom/vim-visual-star-search'
    Plug 'tpope/vim-abolish'
    Plug 'tpope/vim-characterize'
    Plug 'tpope/vim-commentary'
    Plug 'tpope/vim-fugitive'
    Plug 'tpope/vim-repeat'
    Plug 'tpope/vim-speeddating'
    Plug 'tpope/vim-surround'
    Plug 'tpope/vim-unimpaired'
    call plug#end()

    source /home/issa/sensible.vim

where `sensible.vim` is just
[sensible.vim](https://github.com/tpope/vim-sensible).

I also ran (prior to making `init.vim`):

    curl -fLo ~/.alt-vim/autoload/plug.vim --create-dirs \
        https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

which installs vim-plug.

Now all that is left is to run `:PlugInstall` from Vim to install the plugins.

# Other problems

Despite using Vim for almost everything, I still have some problems with
it:

- The way Vim treats long lines (see section above)
- The fact that I have to press `Enter` twice after compiling something (note
  that Neovim fixes this problem).  In Vim, I just use the external
  `make` command `:!make` rather than Vim's `:make` because of this.
- Using eclim for Java completion (along with YCM) results in a strange error
  when running `:make`, even on projects that have nothing to do with Java.
  Specifically, the first line of the quickfix list is always `error: ...`, and
  `:cwindow` is populated with the command output. Adding `@` to each line of
  the makefile gets rid of this error, but that's just a hack. Removing the
  directory `~/.vim/eclim` gets rid of this issue, but then obviously I can't
  use eclim for completions.
- Strange "bug" (not sure if intended behavior): with `incsearch` on, searching
  for text on a long line makes the found search term disappear sometimes, but
  only on gvim. Take the raw text on [this page][incl]. Then turn `incsearch`
  on, then type `/incl` to try to search for "including". After the "c" is
  typed, the match disappears and typing "l" brings it back, and so forth.
  Hitting enter at any point completes the search, *but not on gvim, where it
  just fails*. (Actually trying it again now, it seems to fail everywhere, even
  on Neovim...). Make sure your window height is also small relative to the line
  length. Update (2016-07-26): this is still failing, but now the match doesn't
  even return when typing the next character. The only solution seems to be to
  finish typing, then hit `<CR>`, then back up with `N`.

Things to check in Neovim (or, the list of things that make me wary to switch to
Neovim, and which I should check back on with Neovim because at some point the
benefits may outweigh the costs):

-   Invoking `:Tutor` in a tmux terminal causes artefacts and duplicate lines to
    appear (probably because of the conceal feature?).

-   Pasting to GMail makes newlines disappear, so that everything is in one
    giant paragraph. The same doesn't happen with Vim. See the [GitHub
    thread][clip].
    This only happens with `xclip`, so uninstalling `xclip` and installing
    `xsel` would solve it, but I like `xclip` for its ability to paste as HTML,
    which I don't think exists in `xsel`.
    As far as I know, there is no way in Neovim to specify which clipboard
    provider to use.

-   The following horrible map (intended to be like a ctags for Markdown)
    requires a manual `<CR>`:

        autocmd FileType markdown nnoremap <buffer> <C-]> "zya[:let @z=substitute(@z, "\n", ' ', "g")<CR>:let @z=substitute(@z, "\\s\\+", " ", "g")<CR>:let @z=substitute(@z, " ", "\\\\(\\\\s\\\\\\|\\\\n\\\\)\\\\+", "g")<CR>/\V<C-r>z<CR>

    This map was experimental and I don't use it anymore, but this is intended
    to show that there are possibly edge cases like these where maps work
    in Vim but don't in Neovim.

[clip]: https://github.com/neovim/neovim/issues/4501 "frasercrmck. “Yanking to clipboard does not preserve newlines (when pasting to some applications) #4501”. March 28, 2016."
[hn]: https://news.ycombinator.com/formatdoc
[incl]: https://en.wikipedia.org/w/index.php?title=Fiduciary&action=edit&oldid=731216276
[saw]: http://vimcasts.org/blog/2012/08/on-sharpening-the-saw/

[^evil]: Emacs Evil mode is also an option (it's a fairly good emulation of Vim).

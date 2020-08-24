---
title: Vim
author: Issa Rice
created: 2015-02-28
date: 2016-08-27
---

For most text editing and programming tasks, I use Vim. I started using it
around 2011 as my first "serious" text editor, and although I sometimes use and
have experimented with others (e.g. [Emacs]()), I haven't really felt a desire
to switch.

This page documents some of my musings from using Vim; most of it has probably already been said elsewhere.

I probably spend too much time configuring Vim. I am well past the point where
configuring and installing new plugins for Vim pays off in terms of increased
productivity. I've been trying to cut down on configuration, but find myself
doing it anyway because I find it relaxing.

You can see my [current
vimrc](https://github.com/riceissa/dotfiles/blob/master/.vimrc) in my dotfiles
repository.

You can also see [my contributions to the Vim Tips Wiki](http://vim.wikia.com/wiki/Special:Contributions/IssaRice?useskin=monobook).

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

- Another thing that took me too long to discover: keyword completion using `Ctrl`-`x` `Ctrl`-`p` and `Ctrl`-`x` `Ctrl`-`n`; see [the Vim help section](http://vimdoc.sourceforge.net/htmldoc/insert.html#compl-current).
However, rather than describing it as "keyword completion", I would say it is more like "predictive completion" (like on a smartphone keyboard).

- In a Markdown document with reference-style links at the end of the file, add
  the current line to the list and sort it:

      :+1kl | m$ | $?^$?,$sort | 'l

  This won't work if the file has footnotes at the end instead.
  Additionally, each reference must be on its own line, and
  the references must be contained in a single paragraph (since we search
  backward from the end of the buffer with `$?^$?`).

# Working with long lines

Details about working with long lines are covered in ["Working with long
lines"][long] on the Vim Tips Wiki, which I wrote.

Here are some other details that I didn't want to cover on that page,
especially with regard to the point "Giving up on Vim for these files and using
editors that work fine with long lines (gedit, GNU Emacs, etc.)".

In editing Wikipedia, I've found it useful to learn [CUA keybindings](https://en.wikipedia.org/wiki/IBM_Common_User_Access) like `Ctrl`-`→`, `Ctrl`-`Backspace`, and so forth, which can be used directly on browsers like Firefox.
This suffices for most editing tasks, and I have the extension [It's All Text!](https://addons.mozilla.org/en-US/firefox/addon/its-all-text/) installed and set up to open GVim for more complicated tasks (like search-and-replace), where dealing with long lines in Vim is preferable to dealing with such tasks in the browser's text field.
I've also found [Emacs](emacs) useful (with a bit of practice) if I am dealing with a file that neither Vim nor a CUA editor can easily deal with.

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
(phone numbers, dollar amounts, `@dailycute`, \@-mentions, names of people, etc.)
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

-   With Fugitive, `:Git merge` seems to not work? (I forgot the details of the
    problem I had.)

-   The following horrible map (intended to be like a ctags for Markdown)
    requires a manual `<CR>`:

        autocmd FileType markdown nnoremap <buffer> <C-]> "zya[:let @z=substitute(@z, "\n", ' ', "g")<CR>:let @z=substitute(@z, "\\s\\+", " ", "g")<CR>:let @z=substitute(@z, " ", "\\\\(\\\\s\\\\\\|\\\\n\\\\)\\\\+", "g")<CR>/\V<C-r>z<CR>

    This map was experimental and I don't use it anymore, but this is intended
    to show that there are possibly edge cases like these where maps work
    in Vim but don't in Neovim.

-   Setting the title doesn't work.
    The following works in Vim but not Neovim:

        if &term =~ "screen"
          exec "set t_ts=\<Esc>k"
          exec "set t_fs=\<Esc>\\"
        endif

    This is mostly a problem in tmux, where Vim doesn't set the title by
    default.

-   I want the following to work:

        :w !diff % -
        :w !diff % - | less

    This essentially checks for the unsaved changes to the file, by comparing
    the file on disk with the contents of the buffer (passed through standard
    input).
    The second line is an alternative that passes the output to `less`, so that
    one can always scroll up and down.
    Neovim's `:!` seems to be purposely limited to allow for compatibility
    across operating systems (?).
    Doing `:w :term ...` *should* work in the long run: there is an
    [issue](https://github.com/neovim/neovim/issues/1716) in the Neovim repo on
    this.

    Fugitive's `:Git diff` works on both Vim and Neovim. It does this in the
    definition of the `s:Git()` function by checking for the existence of
    `:terminal`:

        if exists(':terminal')
          let dir = s:repo().tree()
          if expand('%') != ''
            -tabedit %
          else
            -tabnew
          endif
          execute 'lcd' fnameescape(dir)
          execute 'terminal' git args

    Vim also has `:DiffOrig`, but I don't like having to get rid of the second
    buffer.

-   (Fixed in latest.)
    Pasting multibyte characters with `<C-R>"` in insert mode does not work.
    For instance, with the cursor on `木`, doing `vyo<C-R>"a` results in
    `<t_^Z<80>>^Z<t_^Za>` being printed on a new line,
    where `^Z` and `<80>` are single characters.
    Pasting with `p` in normal mode and `<C-R><C-O>` in insert mode work.

-   (Fixed in latest.)
    With `set inccommand=split`, if the line contains multibyte characters,
    sometimes the characters are not shown; rather, partial bytes like
    `<e6><9c>` are shown (but the substitution itself seems to work fine).

-   2020-04-25 (NVIM v0.3.8): Neovim sets `background=dark` for some reason, even though I don't set this in my vimrc.

-   2020-04-25 (NVIM v0.3.8): the following steps produce _two_ status lines for the window on top. This looks like a bug?

    ````
    (open new instance of nvim)
    :h color
    <C-W><C-W> (switch to the bottom window)
    :echo &back<TAB> (then hit enter to select "background")
    <space> (to get rid of the "Press ENTER or type command to continue" prompt)
    <C-W><C-W> (to switch back to the top window)
    ````

    At this point, there are two status lines for the top window. Also, the first line of the top window repeats twice. Pressing CTRL-L gets rid of this.

-   2020-05-29 (NVIM v0.4.3): in urxvt under tmux, if I open neovim and then close it, the cursor in bash starts blinking. (the cursor in urxvt is normally just a box that never blinks.)

-   2020-08-24: I think the popup screen when running `:FZF` looks slightly nicer in vim than on neovim.


On the other hand, here are some things I like better in Neovim/where vim has bugs:

- Fugitive's `:Gpush` command makes the cmdheight go up randomly until I clear the screen with CTRL-L. In general, Gpush leaves screen artefacts and hides the cursor and does annoying things.
- opening/closing vim is slower, and got much slower recently for some reason. In Neovim startup/closing time is very fast.


# Some intuitions

I began using Vim at the latest in the summer of 2011.
In the course of 6+ years of using Vim, I've developed some intuitions; most of
these I've only been able to articulate in the past year or so.

* Conventional beginner advice says to stay in normal mode most of the time,
  and to "dive in" to insert mode to make small changes, and then come up
  to normal mode again -- that this is how Vim differs most from other editors.
  On the contrary, I've found that *insert mode is very powerful and learning
  the parallel commands in insert mode is one of the more useful things one can
  do*.
  rsi.vim especially helps.
* When trying to [build new habits](http://www.moolenaar.net/habits.html), it's
  better to do it in non-ad hoc ways.
  Usually Vim or Tim Pope has a better solution in mind than the one you can
  think of on the spot. More than once I have come up with an ad hoc solution
  only to find that the Vim developers or Tim Pope has solved the problem in
  more idiomatic ways.
* Use mappings to take care of complex tasks like casework rather than simply
  as aliases to built-in commands.
  You might be tempted to map common commands like `:write`, but `:write` is
  often too primitive, and what you really want is something like "Do `:Gwrite`
  and open a split to commit the changes, but fall back to `:write` if the file
  associated with this buffer isn't tracked with Git".  Note how commands like
  `:DiffOrig` are just a bunch of primitive commands chained together.

# See also

* [Software]() for more about the software I use

[hn]: https://news.ycombinator.com/formatdoc
[incl]: https://en.wikipedia.org/w/index.php?title=Fiduciary&action=edit&oldid=731216276
[long]: http://vim.wikia.com/wiki/Working_with_long_lines?useskin=monobook
[saw]: http://vimcasts.org/blog/2012/08/on-sharpening-the-saw/

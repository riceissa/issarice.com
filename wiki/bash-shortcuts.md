---
title: Bash shortcuts
description: a cheat sheet for Bash
tags: linux
# This page is at least as old as the following date.  I don't know if I can find the original date on which I began this document.
created: 2011-08-23
date: 2015-01-02
---

Here are some useful shortcuts when you're working in Bash.
Shortcuts are categorised by use.

These shortcuts will be familiar to those using [[Emacs]]. Many of the
keybindings will also work in many line-based environments, e.g. REPLs for many
languages, Python Jupyter console, MySQL prompt. Even Vim has
[vim-rsi](https://github.com/tpope/vim-rsi) to enable some of these.

# Conventions

-  `Ctrl`-`a`:
Hold the Control key and press 'a'.
-  `Alt`-`a`:
Hold the Alt key and press 'a'. The Alt key is sometimes called the [Meta key](http://en.wikipedia.org/wiki/Meta_key). If the Alt key doesn't work, try using the Escape key instead. (So `Esc`-`a` instead. You might need to let go of the Escape key before pressing 'a'.)
- `key1` `key2`: Press `key1`, let go, then press `key2`.
-  This page is [*case sensitive*](http://en.wikipedia.org/wiki/Case_sensitivity) so `a` is different from `A`.
`A` is the same as `Shift`-`a`.
- A *smallword* is any string of characters that contain *only* characters from the set `{a-z,A-Z,0-9}`.
Smallwords are delimited by non-alphanumeric characters (whitespace, full stop, caret, etc.).
This is similar to a lowercase 'w' in the Vi editor.
- A *bigword* is any string of characters *not containing a whitespace*.
Bigwords are delimited by whitespace characters (space, tab, etc.).
This is similar to an uppercase 'W' in the Vi editor.


# Movement

- `Ctrl`-`a` or `Home`:
Jump to the beginning of the line.
- `Ctrl`-`e` or `End`:
Jump to the end of the line.
- `Ctrl`-`xx`:
Jump between saved locations.
Pressing this will toggle between the current location and the beginning of the line. If you move the cursor after you have jumped to the beginning, then press this again, Bash will remember the location. Press this again to come back to the location you just saved.
- `Ctrl`-`f` or `Right Arrow Key`:
Go forward one character.
-  `Alt`-`f`:
Go forward one smallword. This does not work on the Gnome Terminal because `Alt`-`f` is bound to the "file" menu.
However, `Esc` `f` works.
-  `Ctrl`-`b` or `Left Arrow Key`:
Go back one character.
-  `Alt`-`b`:
Go back one smallword.
-  `Ctrl`-`]` `a`:
Move to the next occurrence of 'a'.
-  `Alt`-`Ctrl`-`]` `a`:
Move to the previous occurrence of 'a'.

# Editing

-  `Ctrl`-`x` `Ctrl`-`u` or `Ctrl`-`/` or `Ctrl`-`_`:
Undo the last operation.
-  `Alt`-`r`:
Revert all changes to the current line. For example, if you edited a command from your history, this would revert to the original.
-  `Ctrl`-`h` or `Backspace`:
Delete the character to the left of the cursor.
-  `Alt`-`Backspace`:
Cut to the beginning of the current smallword. (From left side of the cursor to the beginning of the smallword. Does not cut leading whitespace.)
-  `Ctrl`-`d`:
Delete the character under the cursor. If the line is empty, exit the terminal. This command fails if the cursor is at the end of a non-empty line.
-  `Alt`-`d`:
Cut from under the cursor to the end of the current smallword.
-  `Ctrl`-`y`:
Paste the most recently cut text.
-  `Alt`-`y`:
Rotate between the most recently cut text. (Only works if the last action was either `Ctrl`-`y` or `Alt`-`y`.)
-  `Ctrl`-`u`:
Cut from the left side of the cursor to the beginning of the line.
-  `Ctrl`-`k`:
Cut from under the cursor to the end of the line.
-  `Ctrl`-`l`:
Clear the screen leaving the current line untouched.
Same as the command `clear`, as far as I can tell.
-  `Ctrl`-`w`:
Cut one bigword to the left.
-  `Ctrl`-`t`:
Swap the character under the cursor with the character to the left of the cursor. If this is used at the end of the line, swap the last two characters before the cursor.
-  `Alt`-`t`:
Swap the current smallword with the previous smallword.
-  `Ctrl`-`v`:
Literally insert the next typed character. For example, `Ctrl`-`v` `Tab` will insert a literal Tab character instead of completing the command.
-  `Ctrl`-`x` `Ctrl`-`e`:
Open the default editor and execute the edited command. (This can be set with the `$EDITOR` variable, for example entering `EDITOR=vim` on a separate line will set the editor to Vim.)
-  `Alt`-`c`:
Capitalise the character under the cursor and move to the end of the current smallword.
-  `Alt`-`u`:
Make the current smallword uppercase. (From under the cursor to the end of the current sequence.)
-  `Alt`-`l`:
Make the current smallword all lowercase (from under the cursor to the end of the sequence) and move the cursor to the end the sequence.
-  `Alt`-`.` or `Alt`-`_`:
Paste the last argument of the previous command.
-  `Alt`-`Ctrl`-`y`:
Paste the second bigword of the previous command.
-  `Alt`-`Ctrl`-`e`:
Expand the current line. For example, `~` `Alt`-`Ctrl`-`e` will expand to `/home/$USER`.

# Processes

-  `Ctrl`-`c`:
Terminate the command.
-  `Ctrl`-`z`:
Stop the current process. Typing `bg` will restart it in the background and `fg` will restore it to the foreground.
-  `Ctrl`-`s`:
Freeze the terminal.
-  `Ctrl`-`q`:
Restore a frozen terminal.
-  `Ctrl`-`m` or `Enter`:
Enter the command.
-  `Ctrl`-`o`:
Accept the current line, then fetch the exact same line and print it on the new line.

# History

-  `Ctrl`-`p` or `Up Arrow Key`:
Show the previous command in the history.
-  `Ctrl`-`n` or `Down Arrow Key`:
Show the next command in the history.
-  `Alt`-`<`:
Move to the first item in the history.
-  `Alt`-`>`:
Move to the last item in the history (the current command, not the last executed command).
-  `Ctrl`-`r`:
Reverse-search the history incrementally.
For example, pressing `Ctrl`-`r`, then typing 'string', then pressing `Ctrl`-`r`, `Ctrl`-`r`, ..., will scroll through all commands in the history containing 'string'.
Press `Ctrl`-`g` to break out of the search.
-  `Alt`-`p`:
Reverse search the history non-incrementally.


The following commands are useful if you want to execute similar commands from your history.

- `!!`: An alias for the previous command. (Useful for `sudo !!`, for example.)
- `!string`: Execute the most recent command in the history beginning with 'string'.
- `!string:p`: Print the most recent command in the history beginning with 'string', so you see what *would* have been run if you typed `!string`.
- `!n`: Execute the *n*th command in the history, where *n* is a positive integer. Type `history` to get a list.
- `!$`: An alias for the last bigword of the previous command.
- `!^`: An alias for the first bigword of the previous command.
- `!*`: An alias for the previous command without the last bigword. (So if the previous command was `ls -A /home/$USER`, then `!*` would give just `ls -A`.)
- `!n:p`: Print the *n*th command in the history. `!$:p`, `!^:p`, ..., also work.
- `^string1^string2`: In the previous command, replace the first occurrence of "string1" with "string2", then execute.


# Completions

-  `Ctrl`-`x` `~`:
Print username completions.
-  `Alt`-`~`:
Attempt username completion.
-  `Ctrl`-`x` `!`:
Print command name completions.
-  `Alt`-`!`:
Attempt command name completion.
-  `Ctrl`-`x` `/`:
Print filename completions.
-  `Alt`-`/`:
Attempt filename completion.
-  `Ctrl`-`x` `$`:
Print shell variable completions.
-  `Alt`-`$`:
Attempt shell variable completion.
-  `Ctrl`-`x` `@`:
Show host name completions.
-  `Alt`-`@`:
Attempt hostname completion.
-  `Alt`-`&`:
Perform tilde expansion.
-  `Alt`-`*`:
Insert all possible completions.
-  `Alt`-`?`:
Show the current completion list.
-  `Alt`-`{`:
Insert all filename completions within braces.

# Scrolling

-  `Shift`-`Page Up`:
Scroll up one screen. (This may not work for some terminals. Use your mouse instead if you have one.)
-  `Shift`-`Page Down`:
Scroll down one screen.

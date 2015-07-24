---
title: Bash aliases
#description: none
author: Issa Rice
creation_date: 2015-01-02
last_major-revision_date: 2015-01-02
language: English
# accepts "notes", "draft", "in progress", or "mostly finished"
#status: notes
# accepts "certain", "highly likely", "likely", "possible", "unlikely", "highly unlikely", "remote", "impossible", "log", "emotional", or "fiction"
#belief: 
# accepts "CC0", "CC-BY", or "CC-BY-SA"
license: CC-BY
tags: bash, linux
---


```bash
# For git

alias gstat='git status'
alias gpull='git pull origin master'
alias gpush='git push origin master'

alias yjisho='surfraw duckduckgo -browser=elinks \!yjisho '
alias jisho='surfraw duckduckgo -browser=elinks \!yjisho '
alias j='surfraw duckduckgo -browser=elinks \!yjisho '

alias duck='surfraw duckduckgo -browser=elinks '

alias d='surfraw duckduckgo -browser=elinks \!d '
alias define='surfraw duckduckgo -browser=elinks \!d '

alias google='surfraw google -browser=elinks '
alias goog='surfraw google -browser=elinks '
alias g='surfraw google -browser=elinks '


vim .uim.d/customs/custom-anthy-keys1.scm 
```

```{.bash}
### BEGIN append_to_bashrc.bash

# Save the file as "append_to_bashrc.bash", and source the contents using:
#     source ~/projects/riceissa.github.com/append_to_bashrc.bash
# or something similar inside ".bashrc".

PS1='[\u:\W]> '

# this is for getting the temperature of the computer, but one needs to have the sensors installed
alias temp='sensors | grep -v "N/A"'
alias swapswap='sudo swapoff -a && sudo swapon -a'
alias {update,upgrade}='sudo aptitude update && sudo aptitude upgrade'

# For git

alias gstat='git status'
alias gadd='git add'
alias gpull='git pull origin master'
alias gpush='git push origin master'
alias gdiff='git diff --color'
alias gdiffstage='git diff --cached --color'

# Surfraw

alias yjisho='surfraw duckduckgo -browser=elinks \!yjisho '
alias jisho='surfraw duckduckgo -browser=elinks \!yjisho '
alias j='surfraw duckduckgo -browser=elinks \!yjisho '

alias duck='surfraw duckduckgo -browser=elinks '

alias d='surfraw duckduckgo -browser=elinks \!d '
alias define='surfraw duckduckgo -browser=elinks \!d '

alias google='surfraw google -browser=elinks '
alias goog='surfraw google -browser=elinks '
alias g='surfraw google -browser=elinks '

### END append_to_bashrc.bash
```

---
title: Mutt
date: 2016-11-07
created: 2016-11-07
author: Issa Rice
---

Make sure the file is not readable by anyone except you:

    $ chmod 600 ~/.muttrc

~~~~
# ~/.muttrc
set imap_user = "⟨USERNAME@gmail.com⟩"
set imap_pass = "⟨PASSWORD⟩"

set folder = "imaps://imap.gmail.com:993"
set spoolfile = "imaps://imap.gmail.com:993/INBOX"
set postponed="imaps://imap.gmail.com/[Gmail]/Drafts"

# for more information about different ports, see this page:
# http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
set smtp_url = "smtp://⟨USERNAME⟩@smtp.gmail.com:587/"
set smtp_pass = "⟨PASSWORD⟩"
set from = "⟨USERNAME⟩@gmail.com"
set realname = "⟨First Last⟩"

set message_cachedir="~/.mutt/cache/bodies"
set certificate_file="~/.mutt/certificates"
~~~~


---
title: Disk encryption on Linux
author: Issa Rice
created: 2017-01-28
date: 2017-01-28
---

# Clarifying the terminology

As of Ubuntu 16.10, the default disk encryption method used when selecting
"Encrypt the new Ubuntu installation for security" during installation seems to
use dm-crypt with LUKS.
Here:

* **dm-crypt** is "is the standard device-mapper encryption functionality
  provided by the Linux kernel" ([ArchWiki][arch_de]).
* **LUKS** (Linux Unified Key Setup) is " an additional convenience layer which
  stores all of the needed setup information for dm-crypt on the disk itself
  and abstracts partition and key management in an attempt to improve ease of
  use and cryptographic security" ([ArchWiki][arch_de]).
* **cryptsetup** is the actual utility that you run as a user.

# Backing up the LUKS header

Check that the device is a LUKS device:

    $ sudo cryptsetup isLuks -v /dev/sda5
    Command successful.

Then [back up the header](https://www.gwern.net/Notes#november-2016-data-loss-postmortem):

    sudo cryptsetup luksHeaderBackup /dev/sda5 \
        --header-backup-file luks-header.bin.crypt

See also the cryptsetup FAQ [§6 Backup and Data
Recovery](https://gitlab.com/cryptsetup/cryptsetup/wikis/FrequentlyAskedQuestions#6-backup-and-data-recovery)

# External links

* [What's the difference between LUKS, cryptsetup, and
  dm-crypt?](https://www.reddit.com/r/linuxquestions/comments/5a0kl7/whats_the_difference_between_luks_cryptsetup_and/)
  on /r/linuxquestions

[arch_de]: https://wiki.archlinux.org/index.php/Disk_encryption

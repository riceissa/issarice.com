---
title: Disk encryption on Linux
author: Issa Rice
created: 2017-01-28
date: 2017-01-28
---

# Backing up the LUKS header

Check that the device is a LUKS device:

    $ sudo cryptsetup isLuks -v /dev/sda5
    Command successful.

Then back up the header:

    sudo cryptsetup luksHeaderBackup /dev/sda5 \
        --header-backup-file luks-header.bin.crypt

# External links

* [gwern's "November 2016 data loss
  postmortem"](https://www.gwern.net/Notes#november-2016-data-loss-postmortem)

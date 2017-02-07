---
title: Burning CDs and DVDs on the command line
tags: linux, debian
---
 (Debian Wheezy)

It is occasionally useful to know how to perform basic tasks on the command line, especially since most commands are universal across distributions.
Below we present instructions for burning and verifying CDs and DVDs on the command line.
The following was tested on Debian Wheezy (during testing) using Wodim 1.1.11.

# CD

1. Install `wodim` using

    ~~~~
    sudo aptitude install wodim
    ~~~~

1. Find out which disk is the CD drive using

    ~~~~
    wodim --devices
    ~~~~

    Example output:

    ~~~~
    wodim: Overview of accessible drives (1 found) :
    -------------------------------------------------------------------------
    0  dev='/dev/sg1'  rwrw-- : 'SONY' 'CD-RW  CRX320E'
    -------------------------------------------------------------------------
    ~~~~

    In this document, we will use `/dev/sg1` as the CD drive from now
    on.

1. Insert the CD into the computer.
If Debian automatically mounts the CD, then you must unmount it (we will
explain how).  First, find where the disk is mounted; on Gnome, a file
window may open, in which case you can just hit `Ctrl-l` to see the
location.  On Debian, it is most likely located somewhere in the
`/media` directory.  If you cannot find it there, it may not have even
mounted, in which case you may skip this step and the next step.

    In this document, we will assume the CD automatically mounted at
    `/media/cdrom0` from now on.

1. Unmount the CD (but not eject it) using

    ~~~~
    sudo umount /media/cdrom0
    ~~~~

1. If your CD is a CD-RW with data already on it: Blank the old image using

    ~~~~
    wodim dev=/dev/sg1 blank=fast
    ~~~~

1. Burn the `.iso` image. We will assume the file is called `image.iso`.

    Use the command

    ~~~~
    wodim -v -dao dev=/dev/sg1 image.iso
    ~~~~

    See the manual for `wodim` for more information. Use `man wodim`.

1. Now we must verify whether the image was correctly burned or not.

    Unfortunately there doesn't seem to be any logical way to do this.

    Here is what worked:

    ~~~~
    dd if=/dev/cdrom bs=2048 conv=sync,notrunc | sha1sum
    ~~~~

    that is, if one is to verify using `sha1sum`.  One can of course use
    `md5sum` etc.

    The following also worked:

    ~~~~
    dd if=/dev/cdrom | sha1sum
    ~~~~

    For some reason, none of the following worked:

    ~~~~
    dd if=/dev/sg1 bs=2048 conv=sync,notrunc | sha1sum
    dd if=/dev/cdrom0 bs=2048 conv=sync,notrunc | sha1sum
    dd if=/dev/scd bs=2048 conv=sync,notrunc | sha1sum
    dd if=/dev/scd0 bs=2048 conv=sync,notrunc | sha1sum
    ~~~~

    During the test run, the SHA1 checksum actually matched the original
    checksum. (So this method doesn't completely fail.)

One must remember that CD(-RW)s get old and will eventually cause
problems when reading and writing (burning).  The CD/DVD drive can also
cause problems (i.e., not reading and writing correctly).  In short,
problems can be software or hardware.  It is hoped that this document
eliminates any mysteries regarding the former.



# DVD

1. Install the relevant package:

    ~~~~
    sudo aptitude install dvd\+rw-tools
    ~~~~

1. Reformat/prepare the DVD:

    ~~~~
    dvd+rw-format -force /dev/cdrom
    ~~~~

1. Burn the image; we assume the image file is called `image.iso`:

    ~~~~
    growisofs -dvd-compat -Z /dev/cdrom=image.iso
    ~~~~

1. Check how big the image is:

    ~~~~
    ls -ltr image.iso
    ~~~~

1. Suppose the file size returned by the previous command was `123456789`.
Enter this number in the expression below to find the hash value:

    ~~~~
    dd if=/dev/cdrom bs=512 count=$((123456789/512)) | md5sum
    ~~~~

    Of course, `md5sum` can be replaced by any of `sha1sum`, `sha256sum`, `sha512sum`, etc.

1. Compare the hash from the DVD disc image with the hash from the original ISO image (usually available on the website where you downloaded the image; however if not, `md5sum image.iso` will also work).

# References

The following web pages were especially helpful.

- “Burning iso images with wodim loses 2048 bytes at the end”.
<http://superuser.com/questions/155192/burning-iso-images-with-wodim-loses-2048-bytes-at-the-end>

- “CdDvd/Burning—Command Line (Terminal)—Burning a CD on the Command Line with wodim”.
<https://help.ubuntu.com/community/CdDvd/Burning#Burning_a_CD_on_the_Command_Line_with_wodim>

- “Writing CD and DVD images”.
<https://web.archive.org/web/20140415043153/http://wiki.mandriva.com/en/Writing_CD_and_DVD_images>

- “DVD Burning”.
<https://wiki.archlinux.org/index.php/DVD_Burning>.

- “Why does my burned Ubuntu DVD have a different hash/checksum than the iso?”
<http://askubuntu.com/questions/145611/why-does-my-burned-ubuntu-dvd-have-a-different-hash-checksum-than-the-iso/177625#177625>

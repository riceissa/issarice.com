#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from slugify import slugify_unicode

if __name__ == '__main__':
    line = sys.stdin.next()
    slug = slugify_unicode(line, to_lower=True).encode('utf-8')
    sys.stdout.write(slug)

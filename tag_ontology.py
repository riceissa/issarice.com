#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2014, Issa Rice
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from collections import OrderedDict

# Dictionary of tag synonyms or "shortcuts" to be used with
# standardize_tags.  This is mostly useful when
# a tag can be spelled in multiple ways or has common abbreviations.
# This should be used before doing tag implications.
tag_synonyms = {
    "effective-altruism":
        ["ea", "effective altruism", "effectivealtruism"],
    "university-of-washington":
        ["uw", "uwashington", "university of washington"],
    "computing":
        ["hacking", "computers"],
    "computer-science":
        ["cs", "computer science"],
    "content-creation":
        ["content creation"],
    "set-theory":
        ["set theory"],
    "lesswrong":
        ["lw", "less-wrong", "less wrong"],
    "cognito-mentoring":
        ["cm", "cognito mentoring", "cognito"],
    "math":
        ["maths", "mathematics"],
    "links-collection":
        ["links collection", "link-collection", "link collection",
        "resources", "links"],
    "atmopsheric-sciences":
        ["atmos"],
    "chemistry":
        ["chem"],
    "quantified-self":
        ["qs", "quantified self", "life logging", "life-logging",
        "sousveillance"],
    "psychology":
        ["psych"],
    "university-of-washington-honors-program":
        ["uw-honors", "uw honors", "honors program", "honors-program"],
}

# List of tag implications to be used with imply_tags.  Below, (a, [b])
# means that the tag a implies tag b; so if you have a page with tag a,
# it will automatically also be applied the tag b.  Note that the order
# here is important.  Let's say we also have
#    (b, [c])
# then doing tag a should also imply tag c, since the implication chain
# goes a -> b -> c.  In other words, tag implication should be
# transitive, in that a -> b and b -> c together mean a -> c.  This
# means though that you should put (a, [b]) before (b, [c]), since then
# the first will be applied, leaving you with the tags a and b, and then
# the second will be applied, leaving you with tags a, b, and c. (This
# is an OrderedDict so that the above works.)  It is also assumed here
# that everything in tag_implications is standardized.
tag_implications = OrderedDict([
    ("halmos", ["math"]),
    ("hakyll", ["haskell"]),
    ("python", ["programming"]),
    ("latex", ["computing"]),
    ("linux", ["computing"]),
    ("pandoc", ["computing"]),
    ("openbsd", ["computing"]),
    ("lesswrong", ["rationality"]),
    ("logic", ["math"]),
    ("analysis", ["math"]),
    ("physics", ["science"]),
    ("atmospheric-sciences", ["science"]),
    ("astronomy", ["science"]),
    ("chemistry", ["science"]),
    ("haskell", ["programming"]),
    ("depression", ["psychology"]),
    ("programming", ["computing"]),
])

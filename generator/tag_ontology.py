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
TAG_SYNONYMS = {
    "advantages":
        ["pros", "pro"],
    "advantages and disadvantages":
        ["procon", "pros and cons"],
    "atmospheric sciences":
        ["atmos"],
    "biology":
        ["bio"],
    "Bryan Caplan":
        ["caplan"],
    "chemistry":
        ["chem"],
    "cause prioritization":
        ["cp"],
    "Cognito Mentoring":
        ["cm", "cognito-mentoring", "cognito"],
    "computer science":
        ["cs", "computer-science"],
    "computing":
        ["hacking", "computers"],
    "content creation":
        [],
    "Debian":
        ["deb"],
    "digital preservation":
        ["archival", "archiving", "digital archives", "digital archiving", "digital archival", "data archiving", "data archival"],
    "disadvantages":
        ["con", "cons"],
    "economics":
        ["econ"],
    "effective altruism":
        ["ea", "effective-altruism", "effectivealtruism"],
    "Eliezer Yudkowsky":
        ["eliezer", "yudkowsky"],
    "English":
        [],
    "Facebook":
        [],
    "GitHub":
        [],
    "Halmos":
        [],
    "Haskell":
        [],
    "Hakyll":
        [],
    "human biodiversity":
        ["hbd"],
    "high school":
        ["hs"],
    "Japan":
        [],
    "Jekyll":
        [],
    "LaTeX":
        [],
    "LessWrong":
        ["lw", "less wrong"],
    "links collection":
        ["link-collection", "resources", "links"],
    "Linux":
        [],
    "math":
        ["maths", "mathematics"],
    "open borders":
        ["ob"],
    "OpenBSD":
        [],
    "Pandoc":
        [],
    "Paul Graham":
        [],
    "Peter Thiel":
        ["thiel"],
    "psychology":
        ["psych"],
    "Python":
        ["py"],
    "quantified self":
        ["qs", "life-logging", "sousveillance"],
    "Quora":
        [],
    "Scott Alexander":
        [],
    "self-improvement":
        [],
    "set theory":
        ["set-theory"],
    "site info":
        ["site"],
    "Slate Star Codex":
        ["ssc", "slate-star"],
    "University of Washington":
        ["uw", "uwashington", "university-of-washington"],
    "University of Washington Computer Science and Engineering":
        ["uw cse"],
    "University of Washington course review":
        ["uw course", "uw course review"],
    "University of Washington honors program":
        ["uw-honors", "uw honors", "honors-program"],
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
TAG_IMPLICATIONS = OrderedDict([
    ("Halmos", ["math"]),
    ("Hakyll", ["Haskell"]),
    ("Python", ["programming"]),
    ("LaTeX", ["computing"]),
    ("Linux", ["computing"]),
    ("Pandoc", ["computing"]),
    ("OpenBSD", ["computing"]),
    ("LessWrong", ["rationality"]),
    ("logic", ["math"]),
    ("real analysis", ["analysis"]),
    ("complex analysis", ["analysis"]),
    ("analysis", ["math"]),
    ("probability", ["math"]),
    ("physics", ["science"]),
    ("atmospheric sciences", ["science"]),
    ("astronomy", ["science"]),
    ("chemistry", ["science"]),
    ("Haskell", ["programming"]),
    ("depression", ["psychology"]),
    ("programming", ["computing"]),
    ("University of Washington course review", ["University of Washington"]),
    ("advantages", ["advantages and disadvantages"]),
    ("disadvantages", ["advantages and disadvantages"]),
    ("link rot", ["digital preservation"]),
])

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

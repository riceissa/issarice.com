# PUBLIC DOMAIN

# All the configuration variables for the static site generator.  The
# idea is that the user need only modify this file to suit their own
# static site content organization instead of having to look in other
# files like generator.py.

# Below, in general variables beginning with "SITE_" are those that
# affect the eventual presentation of the site, while those beginning
# with "PRE_" are about the working directory of the site creator.  In
# other words, if one writes one's markdown files in the directory
# "wiki/", then PRE_PAGE_DIRECTORY will be set to; however, if one then
# wants to publish those files to the root directory of the server, then
# SITE_PAGES_DIRECTORY will be "" (i.e. same as the site directory).

SITE_DIRECTORY = "_site/"
SITE_PAGES_DIRECTORY = "" # "" will make it the same as SITE_DIRECTORY
PRE_PAGES_DIRECTORY = "wiki/"
PRE_PAGES_GLOB = "*.md"
# Tags are pulled from the pages themselves, so they won't have a "PRE_"
# equivalent
SITE_TAGS_DIRECTORY = "_tags/"
SITE_CSS_DIRECTORY = "_css/"
PRE_CSS_DIRECTORY = "css/"
PRE_IMAGES_DIRECTORY = "images/"
SITE_IMAGES_DIRECTORY = ""
PRE_TEMPLATES_DIRECTORY = "templates/"
PRE_STATIC_DIRECTORY = "static/"
SITE_STATIC_DIRECTORY = "_static/"

# Pages that are automatically generated
ALL_PAGES_PAGE_LOCATION = "_all"
SITEMAP_LOCATION = "sitemap.xml"
RSS_FEED_LOCATION = "rss.xml"
ATOM_FEED_LOCATION = "atom.xml"

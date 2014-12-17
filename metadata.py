#!/bin/python
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

import json
from pandocfilters import Str, Space
import pandocfilters

def get_metadata_field(json_lst, field):
    '''
    Take a JSON list and a field name (str) and return a 
    the field value.
    '''
    try:
        x = json_lst[0]['unMeta'].get(field, {})
        return walk_metadata(x)
    except KeyError:
        return ''

def walk_metadata(x):
    '''
    x is a JSON dictionary of pandoc metadata
    Walks down a JSON dictionary in the pandoc metadata, returning a
    more manageable representation.
    FIXME: Maybe formatting for e.g. math should be retained instead of
    converting to a string?
    '''
    if x['t'] == 'MetaBool':
        return x['c']
    elif x['t'] == 'MetaInlines':
        final = pandocfilters.stringify(x)
        #print "inlines " + final, type(final)
        return final
    elif x['t'] == 'MetaString':
        final = pandocfilters.stringify(x)
        #print "string " + final, type(final)
        return final
    elif x['t'] == 'MetaList':
        lst = []
        for i in x['c']:
            lst.append(walk_metadata(i))
        return lst

# Functions for dealing with tags

def standardize_tags(tags, tag_synonyms):
    '''
    Take a list of tags (tags :: list) along with a dictionary of tag
    synonyms (tag_synonyms :: dict) and return a new list of tags, where
    all synonymous tags are standardized according to tag_synonyms.  For
    instance, if tag_synonyms contains the line
        "university-of-washington": ["uw", "uwashington"],
    and if tags contains "uw" or "uwashington", then this will be
    replaced by "university-of-washington".
    '''
    result = []
    if tags is None:
        tags = []
    tags = list(tags)
    for tag in tags:
        canonical = [key for key, value in tag_synonyms.items() if tag in value]
        if not canonical:
            canonical = [tag]
        result.extend(canonical)
    return result

def imply_tags(tags, tag_implications):
    '''
    Take a list of tags (tags :: list) along with an OrderedDict of tag
    implications (tag_implications :: OrderedDict).  Return a new list
    of tags that includes all the implications.  Apply this after
    standardizing tags.
    '''
    result = list(tags)
    for key in tag_implications:
        if key in result:
            result.extend(tag_implications.get(key))
    return list(set(result))

def pack_tags(tags):
    '''
    Take a list of tags (tags :: list) and return a YAML-JSON list of
    the tags.
    '''
    result = []
    for tag in tags:
        tag_dict = {'t': 'MetaInlines', 'c': [Str(tag)]}
        result.append(tag_dict)
    return result
    #return list(intersperse([Str(i) for i in tags], Space()))

def get_tags(x):
    '''
    Take a YAML-JSON list or string of comma-delimited tags,
    and return a cleaned list of the tags.
    '''
    tags = get_metadata_field(x, "tags")
    if type(tags) is str or type(tags) is unicode:
        return [tag.strip(" ") for tag in tags.split(",") if tag != '']
    elif type(tags) is list:
        return tags
    else:
        return []

def organize_tags(json_lst, tag_synonyms, tag_implications):
    '''
    Takes a JSON list, a dict of tag_synonyms, and an OrderedDict of
    tag_implications.  Returns a dictionary with two entries:
    under 'json', the JSON string/dump of data with its tags
    organized according to tag_synonyms and tag_implications is stored;
    under 'tags' a list of the cleaned/organized (same as in the JSON
    dump) tags is stored.
    '''
    tags = get_tags(json_lst)
    tags = standardize_tags(tags, tag_synonyms)
    tags = imply_tags(tags, tag_implications)
    keep_tags = list(tags)
    tags_dict = json_lst[0]['unMeta'].get('tags', {})
    tags_dict['t'] = 'MetaList'
    tags_dict['c'] = pack_tags(tags)
    return {'json': json_lst,
            'tags': keep_tags}


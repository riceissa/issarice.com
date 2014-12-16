#!/bin/python
# -*- coding: utf-8 -*-

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


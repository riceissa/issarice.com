# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or distribute
# this software, either in source code form or as a compiled binary, for any
# purpose, commercial or non-commercial, and by any means.
#
# In jurisdictions that recognize copyright laws, the author or authors of this
# software dedicate any and all copyright interest in the software to the public
# domain. We make this dedication for the benefit of the public at large and to
# the detriment of our heirs and successors. We intend this dedication to be an
# overt act of relinquishment in perpetuity of all present and future rights to
# this software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

import json
import yaml
import util

def main():
    with open("tag_ontology.yaml", "r") as f:
        data = yaml.load(f)
    for tag in data:
        if data[tag]:
            for k in data[tag]:
                print(tag)
                data[tag][k] = util.parse_as_list(data[tag][k])
    print(data)


class CyclePresenceException(Exception):
    """
    A cycle is present in the digraph, when it shouldn't be (for a DAG).
    """
    pass

class TagNode(object):
    """
    Stores a node of a tag acyclic digraph. Supports aliases (synonyms).

    Attributes:
        canonical_name: A string containing the canonical form of the tag's
            name.
        aliases: A list of strings, where each string is an alias (synonym) of
            the tag.
    """

    def __init__(self, canonical_name, aliases=[]):
        """
        Initializes TagNode with a canonical_name and empty list of aliases.
        """
        self.canonical_name = canonical_name
        self.aliases = aliases

    def add_alias(self, alias):
        """
        Add a new alias.

        Args:
            alias: A string that is a new alias.

        Returns:
            None.
        """
        self.aliases.append(alias)

    def add_aliases(self, aliases):
        """
        Add a list of aliases to the node.

        Args:
            aliases: A list of strings; each string is a new alias.

        Returns:
            None.
        """
        self.aliases.extend(aliases)

    def __repr__(self):
        return "Tag('{}', {})".format(self.canonical_name.replace("'", "\\'"), self.aliases)

class TagDag(object):
    """
    Represents a directed acyclic graph (DAG) of TagNodes.

    Attributes:
        data: A dictionary containing the DAG. Each key is a string of the
            canonical tag name, and each value is a tuple (TagNode, [TagNode]),
            where the first element is the TagNode object of the node (instead
            of just the canonical name) and the second element is a list of
            TagNodes containing all the parent nodes (i.e. immediate ancestors).
        casing: A string stating how to deal with casing. Allowed options are:
            "smart", "lower", "upper", "literal".
    """

    def __init__(self, casing="smart"):
        """
        Initializes an empty DAG.
        """
        self.data = {}
        self.casing = casing

    def import_from_yaml_file(self, filename):
        """
        Args:
            filename: Location of YAML file.
        """
        with open(filename, "r") as f:
            dictionary = yaml.load(f)
        for tag in dictionary:
            if dictionary[tag]:
                for k in dictionary[tag]:
                    dictionary[tag][k] = util.parse_as_list(dictionary[tag][k])
        for tag in dictionary:
            node = TagNode(tag, dictionary[tag].get("aliases", []))
            self.add_tag(node)


    def __contains__(self, tag):
        """
        Check if a tag is in the DAG.

        Args:
            tag: 
        """
        if isinstance(tag, TagNode):
            return (tag.canonical_name in self.data)
        else:
            return (tag in self.data)

    @staticmethod
    def get_tag_name(tag):
        """
        Strip a tag down to its canonical form, or if it's already a
        string, return itself. Raise TypeError if not TagNode or string.
        """
        if isinstance(tag, TagNode):
            return tag.canonical_name
        elif isinstance(tag, str):
            return tag
        else:
            raise TypeError("Argument 'tag' must be a TagNode or string")

    def add_tag(self, tag):
        """
        Add the TagNode to the DAG. Since adding nodes and adding edges are
        separate processes, we don't have to perform any checks.
        """
        key = tag.canonical_name
        self.data[key] = (tag, [])

    def add_tags(self, tags):
        """
        Add a list of TagNodes to the DAG.
        """
        for tag in tags:
            self.add_tag(tag)

    def get_tag_entry(self, tag):
        query = get_tag_name(tag)
        if query in self.data:
            return self.data.get(query)
        else:
            raise ValueError("No such tag in DAG")

    def set_tag_entry(self, tup):
        if len(tup) != 2 or not isinstance(tup[0], TagNode) or not isinstance(tup[1], list):
            raise ValueError("Tuple tup is not well-formed")
        self.data[tup[0].canonical_name] = tup

    def get_tag(self, tag):
        return self.get_tag_entry(tag)[0]

    def get_parents(self, tag):
        lst = [t.canonical_name for t in self.get_tag_entry(tag)[1]]
        lst.sort()
        return lst

    def show_parents(self, tag):
        """
        Show all parent tags of tag in sorted order, i.e. all tags that
        are implied by tag.
        """
        print(self.show_parents(tag))

    def _get_ancestors(self, tag):
        lst = []
        for t in self.parents(tag):
            lst.append(t)
            lst.extend(self._get_ancestors(t))
        return lst

    def get_ancestors(self, tag):
        return self._get_ancestors(tag).sort()

    def show_ancestors(self, tag):
        print(self.get_ancestors(tag))

    def show_children(self, tag):
        pass

    def add_parent(self, tag, parent):
        """
        Make parent a parent of tag, where both tag and parent are in
        the DAG.
        """
        if self.is_descendant(tag, parent):
            raise CyclePresenceException("Adding this parent would cause a cycle in the DAG")
        else:
            name, parents = self.get_tag_entry(tag)
            p = self.get_tag(parent)
            parents.append(p)

    def add_child(self, tag, child):
        pass

    def add_parents(self, tag, parents):
        pass

    def add_children(self, tag: TagNode, children: '[TagNode]'):
        """
        """
        pass

    def is_descendant(self, tag_one, tag_two):
        """
        (TagNode, TagNode) -> bool

        Check if tag_one is a descendant of tag_two.
        """
        is_des = False


    def implies(self, tag_one, tag_two):
        """
        (TagNode, TagNode) -> bool

        Check if tag_one implies tag_two. Same as is_descendant.
        """
        return self.is_descendant(tag_one, tag_two)

    def write(self):
        pass

    def size(self):
        return len(self.data)

if __name__ == "__main__":
    main()

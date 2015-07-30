class CyclePresenceException(Exception):
    """
    A cycle is present in the digraph, when it shouldn't be (for a DAG).
    """
    pass

class TagNode(object):

    def __init__(self, canonical_name, aliases=[]):
        self.canonical_name = canonical_name
        self.aliases = aliases

    def add_alias(self, alias):
        self.aliases.append(alias)

    def add_aliases(self, aliases):
        self.aliases.extend(aliases)

    def __repr__(self):
        return "Tag({}, {})".format(self.canonical_name, self.aliases)

class TagDag(object):
    def __init__(self, casing="smart"):
        """
        For casing, allowed options are: "smart", "lower", "upper", "literal".
        """
        self.data = {}

    def __contains__(self, item):
        if isinstance(item, TagNode):
            return (item.canonical_name in self.data)
        else:
            return (item in self.data)

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
        Add the TagNode to the DAG. Since adding nodes and adding edges
        are separate processes, we don't have to perform any checks.
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

    def add_children(self, tag, children):
        pass

    def is_descendant(self, tag_one, tag_two):
        """
        (TagNode, TagNode) -> bool
        """
        pass

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


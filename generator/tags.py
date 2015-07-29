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
        return "Tag({}, [{}])".format(self.canonical_name, self.aliases)

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

    def get_tag(self, tag):
        query = get_tag_name(tag)
        if query in self.data:
            return self.data.get(query)[0]
        else:
            raise ValueError("No such tag in DAG")

    def show_parents(self, tag):
        """
        Show all parent tags of tag, i.e. all tags that are implied by
        tag. Return as a list of strings.
        """
        pass

    def show_children(self, tag):
        pass

    def add_parent(self, tag, parent):
        pass

    def add_child(self, tag, child):
        pass

    def add_parents(self, tag, parents):
        pass

    def add_children(self, tag, children):
        pass

    def implies(self, tag_one, tag_two):
        """
        (TagNode, TagNode) -> bool

        Check if tag_one implies tag_two.
        """
        pass

    def write(self):
        pass


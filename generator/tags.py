
class TagNode(object):

    def __init__(self, canonical_name, aliases=[]):
        self.canonical_name = canonical_name
        self.aliases = aliases

    def add_alias(self, alias):
        self.aliases.append(alias)

    def add_aliases(self, aliases):
        self.aliases.extend(aliases)

class TagDag(object):
    def __init__(self):
        self.data = {}

    def __contains__(self, item):
        if isinstance(item, TagNode):
            return (item.canonical_name in self.data)
        else:
            return (item in self.data)

    def add_tag(self, tag):
        key = tag.canonical_name
        self.data[key] = (tag, [])

    def add_tags(self, tags):
        for tag in tags:
            self.add_tag(tag)

    def get_tag(self, tag):
        return self.data.get(tag)

    def show_parents(self, tag):
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


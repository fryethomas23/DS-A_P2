class RouteTrieNode:
    def __init__(self):

        self.route_handler = None
        self.children = {}

    def insert(self, part):
        if part not in self.children:
            self.children[part] = RouteTrieNode()
        else:
            return

    def get_child(self, char):
        return self.children.get(char)

    def get_children(self):
        return self.children

    def set_route_handler(self, handler):
        self.route_handler = handler
        return

    def get_route_handler(self):
        return self.route_handler

# A RouteTrie will store our routes and their associated handlers


class RouteTrie:
    def __init__(self, home_handler, not_found_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.set_route_handler(home_handler)
        self.not_found = not_found_handler

    def insert(self, parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.root

        for part in parts:
            current.insert(part)
            current = current.get_child(part)

        current.set_route_handler(handler)

    def find(self, parts):
        current = self.root
        for part in parts:
            current = current.get_child(part)
            if not current:
                return self.not_found

        handler = current.get_route_handler()
        if handler:
            return handler
        else:
            return self.not_found

    def __str__(self):
        return self.str_recurse(self.root, 0, "")

    def str_recurse(self, node, tab, string):
        for char in node.get_children().keys():
            string += "--"*tab + char + " : {\n"
            string = self.str_recurse(node.get_child(char), tab+1, string)

        if node.get_route_handler():
            string += "--"*tab + "route handler: " + \
                str(node.get_route_handler()) + "\n"
        string += "--"*tab + "}\n"

        return string


class Router:
    def __init__(self, home_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(home_handler, not_found_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        return self.trie.find(self.split_path(path))

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        split = path.split('/')[1:]
        if split[-1] == "":
            split = split[:-1]
        return split


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))

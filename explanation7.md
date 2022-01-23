This problem uses a Trie because it allows O(n) insertion of routes, where n
is the number of parts of the route. It allows O(1) search, since it takes one pass
through the Trie. It also has O(n) space complexity becasue for each
part, n, in a path being inserted, the data structure will be at most
have n additional parts long.

time: O(n)
insertion: O(n)
search: O(l) where l is the length of the path to search for.
space: O(n) where n is the number of characters in a work being inserted.

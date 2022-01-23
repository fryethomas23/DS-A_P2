This problem uses a Trie because it allows O(n) insertion of words, where n
is the length of a word. It allows O(1) search, since it takes one pass
through the Trie. It also has O(n) space complexity becasue for each
character, n, in a word being inserted, the data structure will be at most
have n additional characters. The autocomplete portion would require O(k)
where k is the number of entries after a given prefix.

time: O(k) where k is the number of entries after a given prefix.
space: O(n) where n is the number of characters in a work being inserted.

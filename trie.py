class TNode:
    # Initialize a Trie node with empty children dictionary and mark as not end of word.
    # Time complexity O(1)
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False


class Trie:
    # Initialize the Trie with a root node.
    # Time complexity O(1)
    def __init__(self): self.root = TNode()

    # Return the total number of words stored in the Trie.
    # Time complexity O(N) where N is the total number of nodes
    def __len__(self): return len(self.list_words())

    # iteret over the items of the trie
    # Time complexity: O()
    def __iter__(self): return iter(self.list_words())

    # Return string representation of all words in the Trie separated by spaces.
    # Time complexity O(N) where N is the total number of nodes
    def __repr__(self): return " ".join(self.list_words())

    # Check if a word exists in the Trie using the 'in' operator.
    # Time complexity O(M) where M is the length of the word
    def __contains__(self, item):
        if not item: return False # Empty string validation
        curr_node = self.root
        
        for c in item:
            if c not in curr_node.children: return False
            curr_node = curr_node.children[c]
        return curr_node.is_end_of_word  # FIX: Must check if it's a complete word

    # Insert a word into the Trie by creating nodes for each character if not exist.
    # Time complexity O(M) where M is the length of the word
    def insert(self, word: str) -> bool:
        if not word: return False # Empty string validation
        curr_node = self.root

        for c in word:
            if c not in curr_node.children: curr_node.children[c] = TNode()

            curr_node = curr_node.children[c]
        curr_node.is_end_of_word = True
        return True

    # Search for an exact word in the Trie and return True if found, False otherwise.
    # Time complexity O(M) where M is the length of the word
    def search(self, word: str) -> bool:
        if not word: return False# Empty string validation
        
        curr_node = self.root

        for c in word:
            if c not in curr_node.children: return False
            curr_node = curr_node.children[c]
        return curr_node.is_end_of_word

    # Delete a word from the Trie. Removes nodes that are no longer needed.
    # Time complexity O(M) where M is the length of the word
    def delete(self, word: str) -> bool:
        if not word: return False # Empty string validation
            
        return self._delete(self.root, word, 0)

    # Check if a given prefix exists in the Trie.
    # Time complexity O(M) where M is the length of the prefix
    def has_prefix(self, prefix: str) -> bool:
        if not prefix: return False # Empty prefix validation. Empty prefix is technically valid for all words
        curr_node = self.root
        
        for c in prefix:
            if c not in curr_node.children: return False
            curr_node = curr_node.children[c]
        return True

    # Return all words in the Trie that start with the given prefix.
    # Time complexity O(N) where N is the total number of nodes in the subtree
    def starts_with(self, prefix: str):
        if not prefix: return self.list_words() # Empty prefix returns all words
            
        words = []
        curr_node = self.root

        for c in prefix:
            if c not in curr_node.children: return words

            curr_node = curr_node.children[c]

        def _dfs(curr_node, path):
            if curr_node.is_end_of_word: words.append("".join(path))

            for c, child_node in curr_node.children.items(): _dfs(child_node, path + [c])

        _dfs(curr_node, list(prefix))
        return words
    
    # Deprecated: Use starts_with() instead. Kept for backward compatibility.
    # Time complexity O(N) where N is the total number of nodes in the subtree
    def start_with(self, prefix): return self.starts_with(prefix)

    # Return a list of all words stored in the Trie.
    # Time complexity O(N) where N is the total number of nodes
    def list_words(self):
        words = []

        def _dfs(curr_node, path):
            if curr_node.is_end_of_word: words.append("".join(path))
            
            for c, child_node in curr_node.children.items(): _dfs(child_node, path + [c])

        _dfs(self.root, [])
        return sorted(words)  # ENHANCEMENT: Return sorted list for consistency

    # Helper function for delete that recursively removes a word from the Trie.
    # Time complexity O(M) where M is the length of the word
    def _delete(self, curr_node, word, index):
        if index == len(word):
            if not curr_node.is_end_of_word: return False

            curr_node.is_end_of_word = False
            return len(curr_node.children) == 0
        
        c = word[index]
        node = curr_node.children.get(c)

        if node is None: return False

        if delete_curr_node := self._delete(node, word, index + 1):
            del curr_node.children[c]
            return len(curr_node.children) == 0 and not curr_node.is_end_of_word
        
        return False  # ENHANCEMENT: Explicit return for clarity


if __name__ == "__main__":
    print("==" * 30, "\nTrie:\nBeginning:\n", "__" * 30)
    print()

    T = Trie()

    T.insert("hello")
    T.insert("henry")
    T.insert("mike")
    T.insert("minimal")
    T.insert("minimun")

    print("All words:", T.list_words())
    print("Has prefix 'mi':", T.has_prefix("mi"))
    print("Words starting with 'mi':", T.starts_with("mi"))
    print("Prefix 'hell' exists:", T.has_prefix("hell"))
    print("Word 'hell' in Trie:", "hell" in T)  # Bug fix test: should be False

    deleted = T.delete("minimal")
    print("Deleted 'minimal':", deleted)

    print("Search 'mini':", T.search("mini"))

    T.insert("mini")

    print("Total words:", len(T))
    print("Trie contents:", T)
    print("'henry' in Trie:", "henry" in T)

    for i in T: print(i)

    print("==" * 30, "\nTrie - End\n")
    print()

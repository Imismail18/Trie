# Trie Data Structure Implementation

A robust Trie (prefix tree) implementation in Python with full functionality for word insertion, search, deletion, and prefix matching. Features include input validation, type hints, sorted word listings, and optimized time complexity. Supports finding all words with a given prefix and checking prefix existence. Ideal for autocomplete, spell-checking, and word search applications.

## Features

- **Insert**: Add words to the Trie efficiently
- **Search**: Find exact words with O(M) time complexity
- **Delete**: Remove words while maintaining Trie structure
- **Prefix Matching**: Find all words with a given prefix
- **Prefix Check**: Verify if a prefix exists in the Trie
- **Input Validation**: Handle edge cases like empty strings
- **Type Hints**: Full Python type annotations
- **Sorted Output**: Words returned in sorted order

## Usage

```python
from trie import Trie

# Create a Trie instance
trie = Trie()

# Insert words
trie.insert("hello")
trie.insert("henry")
trie.insert("mike")

# Search for words
print(trie.search("hello"))  # True
print(trie.search("hell"))   # False (prefix, not a word)

# Check if a word is in the Trie
print("hello" in trie)  # True

# Find all words with a prefix
print(trie.starts_with("he"))  # ['hello', 'henry']

# Delete a word
trie.delete("hello")

# List all words
print(trie.list_words())  # Sorted list of all words
```

## Time Complexity

- **insert(word)**: O(M) where M is word length
- **search(word)**: O(M) where M is word length
- **delete(word)**: O(M) where M is word length
- **has_prefix(prefix)**: O(M) where M is prefix length
- **starts_with(prefix)**: O(N) where N is total nodes in subtree
- **list_words()**: O(N) where N is total nodes

## Author

Ismail - [@Imismail18](https://github.com/Imismail18)

## License

MIT License

Copyright (c) 2026 Ismail

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

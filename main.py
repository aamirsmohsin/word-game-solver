class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.word = True

    def search(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.word

class TrieNode:
    def __init__(self):
        self.children = {} # letter -> TrieNode
        self.word = False

def build_trie():
    prefix_tree = Trie()

    with open("words.txt") as f:
        for word in f:
            if len(word.strip()) > 2:
                prefix_tree.insert(word.lower().strip())

    return prefix_tree

def build_board(characters):
    board = [["" for j in range(4)] for i in range(4)]

    for i in range(4):
        for j in range(4):
            board[i][j] = characters[i * 4 + j]

    return board

def find_words(board, valid_words, prefix_tree, scoring):
    directions = [[-1, -1, "LU"], [-1, 0, "U"], [-1, 1, "RU"], [0, 1, "R"], [1, 1, "RD"], [1, 0, "D"], [1, -1, "LD"], [0, -1, "L"]]
    visited = set()
    
    def find_helper(r, c, word, path, node):
        if r not in range(4) or c not in range(4):
            return
        if (r, c) in visited:
            return
        if board[r][c] not in node.children:
            return
        
        visited.add((r, c))

        word += board[r][c]
        node = node.children[board[r][c]]

        if node.word:
            valid_words.append((scoring[len(word)], word, tuple(path)))

        for dr, dc, dir in directions:
            find_helper(r + dr, c + dc, word, path + [dir], node)
        
        visited.remove((r, c))

    for r in range(4):
        for c in range(4):
            find_helper(r, c, "", [(r, c)], prefix_tree.root)

def WordHunt():
    prefix_tree = build_trie()
    scoring = {3 : 100, 4 : 400, 5 : 800, 6 : 1400, 7 : 1800, 8 : 2200}

    characters = input("Enter the board here: ")
    board = build_board(characters)

    valid_words = [] # (value, word, (start, (path))

    find_words(board, valid_words, prefix_tree, scoring)
    valid_words.sort()

    words_seen = set()

    for score, word, path in valid_words:
        if word in words_seen:
            continue

        words_seen.add(word)

        print(f'{word} : {score}\nPath: {path}\n')

def build_list(characters):
    res = [''] * 6

    for i in range(6):
        res[i] = characters[i]
    
    return res

def generate_words(board, valid_words, prefix_tree, scoring):
    visited = set()

    def generate_helper(i, word, node):
        if i in visited:
            return
        if board[i] not in node.children:
            return
        
        visited.add(i)

        word += board[i]
        node = node.children[board[i]]

        if node.word:
            valid_words.append((scoring[len(word)], word))

        for j in range(6):
            generate_helper(j, word, node)
        
        visited.remove(i)

    for i in range(6):
        generate_helper(i, "", prefix_tree.root)    

def Anagrams():
    prefix_tree = build_trie()
    scoring = {3 : 100, 4 : 400, 5 : 1200, 6 : 2000}

    characters = input("Enter the characters here: ")
    board = build_list(characters)

    valid_words = []

    generate_words(board, valid_words, prefix_tree, scoring)
    valid_words.sort()

    words_seen = set()

    for score, word in valid_words:
        if word in words_seen:
            continue

        words_seen.add(word)

        print(f'{word} : {score}')

def main():
    while True:
        print("1: WordHunt")
        print("2: Anagrams")
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            WordHunt()
        elif choice == "2":
            Anagrams()
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
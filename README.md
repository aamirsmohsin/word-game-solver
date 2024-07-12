# word-game-solver

A lightweight solver for popular iMessage games WordHunt and Anagrams.

# How It Works

It implements depth-first search and a trie data structure to compute a list of the highest-scoring valid words (and paths), given the game's board/character set.

# How To Use

1. Download the Github Repository and run `python main.py` in the root directory.

2. Select either the WordHunt or Anagrams mode by entering '1' or '2'.

3. Wait for 'Enter the board here' / 'Enter the characters here'. For WordHunt, input the board from left to right:

i.e. 

Board:
      
	a b c d      
    e f g h
    i j k l
    m n o p

Input:

	abcdefghijklmnop

4. Enter the solutions produced by the script.

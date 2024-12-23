A Python program that solves the Letter Boxed puzzle game (of the New York Times).

Link to the New York Times online game: https://www.nytimes.com/puzzles/letter-boxed

### How to use:
1. Install the requirements (pip install -r requirements.txt)
2. Run create_prefix_set.py, which will download a text file containing 333,000 English words, and save them in serialized data structure as prefix_set.pkl.
   This has to be run only once. The file will be used for all subsequent uses of solve_letter_boxed.py.
3. Run solve_letter_boxed.py.
   In the --spec_path argument, put the path of one of the spec files in the spec directory, or your own custom spec.
   In the --n argument, you can determine the number of solutions to be found (default 1).
   Add --randomize to get different solutions in each run.

### Letter Boxed:
Each puzzle contains 4 groups of 3 letters each.
The goal of the game is to find a list of words that has the following properties:
1. Each word is a real English word
2. Each word begins with the last letter of the previous word (first word can begin with any letter)
3. Subsequent letters must be from different letter groups
4. All 12 letters appear at least once
The shorter the list, the better the solution.
   
![Letter Boxed Image](https://upload.wikimedia.org/wikipedia/en/3/3e/NY_Times_Letter_Boxed.png)

### How it works:
The puzzle is treated as a Graph Traversal problem, where each vertex is a a list of words, and the edges are of 4 types:
1. First letter of first word - can be any letter.
2. Letter addition - only exists if the letter transition is legal in the game, and the last word is still a prefix of some English word (to prune impossible solutions early on).
3. End of word - only exists if the last word is a complete English word.
4. First letter of a new word - must be the last letter of the previous word.

The weights of the edges are 1, 0, 0, 1, respectively, so the weight of a path to a solution is the number of words in the solution.

A vertex whose last word is empty (last word has ended), and which covers all 12 letters, is considered a solution.

### Note:
The word frequency file also contains "words" that are popular in the internet, but are not considered real words, like "talkin" (slang for "talking"). This results in some solutions that contain words that the original game will not accept.

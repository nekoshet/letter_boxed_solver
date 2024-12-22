A Python program that solves the Letter Boxed puzzle game (of the New York Times).
Link to the New York Times online game: https://www.nytimes.com/puzzles/letter-boxed

How to use:
1. Install the requirements (pip install -r requirements.txt)
2. Run create_prefix_set.py, which will download a text file containing 333,000 English words, and save them in serialized data structure as prefix_set.pkl.
   This has to be run only once. The file will be used for all subsequent uses of solve_letter_boxed.py.
3. Run solve_letter_boxed.py.
   In the --spec_path argument, put the path of one of the spec files in the spec directory, or your own custom spec.
   In the --n argument, you can determine the number of solutions to be found (default 1).
   Add --randomize to get different solutions in each run (effectively, only the order of the solutions is changed).

How it works:
The puzzle is treated as a Graph Traversal problem, where each vertex is a series of letters (sperated to multiple words), and each edge represents adding a certain letter.
In addition, there is a unique edge that symbolizes end of word.
The letter addition edge only exists if the letter transition is legal in the game, and the last word is still a prefix of some English word (to prune impossible solutions early on).
The end-of-word edge only exists if the last word IS an English word, making sure each word in the solution is a real word.
A vertex whose last word is a real English word, and which covers all the required letter, is considered a solution.

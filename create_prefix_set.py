# tal.levy
# 16.12.2024
import os
import pickle
import pyprind
import constants
import kagglehub


def create_prefix_set():
    dir_path = kagglehub.dataset_download(constants.word_freq_address)
    word_freq_path = os.path.join(dir_path, os.listdir(dir_path)[0])
    prefix_set = set()
    word_set = set()
    with open(word_freq_path, 'r') as file:
        input_lines = file.readlines()
    progbar = pyprind.ProgBar(iterations=constants.max_words - 1, title=f'iterating input words ({constants.max_words - 1})..')
    for line in input_lines[1:constants.max_words]:
        progbar.update(item_id=line)
        word = line.split(',')[0]
        word_set.add(word)
        for i in range(len(word)):
            prefix_set.add(word[:i])
    with open(constants.prefix_set_pkl, 'wb') as file:
        pickle.dump((prefix_set, word_set), file)


def main():
    create_prefix_set()


if __name__ == '__main__':
    main()

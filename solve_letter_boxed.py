# tal.levy
# 16.12.2024
import random
import pickle
import argparse
import nographs as nog
import constants


def shuffle_list(lst):
    return random.sample(lst, len(lst))


def get_used_letters(words):
    return set(''.join(words))


def get_missing_letters(words, boxed_letters):
    return boxed_letters - get_used_letters(words)


def create_letter_connections(spec):
    connections = {}
    for i in range(len(spec)):
        connected_groups = [spec[j] for j in range(len(spec)) if j != i]
        connected_letters = sum(connected_groups, [])
        curr_group = spec[i]
        for letter in curr_group:
            connections[letter] = connected_letters
    connections['['] = sum(spec, [])
    return connections


def solve_letter_boxed(spec, randomize=False):
    box_letters_set = set(sum(spec, []))
    letter_connections = create_letter_connections(spec)
    with open(constants.prefix_set_pkl, 'rb') as file:
        prefix_set, word_set = pickle.load(file)

    def next_vertices(words, _):
        if not words:
            letter_options = letter_connections['[']
            letter_options = shuffle_list(letter_options) if randomize else letter_options
            for letter in letter_options:
                yield (letter,), 0
        elif not words[-1]:
            yield words[:-1] + (words[-2][-1],), 1
        else:
            letter_options = letter_connections[words[-1][-1]]
            letter_options = shuffle_list(letter_options) if randomize else letter_options
            for letter in letter_options:
                new_word = words[-1] + letter
                if new_word in prefix_set:
                    yield words[:-1] + (new_word,), 0
            if len(words[-1]) >= 3 and words[-1] in word_set:
                yield words + ('',), 1

    def heuristic(words):
        return len(get_missing_letters(words, box_letters_set)) * constants.heuristic_factor

    traversal = nog.TraversalAStar(next_vertices)
    vertex = traversal.start_from(heuristic, ())

    for i, v in enumerate(vertex):
        if v and not v[-1]:
            if len(''.join(v)) >= len(box_letters_set):
                used_letters = get_used_letters(v)
                if used_letters == box_letters_set:
                    yield i, v


def parse_letter_boxed_spec(spec_path):
    spec = []
    with open(spec_path, 'r') as file:
        spec_lines = file.readlines()
    for line in spec_lines:
        line = line.strip()
        letters = line.split(' ')
        spec.append(letters)
    return spec


def print_letter_boxed_solutions(spec, randomize=False):
    for i, sol in solve_letter_boxed(spec, randomize):
        print(sol)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--spec_path', type=str, required=True)
    parser.add_argument('--randomize', action='store_true')
    args = parser.parse_args()
    spec = parse_letter_boxed_spec(args.spec_path)
    print_letter_boxed_solutions(spec, randomize=args.randomize)


if __name__ == '__main__':
    main()

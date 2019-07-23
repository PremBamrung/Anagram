import itertools
def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

english_words=load_words()
# if __name__ == '__main__':
#     english_words = load_words()
#     # demo print
#     print('carot' in english_words)


STRING_TARGET="bread"

possibility_list=(["".join(perm) for perm in itertools.permutations(STRING_TARGET)])
print("For the the word:",STRING_TARGET)
print("Number of possibility :",len(possibility_list))
anagram=[x for x in possibility_list if x in english_words and x != STRING_TARGET]
# anagram=[x for x in anagram if x != STRING_TARGET]
anagram=list(set(anagram))
anagram.sort()
print("Number of anagram :",len(anagram))
print(anagram)
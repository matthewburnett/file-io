# mburne1059@greenvilleschools.us
# Burnett, Matthew

words_alpha = open("words_alpha.txt", "r").read().splitlines()

print(f"Total words: {len(words_alpha)}")
print(
    f"Total 5 letter words: {len([word for word in words_alpha if len(word) == 5])}")
print(
    f"Total words longer than 7 letters: {len([word for word in words_alpha if len(word) > 7])}")

print(
    f"Total characters: {len([letter for word in words_alpha for letter in word])}")

print(
    f"Total words that don't have E: {len([word for word in words_alpha if 'e' not in word])}")

print(
    f"Total words that begin and end with same letter: {len([word for word in words_alpha if word[0] == word[-1]])}")

print(
    f"Total words with exactly 3 A's: {len([word for word in words_alpha if word.count('a') == 3])}")

print(
    f"Total words that have a Q but not followed by U: {len(list(set([word for word in words_alpha for i in range(len(word) - 1) if word[i] == 'q' else if word[i+1] != 'u' else if word[-1] == 'q' else if 'q' in words_alpha])))}")

# zoop = set([])

# for word in words_alpha:
#     for i in range(len(word) - 1):
#         if word[i] == 'q' and word[i+1] != 'u':
#             zoop.add(word)
#         if word[-1] == 'q':
#             zoop.add(word)
    
# if 'q' in words_alpha:
#         zoop.add('q')

# print(len(list(zoop)))


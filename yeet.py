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
    f"Total words that have a Q but not followed by U: {len([word for word in words_alpha if 'qu' not in word and 'q' in word])}")

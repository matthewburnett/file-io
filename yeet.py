words_alpha_r = open("words_alpha.txt", "r")
words_alpha_r = words_alpha_r.read().splitlines()
print(f"Total words: {len(words_alpha_r)}")
print(f"Total 5 letter words: {len([word for word in words_alpha_r if len(word) == 5])}")
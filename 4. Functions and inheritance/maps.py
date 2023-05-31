from random import shuffle

words = ["parsley", "avocados", "lemons", "onions", "tomatoes"]


def jumble(word):
    shuffled_words = list(word)
    shuffle(shuffled_words)
    return "".join(shuffled_words)  # join or the output is ''


# using for loop
shuffled_words = []

for word in words:
    shuffled_words.append(jumble(word))
print(shuffled_words)

# using maps(function, data)
# map(jumble, words)
print(list(map(jumble, words)))  # typecast to list


# using comprehension
print([jumble(word) for word in words])

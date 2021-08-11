# This piece of code is supposed to count the words in a text.

Counts = dict()
print('Enter a line of text: ')
Line = input('')

Words = Line.split()

print('Words: ', Words)

print('Counting... ')
for word in Words:
    Counts[word] = Counts.get(word, 0) + 1
print('Counts', Counts)
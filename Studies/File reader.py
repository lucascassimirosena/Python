
# Counting lines in a file

fhand = open('‪C:/Users/USER/Desktop/Jogos.txt', 'r')
count = 0
for line in fhand:
    count = count + 1
print('Contagem de linhas: ', count)
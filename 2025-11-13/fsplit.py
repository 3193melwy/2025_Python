infile = open(r"C:\chapter08\2025_Python\2025-11-13\proverbs.txt", "r")

for line in infile:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word)
infile.close()
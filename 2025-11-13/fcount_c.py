filename = input("파일명을 입력하세요: ").strip()

infile = open(filename, "r")

freqs = {}

for line in infile:
    for char in line.strip():  
        if char in freqs:  
            freqs[char]+=1  
    else:  
        freqs[char]=1

print(freqs)
infile.close()


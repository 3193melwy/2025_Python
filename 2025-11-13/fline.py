infile=open(r"C:\chapter08\2025_Python\2025-11-13\proverbs.txt")

outfile=open("output.txt","w") 

i=1

for line in infile: 
    outfile.write(str(i)+": "+line)    
    i=i+1 
    
infile.close()  
outfile.close()
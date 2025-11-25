infile=open(r"C:\chapter08\2025_Python\2025-11-13\phones.txt","r", encoding="utf-8")  
line=infile.readline()  
while line!="":

    print(line)  
    
    line=infile.readline()  

infile.close()
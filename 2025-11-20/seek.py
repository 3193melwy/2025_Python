with open(r'C:\chapter08\2025_Python\2025-11-13\proverbs.txt', 'rb') as file:
    file.seek(10,0)

    position = file.tell()
    print("현재 파일 포인터 위치 : ", position)

    data = file.read(5)
    print("읽은 데이터 : ", data)
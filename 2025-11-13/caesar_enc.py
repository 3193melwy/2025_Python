def caesar_cipher(text,key):  
    result=""  
    for char in text:  
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')  
            shifted_char = chr((ord(char) - shift+key) % 26 + shift)  
            result += shifted_char  
        else:  
            result += char
    return result  

def encrypt_file(input_file, output_file, key):  
    with open(input_file, 'r') as file:  
        plaintext = file.read()  
    encrypted_text = caesar_cipher(plaintext, key)  
    with open(output_file,'w') as file:  
        file.write(encrypted_text)  

input_filename = 'phones.txt'  
encrypted_filename = 'phones(enc).txt'  
encryption_key = 3  

encrypt_file(input_filename, encrypted_filename, encryption_key)  
print(f"{input_filename}을(를) 암호화하여{encrypted_filename}로 저장했습니다.")
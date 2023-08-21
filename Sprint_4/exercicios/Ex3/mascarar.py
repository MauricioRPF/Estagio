import hashlib

while True:
    string = input("Digite uma string, ou 'sair' para encerrar: ")
    
    if string.lower() == "sair":
        break
    
    sha1_hash = hashlib.sha1(string.encode()).hexdigest()
    print("Hash SHA-1 da string:", sha1_hash)
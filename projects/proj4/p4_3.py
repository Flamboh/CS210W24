'''
CIS 210 proj 4 - 3
Author: Oliver Boorstein
Credits: N/A
Implement a simple replacement cipher (ROT-13)
'''

def encrypt(msg: str) -> str:
    msg = msg.lower()
    
    encrypted = ""

    for index in range(len(msg)):
        original_ord = ord(msg[index])
        if original_ord >= 97 and original_ord <= 122:
            new_ord = original_ord + 13
            if new_ord > 122:
                new_ord -= 26
        else:
            new_ord = original_ord
        encrypted += chr(new_ord)
    return encrypted

def decrypt(msg: str) -> str:
    msg = msg.lower()

    decrypted = ""

    for index in range(len(msg)):
        current_ord = ord(msg[index])
        if current_ord >= 97 and current_ord <= 122:
            decrypted_ord = current_ord - 13
            if decrypted_ord < 97:
                decrypted_ord += 26
        else:
            decrypted_ord = current_ord
        decrypted += chr(decrypted_ord)
    return decrypted

if __name__ == "__main__":
    
    message = "Two driven jocks help fax my big quiz"
    encrypted = encrypt(message)
    print(encrypted)
    decrypted = decrypt(encrypted)
    print(decrypted)


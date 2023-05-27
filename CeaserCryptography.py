
print("Welcme to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("Encryption")
    msg=input("Enter your message:")
    key=int(input("Enter any key from 1 to 94:"))
    encrypted_text=""
    for i in range(len(msg)):
        temp=(ord(msg[i])+key)
        if(temp>126):
            temp=temp-127+32
        encrypted_text+=chr(temp)    
    print("Encrypted:"+encrypted_text)    
    main()

def decryption():
    print("Decryption")
    en_msg=input("Enter the encrypted message:")
    de_key=int(input("Enter any key from 1 to 94:"))
    decrypted_text=""
    for i in range(len(en_msg)):
        temp=(ord(en_msg[i])-de_key)
        if (temp<32):
            temp=temp+127-32
        decrypted_text+=chr(temp)    
    print("Decrypted:"+decrypted_text)    
    
if __name__ == "__main__":
    main()

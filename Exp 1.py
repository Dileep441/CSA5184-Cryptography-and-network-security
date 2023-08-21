plain_text=input("Enter a your plain text:")
k=int(input("Enter key value:"))
for i in range(len(plain_text)):
    char=plain_text[i]
    if plain_text.isupper():
        print(chr((ord(char)+k-65)%26+65),end=" ")
    else:
        print(chr((ord(char)+k-97)%26+97),end=" ")

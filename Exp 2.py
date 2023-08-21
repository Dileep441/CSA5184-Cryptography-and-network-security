import random

plain_text=input("Enter your plain text:")

message = []
for i in range(65, 90 + 1):
    j = chr(i)
    message.append(j)

original_message = message.copy()  # to save original mesage
random.shuffle(message)

print("Original values are:", original_message)
print("Shuffled values are:", message)

for i in range(len(plain_text)):
    char=plain_text[i]

    for j in range(len(original_message)):
        char2=original_message[j]
        if char==char2:
            n=j
            break
    print(message[n],end=" ")

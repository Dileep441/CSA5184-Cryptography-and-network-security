pt=input("Enter plain text:")
key=input("Enter the key:")
p=list(pt)
k=list(key)
for i in range(len(pt)):
    x=chr(((ord(p[i])-65)+(ord(k[i]))-65)%26+65)
    print(x,end=" ")

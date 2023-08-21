def create_playfair_matrix(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    keyword = keyword.replace("J", "I")
    keyword = "".join(dict.fromkeys(keyword))
    matrix = []
    for letter in keyword + alphabet:
        if letter not in matrix:
            matrix.append(letter)
    playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
    return playfair_matrix

def find_coordinates(matrix, letter):
    for row in range(len(matrix)):
        if letter in matrix[row]:
            col = matrix[row].index(letter)
            return row, col

def decrypt_playfair(ciphertext, keyword):
    playfair_matrix = create_playfair_matrix(keyword)
    plaintext = ""
    ciphertext = ciphertext.replace(" ", "").upper()
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        row1, col1 = find_coordinates(playfair_matrix, pair[0])
        row2, col2 = find_coordinates(playfair_matrix, pair[1])
        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            col1, col2 = col2, col1
        plaintext += playfair_matrix[row1][col1] + playfair_matrix[row2][col2]
    return plaintext

ciphertext = "KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO BOTEI ZONTX BYBNT GONEY CUZWR GDSON SXBOU YWRHE BAAHY USEDQ"
keyword = "YOUR_KEYWORD"  
plaintext = decrypt_playfair(ciphertext, keyword)
print("Decrypted message:", plaintext)

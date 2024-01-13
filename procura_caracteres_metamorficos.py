def tem_dois_caracteres(char):
    char_lower = char.lower()
    return len(char_lower) == 2

for i in range(500):
    char = chr(i)
    if tem_dois_caracteres(char):
        print(f"O caracter '{char}' contou como dois depois da conversao para minusculos.")


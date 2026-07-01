
def sottostringaMigliore(stringa:str):
    a = 0          # indice iniziale della migliore
    b = 0          # indice finale (escluso)
    max_len = 0
    s=clean(stringa)
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sotto = s[i:j]

            if isPalindroma(sotto):
                if (j - i) > max_len:
                    max_len = j - i
                    a = i
                    b = j
    return s[a:b]
    
    
def isPalindroma(stringa:str):
    if stringa[::-1]==stringa:
        return True
    return False


def clean(stringa:str):
    s=""
    for c in stringa:
        hash1=ord(c)
        if 65<=hash1<=90:
            s+=c
        elif 97 <= hash1 <= 122:
            s += chr(hash1-32)
    return s

def main():
    while True:
        testo = input("Inserisci una stringa: ")
        if testo == "" or testo == " ":
            break
        risultato = sottostringaMigliore(testo)
        print("Sottostringa palindroma più lunga:", risultato)


if __name__ == "__main__":
    main()

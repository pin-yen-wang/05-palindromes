#### Fonction secondaire


def ispalindrome(p):
    n = len(p)
    for i in range (n//2):
        if p[i] == p[n-1-i] :
            return True
    return False
    # votre code ici

def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
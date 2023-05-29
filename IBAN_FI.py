aakkoset = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def TarkistaTunnus(tunnus):
    #Formatoi tunnuksen
    tunnus = tunnus.replace(" ", "")
    tunnus = tunnus.lower()

    #Suomalaiset tunnukset ovat aina 18 merkkiä pitkiä
    if len(tunnus) != 18:
        return False

    #Alkavat aina tunnistella FI
    if tunnus[0:2] != "fi":
        return False
    
    #Siirtää tunnisteen ja tarkistus numeron loppuun
    tunnus = tunnus[4:] + tunnus[0:4]
    
    #Korvaa kaikki aakkoset numeroilla. A = 11, B = 12 ... Z = 35.
    for i in range(len(tunnus)):
        if tunnus[i] in aakkoset:
            tunnus = tunnus.replace(tunnus[i], str(aakkoset.index(tunnus[i]) + 10))
    
    #Jakojäännös yksi tarkoittaa oikeaa lukua.
    tunnus = int(tunnus)
    if tunnus % 97 == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    print(TarkistaTunnus("FI42 5000 1510 0000 23")) #True
    print(TarkistaTunnus("FI55 2515 8869 5718 65")) #False
    print(TarkistaTunnus("FI95 1786 3769 6731 97")) #True
    print(TarkistaTunnus("FI07 5762 9588 4181 13")) #False
    print(TarkistaTunnus("FI52 8592 6874 8382 54")) #True
    print(TarkistaTunnus("SE76 9449 8965 5115 5139 7733")) #False
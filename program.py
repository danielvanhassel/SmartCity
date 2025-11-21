import csv
movieFile = open("BF.csv", "r", encoding="utf-8")
reader = csv.DictReader(movieFile, delimiter=";")
movieList = list(reader)

isRunning = True

while isRunning:
    try:
        userOption = input("Kies een optie: \n" \
        "1. Gemiddeld aantal keer uitgeleend\n" \
        "2. Gemiddeld aantal keer uitgeleend voor ingevoerd genre \n" \
        "3. Films langer dan 3 uur\n" \
        "4. Thrillers\n" \
        "5. Top 10 meest uitgeleende films\n" \
        "6. Aantal films van ingevoerd genre uit ingevoerd jaar\n")
    except ValueError:
        print("U heeft een fout nummer ingevoerd")

    if userOption == "1":
        print("1")
        
    elif userOption == "2":
        NotImplemented

    elif userOption == "3":
        NotImplemented

    elif userOption == "4":
        NotImplemented

    elif userOption == "5":
        NotImplemented

    elif userOption == "6":
        NotImplemented

    else:
        print("Uw heeft een incorrect getal ingevoerd")

    userContinue = input("Wilt u doorgaan? Typ X op te stoppen ").lower()
    if userContinue == "x":
        print("Bye!")
        isRunning = False
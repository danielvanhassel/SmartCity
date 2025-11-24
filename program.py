import csv
import os
movieFile = open("BF.csv", "r", encoding="utf-8")
reader = csv.DictReader(movieFile, delimiter=";")
movieList = list(reader)

isRunning = True

while isRunning:
    os.system("cls")
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
        totalRented = 0
        for movie in movieList:
            totalRented += int(movie["RentedAmount2020"])
        averageRented = totalRented / len(movieList)
        print(f"gemiddel aantal keer uitgeleend: {averageRented}")
        
    elif userOption == "2":
        NotImplemented

    elif userOption == "3":
        for movie in movieList:
            runtime = int(movie["durationMins"])
            if runtime >= 180:
                print(movie["movieTitle"])

    elif userOption == "4":
        for movie in movieList:
            if movie["genre"] == "Thriller":
                print(movie["movieTitle"])

    elif userOption == "5":
        NotImplemented

    elif userOption == "6":
        selectedGenre = input("van welk genre wilt u film bekijken? ").lower()
        selectedYear = input("Van welk jaar wilt u films bekijken? ")
        for movie in movieList:
            if selectedGenre == movie["genre"].lower():
                if selectedYear == movie["releaseYear"]:
                    print(movie["movieTitle"])

    else:
        print("Uw heeft een incorrect getal ingevoerd")

    userContinue = input("Wilt u doorgaan? Typ X op te stoppen ").lower()
    if userContinue == "x":
        print("Bye!")
        os.system("cls")
        isRunning = False
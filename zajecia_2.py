temp = -8

if temp < 0:
    water = "lód"
elif temp<100:
    water = "ciecz"
else:
    water = "gaz"

print(f"W temperaturze {temp} st. C woda to {water}")

salary= 7100

if salary >=4000 and salary<=7000:
    podatek = salary * 0.15
    wypłata = salary - podatek
else:
    podatek = salary * 0.05
    wypłata=salary-podatek

print(f"Twoje wynagrodzenie to {wypłata}")

day = 3
if day >=5 and day <= 7:
    print("Weekend")
elif day >= 8 or day <= 1:
    print("nieprawidłowe dane")
else:
    print(f"do weekendu pozostało {(c:=5-day)} dni")


a = "Zarabiasz powyżej przeciętną" if salary>7000 else "zarabiasz przeciętną"if 4000<=salary<=7000 else \
    "zarabiasz poniżej przeciętnej"

print(a)

liczba = int(input("Podaj liczbę: "))

a= "Nieparzysta" if liczba%2 else "parzysta"

print(a)
from models import Person, Kurs

def main():
    p1 = Person(1,"Max","max@web.de")
    print(p1)

    p1.name ="Otto"

    print(p1)

    k1 = Kurs(1,"Python","Otto",4)
    print(k1)



if __name__ == "__main__":
    main()
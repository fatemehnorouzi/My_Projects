from datetime import datetime, date
import inflect

p = inflect.engine()
def main():
    birthday = get_birth()
    today = date.today()
    diff = today - birthday
    minutes = diff.days * 24 * 60
    words = p.number_to_words(minutes, andword="")
    print(f"{words} minutes")


def get_birth():
    birth= input("Date of Birth: ")
    try:
        date= datetime.strptime(birth, "%Y-%m-%d").date()
        return date

    except ValueError:
        print("Invalid Date")


if __name__ == "__main__":
    main()



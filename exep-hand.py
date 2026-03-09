import datetime as date
birthDate = input("Please enter your birthdate on the following format (dd/mm/yyyy): ")
while True:
    try:
        birthDate = date.datetime.strptime(birthDate, "%d/%m/%Y").date()
        break
    except(ValueError):
        birthDate = input("Please enter your birthdate on the following format (dd/mm/yyyy): ")
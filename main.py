def print_user_age(age: int) -> None:

  if age.isdigit():
    if int(age) < 5:
      print("A gdzie są twoi rodzice?")

    else:
      ageArray = list(age)
      lastDigit = ageArray[len(ageArray)-1]
      ageDescription = 'lat';

      if int(age) > 21:
        if lastDigit in ["2", "3", "4"]:
          ageDescription = "lata"

      print(f'Masz {int(age)} {ageDescription}')

  else:
    print(f'{age} nie jest liczbą całkowitą. Musisz podać dodatnią liczbę całkowitą.')

age_input_from_user = input("Podaj wiek: ")
print_user_age(age_input_from_user)




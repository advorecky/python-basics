# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, year_of_birth, city, email, phone_number):
    print(
        f"Пользователь {name} {surname} {year_of_birth} года рождения, проживающий в городе {city}. "
        f"Контакты: эл.почта {email}, телефон {phone_number}.")


print("Введите данные о пользователе")
user_name = input("Имя: ")
user_surname = input("Фамилия: ")
user_year_of_birth = input("Год рождения: ")
user_city = input("Город проживания: ")
user_email = input("Email: ")
user_mobile = input("Телефон: ")

user_data(name=user_name,
          surname=user_surname,
          year_of_birth=user_year_of_birth,
          city=user_city,
          email=user_email,
          phone_number=user_mobile)


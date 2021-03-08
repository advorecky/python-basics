# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

input_seconds = int(input("Введите вермя в секундах: "))

seconds_in_hour = 3600
seconds_in_minute = 60

hours = input_seconds // seconds_in_hour
minutes = (input_seconds % seconds_in_hour) // seconds_in_minute
seconds = (input_seconds % seconds_in_hour) % seconds_in_minute

if hours < 10:
    hours = f"0{hours}"

if minutes < 10:
    minutes = f"0{minutes}"

if seconds < 10:
    seconds = f"0{seconds}"

print("Время: {}:{}:{}".format(hours, minutes, seconds))

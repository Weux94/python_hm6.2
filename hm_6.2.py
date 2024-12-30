user_num = int(input('Введите число от 0 до 8640000: '))
user_d = 0
user_h = 0
user_m = 0
user_s = 0

if user_num >= 8640000:
    print('Помилка, число завелике!!!')
else:
    user_d = int(user_num / 86400)
    user_num = user_num - (user_d * 86400)
    user_h = int(user_num / 3600)
    user_num = user_num - (user_h * 3600)
    user_m = int(user_num / 60)
    user_num = user_num - (user_m * 60)

print('Днів: ', user_d, "Час:", user_h, ":", user_m, ":", user_num)

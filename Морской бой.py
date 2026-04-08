import time
import random
print("𝑀𝑜𝓇𝓈𝓀𝑜𝓎 𝐵𝑜𝓎")
time.sleep(1)
print("Правила: бот ставит корабль 3x1 рандомным способом. Вы пишете координаты для попадания. Поле:")
time.sleep(1)
print("ㅤ1 2 3 4 5")
print("a # # # # #")
print("б # # # # #")
print("в # # # # #")
print("г # # # # #")
print("д # # # # #")

time.sleep(1)

pos_y = random.randint(1,5)

pos_1x = random.randint(2,4)
sur_1 = 1
pos_2x = pos_1x-1
sur_2 = 1
pos_3x = pos_1x+1
sur_3 = 1

while True:
    try:
        pos_igroka = input("Введите координаты выстрела(Первое число - буква, Второе число - цифра, писать через пробел):")
        pos_chasti = pos_igroka.split()
        pos_y_igroka = ord(pos_chasti[0]) - ord("а") + 1
        pos_x_igroka = int(pos_chasti[1])
    except: print("Ошибка ввода!")
    if pos_y_igroka >= 6:
        print("Вы ввели неправильную букву - координату, вводить нужно на русском языке")
        continue
    elif pos_y_igroka <= 0:
        print("Вы ввели неправильную букву - координату, нужно вводить на русском языке")
        continue
    elif pos_x_igroka >= 6:
        print("Вы ввели неправильную цифру - координату, пожалуйста повторите попытку")
        continue
    elif pos_x_igroka <= 0:
        print("Вы ввели неправильную цифру - координату, пожалуйста повторите попытку") 
        continue  

    elif pos_y == pos_y_igroka and pos_1x == pos_x_igroka and sur_1 == 1:
        sur_1 = 0
        print("Попадание!")
    elif pos_y == pos_y_igroka and pos_1x == pos_x_igroka and sur_1 == 0:
        print("Клетка уже подбита!")
    elif pos_y == pos_y_igroka and pos_2x == pos_x_igroka and sur_2 == 1:
        sur_2 = 0
        print("Попадание!")
    elif pos_y == pos_y_igroka and pos_2x == pos_x_igroka and sur_2 == 0:
        print("Клетка уже подбита!")
    elif pos_y == pos_y_igroka and pos_3x == pos_x_igroka and sur_3 == 1:
        sur_3 = 0
        print("Попадание!")
    elif pos_y == pos_y_igroka and pos_3x == pos_x_igroka and sur_3 == 0:
        print("Клетка уже подбита!")
    elif sur_1 == 0 and sur_2 == 0 and sur_3 == 0:
        print("Вы уничтожили все вражеские корабли и выйграли игру!")
        break
    else:
        print("Мимо!")
        
        










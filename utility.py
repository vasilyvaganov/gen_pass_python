#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random
import webbrowser
import ctypes
import configparser
import os
import locale



lang = locale.getdefaultlocale()[0][:2]
config = configparser.ConfigParser()



def createConfig(path):
    try:                                            # file search
        file = open('settings.ini')
    except IOError as e:                            # creates a new one if there is no file
        config.add_section("settings")
        config.set("settings", "warning", "0")

        with open(path, "w") as config_file:
            config.write(config_file)
    else:
        with file:
            pass

if __name__ == "__main__":
    path = "settings.ini"
    createConfig(path)

if not os.path.exists(path):
        createConfig(path)



def warning_ru():
    ctypes.windll.user32.MessageBoxW(0, "Все пароли сохраняются в документ под названием gen_pass.txt только локально для вашего удобства и никуда не отправляются!", "Внимание!", 16)

def warning_eng():
    ctypes.windll.user32.MessageBoxW(0, "All passwords are saved in a document called gen_pass.txt only locally for your convenience and are not sent anywhere!", "Attention!", 16)


#core
def gen_pass_ru():
    path = 'gen_pass.txt'
    Big = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    Low = 'qwertyuiopasdfghjklzxcvbnm'
    Num = '1234567890'
    Spe = '!@#$%^&amp;*()'

    # Пароль должен содержать символы в верхнем регистре (True - да | False - нет)
    BI = True
    # Пароль должен содержать символы в нижнем регистре (True - да | False - нет)
    LO = True
    # Пароль должен содержать цифры (True - да | False - нет)
    NU = True
    # Пароль должен содержать спец символы (True - да | False - нет)
    PS = True

    Password_len = input('Длина пароля: ')

    if Password_len:
        if Password_len.isdigit() == True:
            Password_len = int(Password_len)
        else:
            print('Выход... Значение должно быть цифровое...')
            exit(0)
    else:
        print('Выход... Не указана Длина пароля...')
        exit(0)

    Password_cou = input('Количество паролей: ')
    print('\n')

    if Password_cou:
        if Password_cou.isdigit() == True:
            Password_cou = int(Password_cou)
        else:
            print('Выход... Значение должно быть цифровое...')
            exit(0)
    else:
        print('Выход... Не указано нужное количество паролей...')
        exit(0)

    Pass_Symbol = []
    if BI == True:
        Pass_Symbol.extend(list(Big))

    if LO == True:
        Pass_Symbol.extend(list(Low))

    if NU == True:
        Pass_Symbol.extend(list(Num))

    if PS == True:
        Pass_Symbol.extend(list(Spe))

    random.shuffle(Pass_Symbol)
    psw = []

    for yx in range(Password_cou):
        psw.append(''.join([random.choice(Pass_Symbol)
                   for x in range(Password_len)]))

    print('\n'.join(psw))
    print('\n')

    file = open(path, "a")
    file.write('\n')
    file.write('\n'.join(psw))
    file.write('\n')
    file.close()

    k=input("нажмите enter, чтобы продолжить...")

def gen_pass_eng():
    path = 'gen_pass.txt'
    Big = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    Low = 'qwertyuiopasdfghjklzxcvbnm'
    Num = '1234567890'
    Spe = '!@#$%^&amp;*()'

    BI = True

    LO = True

    NU = True

    PS = True

    Password_len = input('Password length: ')

    if Password_len:
        if Password_len.isdigit() == True:
            Password_len = int(Password_len)
        else:
            print('Output ... Value must be digital ...')
            exit(0)
    else:
        print('Logout ... Not specified Password length ...')
        exit(0)

    Password_cou = input('Number of passwords: ')
    print('\n')

    if Password_cou:
        if Password_cou.isdigit() == True:
            Password_cou = int(Password_cou)
        else:
            print('Output ... Value must be digital ...')
            exit(0)
    else:
        print('Logout ... Not specified Password length ...')
        exit(0)

    Pass_Symbol = []
    if BI == True:
        Pass_Symbol.extend(list(Big))

    if LO == True:
        Pass_Symbol.extend(list(Low))

    if NU == True:
        Pass_Symbol.extend(list(Num))

    if PS == True:
        Pass_Symbol.extend(list(Spe))

    random.shuffle(Pass_Symbol)
    psw = []

    for yx in range(Password_cou):
        psw.append(''.join([random.choice(Pass_Symbol)
                   for x in range(Password_len)]))

    print('\n'.join(psw))
    print('\n')

    file = open(path, "a")
    file.write('\n')
    file.write('\n'.join(psw))
    file.write('\n')
    file.close()

    k=input("press enter to continue...")


#options
def y_n_ru():
    while True:
        try:
            print("1) Сгенерировать новые пароли?")
            print("2) Открыть <gen_pass.txt>?")
            print("3) Очистить файл?")
            print("4) Закрыть программу?")
            print("Введите число операции: ")
            a = int(input(""))
            print("")
            if a == 3:
                file = open('gen_pass.txt', 'w')
                file.write('')
                file.close()
            elif a == 1:
                gen_pass_ru()
            elif  a == 2:
                open("gen_pass.txt", "a")
                webbrowser.open("gen_pass.txt")
            elif a == 4:
                break
        except Exception as e:
            continue

def y_n_eng():
    while True:
        try:
            print("1) Generate new passwords?")
            print("2) Open <gen_pass.txt>?")
            print("3) Clear file?")
            print("4) Close the program?")
            print("Enter the operation number: ")
            a = int(input(""))
            print("")
            if a == 3:
                file = open('gen_pass.txt', 'w')
                file.write('')
                file.close()
            elif a == 1:
                gen_pass_eng()
            elif  a == 2:
                webbrowser.open("gen_pass.txt")
            elif a == 4:
                break
        except Exception as e:
            continue


#start
def start():
    path = "settings.ini"
    config.read('settings.ini')
    warningv = config['settings']['warning']
    if warningv == "0" and lang == "ru":
        config.set("settings", "warning", "1")
        with open(path, "w") as config_file:
            config.write(config_file)
            warning_ru()
    if warningv == "0" and lang == "en":
        config.set("settings", "warning", "1")
        with open(path, "w") as config_file:
            config.write(config_file)
            warning_eng()
    elif warningv == "1" and lang == "ru" or lang == "en":
        pass
    if lang == "ru":
        y_n_ru()
    elif lang == "en":
        y_n_eng()
    elif lang != "en" or lang != "ru":
        y_n_eng()
start()
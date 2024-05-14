import random
from datetime import datetime
import time


# Функция для загрузки файла с паролями
def load_passwords(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        passwords = [line.strip() for line in file]
    return passwords


# Функция для создания модели Маркова на основе паролей
def create_markov_model(passwords):
    markov_model = {}
    for password in passwords:
        for i in range(len(password) - 1):
            prefix = password[i]
            suffix = password[i + 1]
            if prefix not in markov_model:
                markov_model[prefix] = {}
            if suffix not in markov_model[prefix]:
                markov_model[prefix][suffix] = 1
            else:
                markov_model[prefix][suffix] += 1
    return markov_model


# Функция для генерации пароля на основе модели Маркова
def generate_password(markov_model, length=8):
    password = random.choice(list(markov_model.keys()))
    for _ in range(length - 1):
        if password[-1] in markov_model:
            next_char = \
            random.choices(list(markov_model[password[-1]].keys()), weights=list(markov_model[password[-1]].values()))[
                0]
            password += next_char
        else:
            password += random.choice(list(markov_model.keys()))
    return password


# Главная функция
def main():
    # Загрузка паролей из файла rockyou.txt
    passwords = load_passwords("rockyou.txt")

    # Создание модели Маркова
    markov_model = create_markov_model(passwords)
    print('''________________________________________________________
░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░
██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

██╗███╗░░░███╗██╗████████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██║████╗░████║██║╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██║██╔████╔██║██║░░░██║░░░███████║░░░██║░░░██║██║░░██║██╔██╗██║
██║██║╚██╔╝██║██║░░░██║░░░██╔══██║░░░██║░░░██║██║░░██║██║╚████║
██║██║░╚═╝░██║██║░░░██║░░░██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝╚═╝░░░░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░
________________________________________________________
Введите пароль, чтобы проверить его стойкость...
Метод: позиционная атака Маркова
________________________________________________________
        ''')
    real_password = input("Введите пароль: ")
    global start_time
    start_time = datetime.now()
    # Генерация пароля на основе модели Маркова

    while True:
        generated_password = generate_password(markov_model)
        print("Пароль: ", generated_password)
        if real_password == generated_password:
            print("Пароль найден: ", generated_password)
            print("Время работы:  ", datetime.now() - start_time)
            time.sleep(999)
            exit(1999)




if __name__ == "__main__":
    main()

from datetime import datetime
import time

def crack_password(real_password, dictionary_file):
    with open(dictionary_file, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            word = line.strip()
            if real_password == word:
                return word
    return None

if __name__ == "__main__":
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
Метод: перебор по словарю
________________________________________________________
        ''')
    real_password = input("Введите пароль: ")
    start_time = datetime.now()

    # Файл словаря
    dictionary_file = "rockyou.txt"

    # Попытка взлома пароля
    cracked_password = crack_password(real_password, dictionary_file)

    if cracked_password:
        print("Пароль успешно взломан:", cracked_password)
        print("Время работы:  ",datetime.now() - start_time)
        time.sleep(999)
    else:
        print("Пароль не найден в словаре.")
        print("Время работы:  ",datetime.now() - start_time)
        time.sleep(999)
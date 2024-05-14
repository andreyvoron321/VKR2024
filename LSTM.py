from datetime import datetime
import time
from keras.models import load_model
import os
import pandas as pd
import numpy as np
import string
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Функция для чтения стороннего датасета из файла .csv
def read_dataset(file_path):
    return pd.read_csv(file_path, encoding='unicode_escape')

# Путь к файлу с датасетом
dataset_path = "common_passwords.csv"



# Загрузка стороннего датасета из файла .csv
dataset = read_dataset(dataset_path)

# Извлечение паролей из датасета
passwords = dataset['password'].tolist()

# Создание словаря символов
all_chars = string.ascii_letters + string.digits + string.punctuation
num_chars = len(all_chars)
char_to_index = {char: index for index, char in enumerate(all_chars)}

# Создание входной и целевой последовательностей
max_length = max(len(str(password)) for password in passwords)
X = np.zeros((len(passwords), max_length, num_chars), dtype=bool)
y = np.zeros((len(passwords), num_chars), dtype=bool)
for i, password in enumerate(passwords):
    for t, char in enumerate(password):
        if t < num_chars:
            X[i, t, char_to_index[char]] = 1
            y[i, char_to_index[password[-1]]] = 1

model = load_model('my_model.keras')

# Функция для генерации нового пароля
def generate_password(model):
    generated_password = ''
    for _ in range(8):  # длина пароля
        x_pred = np.zeros((1, max_length, num_chars))
        if generated_password:  # Если уже есть часть пароля, используем её как начальное значение
            for t, char in enumerate(generated_password):
                x_pred[0, t, char_to_index[char]] = 1
        preds = model.predict(x_pred, verbose=0)[0]
        next_index = np.random.choice(range(num_chars), p=preds)
        next_char = all_chars[next_index]
        generated_password += next_char
    return generated_password
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
Метод: атака нейросетью
________________________________________________________
    ''')
user_password = input("Введите ваш пароль: ")
global start_time
start_time = datetime.now()
while True:
    generated_password = generate_password(model)
    print("Пароль: ", generated_password)
    if generated_password == user_password:
        print("Пароль совпадает!")
        print("Время работы:  ", datetime.now() - start_time)
        time.sleep(999)
        exit(1999)
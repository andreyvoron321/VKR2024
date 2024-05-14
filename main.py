import tkinter as tk
import subprocess

def execute_brutforce():
    subprocess.Popen(['cmd.exe', '/c', 'start', 'python', 'bruteforce_py_mk2.py'])

def execute_DictForce():
    subprocess.Popen(['cmd.exe', '/c', 'start', 'python', 'DictForce.py'])

def execute_Markov():
    subprocess.Popen(['cmd.exe', '/c', 'start', 'python', 'Markov.py'])

def execute_LSTM():
    subprocess.Popen(['cmd.exe', '/c', 'start', 'python', 'LSTM.py'])

def center_window(window, width, height):
    # Определение размеров экрана
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Вычисление координат x и y для центрирования окна
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Установка координат для центрирования окна
    window.geometry(f"{width}x{height}+{x}+{y}")


root = tk.Tk()

root.overrideredirect(True)
center_window(root, 400, 300)

root.title("Attack Imitation Project Mk.I")

button1 = tk.Button(root, text="Атака брутфорсом", width=25, height=1, command=execute_brutforce)
button2 = tk.Button(root, text="Атака через словарь", width=25, height=1, command=execute_DictForce)
button3 = tk.Button(root, text="Позиционная атака Маркова", width=25, height=1, command=execute_Markov)
button4 = tk.Button(root, text="Атака нейросетью", width=25, height=1, command=execute_LSTM)
ExitButton = tk.Button(root, text="Выход", width=25, height=1, command=exit)

Settings = tk.Button(root, text="⚙", width=2, height=1)
QaA = tk.Button(root, text="?", width=2, height=1)
Bugs = tk.Button(root, text="🐞", width=2, height=1)
Github = tk.Button(root, text="Git", width=2, height=1)

#description_label = tk.Label(root, text="Выберите вариант чтобы продолжить...")
name_label = tk.Label(root, text=''' 
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
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░ ALPHA
''', font=("Arial", 3))


button1.place(x=100, y=140)
button2.place(x=100, y=170)
button3.place(x=100, y=200)
button4.place(x=100, y=230)
Settings.place(x=5, y=270)
QaA.place(x=35, y=270)
Bugs.place(x=340, y=270)
Github.place(x=370, y=270)
ExitButton.place(x=100, y=270)
#description_label.place(x=80, y=270)
name_label.place(x=100, y=0)
root.mainloop()

from tkinter import *
import tkinter as tk

from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import numpy as np

root = Tk()

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w - 225
h = h - 225
root.geometry('500x470+{}+{}'.format(w, h))
root.title("Прийняття колективних рішень")

showinfo(
        title='Оберіть файл з матрицею',
        message='Будь ласка, оберіть файл з матрицею!'
    )

filetypes = (
    ('text files', '*.txt'),
    ('All files', '*.*')
)

filename = fd.askopenfilename(
    title='Відкрити файл',
    initialdir='/',
    filetypes=filetypes)

class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=10, font=('Arial', 10))
                self.e.grid(row=i, column=j, padx=10, pady=10)
                self.e.insert(END, lst[i][j])

lst = np.loadtxt(filename, dtype='U', encoding='utf-8', delimiter=',')

total_rows = len(lst)
total_columns = len(lst[0])
t = Table(root)

def count():

    lst = np.loadtxt(filename, dtype='U', encoding='utf-8', delimiter=',')

    kand_A = np.where(lst == 'А')
    kand_A = list(kand_A[1])
    kand_B = np.where(lst == 'Б')
    kand_B = list(kand_B[1])
    kand_C = np.where(lst == 'С')
    kand_C = list(kand_C[1])

    # Метод Кондорсе

    A_1_1 = []
    A_1_2 = []
    B_1_1 = []
    B_1_2 = []
    C_1_1 = []
    C_1_2 = []

    for i in range(6):

        if kand_A[i] < kand_B[i]:
            A_1_1.append(int(lst[i][0]))
        if kand_B[i] < kand_A[i]:
            B_1_1.append(int(lst[i][0]))

        if kand_A[i] < kand_C[i]:
            A_1_2.append(int(lst[i][0]))
        if kand_C[i] < kand_A[i]:
            C_1_1.append(int(lst[i][0]))

        if kand_B[i] < kand_C[i]:
            B_1_2.append(int(lst[i][0]))
        if kand_C[i] < kand_B[i]:
            C_1_2.append(int(lst[i][0]))

    suma_A_1_1 = sum(A_1_1)
    suma_B_1_1 = sum(B_1_1)

    suma_A_1_2 = sum(A_1_2)
    suma_C_1_1 = sum(C_1_1)

    suma_B_1_2 = sum(B_1_2)
    suma_C_1_2 = sum(C_1_2)

    sum_list_AB = [suma_A_1_1, suma_B_1_1]
    sum_list_AB_max = max(sum_list_AB)
    sum_list_AB_max_id = sum_list_AB.index(sum_list_AB_max)
    if sum_list_AB_max_id == 0:
        result_AB = 'А>Б'
        result_AB_win = 'А'
    if sum_list_AB_max_id == 1:
        result_AB = 'Б>А'
        result_AB_win = 'Б'

    sum_list_AC = [suma_A_1_2, suma_C_1_1]
    sum_list_AC_max = max(sum_list_AC)
    sum_list_AC_max_id = sum_list_AC.index(sum_list_AC_max)
    if sum_list_AC_max_id == 0:
        result_AC = 'А>С'
        result_AC_win = 'А'
    if sum_list_AC_max_id == 1:
        result_AC = 'С>А'
        result_AC_win = 'С'

    sum_list_BC = [suma_B_1_2, suma_C_1_2]
    sum_list_BC_max = max(sum_list_BC)
    sum_list_BC_max_id = sum_list_BC.index(sum_list_BC_max)
    if sum_list_BC_max_id == 0:
        result_BC = 'Б>С'
        result_BC_win = 'Б'
    if sum_list_BC_max_id == 1:
        result_BC = 'С>Б'
        result_BC_win = 'С'

    k = [result_AB_win, result_AC_win, result_BC_win]
    result_1 = max(set(k), key=k.count)

    # Метод Борда

    A_2 = []
    B_2 = []
    C_2 = []

    for i in range(6):

        if kand_A[i] == 1:
            a = kand_A[i]+1
        if kand_A[i] == 2:
            a = kand_A[i]-1
        if kand_A[i] == 3:
            a = kand_A[i]-3
        if kand_B[i] == 1:
            b = kand_B[i] + 1
        if kand_B[i] == 2:
            b = kand_B[i] - 1
        if kand_B[i] == 3:
            b = kand_B[i] - 3
        if kand_C[i] == 1:
            c = kand_C[i] + 1
        if kand_C[i] == 2:
            c = kand_C[i] - 1
        if kand_C[i] == 3:
            c = kand_C[i] - 3

        A_2.append(int(lst[i][0]) * a)
        B_2.append(int(lst[i][0]) * b)
        C_2.append(int(lst[i][0]) * c)

    suma_A_2 = sum(A_2)
    suma_B_2 = sum(B_2)
    suma_C_2 = sum(C_2)

    sum_list_2 = [suma_A_2, suma_B_2, suma_C_2]
    sum_list_2_max = max(sum_list_2)
    sum_list_2_max_id = sum_list_2.index(sum_list_2_max)
    if sum_list_2_max_id == 0:
        result_2 = 'А'
    if sum_list_2_max_id == 1:
        result_2 = 'Б'
    if sum_list_2_max_id == 2:
        result_2 = 'С'

    text1.delete("1.0", END)
    text1.insert("1.0", result_2)
    text1.insert("1.0", '\nОтже, по методу Борда переможе кандидат: ')
    text1.insert("1.0", ' голосів')
    text1.insert("1.0", suma_C_2)
    text1.insert("1.0", '\nКандидат С отримає: ')
    text1.insert("1.0", ' голосів')
    text1.insert("1.0", suma_B_2)
    text1.insert("1.0", '\nКандидат Б отримає: ')
    text1.insert("1.0", ' голосів')
    text1.insert("1.0", suma_A_2)
    text1.insert("1.0", '\nКандидат А отримає: ')
    text1.insert("1.0", '\n\nМетод Борда:')

    text1.insert("1.0", result_1)
    text1.insert("1.0", '\nОтже, по методу Кондорсе переможе кандидат: ')
    text1.insert("1.0", result_BC)
    text1.insert("1.0", '\nПри порівнянні Б з С маємо: ')
    text1.insert("1.0", result_AC)
    text1.insert("1.0", '\nПри порівнянні А з С маємо: ')
    text1.insert("1.0", result_AB)
    text1.insert("1.0", '\nПри порівнянні А з Б маємо: ')
    text1.insert("1.0", 'Метод Кондорсе:')

labelframe = LabelFrame(root, text="Розв'язок", width=480, height=210)
labelframe.place(x=10, y=240)

text1 = tk.Text(width=58, height=11)
text1.place(x=15, y=260)

b1 = tk.Button(text="Обчислити", command=count).place(x=400, y=105)

root.mainloop()
import json
import tkinter as tk
from urllib import response

import requests

def send_request():
    url = input_field.get()
    response = requests.get(url)
    response_text.set(response.text)

def save_to_file():
    filename = save_field.get() + '.json'
    with open(filename, 'w') as f:
        json.dump(response.json(), f)
    print(f'Ответ сохранён в файл {filename}')

root = tk.Tk()
root.title("Взаимодействуем с API")

input_field = tk.Entry(root)
input_field.pack()

response_text = tk.StringVar()
response_label = tk.Label(root, textvariable=response_text)
response_label.pack()

send_button = tk.Button(root, text="Отправить запрос", command=send_request)
send_button.pack()

save_field = tk.Entry(root)
save_field.pack()

save_button = tk.Button(root, text="Сохранить в файл", command=save_to_file)
save_button.pack()

root.mainloop()
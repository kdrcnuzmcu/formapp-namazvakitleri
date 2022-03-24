import tkinter as tk
from tkinter import messagebox
from flask import request_started 
import requests
from bs4 import BeautifulSoup

def yenile():
    url = "https://namazvakitleri.diyanet.gov.tr/tr-TR/9638/kirklareli-icin-namaz-vakti"
    try:
        r = requests.get(url)
        bs = BeautifulSoup(r.text, "html.parser")

        lbl11["text"] = ":  " + bs.find_all('div', class_='tpt-time')[1].get_text()
        lbl22["text"] = ":  " + bs.find_all('div', class_='tpt-time')[2].get_text()
        lbl33["text"] = ":  " + bs.find_all('div', class_='tpt-time')[3].get_text()
        lbl44["text"] = ":  " + bs.find_all('div', class_='tpt-time')[4].get_text()
        lbl55["text"] = ":  " + bs.find_all('div', class_='tpt-time')[5].get_text()
        lbl66["text"] = ":  " + bs.find_all('div', class_='tpt-time')[6].get_text()
    except:
        tk.messagebox.showerror(title="Hata!", message="Veriler alınamadı.")
    # print(r.status_code)
    # vakitler = bs.find_all('div', class_='tpt-time')[].get_text()
    
window = tk.Tk()
window.title = "Namaz Vakitleri"
window.geometry("200x225")
window.resizable(width = False, height = False)

lbl_tarih = tk.Label(master = window, text = "---")

frm_vakitler = tk.Frame(master = window, relief = "ridge", borderwidth = 3)

lbl1 = tk.Label(master = frm_vakitler, text = "İmsak", font = "20")
lbl2 = tk.Label(master = frm_vakitler, text = "Sabah", font = "20")
lbl3 = tk.Label(master = frm_vakitler, text = "Öğle", font = "20")
lbl4 = tk.Label(master = frm_vakitler, text = "İkindi", font = "20")
lbl5 = tk.Label(master = frm_vakitler, text = "Akşam", font = "20")
lbl6 = tk.Label(master = frm_vakitler, text = "Yatsı", font = "20")

lbl11 = tk.Label(master = frm_vakitler, text = ":", font = "20")
lbl22 = tk.Label(master = frm_vakitler, text = ":", font = "20")
lbl33 = tk.Label(master = frm_vakitler, text = ":", font = "20")
lbl44 = tk.Label(master = frm_vakitler, text = ":", font = "20")
lbl55 = tk.Label(master = frm_vakitler, text = ":", font = "20")
lbl66 = tk.Label(master = frm_vakitler, text = ":", font = "20")

lbl1.grid(row = 0, column = 0, padx = 10, sticky = "w")
lbl2.grid(row = 1, column = 0, padx = 10, sticky = "w")
lbl3.grid(row = 2, column = 0, padx = 10, sticky = "w")
lbl4.grid(row = 3, column = 0, padx = 10, sticky = "w")
lbl5.grid(row = 4, column = 0, padx = 10, sticky = "w")
lbl6.grid(row = 5, column = 0, padx = 10, sticky = "w")

lbl11.grid(row = 0, column = 1, padx = 10, sticky = "w")
lbl22.grid(row = 1, column = 1, padx = 10, sticky = "w")
lbl33.grid(row = 2, column = 1, padx = 10, sticky = "w")
lbl44.grid(row = 3, column = 1, padx = 10, sticky = "w")
lbl55.grid(row = 4, column = 1, padx = 10, sticky = "w")
lbl66.grid(row = 5, column = 1, padx = 10, sticky = "w")

frm_vakitler.grid(row = 0, column = 0, pady = 10)
# frm_vakitler.pack()

btn_yenile = tk.Button(master = window, text = "Yenile", command = yenile)
btn_yenile.grid(row = 1, column = 0, sticky = "w", pady = 10, padx = 10)
# btn_yenile.pack()
window.mainloop()
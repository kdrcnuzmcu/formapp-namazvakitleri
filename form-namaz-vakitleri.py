import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import locale

lbl = []
lbl_ = []

lblA = []
lbl_A = []

def yenile():
    url1 = "https://namazvakitleri.diyanet.gov.tr/tr-TR/9638/kirklareli-icin-namaz-vakti"
    url2 = "https://www.accuweather.com/tr/tr/kirklareli/318684/weather-forecast/318684"
    url3 = "https://www.accuweather.com/tr/tr/kirklareli/318684/daily-weather-forecast/318684"
    try:
        r = requests.get(url1)
        bs = BeautifulSoup(r.text, "html.parser")
        for i in range(6):
            lbl_[i]["text"] = bs.find_all('div', class_='tpt-time')[i+1].get_text()
        """   
        lbl11["text"] = bs.find_all('div', class_='tpt-time')[1].get_text()
        
        r = requests.get(url2)
        bs = BeautifulSoup(r.text, "html.parser")
        print(bs.find_all('div', class_ = 'temp').get_text())
        # lbl_A[0]["text"] = bs.find_all('div', class_ = 'temp').get_text()
        """ 
    except:
        tk.messagebox.showerror(title="Hata!", message="Veriler alınamadı.")
    # print(r.status_code)
    # vakitler = bs.find_all('div', class_='tpt-time')[].get_text()

# ----- ----- ----- ----- ----- PENCERE ÖZELLİKLERİ ----- ----- ----- ----- ----- 

window = tk.Tk()
window.resizable(width = False, height = False)
window.title("Merkez/Kırklareli")

# ----- ----- ----- ----- ----- TARİH VE KONUM ----- ----- ----- ----- -----

locale.setlocale(locale.LC_TIME, "tr_TR") # TURKEY
lbl_saat = tk.Label(master = window, text = datetime.today().strftime("%d / %B / %Y %A - %X"))
lbl_saat.grid(row = 0, column = 0, padx = 10)

# ----- ----- ----- ----- ----- NAMAZ VAKİTLERİ ----- ----- ----- ----- -----
frm_namaz = tk.Frame(master = window, relief = "ridge", borderwidth = 3)
frm_namaz.grid(row = 1, column = 0, padx = 10, pady = 10)
vakitler = ["İmsak:", "Sabah:", "Öğle:", "İkindi:", "Akşam:", "Yatsı:"]
for i in range(6):
    lbl.append(tk.Label(master = frm_namaz, text = str(vakitler[i])))
    lbl[i].grid(row = (i), column = 0, padx = 10, sticky = "w")

    lbl_.append(tk.Label(master = frm_namaz, text = "00:00"))
    lbl_[i].grid(row = (i), column = 2, padx = 10, sticky = "w")

# ----- ----- ----- ----- ----- HAVA DURUMU ----- ----- ----- ----- -----
"""
frm_hava = tk.Frame(master = window, relief = "ridge", borderwidth = 3)
frm_hava.grid(row = 1, column = 1, padx = 10, pady = 10)
saatler = ["Şimdi:", "Bugün:", "Yarın:"]
for i in range(3):
    lblA.append(tk.Label(master = frm_hava, text = str(saatler[i])))
    lblA[i].grid(row = i, column = 0, padx = 10, sticky = "w")

    lbl_A.append(tk.Label(master = frm_hava, text = "- \N{DEGREE CELSIUS}"))
    lbl_A[i].grid(row = i, column = 1, padx = 10, sticky = "w")
"""
# ----- ----- ----- ----- ----- YENİLE BUTONU ----- ----- ----- ----- ----- 
btn_yenile = tk.Button(
    master = window, 
    text = "Yenile", 
    command = yenile,
    font = "18")
btn_yenile.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = "e")

yenile()

window.mainloop()

import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import strftime
import locale
from lxml import etree
from urllib.request import urlopen

lbl = []
lbl_ = []

lblA = []
lbl_A = []

lblAA = []
lbl_AA = []
def yenile():
    url1 = "https://namazvakitleri.diyanet.gov.tr/tr-TR/9638/kirklareli-icin-namaz-vakti"
    url2 = "https://weather.com/tr-TR/weather/tenday/l/Kirikkale+K%C4%B1rklareli?canonicalCityId=37097dc384ae4e926f530bb9da8ec0a005b87f4086ffa96a346193db8390d22b"
    url3 =  "https://weather.com/tr-TR/weather/today/l/ed41d066c5c02ef3fcbdc53a5e689b752922fa0e7e7b0d3bd0c7443abc963f8e"
    
    try:
        r = requests.get(url1)
        bs = BeautifulSoup(r.text, "html.parser")
        for i in range(6):
            lbl_[i]["text"] = bs.find_all('div', class_='tpt-time')[i+1].get_text()
        """   
        lbl11["text"] = bs.find_all('div', class_='tpt-time')[1].get_text()
        """ 
        response = urlopen(url3)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        
        for i in range(4):
            lbl_A[i]["text"] = tree.xpath("/html/body/div[1]/main/div[2]/main/div[3]/section/div/ul/li[{}]/a/div[1]/span/text()".format(i+1))[0]
        

        r = requests.get(url2)
        bs = BeautifulSoup(r.text, "html.parser")
        lblAA[0]["text"] = "Şimdi"
        lbl_AA[0]["text"] = bs.find_all('span', class_ = "DailyContent--temp--3d4dn")[0].get_text() + " / " + bs.find_all('span', class_ = "DetailsSummary--lowTempValue--3H-7I")[0].get_text()
        for i in range(1,14):
            lblAA[i]["text"] = bs.find_all('h2', class_ = "DetailsSummary--daypartName--2FBp2")[i].get_text()
            lbl_AA[i]["text"] = bs.find_all('span', class_ = "DetailsSummary--highTempValue--3Oteu")[i].get_text() + " / " + bs.find_all('span', class_ = "DetailsSummary--lowTempValue--3H-7I")[i].get_text()
            
        lbl_AA[0]["text"] = tree.xpath("/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div[2]/div[1]/div[1]/span/text()")[0] + " / " + bs.find_all('span', class_ = "DetailsSummary--lowTempValue--3H-7I")[0].get_text()
        """
        lbl_A[0]["text"] = tree.xpath("/html/body/div[1]/main/div[2]/main/div[3]/section/div/ul/li[1]/a/div[1]/span/text()")[0]
        lbl_A[1]["text"] = tree.xpath("/html/body/div[1]/main/div[2]/main/div[3]/section/div/ul/li[2]/a/div[1]/span/text()")[0]
        lbl_A[2]["text"] = tree.xpath("/html/body/div[1]/main/div[2]/main/div[3]/section/div/ul/li[3]/a/div[1]/span/text()")[0]
        lbl_A[3]["text"] = tree.xpath("/html/body/div[1]/main/div[2]/main/div[3]/section/div/ul/li[4]/a/div[1]/span/text()")[0]
        
        # lbl_A[1]["text"] = bs.find_all('div', class_ = "CurrentConditions--phraseValue--2Z18W")
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
lbl_saat = tk.Label(master = window, text = datetime.today().strftime("%d / %B / %Y \n%A \n%X"))
lbl_saat.grid(row = 0, column = 0, padx = 10)
def time():
	string = strftime('%d / %B / %Y \n%A \n%X')
	lbl_saat.config(text = string)
	lbl_saat.after(1000, time)
    
# ----- ----- ----- ----- ----- NAMAZ VAKİTLERİ ----- ----- ----- ----- -----
frm_namaz = tk.Frame(master = window, relief = "ridge", borderwidth = 3)
frm_namaz.grid(row = 1, column = 0, padx = 10, pady = 10)
vakitler = ["İmsak", "Sabah", "Öğle", "İkindi", "Akşam", "Yatsı"]
for i in range(6):
    lbl.append(tk.Label(master = frm_namaz, text = str(vakitler[i])))
    lbl[i].grid(row = (i), column = 0, padx = 10, sticky = "w")

    lbl_.append(tk.Label(master = frm_namaz, text = "00:00"))
    lbl_[i].grid(row = (i), column = 2, padx = 10, sticky = "w")

# ----- ----- ----- ----- ----- HAVA DURUMU ----- ----- ----- ----- -----

frm_hava = tk.Frame(master = window, relief = "ridge", borderwidth = 3)
frm_hava.grid(row = 1, column = 1, padx = 10, pady = 10)
saatler = ["Sabah", "Öğleden Sonra", "Akşam", "Gece"]
for i in range(4):
    lblA.append(tk.Label(master = frm_hava, text = str(saatler[i])))
    lblA[i].grid(row = i, column = 0, padx = 10, sticky = "w")

    lbl_A.append(tk.Label(master = frm_hava, text = "- \N{DEGREE CELSIUS}"))
    lbl_A[i].grid(row = i, column = 1, padx = 10, sticky = "w")

# ----- ----- ----- ----- ----- HAVA DURUMU - 10 GÜNLÜK ----- ----- ----- ----- -----

frm_hava_hafta = tk.Frame(master = window, relief = "ridge", borderwidth = 3)
frm_hava_hafta.grid(row = 1, column = 2, padx = 10, pady = 10)
for i in range(14):
    lblAA.append(tk.Label(master = frm_hava_hafta, text = "---"))
    lblAA[i].grid(row = i, column = 0, padx = 10, sticky = "w")

    lbl_AA.append(tk.Label(master = frm_hava_hafta, text = "---"))
    lbl_AA[i].grid(row = i, column = 1, padx = 10, sticky = "w")

# ----- ----- ----- ----- ----- YENİLE BUTONU ----- ----- ----- ----- ----- 
btn_yenile = tk.Button(
    master = window, 
    text = "Yenile", 
    command = yenile,
    font = "18")
btn_yenile.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = "w")

yenile()
time()
window.mainloop()

import csv
from datetime import datetime
import Musteri
import Urun

def MusterileriDosyayaYaz(musteriListesi, dosyaAdi):
    # Bu fonksiyon dict halinde parametre olarak verilen nesne verilerini dosyaya yazar
    
    with open(dosyaAdi, 'w', newline='') as file:
        writer = csv.writer(file,delimiter=';')
        writer.writerow(["Tarih","Müşteri No","Ad","Soyad","Sipariş Tutarı (TL)",
                         "Ürün Kodu | Adet","Sipariş Notu"])
        for musteriNo, musteri in musteriListesi.items():
            urunString = ""
            for urun in musteri.siparis.urunListesi:
                urunString = urunString + urun['Ürün'].urunKodu + "|" + str(urun['Adet']) + "\n"
            urunString = urunString[:-1] # en sondaki \n'i kaldır   
            writer.writerow([musteri.tarih.strftime("%d/%m/%Y %H:%M:%S"),str(musteri.musteriNo),
                             musteri.ad,musteri.soyad,str(musteri.siparis.siparisTutari),urunString,
                             musteri.siparis.siparisNotu])
            
def MusterileriDosyadanOku(dosyaAdi, menu):
    musteriListesi = {}
     
    try: 
        with open(dosyaAdi, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            satir = 0
            for row in reader:
                if satir == 0:
                    satir += 1
                else:
                    tarih = datetime.strptime(row[0], "%d/%m/%Y %H:%M:%S")
                    musteriNo = int(row[1])
                    ad = row[2]
                    soyad = row[3]
                    urunListesi = row[5].split("\n")
                    siparisNotu = row[6]
                    
                    musteri = Musteri.Musteri(musteriNo, ad, soyad) # yeni müşteri
                    musteri.tarih = tarih
                    for x in urunListesi:
                        urunKodu, adet = x.split("|")
                        urun = next((urun for urun in menu if urun.urunKodu == urunKodu), None) # menüden ürünü bul
                        musteri.siparis.UrunEkle(urun, int(adet))
                    musteri.siparis.SiparisNotuEkle(siparisNotu)
                    musteriListesi[musteriNo] = musteri
                    satir += 1
    except FileNotFoundError:
        pass
    return musteriListesi


def MenuyuDosyadanOku(dosyaAdi):
    menu = []
    
    try: 
        with open(dosyaAdi, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            satir = 0
            for row in reader:
                if satir == 0:
                    satir += 1
                else:
                    urunKodu = row[0]
                    ad = row[1]
                    fiyat = float(row[2])
                    aciklama = row[3]
                    
                    urun =  Urun.Urun(urunKodu, ad, fiyat, aciklama) # yeni urun
                    menu.append(urun)
                    satir += 1
    except FileNotFoundError:
        pass
    return menu
                
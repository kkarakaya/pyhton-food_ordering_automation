import Siparis
from datetime import datetime

class Musteri:
    def __init__(self, musteriNo, ad, soyad):
        self.musteriNo = musteriNo
        self.ad = ad
        self.soyad = soyad
        self.siparis = Siparis.Siparis()
        self.tarih = datetime.now()
    
    def MusteriBilgileriniYaz(self):
        print("Müşteri Numarası: %d" %(self.musteriNo))
        print("Adı: %s" %(self.ad))
        print("Soyadı: %s" %(self.soyad))
        print("Tarih: %s" %(self.tarih.strftime("%d/%m/%Y %H:%M:%S")))
        print("\nSipariş Bilgileri: ")
        print("--------------------------------------------")
        self.siparis.SiparisBilgileriniYaz()
        
    

    
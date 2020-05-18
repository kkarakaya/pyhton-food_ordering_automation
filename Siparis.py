class Siparis:
    def __init__(self):
        self.urunListesi = []
        self.siparisNotu = ""
        self.siparisTutari = 0
      
    def UrunEkle(self, urun, adet):
        self.urunListesi.append({'Ürün':urun, 'Adet':adet})
        self.siparisTutari = self.siparisTutari + urun.fiyat * adet

    def UrunSil(self, urunNo):            
        try:
            self.siparisTutari = self.siparisTutari - self.urunListesi[urunNo]['Ürün'].fiyat*self.urunListesi[urunNo]['Adet']
            del self.urunListesi[urunNo]
        except IndexError:
            print("Bu Ürün No'ya sahip bir ürün yoktur.")
            return         

    def UrunAdetGuncelle(self, urunNo, yeniAdet):
        try:
            self.siparisTutari = self.siparisTutari - self.urunListesi[urunNo]['Ürün'].fiyat*self.urunListesi[urunNo]['Adet']
            self.urunListesi[urunNo]['Adet'] = yeniAdet
            self.siparisTutari = self.siparisTutari + self.urunListesi[urunNo]['Ürün'].fiyat*self.urunListesi[urunNo]['Adet']
        except IndexError:
            print("Bu Ürün No'ya sahip bir ürün yoktur.")
            return   
        
    def SiparisBilgileriniYaz(self):
        print("%-10s%-15s%-7s%-7s"%("Ürün No", "Ürün Adı", "Adet", "Tutar"))
        for urunNo, urun in enumerate(self.urunListesi):
            print("%-10d%-15s%-7d%-7.2fTL"%(urunNo+1, urun["Ürün"].ad, urun["Adet"], urun["Adet"]*urun["Ürün"].fiyat))
        print("----------------------------------------------")
        print("Sipariş Notu: %s" %(self.siparisNotu))
        print("----------------------------------------------")
        print("Toplam Sipariş Tutarı : %7.2f TL" %self.siparisTutari)

    def SiparisNotuEkle(self, siparisNotu):
        self.siparisNotu = siparisNotu
        

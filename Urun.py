class Urun:
    def __init__(self, urunKodu, ad, fiyat, aciklama = ""):
        self.urunKodu = urunKodu
        self.ad = ad
        self.fiyat = fiyat
        self.aciklama = aciklama
      
    def AdGuncelle(self, yeniAd):
        self.ad = yeniAd
        
    def FiyatGuncelle(self, yeniFiyat):
        self.fiyat = yeniFiyat
        
    def AciklamaGuncelle(self, yeniAciklama):
        self.aciklama = yeniAciklama
    

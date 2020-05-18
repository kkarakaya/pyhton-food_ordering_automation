import Musteri
import DosyaIslemleri

def Menu():

    menu = DosyaIslemleri.MenuyuDosyadanOku("Menu.csv")
    musteriListesi = DosyaIslemleri.MusterileriDosyadanOku("Musteriler.csv", menu)
    
    def AnaMenuYaz():
        print("1- Menü Listele")
        print("2- Sipariş Ekle")
        print("3- Siparişi Güncelle")
        print("4- Hesap Öde")
        print("5- Müşteri Ara")
        print("6- Müşteri No Sorgula")
        print("7- Çıkış")
        
    def MenuListele():
        for i, urun in enumerate(menu):
            print("%-2d- %-15s %-5.2f TL" %(i+1, urun.ad, urun.fiyat))
            # Menüde ürün açıklamalarını eklemek için alttaki satırı yorumdan çıkarın
            #print("\t\t-%s" %(urun.aciklama))
    
    def SiparisAl(musteri):
        sipariseDevam = True
        while sipariseDevam:
            urunNo = int(input("\nSiparişe eklemek istediğinin ürünün numarası: ")) - 1
            adet = int(input("Adet: "))
            try: 
                musteri.siparis.UrunEkle(menu[urunNo], adet)
            except:
                print("\nBu ürün menüde bulunmamaktadır.")
                continue
            while True:
                kullaniciGirisi = input("Yeni ürün eklemek için E/e, siparişi bitirmek için H/h giriniz: ")
                if kullaniciGirisi == 'E' or kullaniciGirisi == 'e':
                    sipariseDevam = True
                    break
                elif kullaniciGirisi == 'H' or kullaniciGirisi == 'h':
                    sipariseDevam = False
                    break
                else:
                    print("Lütfen geçerli bir değer giriniz.")
                
        kullaniciGirisi = input("Siparişe not ekleyebilirsiniz (Geçmek için boş bırakın): ")
        if not (kullaniciGirisi == ''):
                musteri.siparis.SiparisNotuEkle(kullaniciGirisi)
        print("\nSiparişiniz alındı.")
        
    def SiparisEkle():
        def musteriNoOlustur():
            # Bu fonksiyon sayesinde müşteri numarası en düşük ve boşta olan numara olarak seçilir
            for i in range(1,len(musteriListesi)+2):
                try:
                    musteriListesi[i]
                except KeyError:
                    return i
                    
        musteriNo = musteriNoOlustur()
        ad = input("Adınız: ") 
        soyad = input("Soyadınız: ")
        musteri = Musteri.Musteri(musteriNo, ad, soyad) # yeni müşteri
        print("\n--------------------MENU--------------------")
        print("--------------------------------------------")
        MenuListele()
        SiparisAl(musteri)
        print("\nSipariş Bilgileri: ")
        print("--------------------------------------------")
        musteri.siparis.SiparisBilgileriniYaz()
        print("Müşteri Numaranız: %d" %(musteri.musteriNo))
        musteriListesi[musteriNo] = musteri
        DosyaIslemleri.MusterileriDosyayaYaz(musteriListesi, 'Musteriler.csv')
    
    def MusteriAra():
        print("Müşteri numaranızı giriniz.\nEğer müşteri numaranızı unuttuysanız sorgulamak için 0 giriniz.")
        musteriNo = int(input("\nMüşteri Numarası: "))
        if musteriNo == 0:
            MusteriNoSorgula()
            print("--------------------------------------------")
            musteri = MusteriAra()
            return musteri
        else: 
            try:
                musteri = musteriListesi[musteriNo]
                print("\nMüşteri Bilgileri: ")
                print("--------------------------------------------")
                musteri.MusteriBilgileriniYaz()
                return musteri
            except KeyError:
                print("Bu numaraya sahip müşteri bulunamadı.")
                while True:
                    kullaniciGirisi = input("Müşteri numaranızı sorgulamak ister misiniz? (E/e : Evet, H/h: Hayır): ")
                    if kullaniciGirisi == 'E' or kullaniciGirisi == 'e':
                        MusteriNoSorgula()
                        musteri = MusteriAra()
                        return musteri
                    elif kullaniciGirisi == 'H' or kullaniciGirisi == 'h':
                        return 0
                    else:
                        print("Lütfen geçerli bir değer giriniz.")
                return 0
        
    def MusteriNoSorgula():
        ad = input("Adınız: ")
        soyad = input("Soyadınız: ")
        eslesmeler = []
        print("\n--------------------------------------------")
        for musteriNo, musteri in musteriListesi.items():
            if musteri.ad == ad and musteri.soyad == soyad:
                eslesmeler.append(musteri)
                
        if len(eslesmeler) == 0:
            print("Bu bilgilere sahip bir müşteri bulunamadı.")
        else:
            print("%-20s\t\t%-20s" %("Müşteri Numarası", "Tarih"))
            for musteri in eslesmeler:
                print("     %3d\t\t %20s" %(musteri.musteriNo, musteri.tarih.strftime("%d/%m/%Y %H:%M:%S")))
            
    def SiparisiGuncelle():
        musteri = MusteriAra()
        if(not musteri == 0):
            while True: 
                print("\n0- Ana menüye dön.")
                print("1- Siparişe ürün ekle.")
                print("2- Ürün adeti güncelle.")
                print("3- Siparişten ürün çıkar.")
                kullaniciGirisi = int(input("İşlem seçiniz: "))
                if kullaniciGirisi == 0:
                    DosyaIslemleri.MusterileriDosyayaYaz(musteriListesi, 'Musteriler.csv')
                    return
                elif kullaniciGirisi == 1:
                    print("\n--------------------MENU--------------------")
                    print("--------------------------------------------")
                    MenuListele()
                    SiparisAl(musteri)
                    print("\nSipariş Bilgileri: ")
                    print("--------------------------------------------")
                    musteri.siparis.SiparisBilgileriniYaz()
                elif kullaniciGirisi == 2:
                    urunNo = int(input("Adetini güncellemek istediğiniz ürünün numarası: ")) - 1
                    yeniAdet = int(input("Yeni adet: "))
                    musteri.siparis.UrunAdetGuncelle(urunNo, yeniAdet)
                    print("\nSipariş Bilgileri: ")
                    print("--------------------------------------------")
                    musteri.siparis.SiparisBilgileriniYaz()
                elif kullaniciGirisi == 3:
                    kullaniciGirisi = int(input("Çıkarmak istediğiniz ürünün numarasını giriniz: "))
                    musteri.siparis.UrunSil(kullaniciGirisi-1)
                    print("\nSipariş Bilgileri: ")
                    print("--------------------------------------------")
                    musteri.siparis.SiparisBilgileriniYaz()
                else:
                    print("Lütfen geçerli bir seçim yapınız")
    
    def HesapOde():
        musteri = MusteriAra()
        if not (musteri == 0):
            print("--------------------------------------------")
            odeme = float(input("Ödenecek tutarı giriniz: "))
            try:
                if odeme < musteri.siparis.siparisTutari:
                    print("Ödemede %5.2f TL eksik var." %(musteri.siparis.siparisTutari - odeme))
                    musteri.siparis.siparisTutari = musteri.siparis.siparisTutari - odeme
                elif odeme > musteri.siparis.siparisTutari:
                    print("Para üstü %5.2f TL." %(odeme - musteri.siparis.siparisTutari))
                    del musteriListesi[musteri.musteriNo]
                    print("\nHesabınız kapanmıştır. İyi günler dileriz.")
                else:
                    print("Hesap tam olarak ödendi.")
                    del musteriListesi[musteri.musteriNo]
                    print("\nHesabınız kapanmıştır. İyi günler dileriz.")
                DosyaIslemleri.MusterileriDosyayaYaz(musteriListesi, 'Musteriler.csv')
            except TypeError:
                print("Lütfen ödenecek tutarı giriniz. (Örnek: 150.50)")
            
        
    print("\n------- Sipariş Otomasyon Uygulaması -------")
    while True:
        print("--------------------------------------------")
        print("\n")
        AnaMenuYaz()
        kullaniciGirisi = int(input("Yapmak istediğiniz işlemi seçiniz: "))
        if kullaniciGirisi == 1:
            print("\n")
            print("\n--------------------MENU--------------------")
            print("--------------------------------------------")
            MenuListele()
        elif kullaniciGirisi == 2:
            print("\n----------------SIPARIS EKLE----------------")
            print("--------------------------------------------")
            SiparisEkle()
        elif kullaniciGirisi == 3:
            print("\n--------------SIPARIS GUNCELLE--------------")
            print("--------------------------------------------")
            SiparisiGuncelle()
        elif kullaniciGirisi == 4:
            print("\n--------------HESAP ODE--------------")
            print("--------------------------------------------")
            HesapOde()
        elif kullaniciGirisi == 5:
            print("\n--------------MUSTERI ARA--------------")
            print("--------------------------------------------")
            MusteriAra()
        elif kullaniciGirisi == 6:
            print("\n-------------MUSTERI NO SORGULA--------------")
            print("--------------------------------------------")
            MusteriNoSorgula()
        elif kullaniciGirisi == 7:
            print("Çıkış yapılıyor...")
            return
       
    
import random
girishakki = 3
while True:
    secim = input("kayıt olmak için 1\ngiriş yapmak için 2\nbilgileri görmek için 3:")
    if secim == "1":
        ad = input("isim: ")
        soyad = input("soyisim: ")
        numara = input("telefon numarası: ")
        sifre = random.randint(10,1001)
        sifre = str(sifre)
        print(sifre)
        class Musteri():
            def __init__(self,ad,soyad,numara,sifre):
                self.ad = ad
                self.soyad = soyad
                self.numara = numara
                self.sifre = sifre
            def bilgilerigoster(self):
                print("""
                Bilgiler;
                
                İsim: {}
                
                Soyisim: {}
                
                Numara: {}
                
                Şifre: {}""".format(self.ad,self.soyad,("******"+self.numara[-4::]),len(self.sifre)*"*"))
        musteri = Musteri(ad,soyad,numara,sifre)
    elif secim == "2":
        try:
            m_ad = input("isim: ")
            m_soyad = input("soyisim: ")
            m_numara = input("telefon numarasının son 4 hanesi: ")
            m_sifre = input("şifre: ")
            if ad == m_ad and soyad == m_soyad and numara[-4::] == m_numara and sifre == m_sifre:
                print("giriş doğru")
                break
            elif girishakki == 0:
                print("giriş hakkı bitti...")
                break
            else:
                print("giriş yanlış !!!")
                girishakki -= 1
        except NameError:
            print("başa dönüp tekrar deneyiniz..")
    elif secim == "3":
        try:
            musteri.bilgilerigoster()
        except NameError:
            print("kayıt bulunamadı... kayıt olunuz.")
    elif secim == "q":
        print("program kapanıyor..")
        break
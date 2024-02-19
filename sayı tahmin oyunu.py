import random
print("""
*****************
sayı tahmin oyunu
*****************
1 ile 40 arasında sayı seçin..
tahmin hakkınız 5'dir...""")
rastgele_sayi = random.randint(1,40)
tahmin_hakki = 5
while True:
    tahmin = int(input("tahmininiz:"))
    if tahmin < rastgele_sayi:
        print("daha büyük bir sayı giriniz..")
        tahmin_hakki -= 1
    elif tahmin > rastgele_sayi:
        print("daha küçük bir sayı giriniz..")
        tahmin_hakki -= 1
    else:
        print("TEBRİKLER !! Sayımız:",rastgele_sayi)
        break
    if tahmin_hakki == 0:
        print("tahmin hakkınız bitti...\nSayımız:",rastgele_sayi)
        break
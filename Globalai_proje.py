import random

def tas_kagit_makas_dogancan_emir():
    x = random.randint(0, 2)
    secenekler = ["tas", "kagit", "makas"]
    return secenekler[x]

print("""
Hoş Geldiniz!
Taş-Kâğıt-Makas oyununa hoş geldiniz! Bu klasik oyunda, strateji ve şansınızı test edeceksiniz. 
Şimdi size oyunun kurallarını açıklayalım:

Taş, Makas'ı yener.
Makas, Kâğıt'ı yener.
Kâğıt, Taş'ı yener.
Her turda, hem siz hem de bilgisayar bir seçim yapacaksınız. Üç olası sonuç var: Siz kazanabilirsiniz, 
Bilgisayar kazanabilir veya Beraberlik olabilir.

Nasıl Oynanır:
1. Karşınıza çıkan seçeneklerden Taş, Kâğıt veya Makas'ı seçin.
2. Bilgisayar da aynı anda bir seçim yapacak.
3. Kazanan, yukarıda belirtilen kurallara göre belirlenecek.
4. İlk iki turu kazanan, oyunun galibi olur.

Oyundan Çıkış:
Oyunu herhangi bir zamanda kapatmak için çıkış komutunu kullanabilirsiniz.

Şimdi oyun başlasın! Bakalım kim galip gelecek!
""")

bilgisayar_puani = 0
kullanici_puani = 0
oyun_sayisi = 1
tur_sayisi = 0
total_skor_kullanici = 0
total_skor_bilgisayar = 0
devam = 1

while devam == 1:
    bilgisayar_secimi = tas_kagit_makas_dogancan_emir()
    kullanici_secimi = input('Yapmak istediğiniz hamleyi seçiniz (tas, kagit, makas): ')
    tur_sayisi += 1
    print(f"                   #####  OYUN SAYISI: {oyun_sayisi} , TUR SAYISI: {tur_sayisi} #####")
    print(f'💻 Bilgisayar: {bilgisayar_secimi} VS 👤 Siz: {kullanici_secimi}')

    if kullanici_secimi not in ["tas", "kagit", "makas"]:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        tur_sayisi -= 1
        continue  

    elif bilgisayar_secimi == kullanici_secimi:
        print('Berabere')

    elif (bilgisayar_secimi == 'tas' and kullanici_secimi == 'kagit') or \
         (bilgisayar_secimi == 'kagit' and kullanici_secimi == 'makas') or \
         (bilgisayar_secimi == 'makas' and kullanici_secimi == 'tas'):
        kullanici_puani += 1
    else:
        bilgisayar_puani += 1

    print(f'💻 Bilgisayar: {bilgisayar_puani} VS 👤 Siz: {kullanici_puani}')

    if bilgisayar_puani == 2 or kullanici_puani == 2:
        if bilgisayar_puani == 2:
            total_skor_bilgisayar += 1
            print("💻 Hahah kolaydı! Beni mağlup edebilmek için biraz daha çalışman gerekiyor.")
        else:
            total_skor_kullanici += 1
            print("👤 Bu seferlik sen kazandın 😏!")

        print(f"                   ----- 💻 Bilgisayar skor: {total_skor_bilgisayar}, 👤 Kullanıcı skor: {total_skor_kullanici} -------")
        kullanici_cevap = int(input("Oynamaya devam edecek misiniz? (1 veya 0 giriniz): "))
        secenekler = [1, 0]
        bilgisayar_cevap = random.choice(secenekler)

        if kullanici_cevap == 1 and bilgisayar_cevap == 1:
            oyun_sayisi += 1
            tur_sayisi = 0
            bilgisayar_puani = 0
            kullanici_puani = 0
            devam = 1
            print("Hadi tekrar oynayalım!")
        elif kullanici_cevap == 0:
            print("Vazgeçmek de bir stratejidir! 😏 Yine de meydan okumak istersen, ben buradayım. Tekrar görüşmek üzere!")
            devam = 0
            print("Oyun sona erdi. Benimle oynadığın için teşekkür ederim!")
        elif bilgisayar_cevap == 0:
            print("Daha fazla oynamak istemiyorum. Teşekkür ederim.")
            devam = 0
            print("Oyun sona erdi. Benimle oynadığın için teşekkür ederim!")
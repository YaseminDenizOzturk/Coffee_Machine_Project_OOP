from menu import icecekMenusu
from coffee_maker import kahveYapımı
from money_machine import paraMakinesi
from art import art

print(art)
para_makinesi = paraMakinesi()
kahve_yapici = kahveYapımı()
icecek_menusu = icecekMenusu()

makineAcik = True

while makineAcik:
    opsiyonlar = icecek_menusu.menu_goster()
    secim = input(f"Hangi Kahve Çeşidini İstersiniz?\n{opsiyonlar}").lower()
    if secim == "C":
        makineAcik = False 
        # makine bakım-arıza durumlarında kullanılacak.
    elif secim == "rapor":
        kahve_yapici.mevcut_malzeme_raporu()
        para_makinesi.paraDurumuRaporu()
    else:
        kahvem = icecek_menusu.icecek_Kontrol(secim)
    # icecek_Kontrol fonksiyonu öge menüde mevcutsa ögeyi döndürecektir burada da secim menude mevcutsa kahvem = secim olur. eğer menude yoksa menüde olmadığına dair müşteriye olumsuz bir mesaj verir.
        if kahvem=="-1":
            print("üzgünüm istediğin içecek menüde mevcut değil...")
        else:
            if kahve_yapici.yeterliMalzeme(kahvem) and para_makinesi.odemeBasariliMi(kahvem.ucret):
                kahve_yapici.kahveyiYap(kahvem)

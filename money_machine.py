class paraMakinesi:

    PARA_BİRİMİ = "TL"

    PARA_TURLERİ = {
        "Bir_tl": 1,
        "Elli_kurus": 0.50,
        "Yirmibes_kurus": 0.25,
        "On_kurus": 0.10
    }

    def __init__(self):
        self.karDurumu = 0
        self.alinanPara = 0

    def  paraDurumuRaporu(self):
        print(f"Para: {self.karDurumu}{self.PARA_BİRİMİ}")

    def kahveUcretiAlma(self):
        print("Lütfen paranızı ücret bölmesine atınız")
        for bozukPara in self.PARA_TURLERİ:
            self.alinanPara += int(input(f"Kaç tane {bozukPara}?\n")) * self.PARA_TURLERİ[bozukPara]

        return self.alinanPara


    def odemeBasariliMi(self,ucret):
        self.kahveUcretiAlma()
        if self.alinanPara >= ucret:
            paraUstu = round(self.alinanPara - ucret,2)
            print(f"Para üstü {paraUstu}{self.PARA_BİRİMİ}")
            self.karDurumu += ucret
            self.alinanPara = 0
            return True
        else:
            print("üzgünüm paranız seçtiğiniz kahve için yeterli değil...")

            self.alinanPara = 0
            return False
        # yani ödeme başarısızsa buraya girecek.


                      
        

        
class kahveYapımı:
    def __init__(self):
        self.malzemeler = {
            "su": 300,
            "sut": 200,
            "kahve": 150,
        }

    def mevcut_malzeme_raporu(self):
        print(f"su: {self.malzemeler['su']}ml")
        print(f"süt: {self.malzemeler['sut']}ml")
        print(f"kahve: {self.malzemeler['kahve']}g")

    def yeterliMalzeme(self,kahvem):
        yeter_durumu = True
        try:
            for oge in kahvem.icindekiler:
                if kahvem.icindekiler[oge] > self.malzemeler[oge]:
                    print(f"Üzgünüm, seçtiğiniz kahve çeşidi için yeterli {oge} bulunmuyor...")
                    yeter_durumu = False
        except AttributeError:
            print("Baska bir icecek seciniz")
        return yeter_durumu
    
    def kahveyiYap(self,istenenKahve):
        for oge in istenenKahve.icindekiler:
            self.malzemeler[oge] -= istenenKahve.icindekiler[oge]

        print(f"Kahveniz hazır {istenenKahve.isim}☕️ Afiyet Olsun")

        

        



        



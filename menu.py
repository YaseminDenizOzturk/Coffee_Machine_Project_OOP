class MenuModel:

    def __init__(self,isim,su,sut,kahve,ucret):
        self.isim = isim
        self.ucret = ucret
        self.icindekiler = {
            "su":su,
            "sut":sut,
            "kahve":kahve
        }

class icecekMenusu:
    def __init__(self):
        self.icecekmenusu = [
            MenuModel(isim="latte",su=200,sut=150,kahve=24,ucret=2.5),
            MenuModel(isim="espresso",su=50,sut=0,kahve=18,ucret=1.5),
            MenuModel(isim="cappucino",su=250,sut=50,kahve=24,ucret=3),
            MenuModel(isim="americano",su=150,sut=50,kahve=24,ucret=2.5),
            MenuModel(isim="mocha",su=200,sut=20,kahve=20,ucret=3),

        ]

    def menu_goster(self):
        opsiyonlar = ""
        for oge in self.icecekmenusu:
            opsiyonlar += f"{oge.isim}\n"
        return opsiyonlar
    
    def icecek_Kontrol(self,icecek_ismi):
        for oge in self.icecekmenusu:
            if oge.isim == icecek_ismi:
                return oge
        return "-1"
    
        


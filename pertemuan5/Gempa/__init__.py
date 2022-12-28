class Gempa:
    # Property 
    lokasi = ""
    skala = ""

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
    
    def dampak(self):
        # Kondisional
        if self.skala < 2:
            print("Dampak gempa tak berasa")
        elif self.skala == 2 and self.skala < 4:
            print("Dampak gempa bangunan retak - retak")
        elif self.skala == 4 and self.skala < 6:
            print("Dampak gempa bangunan mulai roboh")
        elif self.skala >= 6:
            print("Dampak bangunan roboh dan berpotensi tsunami")
        else:
            print("Inputan yang kamu masukkan salah")
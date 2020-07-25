class PemainBola:
    def __init__(self, nama, no_jersey):
        self.nama = nama
        self.no_jersey = no_jersey

    # GETTER

    def get_pemain(self):
      print(self.nama + ' berjersey nombor ' + str(self.no_jersey))

    # METHODS

    def berlari(self):
        print(self.nama + ' sedang berlari')

    def pass_bola(self, pemain):
        print(self.nama + ' pass bola pada ' + pemain)

    def shoot_bola(self):
        print(self.nama + ' shoot bola')


class Forward(PemainBola):
    def mengelecek_bola(self):
        print(self.nama + ' mengelecek bola')


forward1 = Forward('Sharif', 3)

forward1.get_pemain()

forward1.mengelecek_bola()
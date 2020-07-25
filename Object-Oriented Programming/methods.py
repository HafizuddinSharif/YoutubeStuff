class DuaNombor:
    def __init__(self, nombor1, nombor2):
        self.nombor1 = nombor1
        self.nombor2 = nombor2

    # METHODS

    def add(self):
        print(self.nombor1 + self.nombor2)

    def darab(self):
        print(self.nombor1 * self.nombor2)

    def add_external(self, nombor):
        print(self.nombor1 + self.nombor2 + nombor)


# FUNCTION

def add(nombor1, nombor2):
  print(nombor1 + nombor2)

pertama = DuaNombor(1, 2)

pertama.add()

add(1, 2)




class Manusia:
    def __init__(self, nama):
        self.nama = nama

    def berlari(self):
        print(self.nama + ' sedang berlari')


def berlari(nama):
    print(nama + ' sedang berlari')

manusia1 = Manusia('Sharif')

manusia1.berlari()

berlari('Sharif')
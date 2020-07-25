class Kucing:
  
  def __init__(self, nama, berat, umur, tahap_kekenyangan):

    self.nama = nama

    if berat <= 0:
      self.berat = 0
    else:
      self.berat = berat
    
    if umur <= 0:
      self.umur = 0
    else:
      self.umur = umur

    if tahap_kekenyangan <= 0:
      self.tahap_kekenyangan = 0
    elif tahap_kekenyangan >= 10:
      self.tahap_kekenyangan = 10
    else:
      self.tahap_kekenyangan = tahap_kekenyangan

  # GETTER

  def get_nama(self):
    return self.nama
  
  def get_berat(self):
    return self.berat + 'kg'
  
  def get_umur(self):
    return self.umur + 'tahun'

  def get_tahap_kekenyangan(self):
    if self.tahap_kekenyangan > 6:
      return self.nama  +' rasa sangat kenyang'
    elif self.tahap_kekenyangan > 3:
      return self.nama + 'rasa biasa-biasa sahaja'
    else:
      return self.nama + 'rasa sangat lapar'

  # SETTER

  def set_nama(self, nama):
    self.nama = nama

  def tahap_kekenyangan(self, nilai):
    self.tahap_kekenyangan = self.tahap_kekenyangan + nilai

    if self.tahap_kekenyangan >= 10:
      self.tahap_kekenyangan = 10
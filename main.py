class Sirket():
   def __init__(self, ad):
      self.ad = ad
      self.calisma = True

   def program(self):
      secim = self.menuSecim()

      if secim == 1:
         self.calisanEkle()
      if secim == 2:
         self.calisanCikar()
      if secim == 3:
         self.verilecekMaasGoster()
         ay_yil_secim = input("yıllık baz da görmek ister misiniz?(e/h)")
         if ay_yil_secim == "e":
             self.verilecekMaasGoster(hesap = "y")
         else:
             self.verilecekMaasGoster()
      if secim == 4:
         self.maaslariVer()
      if secim == 5:
         self.masrafGir()
      if secim == 6:
         self.gelirGir()

   def menuSecim(self):
      secim = int(input("*** {} otomasyona hos geldiniz***\n\n 1-Calisan ekle\n 2-Calisan Cikar\n 3-verilecek maas goster\n 4-maaslari ver\n 5-masraf gir\n 6-gelir gir\n\n seçiminizi girin: ".format(self.ad)))
      while secim < 1 or secim > 6:
          secim = input("Lütfen 1 ile 6 arasında değer giriniz: ")
      return secim

   def calisanEkle(self):
      id = 1
      ad = input("çalışanın adını giriniz: ")
      soyad = input("çalışanın soyadını giriniz: ")
      yas = input("çalışanın yaşını giriniz: ")
      cinsiyet = input("çalışanın cinsiyetini giriniz: ")
      maas = input("çalışanın maaşını giriniz: ")

      with open("calisanlar.txt", "r") as dosya:
         calisanlarListesi = dosya.readlines()

      if len(calisanlarListesi) == 0:
         id = 1
      else:
         with open("calisanlar.txt", "r") as dosya:
            id = int(dosya.readlines()[-1].split(")")[0]) + 1

      with open("calisanlar.txt", "a+") as dosya:
         dosya.write("{}){}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,cinsiyet,maas))

   def calisanCikar(self):
      with open("calisanlar.txt","r") as dosya:
         calisanlar = dosya.readlines()

      gCalisanlar = []
      for calisan in calisanlar:
         gCalisanlar.append(" ".join(calisan[:-1].split("-")))

      for calisan in gCalisanlar:
         print(calisan)

      secim = int(input("lütfen çıkarmak istediğiniz kullanıcının id numarasını giriniz 1-{}: ".format(len(gCalisanlar))))
      while secim < 1 or secim > len(gCalisanlar):
         secim = int(input("lütfen (1-{} arasında numara giriniz: ".format(len(gCalisanlar))))

      calisanlar.pop(secim - 1)

      sayac = 1

      dCalisanlar = []
      for calisan in calisanlar:
         dCalisanlar.append(str(sayac) + ")" + calisan.split(")")[1])
         sayac +=1
      with open("calisanlar.txt", "w") as dosya:
         dosya.writelines(dCalisanlar)

   def verilecekMaasGoster(self, hesap = "a"):

       with open("calisanlar.txt", "r") as dosya:
          calisanlar = dosya.readlines()

       maaslar = []

       for calisan in calisanlar:
         maaslar.append(int(calisan.split("-")[1]))
       if hesap == "a":
             print("bu ay toplam vermeniz gereken maaş: {}".format(sum(maaslar)))
       else:
             print("bu yıl toplam vermeniz gereken maaş: {}".format(sum(maaslar)*12))

   def maaslariVer(self):
      with open("calisanlar.txt", "r") as dosya:
         calisanlar = dosya.readlines()

      maaslar = []

      for calisan in calisanlar:
         maaslar.append(int(calisan.split("-")[1]))

      toplamMaas = sum(maaslar)
      """ butceden maas alma"""

      with open("butce.txt", "r") as dosya:
         tbutce = int(dosya.readlines()[0])

      tbutce = tbutce - toplamMaas

      with open("butce.txt", "w") as dosya:
         dosya.write(tbutce)

   def masrafGir(self):
      pass

   def gelirGir(self):
      pass

sirket = Sirket("Lucky Cat Coffee")

while sirket.calisma:
   sirket.program()

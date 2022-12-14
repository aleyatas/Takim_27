# -*- coding: utf-8 -*-
"""YetCoffee.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xWVPsEVz7P7oVuKGOSJvzCYfBCxORYV6

YetGen için bir kahve otomatı yapmak istiyoruz. Bu kahve otomatında aşağıdaki adımları gerçekleştirmesini bekliyoruz. Bu işlemler:


Kahve Ekle

Fiyat Güncelleme

Miktarı Değiştirme (ekle/kaldır)

Otomatı Açma

Otomatı Kapatma


Bu işlemleri gerçekleştirirken mutlaka class yapısını kullanarak projeyi tamamlamalısınız. Sizi sadece yukarıdaki 5 adım ile sınırlandırmıyoruz bunlara ekstra özellikler ekleyerek projenizi daha da geliştirebilirsiniz.
"""

import time
class otomat():
  def __init__(self,
               kahve_menusu = {
          "americano":3.75,
          "latte":4.50,
          "cappucino":5.00,
          "sicak cikolata":3.75,
          "sicak su":2.00,
              },
               sut_menusu ={
          "hayvansal sut":0.00,
          "soya sutu":2.50,
          "yulaf sutu":1.50,
          "badem sutu":2.00,
          "yok":0.00
               },
               otomat_durumu = "Kapalı",
               kahve = "Yok",
               miktar= 0,
               seker_miktari=0,
               kahve_miktari=0):
  

    self.otomat_durumu = otomat_durumu
    self.kahve = kahve
    self.miktar = miktar
    self.seker_miktari = seker_miktari
    self.kahve_menusu = kahve_menusu
    self.sut_menusu = sut_menusu
    self.kahve_miktari = kahve_miktari



  def otomat_ac(self):
    if self.otomat_durumu == "Açık":
      print("Otomat zaten çalışıyor.")
    
    else:
      print("Otomat açıldı.")
    


  def otomat_kapat(self):
    if self.otomat_durumu == "Kapalı":
      print("Otomat kapatıldı.")



  def display_menu(self):
      print("--- KAHVE MENU ---")
      print("Süt seçimi yapmayı unutmayın!")

      for item in list(self.kahve_menusu.keys()):
          print(f"{item.upper()} : {self.kahve_menusu[item]} TL")
  


  def display_sut(self):
      print("--- SUT MENU ---")

      for item in list(self.sut_menusu.keys()):
          print(f"{item.upper()} : {self.sut_menusu[item]} TL")



  def seker_ekleme(self):
    while True:
      seker = input(("Şeker eklemek için '>' azaltmak için '<' çıkış yapmak için '.' tuşlayınız. Kahveniz maksimum 2 şekerli olabilir."))

      if seker == ">" and self.seker_miktari < 2:
        self.seker_miktari +=1
        print("Şeker miktarı: ",self.seker_miktari)
      
      elif seker == "<" and self.seker_miktari != 0:
        self.seker_miktari -=1
        print("Şeker miktarı: ",self.seker_miktari)
      
      else:
        print("Şeker ayarlarından çıkış yapılıyor.")
        print("Güncel şeker miktarı: ",self.seker_miktari)
        break



  def satin_alma(self):

      son_fiyat = 0
      while True:
          eklenecek_urun = input("Hangi kahveyi almak istiyorsunuz? Çıkış yapmak için '0'a basınız. ")
          eklenecek_urun=eklenecek_urun.lower()
          

          if eklenecek_urun == "0":
              print("Fiş yazdırılıyor.")
              break
          print()
          print("'Americano' veya 'Sıcak su' almak istiyorsanız süt seçimine 'yok' yazınız.")
          eklenecek_sut = input("Hangi sütü kullanmak istiyorsunuz? ")
          eklenecek_sut = eklenecek_sut.lower()
          print()
          self.kahve_miktari = 0



          while True:
            adet = input(("Kahveden eklemek için '>' çıkarmak için '<' çıkış yapmak için '.' tuşlayınız."))
            if adet == ">":
              self.kahve_miktari +=1
              print("Kahve miktarı: ",self.kahve_miktari)
            
            elif adet == "<" and self.kahve_miktari != 0:
              self.kahve_miktari -=1
              print("Kahve miktarı: ",self.kahve_miktari)
            else:
              break

        
          fiyat = (self.kahve_menusu[eklenecek_urun] + self.sut_menusu[eklenecek_sut])* self.kahve_miktari

          if (eklenecek_urun != "americano") and (eklenecek_urun != "sıcak su"):
            print (f"{eklenecek_sut} ile hazırlanan {self.kahve_miktari} tane {eklenecek_urun} fiyatı: {fiyat}")
            print()
            son_fiyat += fiyat
            print("Son fiyat: ", son_fiyat)
            print()
          
          else:
            print (f"{self.kahve_miktari} tane {eklenecek_urun} fiyatı: {fiyat}")
            print()
            son_fiyat += fiyat
            print("Son fiyat: ", son_fiyat)
            print()
          
          with open("kasa.txt", "a") as f:
                f.write(str(time.ctime(time.time())))
                f.write("\n")
                f.write(f"Alınan kahve: {eklenecek_urun}")
                f.write("\n")                
                f.write(f"Eklenen süt: {eklenecek_sut}")
                f.write("\n")
                f.write(f"Kahve miktarı: {str(self.kahve_miktari)}")
                f.write("\n")
                f.write(f"Ürün fiyatı {fiyat}")
                f.write("\n")
                f.write(f"Genel toplam: {son_fiyat}")
                f.write("\n")
                f.write("*"*20)
                f.write("\n")

Otomat = otomat()
def main():
      print("YetCoffee'ye hoş geldiniz.\nOtomatı açmak için '1'e basınız.\nKahve menüsünü görüntülemek için '2'ye basınız.\nSüt menüsünü görmek için '3'e basınız.\nŞeker miktarını değiştirmek için '4'e basınız.\nSatın alma işlemi için 5'e basınız.\nOtomatı kapatmak için 6'ya basınız.")
      print()
      program = None
      x = []

      while True:
          
          program = int(input("İşlem tercihiniz: "))
          print()
          
          if program < 0 or program > 6:
              print()
              print("Yanlış tercih yaptınız. Tekrar deneyin.")
      
          elif program == 1:
              x.append("1")
              print()
              Otomat.otomat_ac()
              
          elif program == 2:
              if "1" not in x:
                raise Exception("Önce otomatı açmalısınız.")
              print()
              Otomat.display_menu()

          elif program == 3:
              if "1" not in x:
                raise Exception("Önce otomatı açmalısınız.")
              print()
              Otomat.display_sut()
              
          elif program == 4:
              if "1" not in x:
                raise Exception("Önce otomatı açmalısınız.")
              print()
              Otomat.seker_ekleme()
              
          elif program == 5:
              if "1" not in x:
                raise Exception("Önce otomatı açmalısınız.")
              print()
              Otomat.satin_alma()
              
          elif program == 6:
              if "1" not in x:
                raise Exception("Önce otomatı açmalısınız.")
              print()
              Otomat.otomat_kapat()
              
              print("Çıkış yapılıyor. YetGen'li günler!")
              break
              
          else:
            break

main()
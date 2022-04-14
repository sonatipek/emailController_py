#   input ifadesi mail girilmesi isteniyor 
#   girilen ifadenin mail olup olmadığını belirtip hata var ise hatalı olduğunu söyleyip tekrar girmesini isteyecek program yazın

#Sonsuz döngü kullanarak doğru değer girilmedikçe girdi almaya devam ediyoruz.
from queue import Empty


donguDevam = True

while donguDevam:
    
    kontrol = False
    mail = input("Lütfen mail adresinizi girin:\t")

    for arama in mail:  #String içerisinde gezinerek 
        if (arama == "@"):  #girilen değer içinde '@' işaretli varsa
            kontrol = True #kontrol değişkenini True'ya çeviriyoruz
            break   #Döngüden çıkıyoruz


    if (kontrol == False):  #kontrol değişkeni false'ise 

        print("Girdiğiniz değer mail değildir. Lütfen mail giriniz! 1")   #mail olmadığı ile ilgili bilgilendirme metni döndürüyoruz
        
    else:
        temp = mail.split(".")

        if temp[-1] == "com":
            temp = mail.split("@")
            temp = temp[-1].split(".com")

            if temp[0] != Empty:
                print("Girdiğiniz değer maildir.")  #mail false değil ise  mail olduğu ile ilgili bilgilendirme metni döndürüyoruz
                donguDevam = False
                break   #sınırsız döngüden çıkıyoruz
            
        
        else:      
            print("Girdiğiniz değer mail değildir. Lütfen mail giriniz! 2")
#   input ifadesi mail girilmesi isteniyor 
#   girilen ifadenin mail olup olmadığını belirtip hata var ise hatalı olduğunu söyleyip tekrar girmesini isteyecek program yazın

#Sonsuz döngü kullanarak doğru değer girilmedikçe girdi almaya devam ediyoruz.
donguDevam = True

while donguDevam:
    
    kontrol = False
    mail = input("Lütfen mail adresinizi girin:\t")

    for arama in mail:  #String içerisinde gezinerek 
        if (arama == "@"):  #girilen değer içinde '@' işaretli varsa
            kontrol = True #kontrol değişkenini True'ya çeviriyoruz
            break   #Döngüden çıkıyoruz


    if (kontrol == False):  #kontrol değişkeni false'ise 

        print("Girdiğiniz değer mail değildir. Lütfen mail giriniz!")   #mail olmadığı ile ilgili bilgilendirme metni döndürüyoruz
        
    else:
        mail = mail.split(".")
        if mail[-1] == "com":
            print("Girdiğiniz değer maildir.")  #mail false değil ise  mail olduğu ile ilgili bilgilendirme metni döndürüyoruz
            donguDevam = False
            break   #sınırsız döngüden çıkıyoruz
        else:      
            print("Girdiğiniz değer mail değildir. Lütfen mail giriniz!")
        
#TODO: @işaretlinden sonra subdomain zorunluluğu getir.
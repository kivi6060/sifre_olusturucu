karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
import random

sayi = int(input("Kaç karakterli bir şifre istersin?\n"))

sifre = ""


while True:
    hesap = input("Hangi hesabın için şifre istiyorsin?\n")
    if hesap == "çıkış":
        break
    sayi = int(input("Kaç karakterli bir şifre istersin?\n"))
    sifre = ""
    for i in range(sayi):
        sifre += random.choice(karakterler)
    with open("sifreler.txt", "a") as file:
        file.write(f"{hesap} : {sifre}\n")
    print(f"{hesap} : {sifre}")
4
from dataclasses import dataclass
from hashlib import sha256
import time


class block:
    def __init__(self, timeStamp, data, previousHash=''):
        self.timeStamp = timeStamp
        self.data = data
        self.previousHash = previousHash
        self.pow = 0
        self.hash = self.hesapla()

    def hesapla(self):
        while True:
            self.pow += 1
            ozet = sha256((str(self.timeStamp)+str(self.data)+str(self.previousHash)+str(self.pow)).encode()).hexdigest()
            if ozet[0:2] == '00':
                break
        return ozet

class BlockChain :

    def __init__(self) :
        self.chain = [self.GOlustur()]
        
    def GOlustur(self) :
        return block(time.ctime(), "deneme", "")

    def BEkle(self, data) :
        node =  block(time.ctime(), data, self.chain[-1].hash)
        self.chain.append(node)

    def Kontrol(self) :
        for i in  range(len(self.chain)) :
            
            if i != 0 :
                ilk = self.chain[i-1].hash
                simdi = self.chain[i].previousHash
                if ilk != simdi :
                    return "Zincir kırılmıştır."
                
                if  sha256((str(self.chain[i].timeStamp)+str(self.chain[i].data)+str(self.chain[i].previousHash)+str(self.chain[i].pow)).encode()).hexdigest() != self.chain[i].hash :
                    return "Zincir kırılmıştır."
                    
        return "Zincir kırılmamıştır."

    def yazdir(self) :
        print ("\nBlockchain :\n")
        for i in range(len(self.chain)) :
            print ("\nBlock = ", i )
            print ("\nHash = ", str(self.chain[i].hash))
            print ("\nData = ", str(self.chain[i].data))
            print ("\nTime Stamp = ", str(self.chain[i].timeStamp))
            print ("\nPower = ", str(self.chain[i].pow))
            print ("\nPrevious Hash = ", str(self.chain[i].previousHash))
            print("\n---------------------------------------")

    
RChain = BlockChain()

while True :
    print ("\n1- Blok ekle. \n2- Blokzincirini gör. \n3- Kontrol et. \n4- Çık. \nSeçim = ")
    secim = input ()

    if secim == "1" :
        print ("\nMiktar = ")
        miktar = input()
        RChain.BEkle(miktar)

    elif secim == "2" :
        RChain.yazdir()

    elif secim == "3" :
        print(str(RChain.Kontrol()))

    elif secim == "4" :
        break

    
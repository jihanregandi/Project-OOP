class hewan:
    def suara(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini")
    
class Rubah(hewan):
    def suara(self):
        return "Grhhh!"

class Kucing(hewan):
    def suara(self):
        return "Meoww!"
    
def cetak_suara(hewan):
    print(hewan.suara()) 

hewan1 = Rubah()
hewan2 = Kucing() 

cetak_suara(hewan1)
cetak_suara(hewan2)
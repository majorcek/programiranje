import random

# TO DO: funkcija, ki bo preverila, če je vrstica polna in bo v tem primeru uničila vrstico,vse vrstice nad njo pa bo znižala za eno.
class Igra:
    def __init__(self, sirina = 8, visina = 8):
        self.sirina = sirina
        self.visina = visina
        self.naredi_nov_objekt()
        self.koncne_tocke = []
        #self.spodnje_tocke = []
        
    def __str__(self):
        polja = []
        for _ in range(self.visina):
            polja.append(self.sirina * [' '])
        for par in self.tocke:
            polja[par[1]][par[0]] = '*'
        for par in self.koncne_tocke:
            polja[par[1]][par[0]] = '#'
        rob = '+{}+'.format(self.sirina * '-')
        izpis = ''
        for vrstica in polja:
            izpis += '|{}|\n'.format(''.join(vrstica))
        return '{}\n{}{}'.format(rob,izpis,rob)  

    def prosto_desno(self):
        x, y = self.polozaj
        if x + self.velikost >= self.sirina or (x + self.velikost, y) in self.tocke:
            return False
        else:
            return True

    def prosto_levo(self):
        x, y = self.polozaj
        if x == 0 or (x - 1, y) in self.tocke:
            return False
        else:
            return True
        
    def fiksen(self):
        ja_ne = 0
        self.stevec = 0
        print(self.koncne_tocke)
        print("?", self.spodnje_tocke)
        for tocka in self.spodnje_tocke:            
            x,y = tocka[0], tocka[1]
            if y < self.visina - 1 and (x,y + 1) not in self.koncne_tocke and ja_ne == 0:
                self.stevec += 1
                ja_ne = 0
            else:
                ja_ne = 1
        if self.stevec == len(self.spodnje_tocke):
            print('nisem')
            return False
        else:     
            print('res sem')
            return True
            
    def shrani_kanvas(self):
        self.koncne_tocke.extend(self.tocke)
        #pobarvaj jih rumeno
                
    def naredi_nov_objekt(self):
        self.število = random.randrange(1,5)
        x = 3
        self.polozaj = (3,0)
        self.postavitev = 0
        if self.število == 1:
            self.tocke = [(x,0)]
            self.velikost = 1
            self.spodnje_tocke = [(x,0)]
        elif self.število == 2:
            self.tocke = [(x,0),(x + 1,0)]
            self.velikost = 2
            self.spodnje_tocke = [(x,0),(x + 1,0)]
        elif self.število == 3:
            self.tocke = [(x,0),(x + 1,0),(x + 2,0)]
            self.velikost = 3
            self.spodnje_tocke = [(x,0),(x + 1,0),(x + 2,0)]
        elif self.število == 4:
            self.tocke = [(x,1),(x + 1,1),(x,0),(x + 1,0)]
            self.velikost = 2
            self.spodnje_tocke = [(x,1),(x + 1,1)]
            
    def desno(self):
        if self.prosto_desno() == False:
            print('ne morem v desno')
        else:
            print(self.tocke)
            tocke = []
            spodnje_tocke = []
            self.polozaj = (self.polozaj[0] + 1, self.polozaj[1])
            for par in self.tocke:
                par = (par[0] + 1, par[1])
                tocke.append(par)
            self.tocke = tocke
            print("kl",self.tocke)
            for par in self.spodnje_tocke:
                par = (par[0] + 1, par[1])
                spodnje_tocke.append(par)
            self.spodnje_tocke = spodnje_tocke
            if igra.fiksen() == True:
                igra.shrani_kanvas()
                igra.naredi_nov_objekt()
        
    def levo(self):
        if self.prosto_levo() == False:
            print('ne morem v levo')
        else:
            tocke = []
            spodnje_tocke = []
            self.polozaj = (self.polozaj[0] - 1, self.polozaj[1])
            for par in self.tocke:
                par = (par[0] - 1, par[1])
                tocke.append(par)
            self.tocke = tocke
            for par in self.spodnje_tocke:
                par = (par[0] - 1, par[1])
                spodnje_tocke.append(par)
            self.spodnje_tocke = spodnje_tocke
            if igra.fiksen() == True:
                igra.shrani_kanvas()
                igra.naredi_nov_objekt()
        
    def premakni(self):
        self.polozaj = (self.polozaj[0], self.polozaj[1] + 1)
        tocke = []
        spodnje_tocke = []
        for par in self.tocke:
            par = (par[0], par[1] + 1)
            tocke.append(par)
        self.tocke = tocke
        for par in self.spodnje_tocke:
            par = (par[0], par[1] + 1)
            spodnje_tocke.append(par)
        self.spodnje_tocke = spodnje_tocke
        if igra.fiksen() == True:
            print('fiksen')
            igra.shrani_kanvas()
            igra.naredi_nov_objekt()
            
    def zavrti(self):
        if igra.lahko_zavrtim() == True:
            if self.število == 2:   
                if self.postavitev % 4 == 0:
                    self.tocke = [self.polozaj, (self.polozaj[0], self.polozaj[1] + 1)]
                    self.spodnje_tocke = [(self.polozaj[0], self.polozaj[1] + 1)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [self.polozaj, (self.polozaj[0] - 1, self.polozaj[1])]
                    self.spodnje_tocke = [(self.polozaj[0] - 1, self.polozaj[1]), (self.polozaj[0], self.polozaj[1])]
                elif self.postavitev % 4 == 2:
                    self.tocke = [self.polozaj, (self.polozaj[0], self.polozaj[1] - 1)]
                    self.spodnje_tocke = [self.polozaj]
                else:
                    self.tocke = [self.polozaj, (self.polozaj[0] + 1, self.polozaj[1])]
                    self.spodnje_tocke = [self.polozaj,(self.polozaj[0] + 1, self.polozaj[1])]
                 
            elif self.število == 3:
                if self.postavitev % 4 == 0:
                    self.tocke = [self.polozaj, (self.polozaj[0], self.polozaj[1] + 1),(self.polozaj[0], self.polozaj[1] + 2)]
                    self.spodnje_tocke = [(self.polozaj[0], self.polozaj[1] + 2)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [self.polozaj, (self.polozaj[0] - 1, self.polozaj[1]), (self.polozaj[0] - 2, self.polozaj[1])]
                    self.spodnje_tocke = [(self.polozaj[0], self.polozaj[1]), (self.polozaj[0] - 1, self.polozaj[1]), (self.polozaj[0]- 2, self.polozaj[1])]
                elif self.postavitev % 4 == 2:
                    self.tocke = [self.polozaj, (self.polozaj[0], self.polozaj[1] - 1), (self.polozaj[0], self.polozaj[1] - 2)]
                    self.spodnje_tocke = [self.polozaj]
                else:
                    self.tocke = [self.polozaj, (self.polozaj[0] + 1, self.polozaj[1]), (self.polozaj[0] + 2, self.polozaj[1])]
                    self.spodnje_tocke = [(self.polozaj[0], self.polozaj[1]), (self.polozaj[0] + 1, self.polozaj[1]), (self.polozaj[0] + 2, self.polozaj[1])]
            self.postavitev += 1
        else:
            print('ne morem obrnit')
        
    def lahko_zavrtim(self):
        if self.število == 1:
            return True
        elif self.število  == 2:
            if self.postavitev % 4 == 0:
                if self.polozaj[1] < self.visina - 1 and (self.polozaj[0], self.polozaj[1] - 1) not in self.tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 1:
                if self.polozaj[0] > 0 and (self.polozaj[0] - 1, self.polozaj[1]) not in self.tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 2:
                if self.objekt.polozaj[1] > 0:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 3:
                if self.polozaj[0] < self.sirina - 1 and (self.polozaj[0] + 1, self.objekt.polozaj[1]) not in self.tocke:
                    return True
                else:
                    return False

        elif self.število == 3:
            if self.postavitev % 4  == 0:
                if self.polozaj[1] < self.visina - 2 and (self.polozaj[0], self.polozaj[1] - 1) not in self.tocke and (self.polozaj[0], self.polozaj[1] - 2) not in self.tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 1:
                if self.polozaj[0] > 1 and (self.polozaj[0] - 1, self.polozaj[1]) not in self.tocke and (self.polozaj[0] - 2, self.polozaj[1]) not in self.tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 2:
                if self.polozaj[1] > 1:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 3:
                if self.polozaj[0] < self.sirina - 2 and (self.polozaj[0] + 1, self.polozaj[1]) not in self.tocke and (self.polozaj[0] + 2, self.polozaj[1]) not in self.tocke:
                    return True
                else:
                    return False
        elif self.število == 4:
            return True
                
igra = Igra(8,8)

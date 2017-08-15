import random
# TO DO: SPODNJE TOČKE POBARVAJ
#        Če uspe, vsak lik svoje barve
# dodaj še trikotno na obe strani in štirki z izrastkom


class Igra:
    def __init__(self, sirina = 20, visina = 20):
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

    def naredi_nov_objekt(self):
        self.število = random.randrange(1,15)
        #self.število = 4
        x = 4
        self.polozaj = (x,0)
        self.postavitev = 0
        if self.število == 1: #enka
            self.tocke = [(x,0)]
            self.velikost = 1
            self.spodnje_tocke = [(x,0)]
        elif self.število == 2: #dvojka
            self.tocke = [(x,0),(x + 1,0)]
            self.velikost = 2
            self.spodnje_tocke = [(x,0),(x + 1,0)]
        elif self.število == 3: #trojka
            self.tocke = [(x,0),(x + 1,0),(x + 2,0)]
            self.velikost = 3
            self.spodnje_tocke = [(x,0),(x + 1,0),(x + 2,0)]
        elif self.število == 4: #štirka
            self.tocke = [(x,0),(x + 1,0),(x + 2,0),(x + 3,0)]
            self.velikost = 4
            self.spodnje_tocke = [(x,0),(x + 1,0),(x + 2,0),(x + 3,0)]
        elif self.število == 5: #kvadrat
            self.tocke = [(x,1),(x + 1,1),(x,0),(x + 1,0)]
            self.velikost = 2
            self.spodnje_tocke = [(x,1),(x + 1,1)]
        elif self.število == 6: #kvadrat z izrastkom
            self.tocke = [(x,1),(x + 1,1),(x + 2, 1),(x,0),(x + 1,0)]
            self.velikost = 3
            self.spodnje_tocke = [(x,1),(x + 1,1),(x + 2, 1)]
        elif self.število == 7: #mali L v levo
            self.tocke = [(x,1),(x + 1,1),(x + 2, 1),(x + 2,0)]
            self.velikost = 3
            self.spodnje_tocke = [(x,1),(x + 1,1),(x + 2, 1)]
        elif self.število == 8: #mali L v levo z izrastkom
            self.tocke = [(x,1),(x + 1,1),(x + 2, 1),(x + 2,0),(x + 1,2)]
            self.velikost = 3
            self.spodnje_tocke = [(x,1),(x + 1,2),(x + 2, 1)]
        elif self.število == 9: #mali L v desno
            self.tocke = [(x,1),(x + 1,1),(x + 2, 1),(x,0)]
            self.velikost = 3
            self.spodnje_tocke = [(x,1),(x + 1,1),(x + 2, 1),(x,0)]
        elif self.število == 10: # mali L v desno z izrastkom
            self.tocke = [(x,1),(x + 1,1),(x + 2, 1),(x,0), (x + 1,1)]
            self.velikost = 3
            self.spodnje_tocke = [(x,1),(x + 1,2),(x + 2, 1)]
        elif self.število == 11: # velik L v desno 
            self.tocke = [(x,1),(x + 1,1),(x + 2, 1),(x + 3, 1),(x,0)]
            self.velikost = 3
            self.spodnje_tocke = [(x,1),(x + 1,1),(x + 2, 1),(x + 3, 1)]
        elif self.število == 12: #velik L v levo 
            self.tocke = [(x,1),(x + 1,1),(x + 2, 1),(x + 3, 1),(x,0)]
            self.velikost = 3
            self.spodnje_tocke = [(x,1),(x + 1,1),(x + 2, 1),(x + 3, 1)]
        elif self.število == 13: #kotna 2
            self.tocke = [(x,1),(x + 1,1),(x,0)]
            self.velikost = 2
            self.spodnje_tocke = [(x,1),(x + 1,1),(x + 2, 1)]
        elif self.število == 14: #kotna 3
            self.tocke = [(x,2),(x + 1,2),(x + 2, 2),(x,0),(x,1)]
            self.velikost = 3
            self.spodnje_tocke = [(x,2),(x + 1,2),(x + 2, 2)]
        
    def desno(self):
        if self.prosto_desno() == False:
            print('ne morem v desno')
        else:
            tocke = []
            spodnje_tocke = []
            self.polozaj = (self.polozaj[0] + 1, self.polozaj[1])
            for par in self.tocke:
                par = (par[0] + 1, par[1])
                tocke.append(par)
            self.tocke = tocke
            for par in self.spodnje_tocke:
                par = (par[0] + 1, par[1])
                spodnje_tocke.append(par)
            self.spodnje_tocke = spodnje_tocke
            if igra.fiksen() == True:
                igra.shrani_kanvas()
                igra.naredi_nov_objekt()
        print(igra)

    def prosto_desno(self):
        x, y = self.polozaj
        ja_ne = 1
        for tocka in self.tocke:
            if tocka[0] == self.sirina - 1 or (tocka[0] + 1, tocka[1]) in self.koncne_tocke or ja_ne == 0:
                ja_ne = 0
        if ja_ne == 1:
            return True
        else:
            return False

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
        print(igra)
        
    def prosto_levo(self):
        x, y = self.polozaj
        ja_ne = 1
        for tocka in self.tocke:
            if tocka[0] == 0 or (tocka[0] - 1, tocka[1]) in self.koncne_tocke or ja_ne == 0:
                ja_ne = 0
        if ja_ne == 1:
            return True
        else:
            print(x,y,self.tocke)
            return False

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
            igra.shrani_kanvas()
            igra.polna_vrstica()                
            igra.naredi_nov_objekt()
        print(igra)
        
    def fiksen(self):
        ja_ne = 0
        števec = 0
        for tocka in self.spodnje_tocke:            
            if tocka[1] < self.visina - 1 and (tocka[0],tocka[1] + 1) not in self.koncne_tocke and ja_ne == 0:
                #števec += 1
                ja_ne = 0
            else:
                ja_ne = 1
        if ja_ne == 0: #števec == len(self.spodnje_tocke):
            return False
        else:     
            return True         
            
    def zavrti(self):
        x,y = self.polozaj
        if igra.lahko_zavrtim() == True:
            if self.število == 1: #enka
                pass
            
            elif self.število == 2: #dvojka
                if self.postavitev % 4 == 0:
                    self.tocke = [(x,y), (x,y + 1)]
                    self.spodnje_tocke = [(x,y + 1)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [(x,y), (x - 1,y)]
                    self.spodnje_tocke = [(x, y),(x - 1,y)]
                elif self.postavitev % 4 == 2:
                    self.tocke = [(x,y), (x,y - 1)]
                    self.spodnje_tocke = [(x,y)]
                else:
                    self.tocke = [(x,y), (x + 1,y)]
                    self.spodnje_tocke = [(x,y),(x + 1,y)]
                self.velikost = len(self.spodnje_tocke)
                 
            elif self.število == 3: #trojka
                if self.postavitev % 4 == 0:
                    self.tocke = [(x,y),(x,y + 1),(x,y + 2)]
                    self.spodnje_tocke = [(x,y + 2)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [(x,y),(x - 1,y),(x - 2,y)]
                    self.spodnje_tocke = [(x, y),(x - 1,y),(x - 2,y)]
                elif self.postavitev % 4 == 2:
                    self.tocke = [(x,y),(x,y - 1),(x,y - 2)]
                    self.spodnje_tocke = [(x,y)]
                else:
                    self.tocke = [(x,y),(x + 1,y),(x + 2,y)]
                    self.spodnje_tocke = [(x,y),(x + 1,y),(x + 2,y)]
                self.velikost = len(self.spodnje_tocke)
                
            elif self.število == 4: #štirka
                if self.postavitev % 4 == 0:
                    self.tocke = [(x,y),(x,y + 1),(x,y + 2),(x,y + 3)]
                    self.spodnje_tocke = [(x,y + 3)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [(x,y),(x - 1,y),(x - 2,y),(x - 3,y)]
                    self.spodnje_tocke = [(x, y),(x - 1,y),(x - 2,y),(x - 3,y)]
                elif self.postavitev % 4 == 2:
                    self.tocke = [(x,y),(x,y - 1),(x,y - 2),(x,y - 3)]
                    self.spodnje_tocke = [(x,y)]
                else:
                    self.tocke = [(x,y),(x + 1,y),(x + 2,y),(x + 3,y)]
                    self.spodnje_tocke = [(x,y),(x + 1,y),(x + 2,y),(x + 3,y)]
                self.velikost = len(self.spodnje_tocke)
                
            elif self.število == 5: #kvadrat
                pass
            
            elif self.število == 6: #kvadrat z izrastkom
                if self.postavitev % 4 == 0:
                    self.tocke = [(x,y),(x,y + 1),(x,y + 2),(x + 1,y),(x + 1,y + 1)]
                    self.spodnje_tocke = [(x,y + 2),(x + 1,y + 1)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [(x,y),(x - 1,y),(x - 2,y),(x,y + 1),(x - 1,y + 1)]
                    self.spodnje_tocke = [(x,y + 1),(x - 1,y + 1),(x - 2,y)]
                elif self.postavitev % 4 == 2:
                    self.tocke = [(x,y),(x,y - 1),(x,y - 2),(x + 1,y),(x + 1,y - 1)]
                    self.spodnje_tocke = [(x,y),(x + 1,y)]
                else:
                    self.tocke = [(x,y),(x + 1,y),(x + 2,y),(x,y - 1),(x + 1,y - 1)]
                    self.spodnje_tocke = [(x,y),(x + 1,y),(x + 2,y)]
                self.velikost = len(self.spodnje_tocke)
                
            elif self.število == 7: # majhen L v levo
                if self.postavitev % 4 == 0:
                    self.tocke = [(x,y),(x,y + 1),(x,y + 2),(x + 1, y + 2)]
                    self.spodnje_tocke = [(x,y + 2),(x + 1,y + 2)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [(x,y),(x - 1,y),(x - 2,y),(x - 2,y + 1)]
                    self.spodnje_tocke = [(x, y),(x - 1,y),(x - 2,y + 1)]
                elif self.postavitev % 4 == 2:
                    self.tocke = [(x,y),(x,y - 1),(x,y - 2),(x - 1, y - 2)]
                    self.spodnje_tocke = [(x,y),(x - 1,y - 2)]
                else:
                    self.tocke = [(x,y),(x + 1,y),(x + 2,y),(x + 2,y - 1)]
                    self.spodnje_tocke = [(x,y),(x + 1,y),(x + 2,y)]
                self.velikost = len(self.spodnje_tocke)
                
            elif self.število == 8: # majhen L v levo z izrastkom
                if self.postavitev % 4 == 0:
                    self.tocke = [(x,y),(x,y + 1),(x,y + 2),(x + 1,y + 2),(x - 1,y + 1)]
                    self.spodnje_tocke = [(x - 1,y + 1),(x,y + 2),(x + 1,y + 2)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [(x,y),(x - 1,y),(x - 2,y),(x - 2,y + 1),(x - 1,y - 1)]
                    self.spodnje_tocke = [(x,y),(x - 1,y),(x - 2,y + 1)]
                elif self.postavitev % 4 == 2:
                    self.tocke = [(x,y),(x,y - 1),(x,y - 2),(x - 1,y - 2),(x + 1,y - 1)]
                    self.spodnje_tocke = [(x - 1,y - 2),(x,y),(x + 1,y - 1)]
                else:
                    self.tocke = [(x,y),(x + 1,y),(x + 2,y),(x + 2,y - 1),(x + 1,y + 1)]
                    self.spodnje_tocke = [(x,y),(x + 1,y + 1),(x + 2,y)]
                self.velikost = len(self.spodnje_tocke)
                
            elif self.število == 9: #majhen L v desno
                if self.postavitev % 4 == 0:
                    self.tocke = [(x,y),(x,y + 1),(x,y + 2),(x + 1,y)]
                    self.spodnje_tocke = [(x,y + 2),(x + 1,y)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [(x,y),(x - 1,y),(x - 2,y),(x,y + 1)]
                    self.spodnje_tocke = [(x, y + 1),(x - 1,y),(x - 2,y)]
                elif self.postavitev % 4 == 2:
                    self.tocke = [(x,y),(x,y - 1),(x,y - 2),(x - 1,y)]
                    self.spodnje_tocke = [(x,y),(x - 1,y)]
                else:
                    self.tocke = [(x,y),(x + 1,y),(x + 2,y),(x,y - 1)]
                    self.spodnje_tocke = [(x,y),(x + 1,y),(x + 2,y)]
                self.velikost = len(self.spodnje_tocke)
                
            elif self.število == 10: #majhen L v desno z izrastkom
                if self.postavitev % 4 == 0:
                    self.tocke = [(x,y),(x,y + 1),(x,y + 2),(x + 1,y),(x - 1, y + 1)]
                    self.spodnje_tocke = [(x - 1, y + 1),(x,y + 2),(x + 1,y)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [(x,y),(x - 1,y),(x - 2,y),(x,y + 1),(x - 1, y - 1)]
                    self.spodnje_tocke = [(x, y + 1),(x - 1,y),(x - 2,y)]
                elif self.postavitev % 4 == 2:
                    self.tocke = [(x,y),(x,y - 1),(x,y - 2),(x - 1,y),(x + 1, y - 1)]
                    self.spodnje_tocke = [(x,y),(x - 1,y),(x + 1, y - 1)]
                else:
                    self.tocke = [(x,y),(x + 1,y),(x + 2,y),(x,y - 1),(x + 1, y + 1)]
                    self.spodnje_tocke = [(x,y),(x + 1,y + 1),(x + 2,y)]
                self.velikost = len(self.spodnje_tocke)
                
            elif self.število == 11: # velik L v levo
                if self.postavitev % 4 == 0:
                    self.tocke = [(x,y),(x,y + 1),(x,y + 2),(x,y + 3),(x + 1, y + 3)]
                    self.spodnje_tocke = [(x,y + 3),(x + 1,y + 3)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [(x,y),(x - 1,y),(x - 2,y),(x - 3,y),(x - 3,y + 1)]
                    self.spodnje_tocke = [(x, y),(x - 1,y),(x - 2,y),(x - 3,y + 1)]
                elif self.postavitev % 4 == 2:
                    self.tocke = [(x,y),(x,y - 1),(x,y - 2),(x,y - 3),(x - 1, y - 3)]
                    self.spodnje_tocke = [(x,y),(x - 1,y - 3)]
                else:
                    self.tocke = [(x,y),(x + 1,y),(x + 2,y),(x + 3,y),(x + 3,y - 1)]
                    self.spodnje_tocke = [(x,y),(x + 1,y),(x + 3,y),(x + 3,y - 1)]
                self.velikost = len(self.spodnje_tocke)
                
            elif self.število == 12: #velik L v desno
                if self.postavitev % 4 == 0:
                    self.tocke = [(x,y),(x,y + 1),(x,y + 2),(x,y + 3),(x + 1,y)]
                    self.spodnje_tocke = [(x,y + 3),(x + 1,y)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [(x,y),(x - 1,y),(x - 2,y),(x - 3,y)]
                    self.spodnje_tocke = [(x, y),(x - 1,y),(x - 2,y),(x - 3,y + 1)]
                elif self.postavitev % 4 == 2:
                    self.tocke = [(x,y),(x,y - 1),(x,y - 2),(x,y - 3)]
                    self.spodnje_tocke = [(x,y),(x - 1,y - 3)]
                else:
                    self.tocke = [(x,y),(x + 1,y),(x + 2,y),(x + 3,y)]
                    self.spodnje_tocke = [(x,y),(x + 1,y),(x + 2,y),(x + 3,y)]
                self.velikost = len(self.spodnje_tocke)
            #kotna2
            elif self.število == 13: 
                if self.postavitev % 4 == 0:
                    self.tocke = [(x,y),(x + 1,y),(x,y + 1)]
                    self.spodnje_tocke = [(x,y + 1),(x + 1,y)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [(x,y),(x - 1,y),(x,y + 1)]
                    self.spodnje_tocke = [(x,y + 1),(x - 1,y)]
                elif self.postavitev % 4 == 2:
                    self.tocke = [(x,y),(x,y - 1),(x - 1,y)]
                    self.spodnje_tocke = [(x,y),(x - 1,y)]
                else:
                    self.tocke = [(x,y), (x + 1,y),(x,y - 1)]
                    self.spodnje_tocke = [(x,y),(x + 1,y)]
                self.velikost = len(self.spodnje_tocke)
            #kotna3
            elif self.število == 14: 
                if self.postavitev % 4 == 0:
                    self.tocke = [(x,y),(x + 1,y),(x + 2,y),(x,y + 1),(x,y + 2)]
                    self.spodnje_tocke = [(x,y + 2),(x + 1,y),(x + 2,y)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [(x,y),(x - 1,y),(x - 2,y),(x,y + 1),(x,y + 2)]
                    self.spodnje_tocke = [(x,y + 2),(x - 1,y),(x - 2,y)]
                elif self.postavitev % 4 == 2:
                    self.tocke = [(x,y),(x,y - 1),(x,y - 2),(x - 1,y),(x - 2,y)]
                    self.spodnje_tocke = [(x,y),(x - 1,y),(x - 2,y)]
                else:
                    self.tocke = [(x,y),(x + 1,y),(x + 2,y),(x,y - 1),(x,y - 2)]
                    self.spodnje_tocke = [(x,y),(x + 1,y),(x + 2,y)]
                self.velikost = len(self.spodnje_tocke)         

            self.postavitev += 1
            print(igra)
        else:
            print('ne morem obrnit',self.polozaj)
        
    def lahko_zavrtim(self):
        x,y = self.polozaj
        if self.število == 1: #enka
            return True
        elif self.število  == 2: #dvojka
            if self.postavitev % 4 == 0:
                if self.polozaj[1] < self.visina - 1 and (self.polozaj[0], self.polozaj[1] + 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 1:
                if self.polozaj[0] > 0 and (self.polozaj[0] - 1, self.polozaj[1]) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 2:
                if self.polozaj[1] > 0:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 3:
                if self.polozaj[0] < self.sirina - 1 and (self.polozaj[0] + 1, self.polozaj[1]) not in self.koncne_tocke:
                    return True
                else:
                    return False

        elif self.število == 3: #trojka
            x,y = self.polozaj
            if self.postavitev % 4  == 0:
                if y < self.visina + 2 and (x, y + 1) not in self.koncne_tocke and (x, y + 2) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 1:
                if x > 1 and (x - 1, y) not in self.koncne_tocke and (x - 2, y) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 2:
                if y >= 2:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 3:
                if x < self.sirina - 2 and (x + 1, y) not in self.koncne_tocke and (x + 2, y) not in self.koncne_tocke:
                    return True
                else:
                    return False
                                  
        elif self.število == 4: #štirka
            if self.postavitev % 4  == 0:
                if y < self.visina - 4 and (x,y + 1) not in self.koncne_tocke and (x, y + 2) not in self.koncne_tocke and (x,y + 3) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 1:
                if x >= 3 and (x - 1, y) not in self.koncne_tocke and (x - 2, y) not in self.koncne_tocke and (x - 3, y) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 2:
                if y >= 3:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 3:
                if x <= self.sirina - 4 and (x + 1, y) not in self.koncne_tocke and (x + 2, y) not in self.koncne_tocke and (x + 3, y) not in self.koncne_tocke:
                    return True
                else:
                    return False
                                  
        elif self.število == 5: #kvadrat
            return True
                                  
        elif self.število == 6: #kvadrat z izrastkom
            if self.postavitev % 4  == 0:
                if y <= self.visina - 3 and (x,y + 1) not in self.koncne_tocke and (x, y + 2) not in self.koncne_tocke and (x + 1,y + 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 1:
                if x >= 2 and (x - 2, y) not in self.koncne_tocke and (x - 1, y) not in self.koncne_tocke and (x - 1, y + 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 2:
                if y >= 2:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 3:
                if x <= self.sirina - 3 and (x + 1, y) not in self.koncne_tocke and (x + 2, y) not in self.koncne_tocke and (x + 1, y - 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
        elif self.število == 7: # mali L v levo
            if self.postavitev % 4  == 0:
                if y < self.visina - 3 and (x,y + 1) not in self.koncne_tocke and (x, y + 2) not in self.koncne_tocke and (x + 1,y + 2) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 1:
                if x >= 2 and (x - 2, y) not in self.koncne_tocke and (x - 1, y) not in self.koncne_tocke and (x - 2, y + 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 2:
                if y >= 2:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 3:
                if x <= self.sirina - 3 and (x + 1, y) not in self.koncne_tocke and (x + 2, y) not in self.koncne_tocke and (x + 2, y - 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
        elif self.število == 8: # mali L v levo z izrastkom
            if self.postavitev % 4  == 0:
                if y < self.visina - 3 and (x,y + 1) not in self.koncne_tocke and (x, y + 2) not in self.koncne_tocke and (x + 1,y + 2) not in self.koncne_tocke and (x - 1,y + 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 1:
                if x >= 2 and (x - 2, y) not in self.koncne_tocke and (x - 1, y) not in self.koncne_tocke and (x - 2, y + 1) not in self.koncne_tocke and (x - 1,y - 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 2 and (x + 1,y - 1) not in self.koncne_tocke:
                if y >= 2:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 3:
                if x <= self.sirina - 3 and (x + 1, y) not in self.koncne_tocke and (x + 2, y) not in self.koncne_tocke and (x + 2, y + 1) not in self.koncne_tocke and (x + 1,y + 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
        elif self.število == 9: # mali L v desno
            if self.postavitev % 4  == 0:
                if y < self.visina - 2 and (x,y + 1) not in self.koncne_tocke and (x, y + 2) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 1:
                if x >= 3 and (x - 2, y) not in self.koncne_tocke and (x - 1, y) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 2:
                if y >= 3:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 3:
                if x <= self.sirina - 3 and (x + 1, y) not in self.koncne_tocke and (x + 2, y) not in self.koncne_tocke:
                    return True
                else:
                    return False
        elif self.število == 10: # mali L v desno z izrastkom
            if self.postavitev % 4  == 0:
                if y < self.visina - 2 and (x,y + 1) not in self.koncne_tocke and (x, y + 2) not in self.koncne_tocke and (x - 1, y + 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 1:
                if x >= 3 and (x - 2, y) not in self.koncne_tocke and (x - 1, y) not in self.koncne_tocke and (x - 1, y - 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 2 and (x + 1, y - 1) not in self.koncne_tocke:
                if y >= 3:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 3:
                if x <= self.sirina - 3 and (x + 1, y) not in self.koncne_tocke and (x + 2, y) not in self.koncne_tocke and (x + 1, y + 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
        elif self.število == 11: # velik L v levo
            if self.postavitev % 4  == 0:
                if y <= self.visina - 4 and (x,y + 1) not in self.koncne_tocke and (x,y + 2) not in self.koncne_tocke and (x,y + 3) not in self.koncne_tocke and (x + 1,y + 3) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 1:
                if x >= 3 and (x - 1,y) not in self.koncne_tocke and (x - 2,y) not in self.koncne_tocke and (x - 3,y) not in self.koncne_tocke and (x - 3,y + 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 2 :
                if y >= 3 and (x,y - 1) not in self.koncne_tocke and (x,y - 2) not in self.koncne_tocke and (x, y - 3) not in self.koncne_tocke and (x - 1,y - 3) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 3:
                if x <= self.sirina - 4 and (x + 1,y) not in self.koncne_tocke and (x + 2,y) not in self.koncne_tocke and (x + 3,y) not in self.koncne_tocke and (x + 3,y - 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
        elif self.število == 12: # velik L v desno
            if self.postavitev % 4  == 0:
                if y <= self.visina - 4 and (x,y + 1) not in self.koncne_tocke and (x, y + 2) not in self.koncne_tocke and (x, y + 3) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 1:
                if x >= 3 and (x - 1, y) not in self.koncne_tocke and (x - 2, y) not in self.koncne_tocke and (x - 3, y) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 2:
                if y >= 3 and (x, y - 1) not in self.koncne_tocke and (x,y - 2) not in self.koncne_tocke and (x,y - 3) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 3:
                if x <= self.sirina - 4 and (x + 1, y) not in self.koncne_tocke and (x + 2, y) not in self.koncne_tocke and (x + 3, y) not in self.koncne_tocke:
                    return True
                else:
                    return False
        elif self.število == 13: # kotna 2
            if self.postavitev % 4  == 0:
                if y <= self.visina - 2 and (x,y + 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 1:
                if x >= 1 and (x - 1,y) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 2:
                if y >= 1 and (x,y - 1) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 3:
                if x <= self.sirina - 2 and (x + 1,y) not in self.koncne_tocke:
                    return True
                else:
                    return False
        elif self.število == 14: # kotna 3
            if self.postavitev % 4  == 0:
                if y <= self.visina - 3 and (x,y + 1) not in self.koncne_tocke and (x,y + 2) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 1:
                if x >= 2 and (x - 1,y) not in self.koncne_tocke and (x - 2,y) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 2:
                if y >= 2 and (x,y - 1) not in self.koncne_tocke and (x,y - 2) not in self.koncne_tocke:
                    return True
                else:
                    return False
            elif self.postavitev % 4 == 3:
                if x <= self.sirina - 3 and (x + 1, y) not in self.koncne_tocke and (x + 2, y) not in self.koncne_tocke:
                    return True
                else:
                    return False
            
            
    def shrani_kanvas(self):
        self.koncne_tocke.extend(self.tocke)
        #pobarvaj jih rumeno
                
    def polna_vrstica(self):
        for številka in range(self.visina):
            števec = 0
            koncne_tocke = self.koncne_tocke
            self.koncne_tocke = []
            for tocka in koncne_tocke:
                if tocka[1] == številka:
                    števec += 1
            if števec == self.sirina:
                for tocka in koncne_tocke:
                    if tocka[1] == številka:
                        del tocka
                    elif tocka[1] < številka:
                        tocka = (tocka[0], tocka[1] + 1)
                        self.koncne_tocke.append(tocka)
                    else:
                        self.koncne_tocke.append(tocka)
            else:
                self.koncne_tocke = koncne_tocke
        
    def konec(self):
        if (9,0) in self.koncne_tocke:
            return True
        elif (10,0) in self.koncne_tocke and self.velikost == 2:
            return True
        elif (11,0) in self.koncne_tocke and self.velikost == 3:
            return True
        else:
            return False

            
            
igra = Igra(10,7)

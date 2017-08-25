import random
ENKA = '1'
DVOJKA = '2'
TROJKA = '3'
ŠTIRKA = '4'
KVADRAT = '5'
KVADRAT_IZRASTEK = '6'
MALI_L_LEVO = '7'
MALI_L_LEVO_IZRASTEK = '8'
MALI_L_DESNO = '9'
MALI_L_DESNO_IZRASTEK = '10'
VELIK_L_LEVO = '11'
VELIK_L_DESNO = '12'
KOTNA2 = '13'
KOTNA3 = '14'
slovar_oblik = [ENKA, DVOJKA, TROJKA, ŠTIRKA, KVADRAT, KVADRAT_IZRASTEK, MALI_L_LEVO, MALI_L_LEVO_IZRASTEK, MALI_L_DESNO, MALI_L_DESNO_IZRASTEK, VELIK_L_LEVO, VELIK_L_DESNO, KOTNA2, KOTNA3]

class Igra:
    def __init__(self, sirina, visina):
        self.sirina = sirina
        self.visina = visina
        self.naredi_nov_objekt()
        self.koncne_tocke = []
        self.rezultat = 0

    def naredi_nov_objekt(self):
        število = random.randrange(1,15)
        self.oblika = slovar_oblik[število - 1]
        x = 8
        self.polozaj = (x,0)
        self.postavitev = 0
        try:
            self.rezultat += 10
        except:
            self.rezultat = 10
        #velikost pomeni širino elementa (kocke)
        if self.oblika == ENKA: 
            self.tocke = [(x,0)]
            self.velikost = 1
            self.spodnje_tocke = [(x,0)]
        elif self.oblika == DVOJKA:
            self.tocke = [(x,0),(x + 1,0)]
            self.velikost = 2
            self.spodnje_tocke = [(x,0),(x + 1,0)]
        elif self.oblika == TROJKA:
            self.tocke = [(x,0),(x + 1,0),(x + 2,0)]
            self.oblika = 3
            self.spodnje_tocke = [(x,0),(x + 1,0),(x + 2,0)]
        elif self.oblika == ŠTIRKA:
            self.tocke = [(x,0),(x + 1,0),(x + 2,0),(x + 3,0)]
            self.velikost = 4
            self.spodnje_tocke = [(x,0),(x + 1,0),(x + 2,0),(x + 3,0)]
        elif self.oblika == KVADRAT:
            self.tocke = [(x,1),(x + 1,1),(x,0),(x + 1,0)]
            self.velikost = 2
            self.spodnje_tocke = [(x,1),(x + 1,1)]
        elif self.oblika == KVADRAT_IZRASTEK:
            self.tocke = [(x,1),(x + 1,1),(x + 2, 1),(x,0),(x + 1,0)]
            self.velikost = 3
            self.spodnje_tocke = [(x,1),(x + 1,1),(x + 2, 1)]
        elif self.oblika == MALI_L_LEVO:
            self.tocke = [(x,1),(x + 1,1),(x + 2, 1),(x + 2,0)]
            self.velikost = 3
            self.spodnje_tocke = [(x,1),(x + 1,1),(x + 2, 1)]
        elif self.oblika == MALI_L_LEVO_IZRASTEK:
            self.tocke = [(x,1),(x + 1,1),(x + 2, 1),(x + 2,0),(x + 1,2)]
            self.velikost = 3
            self.spodnje_tocke = [(x,1),(x + 1,2),(x + 2, 1)]
        elif self.oblika == MALI_L_DESNO:
            self.tocke = [(x,1),(x + 1,1),(x + 2, 1),(x,0)]
            self.velikost = 3
            self.spodnje_tocke = [(x,1),(x + 1,1),(x + 2, 1)]
        elif self.oblika == MALI_L_DESNO_IZRASTEK:
            self.tocke = [(x,1),(x + 1,1),(x + 2, 1),(x,0), (x + 1,2)]
            self.velikost = 3
            self.spodnje_tocke = [(x,1),(x + 1,2),(x + 2, 1)]
        elif self.oblika == VELIK_L_LEVO: 
            self.tocke = [(x,1),(x + 1,1),(x + 2, 1),(x + 3, 1),(x + 3,0)]
            self.velikost = 4
            self.spodnje_tocke = [(x,1),(x + 1,1),(x + 2, 1),(x + 3, 1)]
        elif self.oblika == VELIK_L_DESNO: 
            self.tocke = [(x,1),(x + 1,1),(x + 2, 1),(x + 3, 1),(x,0)]
            self.velikost = 4
            self.spodnje_tocke = [(x,1),(x + 1,1),(x + 2, 1),(x + 3, 1)]
        elif self.oblika == KOTNA2:
            self.tocke = [(x,1),(x + 1,1),(x,0)]
            self.velikost = 2
            self.spodnje_tocke = [(x,1),(x + 1,1)]
        elif self.oblika == KOTNA3:
            self.tocke = [(x,2),(x + 1,2),(x + 2, 2),(x,0),(x,1)]
            self.velikost = 3
            self.spodnje_tocke = [(x,2),(x + 1,2),(x + 2, 2)]
        
    def desno(self):
        if self.prosto_desno() == False:
            print('ne morem v desno')
            pass
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
            if self.fiksen() == True:
                self.shrani_kanvas()
                self.naredi_nov_objekt()

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
            pass
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
            if self.fiksen() == True:
                self.shrani_kanvas()
                self.naredi_nov_objekt()
        
    def prosto_levo(self):
        x, y = self.polozaj
        ja_ne = 1
        for tocka in self.tocke:
            if tocka[0] == 0 or (tocka[0] - 1, tocka[1]) in self.koncne_tocke or ja_ne == 0:
                ja_ne = 0
        if ja_ne == 1:
            return True
        else:
            return False

    def premakni(self):
        if self.fiksen() == False:
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
        
    def fiksen(self):
        ja_ne = 0
        for tocka in self.spodnje_tocke:            
            if tocka[1] == self.visina - 1 or (tocka[0],tocka[1] + 1) in self.koncne_tocke or ja_ne == 1:
                ja_ne = 1
                return True 
                break
            
        if ja_ne == 0:
            return False        
            
    def zavrti(self):
        x,y = self.polozaj
        if self.lahko_zavrtim() == True:
            if self.oblika == ENKA: 
                pass

            elif self.oblika == DVOJKA: 
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
                
            elif self.oblika == TROJKA: 
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
 
            elif self.oblika == ŠTIRKA: 
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
  
            elif self.oblika == KVADRAT: 
                pass

            elif self.oblika == KVADRAT_IZRASTEK: 
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
    
            elif self.oblika == MALI_L_LEVO: 
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
  
            elif self.oblika == MALI_L_LEVO_IZRASTEK: 
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
 
            elif self.oblika == MALI_L_DESNO: 
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

            elif self.oblika == MALI_L_DESNO_IZRASTEK: 
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
   
            elif self.oblika == VELIK_L_LEVO: 
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
                    self.spodnje_tocke = [(x,y),(x + 1,y),(x + 2,y),(x + 3,y)]
                self.velikost = len(self.spodnje_tocke)
    
            elif self.oblika == VELIK_L_DESNO: 
                if self.postavitev % 4 == 0:
                    self.tocke = [(x,y),(x,y + 1),(x,y + 2),(x,y + 3),(x + 1,y)]
                    self.spodnje_tocke = [(x,y + 3),(x + 1,y)]
                elif self.postavitev % 4 == 1:
                    self.tocke = [(x,y + 1),(x,y),(x - 1,y),(x - 2,y),(x - 3,y)]
                    self.spodnje_tocke = [(x,y + 1),(x - 1,y),(x - 2,y),(x - 3,y)]
                elif self.postavitev % 4 == 2:
                    self.tocke = [(x,y),(x,y - 1),(x,y - 2),(x,y - 3),(x - 1,y)]
                    self.spodnje_tocke = [(x,y),(x - 1,y)]
                else:
                    self.tocke = [(x,y),(x + 1,y),(x + 2,y),(x + 3,y),(x,y - 1)]
                    self.spodnje_tocke = [(x,y),(x + 1,y),(x + 2,y),(x + 3,y)]
                self.velikost = len(self.spodnje_tocke)

            elif self.oblika == KOTNA2: 
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
                
            elif self.oblika == KOTNA3: 
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
            
        else:
            print('ne morem obrnit',self.polozaj)
        
    def lahko_zavrtim(self):
        x,y = self.polozaj
        if self.oblika == ENKA: 
            return True

        elif self.oblika == DVOJKA: 
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
        
        elif self.oblika == TROJKA: 
            print(self.koncne_tocke)
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
                                  
        elif self.oblika == ŠTIRKA: 
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
                                  
        elif self.oblika == KVADRAT: 
            return True
                        
        elif self.oblika == KVADRAT_IZRASTEK: 
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

        elif self.oblika == MALI_L_LEVO: 
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
        
        elif self.oblika == MALI_L_LEVO_IZRASTEK: 
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

        elif self.oblika == MALI_L_DESNO: 
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

        elif self.oblika == MALI_L_DESNO_IZRASTEK: 
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

        elif self.oblika == VELIK_L_LEVO: 
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

        elif self.oblika == VELIK_L_DESNO: 
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
    
        elif self.oblika == KOTNA2: 
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
                
        elif self.oblika == KOTNA3: 
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
                
    def polna_vrstica(self):
        for številka in range(self.visina):
            števec = 0
            koncne_tocke = self.koncne_tocke
            self.koncne_tocke = []
            for tocka in koncne_tocke:
                if tocka[1] == številka:
                    števec += 1
            if števec == self.sirina:
                self.rezultat += 100
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
        if (8,0) in self.koncne_tocke:
            return True
        elif (9,0) in self.koncne_tocke and self.velikost >= 2:
            return True
        elif (10,0) in self.koncne_tocke and self.velikost >= 3:
            return True
        elif (11,0) in self.koncne_tocke and self.velikost >= 4:
            return True
        else:
            return False

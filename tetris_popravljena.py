import tkinter as tk
import popravljena

VELIKOST_POLJA = 20
ODMIK = 5

#koliko korakov naj naredi v sekundi
HITROST = 5

class Tetris:
    def __init__(self, okno):
        #nastavimo model
        self.igra = popravljena.Igra(18,30)
        
        #pripravimo grafični vmesnik
        self.okno = okno
        self.okno.title("Tetris")
        self.semafor = tk.Canvas(
            width = VELIKOST_POLJA * self.igra.sirina + 2 * ODMIK,
            height = 60
        )        
        self.semafor.pack()
        self.semafor.create_text(170,30,fill = "darkblue",font = "Times 20 italic bold",
                        text = 'Trenutni rezultat je 0 točk')
        
        self.igralna_plosca = tk.Canvas(
            width=VELIKOST_POLJA * self.igra.sirina + 2 * ODMIK,
            height=VELIKOST_POLJA * self.igra.visina + 2 * ODMIK
        )
        self.igralna_plosca.pack()
        self.okno.bind('<Key>', self.obdelaj_tipko)

        #zaženemo osnovno zanko igre
        self.osnovna_zanka()
        
                                 
    def osnovna_zanka(self):
        if self.igra.fiksen() == True:
            self.igra.shrani_kanvas()
            if self.igra.konec() == True:
                self.igralna_plosca.delete('all')
                self.igralna_plosca.create_text(170,30,fill="darkblue",font="Times 20 italic bold",
                        text="KONEC IGRE!")
                self.semafor.delete('all')
                self.semafor.create_text(170,30,fill="darkblue",font="Times 20 italic bold",
                        text = "Končni rezultat je: " + str(self.igra.rezultat)+ ' točk.')
                self.ustvari_nov_zapis('rezultati.txt')
            else:
                self.igra.polna_vrstica()
                self.osvezi_semafor()
                self.igra.naredi_nov_objekt()    
                self.osvezi_prikaz()
                self.okno.after(int(1000 // HITROST), self.osnovna_zanka)
        elif self.igra.fiksen() == False:
            self.premakni()
            self.okno.after(int(1000 // HITROST), self.osnovna_zanka)        
     
    def osvezi_semafor(self):
        self.semafor.delete('all')
        self.semafor.create_text(170,30,fill = "darkblue",font = "Times 20 italic bold",
                                 text = 'Trenutni rezultat je: ' + str(self.igra.rezultat) + ' točk')

    def osvezi_prikaz(self):
        self.igralna_plosca.delete('all')
        self.igralna_plosca.create_rectangle(
            ODMIK,
            ODMIK,
            int(self.igralna_plosca['width']) - ODMIK,
            int(self.igralna_plosca['height']) - ODMIK
        )
        for x,y in self.igra.tocke:
            self.igralna_plosca.create_oval(
                ODMIK + VELIKOST_POLJA * x,
                ODMIK + VELIKOST_POLJA * y,
                ODMIK + VELIKOST_POLJA * x + VELIKOST_POLJA,
                ODMIK + VELIKOST_POLJA * y + VELIKOST_POLJA,
                fill = "orange"
            )
        for x,y in self.igra.koncne_tocke:
            self.igralna_plosca.create_oval(
                ODMIK + VELIKOST_POLJA * x,
                ODMIK + VELIKOST_POLJA * y,
                ODMIK + VELIKOST_POLJA * x + VELIKOST_POLJA,
                ODMIK + VELIKOST_POLJA * y + VELIKOST_POLJA,
                fill = "darkgreen"
            )

    def obdelaj_tipko(self,event):
        if event.keysym == 'Right':
            self.desno()
        elif event.keysym == 'Left':
            self.levo()
        elif event.keysym == 'Down':
            self.igra.premakni()
        elif event.keysym == 'Up':
            self.zavrti()
            
    def premakni(self):
        if self.igra.fiksen() == True:
            self.osvezi_prikaz()
        elif self.igra.fiksen() == False:
            self.igra.premakni()
            self.osvezi_prikaz()
            
    def desno(self):
        if self.igra.prosto_desno() == True and self.igra.konec() == False:
            self.igra.desno()
        self.osvezi_prikaz()
        
    def levo(self):
        if self.igra.prosto_levo() == True and self.igra.konec() == False:
            self.igra.levo()
        self.osvezi_prikaz()

    def zavrti(self):
        if self.igra.lahko_zavrtim() == True and self.igra.konec() == False:
            self.igra.zavrti()
        self.osvezi_prikaz()

    def ustvari_nov_zapis(self,datoteka):
        try:
            with open(datoteka, "r+") as f:
                old = f.readlines()
                stevec = 1
                seznam = []
                stevec2 = 0            
                while stevec2 < len(old):
                    if stevec2 == len(old) - 1:
                        izzid = int(old[stevec2][4:])
                    else:
                        izzid = int(old[stevec2][4:-1])
                    seznam.append(izzid)
                    stevec2 += 1
                seznam.append(self.igra.rezultat)
                seznam.sort()
                niz = ''
                while len(seznam) > 0:
                    if stevec // 10 == 0:
                        niz += ' ' + str(stevec) + "  " + str(seznam[0]) + '\n'
                    else:
                        niz += '' + str(stevec) + "  " + str(seznam[0]) + '\n'
                    del(seznam[0])
                    stevec += 1
                with open(datoteka,"w") as t:
                    t.write(niz)
        except:
            with open(datoteka, "w") as f:
                niz = ' ' + str(1) + "  " + str(self.igra.rezultat) + '\n'
                with open(datoteka,"w") as t:
                    t.write(niz)


okno = tk.Tk()
moj_stevec = Tetris(okno)
okno.mainloop()

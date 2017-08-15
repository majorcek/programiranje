import tkinter as tk
import poskus

VELIKOST_POLJA = 10
ODMIK = 5

#koliko korakov naj naredi v sekundi
HITROST = 3


class Tetris:
    def __init__(self, okno):
        #nastavimo model
        self.igra = poskus.Igra(20,20)
        
        #pripravimo grafični vmesnik
        self.okno = okno
        self.igralna_plosca = tk.Canvas(
            width=VELIKOST_POLJA * self.igra.sirina + 2 * ODMIK,
            height=VELIKOST_POLJA * self.igra.visina + 2 * ODMIK
        )
        self.igralna_plosca.pack()
        self.okno.bind('<Key>', self.obdelaj_tipko)

        #zaženemo osnovno zanko igre
        self.osnovna_zanka()

    def osnovna_zanka(self):
        if self.igra.fiksen() == False:
            self.igra.premakni()   
        else:
            self.igra.shrani_kanvas()
            self.igra.polna_vrstica()
            self.igra.naredi_nov_objekt()    
        self.osvezi_prikaz()
        self.okno.after(int(1000 // HITROST), self.osnovna_zanka)
     
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
                ODMIK + VELIKOST_POLJA * y + VELIKOST_POLJA
            )
        for x,y in self.igra.koncne_tocke:
            self.igralna_plosca.create_oval(
                ODMIK + VELIKOST_POLJA * x,
                ODMIK + VELIKOST_POLJA * y,
                ODMIK + VELIKOST_POLJA * x + VELIKOST_POLJA,
                ODMIK + VELIKOST_POLJA * y + VELIKOST_POLJA
            )
            
    def osvezi_prikaz_stari(self):
        for x,y in self.igra.tocke:
            self.igralna_plosca.create_oval(
                ODMIK + VELIKOST_POLJA * x,
                ODMIK + VELIKOST_POLJA * y,
                ODMIK + VELIKOST_POLJA * x + VELIKOST_POLJA,
                ODMIK + VELIKOST_POLJA * y + VELIKOST_POLJA
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
        if self.igra.fiksen() == False and self.igra.konec() == False:
            self.igra.premakni()
        self.osvezi_prikaz()
            
    def desno(self):
        if self.igra.prosto_desno() == True:
            self.igra.desno()
        self.osvezi_prikaz()
        
    def levo(self):
        if self.igra.prosto_levo() == True:
            self.igra.levo()
        self.osvezi_prikaz()

    def zavrti(self):
        if self.igra.lahko_zavrtim() == True:
            self.igra.zavrti()
        self.osvezi_prikaz()



okno = tk.Tk()
moj_stevec = Tetris(okno)
okno.mainloop()

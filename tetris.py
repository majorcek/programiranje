import tkinter as tk
import poskus

# TO DO: števec točk: vsaka kocka 10 točk, podrta vrstica 100 točk

VELIKOST_POLJA = 20
ODMIK = 5

#koliko korakov naj naredi v sekundi
HITROST = 1


class Tetris:
    def __init__(self, okno):
        #nastavimo model
        self.igra = poskus.Igra(18,30)
        
        #pripravimo grafični vmesnik
        self.okno = okno
        
        self.semafor = tk.Canvas(
            width = VELIKOST_POLJA * self.igra.sirina + 2 * ODMIK,
            height = 60
        )
        self.semafor.create_text(50,50,fill = "darkblue",font = "Times 20 italic bold",
                        text = 'Trenutni rezultat je 0 točk')
        
        self.semafor.pack()
        
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
            self.premakni()
            self.osvezi_prikaz()
            self.okno.after(int(1000 // HITROST), self.osnovna_zanka)
        else:
            self.igra.shrani_kanvas()
            if self.igra.konec() == True:
                self.igralna_plosca.delete('all')
                self.igralna_plosca.create_text(100,100,fill="darkblue",font="Times 20 italic bold",
                        text="KONEC IGRE!")
            else:
                self.igra.polna_vrstica()
                self.osvezi_semafor()
                print('!')
                self.naredi_nov_objekt()    
                self.osvezi_prikaz()
                self.okno.after(int(1000 // HITROST), self.osnovna_zanka)
     
    def osvezi_semafor(self):
        #mogoče je treba brez selfa
        self.semafor.delete('all')
        self.semafor.create_text(30,30,fill = "darkblue",font = "Times 20 italic bold",
                                 text = 'Trenutni rezultat je: mlkmyxkc')
        print('?')

                        #text = 'Trenutni rezultat je:' + str(self.igra.rezultat))

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

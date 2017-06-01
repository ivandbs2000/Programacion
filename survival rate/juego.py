from tkinter import *
import random
import time

#===========================================================================VENTANA===================================================#

v = Tk()
v.title("Survival Rate")
v.geometry("1366x768")

#=====================================================IMAGENES==========================================================#
imagen = PhotoImage(file = "menu3.png")
images = Label(v,image = imagen).place(x = 0, y= 0)
imagex = PhotoImage(file = "im.png")
imagee = PhotoImage(file = "controlesm.png")
imbn = PhotoImage(file = "newgame.png")
imbl = PhotoImage(file = "loadgame.png")
imx = PhotoImage(file = "exit2.png")
im4 = PhotoImage(file = "menu4.png")
lvl1 = PhotoImage(file = "lvl1.png")
lvl2 = PhotoImage(file = "lvl2.png")
lvl3 = PhotoImage(file = "lvl3.png")
lvl4 = PhotoImage(file = "lvl4.png")
lvl5 = PhotoImage(file = "lvl5.png")
Nivel1= PhotoImage(file = "nivel111.png")
Nivel2 = PhotoImage(file = "nivel22.png")
Nivel3 = PhotoImage(file = "nivel33.png")
Nivel4 = PhotoImage(file = "nivel44.png")
Nivel5 = PhotoImage(file = "nivel55.png")
carro1 = PhotoImage(file = "player1.png")
mitad = PhotoImage(file = "mitad.png")
carro2 = PhotoImage(file = "player2.png")
minivan = PhotoImage(file = "minivan.png")
runer = PhotoImage(file = "runner.png")
gas = PhotoImage(file = "gasolina.png")
fihter = PhotoImage(file = "fighter.png")
bomba = PhotoImage(file = "bom.png")
win = PhotoImage(file = "win.png")
lose = PhotoImage(file = "loser.png")
mancha = PhotoImage(file = "mancha1.png")
iz = PhotoImage(file = "player1De.png")

#=========================================================================FUENTES===========================================================#

neon = ("Neon 80s",17)
bit = ("8BIT WONDER",22)
neon1 = ("Neon 80s",30)



#========================================================================GLOBALES=============================================================#

v1 = ""
v2 = ""
v3 = "" 
v4 = ""
v5 = ""
namep1 = ""
namep2 = ""
h = []




#===================================================================INSTRUCCIONES=========================================================================#
def instrucciones():
    """
esta funcion utiliza la ventana original para crear una subventana (toplevel) donde el usuario podra ver las instrucciones del juego
    """
    global imagex,v1

    
        
    v1 = Toplevel()
    v1.title("Survival Rate")
    v1.geometry("1366x768")
    widget = Label(v1, image= imagex).place(x = 0, y= 0)
    etiqueta = Label(v1,text = '-No chocar con ninguno de los carros rivales \n'
                               '-No dejar que la gasolina llegue a 0 \n'
                               '-No chocar contra las paredes \n'
                               '-Si pierdes por alguna razón empezaras en el principio de ese mismo nivel \n'
                               '-Atrapa el auto azul que brilla para una bonificación de gasolina \n'
                               '-Para pasar al siguiente nivel tienes que llegar a la meta \n'
                               '-Una vez se termine un nivel , la gasolina se reinicia \n'
                               '-Solo se puede guardar al terminar un nivel \n'
                               , font = neon, relief = "sunken" , bg = "Black" , fg = "White" , bd = 8
                                ).place(x= 285, y= 250)
    

   
    bsalir = Button(v1,text = " ATRAS",command = salir2,font = bit,fg = "Blue",bg = "Black",bd = 5).place(x = 580, y = 520)
    
#=====================================================================CONTROLES==========================================================================#     
def controles():
    """
esta funcion utiliza la ventana original para crear una subventana (toplevel) donde el usuario podra ver los controles que podra utilizar en el  juego
    """
    global imagee,v2

    v2 = Toplevel()
    v2.title("Survival Rate")
    v2.geometry("1366x768")
    widget1 = Label(v2, image= imagee).place(x = 0, y= 0)
    etiqueta1 = Label(v2, text = " A ", font = neon1,fg = "Blue",bg= "Black",bd= 7,relief = "raised").place(x = 143,y = 270)
    etiqueta2 = Label(v2, text = " D ", font = neon1,fg = "Blue",bg= "Black",bd= 7,relief = "raised").place(x = 143,y = 430)
    etiqueta3 = Label(v2, text = " J ", font = neon1,fg = "Blue",bg= "Black",bd= 7,relief = "raised").place(x = 1115,y = 270)
    etiqueta4 = Label(v2, text = " L ", font = neon1,fg = "Blue",bg= "Black",bd= 7,relief = "raised").place(x = 1115,y = 430)
    
    
    
        
    bsalir = Button(v2,text = " ATRAS",command = salir5,font = bit,fg = "Blue",bg = "Black",bd = 5).place(x = 550, y = 570)

#========================================================================START======================================================================#
def start():
    """
esta funcion utiliza la ventana original para crear una subventana (toplevel) donde el podra seleccionar si empezar una nueva partida o cargarla
    """
    global imagen , imbn, imbl, imx,im4,lvl1 ,lvl2,lvl3,lvl4,lvl5,carro1,mitad,carro2,v3

    v.iconify()
    v3 = Toplevel()
    v3.title("Survival Rate")
    v3.geometry("1366x768")
    widget2 = Label(v3,image = imagen).place(x = 0,y = 0)
    def load():
        """
        """
        pass
    
    bn = Button(v3,image=imbn,command = new, height = 40,width =150).place(x= 600,y = 320)
    bl = Button(v3,image=imbl,command = load, height = 40, width =150).place(x=600, y = 450)
    bx = Button(v3,image=imx,command = salir3,height = 40, width =150).place(x=600, y = 580)
    
#=====================================================================NEW=========================================================================#
    
def new():
    """
esta funcion utiliza la ventana original para crear una subventana (toplevel) donde el podra seleccionar un nivel entre todos los que hay teniendo en cuenta que
entre el nivel sea mas alto, mayor sera s dificultad.Ademas de esto los usuarios podran poner el nickname con el que desean reconocerse
    """
    global im4,lvl1,lvl2,lvl3,lvl4,lvl5,Nivel1,carro1,carro2,v3,v4,namep1,namep2
    v3.iconify()
    v4 = Toplevel()
    v4.title("Survival Rate")
    v4.geometry("1366x768")
    widget3 = Label(v4,image = im4).place(x= 0,y= 0)
    namep1 = StringVar()
    namep2 = StringVar()
    namep1.set("Player 1")
    namep2.set("Player 2")
    name1 = Entry(v4,textvariable = namep1 ,width = 50).place(x=630,y=312)
    name2 = Entry(v4,textvariable = namep2, width = 50).place(x=630,y=415)
    blvl1 = Button(v4,image= lvl1,command = nivel1,height = 35 , width = 110).place(x = 183, y = 550)
    blvl2 = Button(v4,image= lvl2,command = nivel2,height = 35 , width = 110).place(x = 383, y = 550)
    blvl3 = Button(v4,image= lvl3,command = nivel3,height = 35 , width = 110).place(x = 583, y = 550)
    blvl4 = Button(v4,image= lvl4,command = nivel4,height = 35 , width = 110).place(x = 783, y = 550)
    blvl5 = Button(v4,image= lvl5,command = nivel5,height = 35 , width = 110).place(x = 983, y = 550)
    bx2 = Button(v4,image=imx,command = salir4,height = 40, width =150).place(x=600, y = 650)

    
#===================================================================SALIR=======================================================================#   
def salir():
    """
cierra el menu pricipal, por lo tanto  la aplicacion seria cerrada
    """
    v.destroy()

def salir2 ():
    """
cierra la ventana de las instrucciones y vuelve al menu principal
    """
    v1.destroy()
    
def salir3():
    """
cierra la ventana de los controles  y vuelve al menu principal
    """
    v3.destroy()
    v.deiconify()
        
def salir4():
    """
cierra la vetana de opciones de juego y vuelve al menu principal
    """
    v4.destroy()
    v3.deiconify()
    
def salir5():
    """
cierra la ventana de seleccion de niveles y vuelve a la de opciones de juego
    """
    v2.destroy()

#===========================================================================================================================================================#
                                                        #NIVEL 1 #

def nivel1():
    """
En esta  funcion el nivel de dificultad del nivel es muy bajo, en este sentido, se importan las imgenes necesarias para hacer que el nivel funcione
y mediante un "while" se hace que el nivel se mueva, y asi mismo, todos los objetos que hay en este(enemigos),incluyendo al jugador, se usa la herramienta random
para poder poner de forma aleatoria el lugar donde apareceran los enemigos
    """
    global Nivel1,mitad,carro2,v4,v5,namep1,namep2,nivelone,carrete1,h,minivan,runer,gas,fihter,bomba,win,lose,mancha,iz
    v4.iconify()
    v5 = Toplevel()
    v5.title("Survival Rate")
    v5.geometry("1366x768")
    nivelone = Canvas(v5,height = 768 , width = 1366)
    nivelonee = nivelone.create_image(683,387, image = Nivel1)
    carrete1 = nivelone.create_image(300,642, image = carro1)
    nivelonnee = nivelone.create_image(681,386, image = mitad)
    carrete2 = nivelone.create_image(1020,642,image = carro2)
    jugadorOne = Label(nivelone,  text = namep1.get(),bg = "Black",fg = "White",font = neon).place(x = 640, y = 80)
    jugadorTwo = Label(nivelone,  text = namep2.get(),bg = "Black",fg = "White",font = neon).place(x = 640, y = 470)
    xi = random.randint(165,457)
    xi2 = random.randint(860,1178)
    xl = random.randint(165,457)
    xl2 = random.randint(860,1178)
    xg = random.randint(165,457)
    xg2 = random.randint(860,1178)
    xm = random.randint(165,457)
    xm2 = random.randint(860,1178)
    minivann = nivelone.create_image(xi,1,image = minivan)
    minivann2 = nivelone.create_image(xi2,1,image = minivan)
    runner = nivelone.create_image(xl,1,image = runer)
    runner2 = nivelone.create_image(xl2,1,image = runer)
    gasolina = nivelone.create_image(xg,1,image = gas)
    gasolinaa = nivelone.create_image(xg2,1,image = gas)
    fighter = nivelone.create_image(300,1,image = fihter)
    fighter2 = nivelone.create_image(1020,1,image = fihter)
    mancha1 = nivelone.create_image(xm,1,image = mancha)
    mancha2 = nivelone.create_image(xm2,1,image = mancha)
    
    
        
    def keyup(e):
        """
        """
        global h
        if(e.keycode in h):
            h.pop(h.index(e.keycode))

    def keydown(e):
        """
        """
        global h
        if(not e.keycode in h):
            h.append(e.keycode)

    
    def key():
        """
        """
        global h
        #Player1
        if(nivelone.coords(carrete1)[0] > 130):
            if(65 in h):
                nivelone.move(carrete1,-7,0)
        if(nivelone.coords(carrete1)[0] < 467):
            if(68 in h):
                nivelone.move(carrete1,7,0)
        #Player2
        if(nivelone.coords(carrete2)[0] > 855):        
            if(74 in h):
                nivelone.move(carrete2,-7,0)
        if(nivelone.coords(carrete2)[0] < 1187):
            if(76 in h):
                nivelone.move(carrete2,7,0)
        nivelone.after(15,key)
                
    nivelone.bind("<KeyPress>", keydown)
    nivelone.bind("<KeyRelease>",keyup)
    nivelone.focus_set()
    key()
    
    nivelone.pack()
    pOne = 600
    pTwo = 600
    scoreOne = 0
    scoreTwo = 0
    y = 10
    
    while(True):
        nivelone.move(nivelonee,0,y)
        #Puntaje de la gasolina
        gasolina1 = Label(nivelone,text = pOne,bg = "Black",fg = "white",font = bit).place(x = 635, y = 220)
        gasolina2 = Label(nivelone,text = pTwo,bg = "Black",fg = "white",font = bit).place(x = 635, y = 590)
        pOne = pOne - 1 
        pTwo = pTwo - 1
        #Score
        score1 = Label(nivelone,text = scoreOne,bg = "Black",fg = "white",font = bit).place(x = 635, y = 340)
        score2 = Label(nivelone,text = scoreTwo,bg = "Black",fg = "white",font = bit).place(x = 635, y = 700)
        scoreOne = scoreOne + 1
        scoreTwo = scoreTwo + 1
        #minivan
        if(nivelone.coords(minivann)[1] <= 740):
            nivelone.move(minivann,0,7)
            posx = nivelone.coords(minivann)[0]
            posy = nivelone.coords(minivann)[1]
            fx = nivelone.coords(carrete1)[0]
            fy = nivelone.coords(carrete1)[1]
            if( fx >= posx and fx <= posx + 42 and fy >= posy and fy <= posy + 94):
                nivelone.move(minivann,0,150)
                pOne = pOne - 15
                scoreOne = 0
                y = 5
                                               
            if( fx <= posx and fx + 42 >= posx  and fy <= posy and fy + 94 <= posy ):
                nivelone.move(minivann,0,150)
                pOne = pOne - 15
                scoreOne = 0
                y = 5
                                
            if( fx <= posx and fx >= posx - 42 and fy <= posy and fy >= posy - 94):
                nivelone.move(minivann,0,150)
                pOne = pOne - 15
                scoreOne = 0
                y = 5
                           
            if( fx >= posx and fx + 42 <= posx  and fy >= posy and fy + 94 >= posy ):
                nivelone.move(minivann,0,150)
                pOne = pOne - 15
                scoreOne = 0
                y = 5

            else:
                y = 10
                           

                  
        if(nivelone.coords(minivann)[1] > 740):
            nivelone.delete(minivann)
            xi = random.randint(165,457)
            minivann = nivelone.create_image(xi,1,image = minivan)
            
        #minivan2
        if(nivelone.coords(minivann2)[1] <= 740):
            nivelone.move(minivann2,0,7)
            posxx = nivelone.coords(minivann2)[0]
            posyy = nivelone.coords(minivann2)[1]
            fxx = nivelone.coords(carrete2)[0]
            fyy = nivelone.coords(carrete2)[1]
            if( fxx >= posxx and fxx <= posxx + 42 and fyy >= posyy and fyy <= posyy + 94):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
                                
            if( fxx <= posxx and fxx + 42 >= posxx  and fyy <= posyy and fyy + 94 <= posyy ):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
                
            if( fxx <= posxx and fxx >= posxx - 42 and fyy <= posyy and fyy >= posyy - 94):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
                                
            if( fxx >= posxx and fxx + 42 <= posxx  and fyy >= posyy and fyy + 94 >= posyy ):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5

            else:
                y = 10
                       
                        
        if(nivelone.coords(minivann2)[1] > 740):
            nivelone.delete(minivann2)
            xi2 = random.randint(860,1178)
            minivann2 = nivelone.create_image(xi2,1,image = minivan)
        #runner
        if(nivelone.coords(runner)[1] <= 740):
            if(nivelone.coords(runner)[0] <= 467 and nivelone.coords(runner)[0] >= 155):
                z = random.randint(-9,9)
                c = random.randint(1,6)
                nivelone.move(runner,z,c)
            if(nivelone.coords(runner)[0] > 467):
                z = random.randint(-9,0)
                c = random.randint(1,6)
                nivelone.move(runner,z,c)
            if(nivelone.coords(runner)[0] < 155):
                z = random.randint(0,9)
                c = random.randint(1,6)
                nivelone.move(runner,z,c)
            posxr = nivelone.coords(runner)[0]
            posyr = nivelone.coords(runner)[1]
            fxr = nivelone.coords(carrete1)[0]
            fyr = nivelone.coords(carrete1)[1]
            if( fxr >= posxr and fxr <= posxr + 45 and fyr >= posyr and fyr <= posyr + 82):
                nivelone.move(runner,0,150)
                scoreOne = 0
                pOne = pOne - 15
                y = 5                
            if( fxr <= posxr and fxr + 45 >= posxr  and fyr <= posyr and fyr + 82 <= posyr ):
                nivelone.move(runner,0,150)
                scoreOne = 0
                pOne = pOne - 15
                y = 5
            if( fxr <= posxr and fxr >= posxr - 45 and fyr <= posyr and fyr >= posyr - 82):
                nivelone.move(runner,0,150)
                scoreOne = 0
                pOne = pOne - 15
                y = 5                
            if( fxr >= posxr and fxr + 45 <= posxr  and fyr >= posyr and fyr + 82 >= posyr ):
                nivelone.move(runner,0,150)
                scoreOne = 0
                pOne = pOne - 15
                y = 5           

        if(nivelone.coords(runner)[1] >= 740):
            nivelone.delete(runner)
            xl = random.randint(165,457)
            runner = nivelone.create_image(xl,1,image = runer)
        #runner2
        if(nivelone.coords(runner2)[1] <= 740):
            if(nivelone.coords(runner2)[0] <= 1187 and nivelone.coords(runner2)[0] >= 855):
                z2 = random.randint(-9,9)
                c2 = random.randint(1,6)
                nivelone.move(runner2,z2,c2)
            if(nivelone.coords(runner2)[0] > 1187):
                z2 = random.randint(-9,0)
                c2 = random.randint(1,6)
                nivelone.move(runner2,z2,c2)
            if(nivelone.coords(runner2)[0] < 855):
                z2 = random.randint(0,9)
                c2 = random.randint(1,6)
                nivelone.move(runner2,z2,c2)
            posxrr = nivelone.coords(runner2)[0]
            posyrr = nivelone.coords(runner2)[1]
            fxrr = nivelone.coords(carrete2)[0]
            fyrr = nivelone.coords(carrete2)[1]
            if( fxrr >= posxrr and fxrr <= posxrr + 45 and fyrr >= posyrr and fyrr <= posyrr + 82):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5               
            if( fxrr <= posxrr and fxrr + 45 >= posxrr  and fyrr <= posyrr and fyrr + 82 <= posyrr ):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
            if( fxrr <= posxrr and fxrr >= posxrr - 45 and fyrr <= posyrr and fyrr >= posyrr - 82):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5                
            if( fxrr >= posxrr and fxrr + 45 <= posxrr  and fyrr >= posyrr and fyrr + 82 >= posyrr ):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
        if(nivelone.coords(runner2)[1] >= 740):
            nivelone.delete(runner2)
            xl2 = random.randint(860,1178)
            runner2 = nivelone.create_image(xl2,1,image = runer)


        #fighter
        if(nivelone.coords(fighter)[1] <= 1400):
            if(nivelone.coords(fighter)[0] < nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,3,4)
            if(nivelone.coords(fighter)[0] > nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,-3,4)
            if(nivelone.coords(fighter)[0] == nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,0,4)
            posxf = nivelone.coords(fighter)[0]
            posyf = nivelone.coords(fighter)[1]
            fxf = nivelone.coords(carrete1)[0]
            fyf = nivelone.coords(carrete1)[1]
            if( fxf >= posxf and fxf <= posxf + 45 and fyf >= posyf and fyf <= posyf + 82):
                nivelone.move(fighter,0,150)
                pOne = pOne - 15
                scoreOne = 0
                y = 5                 
            if( fxf <= posxf and fxf + 45 >= posxf  and fyf <= posyf and fyf + 82 <= posyf ):
                nivelone.move(fighter,0,150)
                scoreOne = 0
                pOne = pOne - 15
                y = 5 
            if( fxf <= posxf and fxf >= posxf - 45 and fyf <= posyf and fyf >= posyf - 82):
                nivelone.move(fighter,0,150)
                scoreOne = 0
                pOne = pOne - 15
                y = 5                 
            if( fxf >= posxf and fxf + 45 <= posxf  and fyf >= posyf and fyf + 82 >= posyf ):
                nivelone.move(fighter,0,150)
                scoreOne = 0
                pOne = pOne - 15
                y = 5 
        if(nivelone.coords(fighter)[1] > 1400):
            nivelone.delete(fighter)
            xf = random.randint(165,457)
            fighter = nivelone.create_image(xf,1,image = fihter)

        #fighter2
        if(nivelone.coords(fighter2)[1] <= 1400):
            if(nivelone.coords(fighter2)[0] < nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,3,4)
            if(nivelone.coords(fighter2)[0] > nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,-3,4)
            if(nivelone.coords(fighter2)[0] == nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,0,4)
            posxff = nivelone.coords(fighter2)[0]
            posyff = nivelone.coords(fighter2)[1]
            fxff = nivelone.coords(carrete2)[0]
            fyff = nivelone.coords(carrete2)[1]
            if( fxff >= posxff and fxff <= posxff + 45 and fyff >= posyff and fyff <= posyff + 82):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5               
            if( fxff <= posxff and fxff + 45 >= posxff  and fyff <= posyff and fyff + 82 <= posyff ):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
            if( fxff <= posxff and fxff >= posxff - 45 and fyff <= posyff and fyff >= posyff - 82):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5                
            if( fxff >= posxff and fxff + 45 <= posxff  and fyff >= posyff and fyff + 82 >= posyff ):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
        if(nivelone.coords(fighter2)[1] > 1400):
            nivelone.delete(fighter2)
            xf2 = random.randint(860,1178)
            fighter2 = nivelone.create_image(xf2,1,image = fihter)

        #gasolina2
        if(nivelone.coords(gasolinaa)[1] <= 2400):
            nivelone.move(gasolinaa,0,7)
            posxgg = nivelone.coords(gasolinaa)[0]
            posygg = nivelone.coords(gasolinaa)[1]
            fxgg = nivelone.coords(carrete2)[0]
            fygg = nivelone.coords(carrete2)[1]
            if( fxgg >= posxgg and fxgg <= posxgg + 34 and fygg >= posygg and fygg <= posygg + 58):
                nivelone.move(gasolinaa,0,200)
                pTwo = pTwo + 250
                                 
               
            if( fxgg <= posxgg and fxgg >= posxgg - 34 and fygg <= posygg and fygg >= posygg - 58):
                nivelone.move(gasolinaa,0,200)
                pTwo = pTwo + 250
                                 
             
            
        if(nivelone.coords(gasolinaa)[1] > 2400):
            nivelone.delete(gasolinaa)
            xg2 = random.randint(860,1178)
            gasolinaa = nivelone.create_image(xg2,1,image = gas)
   
        #gasolina
        if(nivelone.coords(gasolina)[1] <= 2400):
            nivelone.move(gasolina,0,7)
            posxg = nivelone.coords(gasolina)[0]
            posyg = nivelone.coords(gasolina)[1]
            fxg = nivelone.coords(carrete1)[0]
            fyg = nivelone.coords(carrete1)[1]
            if( fxg >= posxg and fxg <= posxg + 34 and fyg >= posyg and fyg <= posyg + 58):
                nivelone.move(gasolina,0,200)
                pOne = pOne + 250
                                 

                 
            if( fxg <= posxg and fxg >= posxg - 34 and fyg <= posyg and fyg >= posyg - 58):
                nivelone.move(gasolina,0,200)
                pOne = pOne + 250
                                 
               
        if(nivelone.coords(gasolina)[1] > 2400):
            nivelone.delete(gasolina)
            xg = random.randint(165,457)
            gasolina = nivelone.create_image(xg,1,image = gas)

        #mancha1
        if(nivelone.coords(mancha1)[1] <= 900):
            nivelone.move(mancha1,0,7)
            posxm = nivelone.coords(mancha1)[0]
            posym = nivelone.coords(mancha1)[1]
            fxm = nivelone.coords(carrete1)[0]
            fym = nivelone.coords(carrete1)[1]
            if( fxm >= posxm and fxm <= posxm + 42 and fym >= posym and fym <= posym + 94):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,17,0)
                One = pOne - 15
                scoreOne = 0
                y = 2
                                               
            if( fxm <= posxm and fxm + 42 >= posxm  and fym <= posym and fym + 94 <= posym ):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,17,0)
                pOne = pOne - 15
                scoreOne = 0
                y = 2
                                
            if( fxm <= posxm and fxm >= posxm - 42 and fym <= posym and fym >= posym - 94):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,17,0)
                pOne = pOne - 15
                scoreOne = 0
                y = 2
                           
            if( fxm >= posxm and fxm + 42 <= posxm  and fym >= posym and fym + 94 >= posym ):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,17,0)
                pOne = pOne - 15
                scoreOne = 0
                y = 2

            else:
                y = 10
        if(nivelone.coords(mancha1)[1] > 900):
            nivelone.delete(mancha1)
            xm1 = random.randint(165,457)
            mancha1 = nivelone.create_image(xm1,1,image = mancha)
        #mancha2
        if(nivelone.coords(mancha2)[1] <= 900):
            nivelone.move(mancha2,0,7)
            posxmm = nivelone.coords(mancha2)[0]
            posymm = nivelone.coords(mancha2)[1]
            fxmm = nivelone.coords(carrete2)[0]
            fymm = nivelone.coords(carrete2)[1]
            if( fxmm >= posxmm  and fxm <= posxmm + 42 and fym >= posymm and fymm <= posymm + 94):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,17,0)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 2
                                               
            if( fxmm <= posxmm and fxmm + 42 >= posxmm  and fymm <= posymm and fymm + 94 <= posymm ):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,17,0)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 2
                                
            if( fxmm <= posxmm and fxmm >= posxmm - 42 and fymm <= posymm and fymm >= posymm - 94):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,17,0)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 2
                           
            if( fxmm >= posxmm and fxmm + 42 <= posxmm  and fymm >= posymm and fymm + 94 >= posymm ):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,17,0)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 2

            else:
                y = 10
        if(nivelone.coords(mancha2)[1] > 900):
            nivelone.delete(mancha2)
            xm2 = random.randint(860,1178)
            mancha2 = nivelone.create_image(xm2,1,image = mancha)
        
        

        #Limites
        if(pTwo <= 0 ):
            win2 = nivelone.create_image(300,350,image = win)
            lose2 = nivelone.create_image(1020,350,image = lose)
            break
        if(pOne <= 0):
            win2 = nivelone.create_image(1020,350,image = win)
            lose2 = nivelone.create_image(300,350,image = lose)
            break
            
        if(nivelone.coords(nivelonee)[1] >28000):
            xs = pTwo * 10
            xd = pOne * 10
            scoreOne = scoreOne + xd
            scoreTwo = scoreTwo + xs
            
            if(scoreOne > scoreTwo):
                win1 = nivelone.create_image(300,350,image = win)
                lose1 = nivelone.create_image(1020,350,image = lose)
                break
            
            if(scoreOne < scoreTwo):
                win2 = nivelone.create_image(1020,350,image = win)
                lose2 = nivelone.create_image(300,350,image = lose)
                break
                  
            
            
            
        v5.update()
        time.sleep(0.03)
#===========================================================================================================================================================#
                                                        #NIVEL 2 #
        
def nivel2():
    """
En esta  funcion el nivel de dificultad del nivel es  bajo, en este sentido, se importan las imgenes necesarias para hacer que el nivel funcione
y mediante un "while" se hace que el nivel se mueva, y asi mismo, todos los objetos que hay en este(enemigos),incluyendo al jugador, se usa la herramienta random
para poder poner de forma aleatoria el lugar donde apareceran los enemigos
    """
    global Nivel2,mitad,carro2,v4,v5,namep1,namep2,nivelone,carrete1,h,minivan,runer,gas,fihter,bomba,win,lose,mancha,iz
    v4.iconify()
    v5 = Toplevel()
    v5.title("Survival Rate")
    v5.geometry("1366x768")
    nivelone = Canvas(v5,height = 768 , width = 1366)
    nivelonee = nivelone.create_image(683,387, image = Nivel2)
    carrete1 = nivelone.create_image(300,642, image = carro1)
    nivelonnee = nivelone.create_image(681,386, image = mitad)
    carrete2 = nivelone.create_image(1020,642,image = carro2)
    jugadorOne = Label(nivelone,  text = namep1.get(),bg = "Black",fg = "White",font = neon).place(x = 640, y = 80)
    jugadorTwo = Label(nivelone,  text = namep2.get(),bg = "Black",fg = "White",font = neon).place(x = 640, y = 470)
    xi = random.randint(165,457)
    xi2 = random.randint(860,1178)
    xl = random.randint(165,457)
    xl2 = random.randint(860,1178)
    xg = random.randint(165,457)
    xg2 = random.randint(860,1178)
    xm = random.randint(165,457)
    xm2 = random.randint(860,1178)
    minivann = nivelone.create_image(xi,1,image = minivan)
    minivann2 = nivelone.create_image(xi2,1,image = minivan)
    runner = nivelone.create_image(xl,1,image = runer)
    runner2 = nivelone.create_image(xl2,1,image = runer)
    gasolina = nivelone.create_image(xg,1,image = gas)
    gasolinaa = nivelone.create_image(xg2,1,image = gas)
    fighter = nivelone.create_image(300,1,image = fihter)
    fighter2 = nivelone.create_image(1020,1,image = fihter)
    mancha1 = nivelone.create_image(xm,1,image = mancha)
    mancha2 = nivelone.create_image(xm2,1,image = mancha)
    
    
        
    def keyup(e):
        """
        """
        global h
        if(e.keycode in h):
            h.pop(h.index(e.keycode))

    def keydown(e):
        """
        """
        global h
        if(not e.keycode in h):
            h.append(e.keycode)

    
    def key():
        """
        """
        global h
        #Player1
        if(nivelone.coords(carrete1)[0] > 130):
            if(65 in h):
                nivelone.move(carrete1,-7,0)
        if(nivelone.coords(carrete1)[0] < 467):
            if(68 in h):
                nivelone.move(carrete1,7,0)
        #Player2
        if(nivelone.coords(carrete2)[0] > 855):        
            if(74 in h):
                nivelone.move(carrete2,-7,0)
        if(nivelone.coords(carrete2)[0] < 1187):
            if(76 in h):
                nivelone.move(carrete2,7,0)
        nivelone.after(15,key)
                
    nivelone.bind("<KeyPress>", keydown)
    nivelone.bind("<KeyRelease>",keyup)
    nivelone.focus_set()
    key()
    
    nivelone.pack()
    pOne = 600
    pTwo = 600
    scoreOne = 0
    scoreTwo = 0
    y = 10
    
    while(True):
        nivelone.move(nivelonee,0,y)
        #Puntaje de la gasolina
        gasolina1 = Label(nivelone,text = pOne,bg = "Black",fg = "white",font = bit).place(x = 635, y = 220)
        gasolina2 = Label(nivelone,text = pTwo,bg = "Black",fg = "white",font = bit).place(x = 635, y = 590)
        pOne = pOne - 1 
        pTwo = pTwo - 1
        #Score
        score1 = Label(nivelone,text = scoreOne,bg = "Black",fg = "white",font = bit).place(x = 635, y = 340)
        score2 = Label(nivelone,text = scoreTwo,bg = "Black",fg = "white",font = bit).place(x = 635, y = 700)
        scoreOne = scoreOne + 1
        scoreTwo = scoreTwo + 1
        #minivan
        if(nivelone.coords(minivann)[1] <= 740):
            nivelone.move(minivann,0,8)
            posx = nivelone.coords(minivann)[0]
            posy = nivelone.coords(minivann)[1]
            fx = nivelone.coords(carrete1)[0]
            fy = nivelone.coords(carrete1)[1]
            if( fx >= posx and fx <= posx + 42 and fy >= posy and fy <= posy + 94):
                nivelone.move(minivann,0,150)
                pOne = pOne - 15
                scoreOne = 0
                y = 5
                                               
            if( fx <= posx and fx + 42 >= posx  and fy <= posy and fy + 94 <= posy ):
                nivelone.move(minivann,0,150)
                pOne = pOne - 15
                scoreOne = 0
                y = 5
                                
            if( fx <= posx and fx >= posx - 42 and fy <= posy and fy >= posy - 94):
                nivelone.move(minivann,0,150)
                pOne = pOne - 15
                scoreOne = 0
                y = 5
                           
            if( fx >= posx and fx + 42 <= posx  and fy >= posy and fy + 94 >= posy ):
                nivelone.move(minivann,0,150)
                pOne = pOne - 15
                scoreOne = 0
                y = 5

            else:
                y = 10
                           

                  
        if(nivelone.coords(minivann)[1] > 740):
            nivelone.delete(minivann)
            xi = random.randint(165,457)
            minivann = nivelone.create_image(xi,1,image = minivan)
            
        #minivan2
        if(nivelone.coords(minivann2)[1] <= 740):
            nivelone.move(minivann2,0,8)
            posxx = nivelone.coords(minivann2)[0]
            posyy = nivelone.coords(minivann2)[1]
            fxx = nivelone.coords(carrete2)[0]
            fyy = nivelone.coords(carrete2)[1]
            if( fxx >= posxx and fxx <= posxx + 42 and fyy >= posyy and fyy <= posyy + 94):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
                                
            if( fxx <= posxx and fxx + 42 >= posxx  and fyy <= posyy and fyy + 94 <= posyy ):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
                
            if( fxx <= posxx and fxx >= posxx - 42 and fyy <= posyy and fyy >= posyy - 94):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
                                
            if( fxx >= posxx and fxx + 42 <= posxx  and fyy >= posyy and fyy + 94 >= posyy ):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5

            else:
                y = 10
                       
                        
        if(nivelone.coords(minivann2)[1] > 740):
            nivelone.delete(minivann2)
            xi2 = random.randint(860,1178)
            minivann2 = nivelone.create_image(xi2,1,image = minivan)
        #runner
        if(nivelone.coords(runner)[1] <= 740):
            if(nivelone.coords(runner)[0] <= 467 and nivelone.coords(runner)[0] >= 155):
                z = random.randint(-10,10)
                c = random.randint(1,7)
                nivelone.move(runner,z,c)
            if(nivelone.coords(runner)[0] > 467):
                z = random.randint(-10,0)
                c = random.randint(1,7)
                nivelone.move(runner,z,c)
            if(nivelone.coords(runner)[0] < 155):
                z = random.randint(0,10)
                c = random.randint(1,7)
                nivelone.move(runner,z,c)
            posxr = nivelone.coords(runner)[0]
            posyr = nivelone.coords(runner)[1]
            fxr = nivelone.coords(carrete1)[0]
            fyr = nivelone.coords(carrete1)[1]
            if( fxr >= posxr and fxr <= posxr + 45 and fyr >= posyr and fyr <= posyr + 82):
                nivelone.move(runner,0,150)
                scoreOne = 0
                pOne = pOne - 15
                y = 5                
            if( fxr <= posxr and fxr + 45 >= posxr  and fyr <= posyr and fyr + 82 <= posyr ):
                nivelone.move(runner,0,150)
                scoreOne = 0
                pOne = pOne - 15
                y = 5
            if( fxr <= posxr and fxr >= posxr - 45 and fyr <= posyr and fyr >= posyr - 82):
                nivelone.move(runner,0,150)
                scoreOne = 0
                pOne = pOne - 15
                y = 5                
            if( fxr >= posxr and fxr + 45 <= posxr  and fyr >= posyr and fyr + 82 >= posyr ):
                nivelone.move(runner,0,150)
                scoreOne = 0
                pOne = pOne - 15
                y = 5           

        if(nivelone.coords(runner)[1] >= 740):
            nivelone.delete(runner)
            xl = random.randint(165,457)
            runner = nivelone.create_image(xl,1,image = runer)
        #runner2
        if(nivelone.coords(runner2)[1] <= 740):
            if(nivelone.coords(runner2)[0] <= 1187 and nivelone.coords(runner2)[0] >= 855):
                z2 = random.randint(-10,10)
                c2 = random.randint(1,7)
                nivelone.move(runner2,z2,c2)
            if(nivelone.coords(runner2)[0] > 1187):
                z2 = random.randint(-10,0)
                c2 = random.randint(1,7)
                nivelone.move(runner2,z2,c2)
            if(nivelone.coords(runner2)[0] < 855):
                z2 = random.randint(0,10)
                c2 = random.randint(1,7)
                nivelone.move(runner2,z2,c2)
            posxrr = nivelone.coords(runner2)[0]
            posyrr = nivelone.coords(runner2)[1]
            fxrr = nivelone.coords(carrete2)[0]
            fyrr = nivelone.coords(carrete2)[1]
            if( fxrr >= posxrr and fxrr <= posxrr + 45 and fyrr >= posyrr and fyrr <= posyrr + 82):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5               
            if( fxrr <= posxrr and fxrr + 45 >= posxrr  and fyrr <= posyrr and fyrr + 82 <= posyrr ):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
            if( fxrr <= posxrr and fxrr >= posxrr - 45 and fyrr <= posyrr and fyrr >= posyrr - 82):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5                
            if( fxrr >= posxrr and fxrr + 45 <= posxrr  and fyrr >= posyrr and fyrr + 82 >= posyrr ):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
        if(nivelone.coords(runner2)[1] >= 740):
            nivelone.delete(runner2)
            xl2 = random.randint(860,1178)
            runner2 = nivelone.create_image(xl2,1,image = runer)


        #fighter
        if(nivelone.coords(fighter)[1] <= 1400):
            if(nivelone.coords(fighter)[0] < nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,4,4)
            if(nivelone.coords(fighter)[0] > nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,-4,4)
            if(nivelone.coords(fighter)[0] == nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,0,4)
            posxf = nivelone.coords(fighter)[0]
            posyf = nivelone.coords(fighter)[1]
            fxf = nivelone.coords(carrete1)[0]
            fyf = nivelone.coords(carrete1)[1]
            if( fxf >= posxf and fxf <= posxf + 45 and fyf >= posyf and fyf <= posyf + 82):
                nivelone.move(fighter,0,150)
                pOne = pOne - 15
                scoreOne = 0
                y = 5                 
            if( fxf <= posxf and fxf + 45 >= posxf  and fyf <= posyf and fyf + 82 <= posyf ):
                nivelone.move(fighter,0,150)
                scoreOne = 0
                pOne = pOne - 15
                y = 5 
            if( fxf <= posxf and fxf >= posxf - 45 and fyf <= posyf and fyf >= posyf - 82):
                nivelone.move(fighter,0,150)
                scoreOne = 0
                pOne = pOne - 15
                y = 5                 
            if( fxf >= posxf and fxf + 45 <= posxf  and fyf >= posyf and fyf + 82 >= posyf ):
                nivelone.move(fighter,0,150)
                scoreOne = 0
                pOne = pOne - 15
                y = 5 
        if(nivelone.coords(fighter)[1] > 1400):
            nivelone.delete(fighter)
            xf = random.randint(165,457)
            fighter = nivelone.create_image(xf,1,image = fihter)

        #fighter2
        if(nivelone.coords(fighter2)[1] <= 1400):
            if(nivelone.coords(fighter2)[0] < nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,4,4)
            if(nivelone.coords(fighter2)[0] > nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,-4,4)
            if(nivelone.coords(fighter2)[0] == nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,0,4)
            posxff = nivelone.coords(fighter2)[0]
            posyff = nivelone.coords(fighter2)[1]
            fxff = nivelone.coords(carrete2)[0]
            fyff = nivelone.coords(carrete2)[1]
            if( fxff >= posxff and fxff <= posxff + 45 and fyff >= posyff and fyff <= posyff + 82):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5               
            if( fxff <= posxff and fxff + 45 >= posxff  and fyff <= posyff and fyff + 82 <= posyff ):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
            if( fxff <= posxff and fxff >= posxff - 45 and fyff <= posyff and fyff >= posyff - 82):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5                
            if( fxff >= posxff and fxff + 45 <= posxff  and fyff >= posyff and fyff + 82 >= posyff ):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
        if(nivelone.coords(fighter2)[1] > 1400):
            nivelone.delete(fighter2)
            xf2 = random.randint(860,1178)
            fighter2 = nivelone.create_image(xf2,1,image = fihter)

        #gasolina2
        if(nivelone.coords(gasolinaa)[1] <= 2400):
            nivelone.move(gasolinaa,0,7)
            posxgg = nivelone.coords(gasolinaa)[0]
            posygg = nivelone.coords(gasolinaa)[1]
            fxgg = nivelone.coords(carrete2)[0]
            fygg = nivelone.coords(carrete2)[1]
            if( fxgg >= posxgg and fxgg <= posxgg + 34 and fygg >= posygg and fygg <= posygg + 58):
                nivelone.move(gasolinaa,0,200)
                pTwo = pTwo + 250
                                 
               
            if( fxgg <= posxgg and fxgg >= posxgg - 34 and fygg <= posygg and fygg >= posygg - 58):
                nivelone.move(gasolinaa,0,200)
                pTwo = pTwo + 250
                                 
             
            
        if(nivelone.coords(gasolinaa)[1] > 2400):
            nivelone.delete(gasolinaa)
            xg2 = random.randint(860,1178)
            gasolinaa = nivelone.create_image(xg2,1,image = gas)
   
        #gasolina
        if(nivelone.coords(gasolina)[1] <= 2400):
            nivelone.move(gasolina,0,7)
            posxg = nivelone.coords(gasolina)[0]
            posyg = nivelone.coords(gasolina)[1]
            fxg = nivelone.coords(carrete1)[0]
            fyg = nivelone.coords(carrete1)[1]
            if( fxg >= posxg and fxg <= posxg + 34 and fyg >= posyg and fyg <= posyg + 58):
                nivelone.move(gasolina,0,200)
                pOne = pOne + 250
                                 

                 
            if( fxg <= posxg and fxg >= posxg - 34 and fyg <= posyg and fyg >= posyg - 58):
                nivelone.move(gasolina,0,200)
                pOne = pOne + 250
                                 
               
        if(nivelone.coords(gasolina)[1] > 2400):
            nivelone.delete(gasolina)
            xg = random.randint(165,457)
            gasolina = nivelone.create_image(xg,1,image = gas)

        #mancha1
        if(nivelone.coords(mancha1)[1] <= 900):
            nivelone.move(mancha1,0,8)
            posxm = nivelone.coords(mancha1)[0]
            posym = nivelone.coords(mancha1)[1]
            fxm = nivelone.coords(carrete1)[0]
            fym = nivelone.coords(carrete1)[1]
            if( fxm >= posxm and fxm <= posxm + 42 and fym >= posym and fym <= posym + 94):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,19,0)
                One = pOne - 15
                y = 2
                                               
            if( fxm <= posxm and fxm + 42 >= posxm  and fym <= posym and fym + 94 <= posym ):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,19,0)
                pOne = pOne - 15
                scoreOne = 0
                y = 2
                                
            if( fxm <= posxm and fxm >= posxm - 42 and fym <= posym and fym >= posym - 94):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,19,0)
                scoreOne = 0
                pOne = pOne - 15
                y = 2
                           
            if( fxm >= posxm and fxm + 42 <= posxm  and fym >= posym and fym + 94 >= posym ):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,19,0)
                scoreOne = 0
                pOne = pOne - 15
                y = 2

            else:
                y = 10
        if(nivelone.coords(mancha1)[1] > 900):
            nivelone.delete(mancha1)
            xm1 = random.randint(165,457)
            mancha1 = nivelone.create_image(xm1,1,image = mancha)
        #mancha2
        if(nivelone.coords(mancha2)[1] <= 900):
            nivelone.move(mancha2,0,8)
            posxmm = nivelone.coords(mancha2)[0]
            posymm = nivelone.coords(mancha2)[1]
            fxmm = nivelone.coords(carrete2)[0]
            fymm = nivelone.coords(carrete2)[1]
            if( fxmm >= posxmm  and fxm <= posxmm + 42 and fym >= posymm and fymm <= posymm + 94):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,19,0)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 2
                                               
            if( fxmm <= posxmm and fxmm + 42 >= posxmm  and fymm <= posymm and fymm + 94 <= posymm ):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,19,0)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 2
                                
            if( fxmm <= posxmm and fxmm >= posxmm - 42 and fymm <= posymm and fymm >= posymm - 94):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,19,0)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 2
                           
            if( fxmm >= posxmm and fxmm + 42 <= posxmm  and fymm >= posymm and fymm + 94 >= posymm ):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,19,0)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 2

            else:
                y = 10
        if(nivelone.coords(mancha2)[1] > 900):
            nivelone.delete(mancha2)
            xm2 = random.randint(860,1178)
            mancha2 = nivelone.create_image(xm2,1,image = mancha)
        
        

        #Limites
        if(pTwo <= 0 ):
            win2 = nivelone.create_image(300,350,image = win)
            lose2 = nivelone.create_image(1020,350,image = lose)
            break
        if(pOne <= 0):
            win2 = nivelone.create_image(1020,350,image = win)
            lose2 = nivelone.create_image(300,350,image = lose)
            break
            
        if(nivelone.coords(nivelonee)[1] >28000):
            xs = pTwo * 10
            xd = pOne * 10
            scoreOne = scoreOne + xd
            scoreTwo = scoreTwo + xs
            
            if(scoreOne > scoreTwo):
                win1 = nivelone.create_image(300,350,image = win)
                lose1 = nivelone.create_image(1020,350,image = lose)
                break
            
            if(scoreOne < scoreTwo):
                win2 = nivelone.create_image(1020,350,image = win)
                lose2 = nivelone.create_image(300,350,image = lose)
                break
            
            
            
        v5.update()
        time.sleep(0.03)
#===========================================================================================================================================================#
                                                        #NIVEL 3 #

def nivel3():
    """
En esta  funcion el nivel de dificultad del nivel es medio, en este sentido, se importan las imgenes necesarias para hacer que el nivel funcione
y mediante un "while" se hace que el nivel se mueva, y asi mismo, todos los objetos que hay en este(enemigos),incluyendo al jugador, se usa la herramienta random
para poder poner de forma aleatoria el lugar donde apareceran los enemigos
    """
    global Nivel3,mitad,carro2,v4,v5,namep1,namep2,nivelone,carrete1,h,minivan,runer,gas,fihter,bomba,win,lose,mancha,iz
    v4.iconify()
    v5 = Toplevel()
    v5.title("Survival Rate")
    v5.geometry("1366x768")
    nivelone = Canvas(v5,height = 768 , width = 1366)
    nivelonee = nivelone.create_image(683,387, image = Nivel3)
    carrete1 = nivelone.create_image(300,642, image = carro1)
    nivelonnee = nivelone.create_image(681,386, image = mitad)
    carrete2 = nivelone.create_image(1020,642,image = carro2)
    jugadorOne = Label(nivelone,  text = namep1.get(),bg = "Black",fg = "White",font = neon).place(x = 640, y = 80)
    jugadorTwo = Label(nivelone,  text = namep2.get(),bg = "Black",fg = "White",font = neon).place(x = 640, y = 470)
    xi = random.randint(165,457)
    xi2 = random.randint(860,1178)
    xl = random.randint(165,457)
    xl2 = random.randint(860,1178)
    xg = random.randint(165,457)
    xg2 = random.randint(860,1178)
    xm = random.randint(165,457)
    xm2 = random.randint(860,1178)
    minivann = nivelone.create_image(xi,1,image = minivan)
    minivann2 = nivelone.create_image(xi2,1,image = minivan)
    runner = nivelone.create_image(xl,1,image = runer)
    runner2 = nivelone.create_image(xl2,1,image = runer)
    gasolina = nivelone.create_image(xg,1,image = gas)
    gasolinaa = nivelone.create_image(xg2,1,image = gas)
    fighter = nivelone.create_image(300,1,image = fihter)
    fighter2 = nivelone.create_image(1020,1,image = fihter)
    mancha1 = nivelone.create_image(xm,1,image = mancha)
    mancha2 = nivelone.create_image(xm2,1,image = mancha)
    
    
        
    def keyup(e):
        """
        """
        global h
        if(e.keycode in h):
            h.pop(h.index(e.keycode))

    def keydown(e):
        """
        """
        global h
        if(not e.keycode in h):
            h.append(e.keycode)

    
    def key():
        """
        """
        global h
        #Player1
        if(nivelone.coords(carrete1)[0] > 130):
            if(65 in h):
                nivelone.move(carrete1,-7,0)
        if(nivelone.coords(carrete1)[0] < 467):
            if(68 in h):
                nivelone.move(carrete1,7,0)
        #Player2
        if(nivelone.coords(carrete2)[0] > 855):        
            if(74 in h):
                nivelone.move(carrete2,-7,0)
        if(nivelone.coords(carrete2)[0] < 1187):
            if(76 in h):
                nivelone.move(carrete2,7,0)
        nivelone.after(15,key)
                
    nivelone.bind("<KeyPress>", keydown)
    nivelone.bind("<KeyRelease>",keyup)
    nivelone.focus_set()
    key()
    
    nivelone.pack()
    pOne = 600
    pTwo = 600
    scoreOne = 0
    scoreTwo = 0
    y = 10
    
    while(True):
        nivelone.move(nivelonee,0,y)
        #Puntaje de la gasolina
        gasolina1 = Label(nivelone,text = pOne,bg = "Black",fg = "white",font = bit).place(x = 635, y = 220)
        gasolina2 = Label(nivelone,text = pTwo,bg = "Black",fg = "white",font = bit).place(x = 635, y = 590)
        pOne = pOne - 1 
        pTwo = pTwo - 1
        #Score
        score1 = Label(nivelone,text = scoreOne,bg = "Black",fg = "white",font = bit).place(x = 635, y = 340)
        score2 = Label(nivelone,text = scoreTwo,bg = "Black",fg = "white",font = bit).place(x = 635, y = 700)
        scoreOne = scoreOne + 1
        scoreTwo = scoreTwo + 1
        #minivan
        if(nivelone.coords(minivann)[1] <= 740):
            nivelone.move(minivann,0,8)
            posx = nivelone.coords(minivann)[0]
            posy = nivelone.coords(minivann)[1]
            fx = nivelone.coords(carrete1)[0]
            fy = nivelone.coords(carrete1)[1]
            if( fx >= posx and fx <= posx + 42 and fy >= posy and fy <= posy + 94):
                nivelone.move(minivann,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5
                                               
            if( fx <= posx and fx + 42 >= posx  and fy <= posy and fy + 94 <= posy ):
                nivelone.move(minivann,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5
                                
            if( fx <= posx and fx >= posx - 42 and fy <= posy and fy >= posy - 94):
                nivelone.move(minivann,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5
                           
            if( fx >= posx and fx + 42 <= posx  and fy >= posy and fy + 94 >= posy ):
                nivelone.move(minivann,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5

            else:
                y = 10
                           

                  
        if(nivelone.coords(minivann)[1] > 740):
            nivelone.delete(minivann)
            xi = random.randint(165,457)
            minivann = nivelone.create_image(xi,1,image = minivan)
            
        #minivan2
        if(nivelone.coords(minivann2)[1] <= 740):
            nivelone.move(minivann2,0,8)
            posxx = nivelone.coords(minivann2)[0]
            posyy = nivelone.coords(minivann2)[1]
            fxx = nivelone.coords(carrete2)[0]
            fyy = nivelone.coords(carrete2)[1]
            if( fxx >= posxx and fxx <= posxx + 42 and fyy >= posyy and fyy <= posyy + 94):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5
                                
            if( fxx <= posxx and fxx + 42 >= posxx  and fyy <= posyy and fyy + 94 <= posyy ):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5
                
            if( fxx <= posxx and fxx >= posxx - 42 and fyy <= posyy and fyy >= posyy - 94):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5
                                
            if( fxx >= posxx and fxx + 42 <= posxx  and fyy >= posyy and fyy + 94 >= posyy ):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5

            else:
                y = 10
                       
                        
        if(nivelone.coords(minivann2)[1] > 740):
            nivelone.delete(minivann2)
            xi2 = random.randint(860,1178)
            minivann2 = nivelone.create_image(xi2,1,image = minivan)
        #runner
        if(nivelone.coords(runner)[1] <= 740):
            if(nivelone.coords(runner)[0] <= 467 and nivelone.coords(runner)[0] >= 155):
                z = random.randint(-10,10)
                c = random.randint(1,7)
                nivelone.move(runner,z,c)
            if(nivelone.coords(runner)[0] > 467):
                z = random.randint(-10,0)
                c = random.randint(1,7)
                nivelone.move(runner,z,c)
            if(nivelone.coords(runner)[0] < 155):
                z = random.randint(0,10)
                c = random.randint(1,7)
                nivelone.move(runner,z,c)
            posxr = nivelone.coords(runner)[0]
            posyr = nivelone.coords(runner)[1]
            fxr = nivelone.coords(carrete1)[0]
            fyr = nivelone.coords(carrete1)[1]
            if( fxr >= posxr and fxr <= posxr + 45 and fyr >= posyr and fyr <= posyr + 82):
                nivelone.move(runner,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5                
            if( fxr <= posxr and fxr + 45 >= posxr  and fyr <= posyr and fyr + 82 <= posyr ):
                nivelone.move(runner,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5
            if( fxr <= posxr and fxr >= posxr - 45 and fyr <= posyr and fyr >= posyr - 82):
                nivelone.move(runner,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5                
            if( fxr >= posxr and fxr + 45 <= posxr  and fyr >= posyr and fyr + 82 >= posyr ):
                nivelone.move(runner,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5           

        if(nivelone.coords(runner)[1] >= 740):
            nivelone.delete(runner)
            xl = random.randint(165,457)
            runner = nivelone.create_image(xl,1,image = runer)
        #runner2
        if(nivelone.coords(runner2)[1] <= 740):
            if(nivelone.coords(runner2)[0] <= 1187 and nivelone.coords(runner2)[0] >= 855):
                z2 = random.randint(-10,10)
                c2 = random.randint(1,7)
                nivelone.move(runner2,z2,c2)
            if(nivelone.coords(runner2)[0] > 1187):
                z2 = random.randint(-10,0)
                c2 = random.randint(1,7)
                nivelone.move(runner2,z2,c2)
            if(nivelone.coords(runner2)[0] < 855):
                z2 = random.randint(0,10)
                c2 = random.randint(1,7)
                nivelone.move(runner2,z2,c2)
            posxrr = nivelone.coords(runner2)[0]
            posyrr = nivelone.coords(runner2)[1]
            fxrr = nivelone.coords(carrete2)[0]
            fyrr = nivelone.coords(carrete2)[1]
            if( fxrr >= posxrr and fxrr <= posxrr + 45 and fyrr >= posyrr and fyrr <= posyrr + 82):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5               
            if( fxrr <= posxrr and fxrr + 45 >= posxrr  and fyrr <= posyrr and fyrr + 82 <= posyrr ):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5
            if( fxrr <= posxrr and fxrr >= posxrr - 45 and fyrr <= posyrr and fyrr >= posyrr - 82):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5                
            if( fxrr >= posxrr and fxrr + 45 <= posxrr  and fyrr >= posyrr and fyrr + 82 >= posyrr ):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5
        if(nivelone.coords(runner2)[1] >= 740):
            nivelone.delete(runner2)
            xl2 = random.randint(860,1178)
            runner2 = nivelone.create_image(xl2,1,image = runer)


        #fighter
        if(nivelone.coords(fighter)[1] <= 1400):
            if(nivelone.coords(fighter)[0] < nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,4,5)
            if(nivelone.coords(fighter)[0] > nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,-4,5)
            if(nivelone.coords(fighter)[0] == nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,0,5)
            posxf = nivelone.coords(fighter)[0]
            posyf = nivelone.coords(fighter)[1]
            fxf = nivelone.coords(carrete1)[0]
            fyf = nivelone.coords(carrete1)[1]
            if( fxf >= posxf and fxf <= posxf + 45 and fyf >= posyf and fyf <= posyf + 82):
                nivelone.move(fighter,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5                 
            if( fxf <= posxf and fxf + 45 >= posxf  and fyf <= posyf and fyf + 82 <= posyf ):
                nivelone.move(fighter,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5 
            if( fxf <= posxf and fxf >= posxf - 45 and fyf <= posyf and fyf >= posyf - 82):
                nivelone.move(fighter,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5                 
            if( fxf >= posxf and fxf + 45 <= posxf  and fyf >= posyf and fyf + 82 >= posyf ):
                nivelone.move(fighter,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5 
        if(nivelone.coords(fighter)[1] > 1400):
            nivelone.delete(fighter)
            xf = random.randint(165,457)
            fighter = nivelone.create_image(xf,1,image = fihter)

        #fighter2
        if(nivelone.coords(fighter2)[1] <= 1400):
            if(nivelone.coords(fighter2)[0] < nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,4,5)
            if(nivelone.coords(fighter2)[0] > nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,-4,5)
            if(nivelone.coords(fighter2)[0] == nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,0,5)
            posxff = nivelone.coords(fighter2)[0]
            posyff = nivelone.coords(fighter2)[1]
            fxff = nivelone.coords(carrete2)[0]
            fyff = nivelone.coords(carrete2)[1]
            if( fxff >= posxff and fxff <= posxff + 45 and fyff >= posyff and fyff <= posyff + 82):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5               
            if( fxff <= posxff and fxff + 45 >= posxff  and fyff <= posyff and fyff + 82 <= posyff ):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5
            if( fxff <= posxff and fxff >= posxff - 45 and fyff <= posyff and fyff >= posyff - 82):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5                
            if( fxff >= posxff and fxff + 45 <= posxff  and fyff >= posyff and fyff + 82 >= posyff ):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5
        if(nivelone.coords(fighter2)[1] > 1400):
            nivelone.delete(fighter2)
            xf2 = random.randint(860,1178)
            fighter2 = nivelone.create_image(xf2,1,image = fihter)

        #gasolina2
        if(nivelone.coords(gasolinaa)[1] <= 2400):
            nivelone.move(gasolinaa,0,8)
            posxgg = nivelone.coords(gasolinaa)[0]
            posygg = nivelone.coords(gasolinaa)[1]
            fxgg = nivelone.coords(carrete2)[0]
            fygg = nivelone.coords(carrete2)[1]
            if( fxgg >= posxgg and fxgg <= posxgg + 34 and fygg >= posygg and fygg <= posygg + 58):
                nivelone.move(gasolinaa,0,200)
                pTwo = pTwo + 250
                                 
               
            if( fxgg <= posxgg and fxgg >= posxgg - 34 and fygg <= posygg and fygg >= posygg - 58):
                nivelone.move(gasolinaa,0,200)
                pTwo = pTwo + 250
                                 
             
            
        if(nivelone.coords(gasolinaa)[1] > 2400):
            nivelone.delete(gasolinaa)
            xg2 = random.randint(860,1178)
            gasolinaa = nivelone.create_image(xg2,1,image = gas)
   
        #gasolina
        if(nivelone.coords(gasolina)[1] <= 2400):
            nivelone.move(gasolina,0,8)
            posxg = nivelone.coords(gasolina)[0]
            posyg = nivelone.coords(gasolina)[1]
            fxg = nivelone.coords(carrete1)[0]
            fyg = nivelone.coords(carrete1)[1]
            if( fxg >= posxg and fxg <= posxg + 34 and fyg >= posyg and fyg <= posyg + 58):
                nivelone.move(gasolina,0,200)
                pOne = pOne + 250
                                 

                 
            if( fxg <= posxg and fxg >= posxg - 34 and fyg <= posyg and fyg >= posyg - 58):
                nivelone.move(gasolina,0,200)
                pOne = pOne + 250
                                 
               
        if(nivelone.coords(gasolina)[1] > 2400):
            nivelone.delete(gasolina)
            xg = random.randint(165,457)
            gasolina = nivelone.create_image(xg,1,image = gas)

        #mancha1
        if(nivelone.coords(mancha1)[1] <= 900):
            nivelone.move(mancha1,0,8)
            posxm = nivelone.coords(mancha1)[0]
            posym = nivelone.coords(mancha1)[1]
            fxm = nivelone.coords(carrete1)[0]
            fym = nivelone.coords(carrete1)[1]
            if( fxm >= posxm and fxm <= posxm + 42 and fym >= posym and fym <= posym + 94):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,20,0)
                One = pOne - 17
                scoreOne = 0
                y = 2
                                               
            if( fxm <= posxm and fxm + 42 >= posxm  and fym <= posym and fym + 94 <= posym ):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,20,0)
                pOne = pOne - 17
                scoreOne = 0
                y = 2
                                
            if( fxm <= posxm and fxm >= posxm - 42 and fym <= posym and fym >= posym - 94):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,20,0)
                pOne = pOne - 17
                scoreOne = 0
                y = 2
                           
            if( fxm >= posxm and fxm + 42 <= posxm  and fym >= posym and fym + 94 >= posym ):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,20,0)
                pOne = pOne - 17
                scoreOne = 0
                y = 2

            else:
                y = 10
        if(nivelone.coords(mancha1)[1] > 900):
            nivelone.delete(mancha1)
            xm1 = random.randint(165,457)
            mancha1 = nivelone.create_image(xm1,1,image = mancha)
        #mancha2
        if(nivelone.coords(mancha2)[1] <= 900):
            nivelone.move(mancha2,0,8)
            posxmm = nivelone.coords(mancha2)[0]
            posymm = nivelone.coords(mancha2)[1]
            fxmm = nivelone.coords(carrete2)[0]
            fymm = nivelone.coords(carrete2)[1]
            if( fxmm >= posxmm  and fxm <= posxmm + 42 and fym >= posymm and fymm <= posymm + 94):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,20,0)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 2
                                               
            if( fxmm <= posxmm and fxmm + 42 >= posxmm  and fymm <= posymm and fymm + 94 <= posymm ):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,20,0)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 2
                                
            if( fxmm <= posxmm and fxmm >= posxmm - 42 and fymm <= posymm and fymm >= posymm - 94):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,20,0)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 2
                           
            if( fxmm >= posxmm and fxmm + 42 <= posxmm  and fymm >= posymm and fymm + 94 >= posymm ):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,20,0)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 2

            else:
                y = 10
        if(nivelone.coords(mancha2)[1] > 900):
            nivelone.delete(mancha2)
            xm2 = random.randint(860,1178)
            mancha2 = nivelone.create_image(xm2,1,image = mancha)
        
        

        #Limites
        if(pTwo <= 0 ):
            win2 = nivelone.create_image(300,350,image = win)
            lose2 = nivelone.create_image(1020,350,image = lose)
            break
        if(pOne <= 0):
            win2 = nivelone.create_image(1020,350,image = win)
            lose2 = nivelone.create_image(300,350,image = lose)
            break
            
        if(nivelone.coords(nivelonee)[1] >28000):
            xs = pTwo * 10
            xd = pOne * 10
            scoreOne = scoreOne + xd
            scoreTwo = scoreTwo + xs
            
            if(scoreOne > scoreTwo):
                win1 = nivelone.create_image(300,350,image = win)
                lose1 = nivelone.create_image(1020,350,image = lose)
                break
            
            if(scoreOne < scoreTwo):
                win2 = nivelone.create_image(1020,350,image = win)
                lose2 = nivelone.create_image(300,350,image = lose)
                break
                  
            
            
            
        v5.update()
        time.sleep(0.03)
#===========================================================================================================================================================#
                                                        #NIVEL 4 #

def nivel4():
    """
En esta  funcion el nivel de dificultad del nivel es dificil, en este sentido, se importan las imgenes necesarias para hacer que el nivel funcione
y mediante un "while" se hace que el nivel se mueva, y asi mismo, todos los objetos que hay en este(enemigos),incluyendo al jugador, se usa la herramienta random
para poder poner de forma aleatoria el lugar donde apareceran los enemigos
    """
    global Nivel4,mitad,carro2,v4,v5,namep1,namep2,nivelone,carrete1,h,minivan,runer,gas,fihter,bomba,win,lose,mancha,iz
    v4.iconify()
    v5 = Toplevel()
    v5.title("Survival Rate")
    v5.geometry("1366x768")
    nivelone = Canvas(v5,height = 768 , width = 1366)
    nivelonee = nivelone.create_image(683,387, image = Nivel4)
    carrete1 = nivelone.create_image(300,642, image = carro1)
    nivelonnee = nivelone.create_image(681,386, image = mitad)
    carrete2 = nivelone.create_image(1020,642,image = carro2)
    jugadorOne = Label(nivelone,  text = namep1.get(),bg = "Black",fg = "White",font = neon).place(x = 640, y = 80)
    jugadorTwo = Label(nivelone,  text = namep2.get(),bg = "Black",fg = "White",font = neon).place(x = 640, y = 470)
    xi = random.randint(165,457)
    xi2 = random.randint(860,1178)
    xl = random.randint(165,457)
    xl2 = random.randint(860,1178)
    xg = random.randint(165,457)
    xg2 = random.randint(860,1178)
    xm = random.randint(165,457)
    xm2 = random.randint(860,1178)
    minivann = nivelone.create_image(xi,1,image = minivan)
    minivann2 = nivelone.create_image(xi2,1,image = minivan)
    runner = nivelone.create_image(xl,1,image = runer)
    runner2 = nivelone.create_image(xl2,1,image = runer)
    gasolina = nivelone.create_image(xg,1,image = gas)
    gasolinaa = nivelone.create_image(xg2,1,image = gas)
    fighter = nivelone.create_image(300,1,image = fihter)
    fighter2 = nivelone.create_image(1020,1,image = fihter)
    mancha1 = nivelone.create_image(xm,1,image = mancha)
    mancha2 = nivelone.create_image(xm2,1,image = mancha)
    
    
        
    def keyup(e):
        """
        """
        global h
        if(e.keycode in h):
            h.pop(h.index(e.keycode))

    def keydown(e):
        """
        """
        global h
        if(not e.keycode in h):
            h.append(e.keycode)

    
    def key():
        """
        """
        global h
        #Player1
        if(nivelone.coords(carrete1)[0] > 130):
            if(65 in h):
                nivelone.move(carrete1,-7,0)
        if(nivelone.coords(carrete1)[0] < 467):
            if(68 in h):
                nivelone.move(carrete1,7,0)
        #Player2
        if(nivelone.coords(carrete2)[0] > 855):        
            if(74 in h):
                nivelone.move(carrete2,-7,0)
        if(nivelone.coords(carrete2)[0] < 1187):
            if(76 in h):
                nivelone.move(carrete2,7,0)
        nivelone.after(15,key)
                
    nivelone.bind("<KeyPress>", keydown)
    nivelone.bind("<KeyRelease>",keyup)
    nivelone.focus_set()
    key()
    
    nivelone.pack()
    pOne = 600
    pTwo = 600
    scoreOne = 0
    scoreTwo = 0
    y = 10
    
    while(True):
        nivelone.move(nivelonee,0,y)
        #Puntaje de la gasolina
        gasolina1 = Label(nivelone,text = pOne,bg = "Black",fg = "white",font = bit).place(x = 635, y = 220)
        gasolina2 = Label(nivelone,text = pTwo,bg = "Black",fg = "white",font = bit).place(x = 635, y = 590)
        pOne = pOne - 1 
        pTwo = pTwo - 1
        #Score
        score1 = Label(nivelone,text = scoreOne,bg = "Black",fg = "white",font = bit).place(x = 635, y = 340)
        score2 = Label(nivelone,text = scoreTwo,bg = "Black",fg = "white",font = bit).place(x = 635, y = 700)
        scoreOne = scoreOne + 1
        scoreTwo = scoreTwo + 1
        #minivan
        if(nivelone.coords(minivann)[1] <= 740):
            nivelone.move(minivann,0,9)
            posx = nivelone.coords(minivann)[0]
            posy = nivelone.coords(minivann)[1]
            fx = nivelone.coords(carrete1)[0]
            fy = nivelone.coords(carrete1)[1]
            if( fx >= posx and fx <= posx + 42 and fy >= posy and fy <= posy + 94):
                nivelone.move(minivann,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5
                                               
            if( fx <= posx and fx + 42 >= posx  and fy <= posy and fy + 94 <= posy ):
                nivelone.move(minivann,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5
                                
            if( fx <= posx and fx >= posx - 42 and fy <= posy and fy >= posy - 94):
                nivelone.move(minivann,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5
                           
            if( fx >= posx and fx + 42 <= posx  and fy >= posy and fy + 94 >= posy ):
                nivelone.move(minivann,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5

            else:
                y = 10
                           

                  
        if(nivelone.coords(minivann)[1] > 740):
            nivelone.delete(minivann)
            xi = random.randint(165,457)
            minivann = nivelone.create_image(xi,1,image = minivan)
            
        #minivan2
        if(nivelone.coords(minivann2)[1] <= 740):
            nivelone.move(minivann2,0,9)
            posxx = nivelone.coords(minivann2)[0]
            posyy = nivelone.coords(minivann2)[1]
            fxx = nivelone.coords(carrete2)[0]
            fyy = nivelone.coords(carrete2)[1]
            if( fxx >= posxx and fxx <= posxx + 42 and fyy >= posyy and fyy <= posyy + 94):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5
                                
            if( fxx <= posxx and fxx + 42 >= posxx  and fyy <= posyy and fyy + 94 <= posyy ):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5
                
            if( fxx <= posxx and fxx >= posxx - 42 and fyy <= posyy and fyy >= posyy - 94):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5
                                
            if( fxx >= posxx and fxx + 42 <= posxx  and fyy >= posyy and fyy + 94 >= posyy ):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5

            else:
                y = 10
                       
                        
        if(nivelone.coords(minivann2)[1] > 740):
            nivelone.delete(minivann2)
            xi2 = random.randint(860,1178)
            minivann2 = nivelone.create_image(xi2,1,image = minivan)
        #runner
        if(nivelone.coords(runner)[1] <= 740):
            if(nivelone.coords(runner)[0] <= 467 and nivelone.coords(runner)[0] >= 155):
                z = random.randint(-11,11)
                c = random.randint(1,8)
                nivelone.move(runner,z,c)
            if(nivelone.coords(runner)[0] > 467):
                z = random.randint(-11,0)
                c = random.randint(1,8)
                nivelone.move(runner,z,c)
            if(nivelone.coords(runner)[0] < 155):
                z = random.randint(0,11)
                c = random.randint(1,8)
                nivelone.move(runner,z,c)
            posxr = nivelone.coords(runner)[0]
            posyr = nivelone.coords(runner)[1]
            fxr = nivelone.coords(carrete1)[0]
            fyr = nivelone.coords(carrete1)[1]
            if( fxr >= posxr and fxr <= posxr + 45 and fyr >= posyr and fyr <= posyr + 82):
                nivelone.move(runner,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5                
            if( fxr <= posxr and fxr + 45 >= posxr  and fyr <= posyr and fyr + 82 <= posyr ):
                nivelone.move(runner,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5
            if( fxr <= posxr and fxr >= posxr - 45 and fyr <= posyr and fyr >= posyr - 82):
                nivelone.move(runner,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5                
            if( fxr >= posxr and fxr + 45 <= posxr  and fyr >= posyr and fyr + 82 >= posyr ):
                nivelone.move(runner,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5           

        if(nivelone.coords(runner)[1] >= 740):
            nivelone.delete(runner)
            xl = random.randint(165,457)
            runner = nivelone.create_image(xl,1,image = runer)
        #runner2
        if(nivelone.coords(runner2)[1] <= 740):
            if(nivelone.coords(runner2)[0] <= 1187 and nivelone.coords(runner2)[0] >= 855):
                z2 = random.randint(-11,11)
                c2 = random.randint(1,8)
                nivelone.move(runner2,z2,c2)
            if(nivelone.coords(runner2)[0] > 1187):
                z2 = random.randint(-11,0)
                c2 = random.randint(1,8)
                nivelone.move(runner2,z2,c2)
            if(nivelone.coords(runner2)[0] < 855):
                z2 = random.randint(0,11)
                c2 = random.randint(1,8)
                nivelone.move(runner2,z2,c2)
            posxrr = nivelone.coords(runner2)[0]
            posyrr = nivelone.coords(runner2)[1]
            fxrr = nivelone.coords(carrete2)[0]
            fyrr = nivelone.coords(carrete2)[1]
            if( fxrr >= posxrr and fxrr <= posxrr + 45 and fyrr >= posyrr and fyrr <= posyrr + 82):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5               
            if( fxrr <= posxrr and fxrr + 45 >= posxrr  and fyrr <= posyrr and fyrr + 82 <= posyrr ):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
            if( fxrr <= posxrr and fxrr >= posxrr - 45 and fyrr <= posyrr and fyrr >= posyrr - 82):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5                
            if( fxrr >= posxrr and fxrr + 45 <= posxrr  and fyrr >= posyrr and fyrr + 82 >= posyrr ):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 15
                scoreTwo = 0
                y = 5
        if(nivelone.coords(runner2)[1] >= 740):
            nivelone.delete(runner2)
            xl2 = random.randint(860,1178)
            runner2 = nivelone.create_image(xl2,1,image = runer)


        #fighter
        if(nivelone.coords(fighter)[1] <= 1400):
            if(nivelone.coords(fighter)[0] < nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,5,5)
            if(nivelone.coords(fighter)[0] > nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,-5,5)
            if(nivelone.coords(fighter)[0] == nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,0,5)
            posxf = nivelone.coords(fighter)[0]
            posyf = nivelone.coords(fighter)[1]
            fxf = nivelone.coords(carrete1)[0]
            fyf = nivelone.coords(carrete1)[1]
            if( fxf >= posxf and fxf <= posxf + 45 and fyf >= posyf and fyf <= posyf + 82):
                nivelone.move(fighter,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5                 
            if( fxf <= posxf and fxf + 45 >= posxf  and fyf <= posyf and fyf + 82 <= posyf ):
                nivelone.move(fighter,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5 
            if( fxf <= posxf and fxf >= posxf - 45 and fyf <= posyf and fyf >= posyf - 82):
                nivelone.move(fighter,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5                 
            if( fxf >= posxf and fxf + 45 <= posxf  and fyf >= posyf and fyf + 82 >= posyf ):
                nivelone.move(fighter,0,150)
                pOne = pOne - 17
                scoreOne = 0
                y = 5 
        if(nivelone.coords(fighter)[1] > 1400):
            nivelone.delete(fighter)
            xf = random.randint(165,457)
            fighter = nivelone.create_image(xf,1,image = fihter)

        #fighter2
        if(nivelone.coords(fighter2)[1] <= 1400):
            if(nivelone.coords(fighter2)[0] < nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,5,5)
            if(nivelone.coords(fighter2)[0] > nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,-5,5)
            if(nivelone.coords(fighter2)[0] == nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,0,5)
            posxff = nivelone.coords(fighter2)[0]
            posyff = nivelone.coords(fighter2)[1]
            fxff = nivelone.coords(carrete2)[0]
            fyff = nivelone.coords(carrete2)[1]
            if( fxff >= posxff and fxff <= posxff + 45 and fyff >= posyff and fyff <= posyff + 82):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5               
            if( fxff <= posxff and fxff + 45 >= posxff  and fyff <= posyff and fyff + 82 <= posyff ):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5
            if( fxff <= posxff and fxff >= posxff - 45 and fyff <= posyff and fyff >= posyff - 82):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5                
            if( fxff >= posxff and fxff + 45 <= posxff  and fyff >= posyff and fyff + 82 >= posyff ):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 5
        if(nivelone.coords(fighter2)[1] > 1400):
            nivelone.delete(fighter2)
            xf2 = random.randint(860,1178)
            fighter2 = nivelone.create_image(xf2,1,image = fihter)

        #gasolina2
        if(nivelone.coords(gasolinaa)[1] <= 2400):
            nivelone.move(gasolinaa,0,7)
            posxgg = nivelone.coords(gasolinaa)[0]
            posygg = nivelone.coords(gasolinaa)[1]
            fxgg = nivelone.coords(carrete2)[0]
            fygg = nivelone.coords(carrete2)[1]
            if( fxgg >= posxgg and fxgg <= posxgg + 34 and fygg >= posygg and fygg <= posygg + 58):
                nivelone.move(gasolinaa,0,200)
                pTwo = pTwo + 270
                                 
               
            if( fxgg <= posxgg and fxgg >= posxgg - 34 and fygg <= posygg and fygg >= posygg - 58):
                nivelone.move(gasolinaa,0,200)
                pTwo = pTwo + 270
                                 
             
            
        if(nivelone.coords(gasolinaa)[1] > 2400):
            nivelone.delete(gasolinaa)
            xg2 = random.randint(860,1178)
            gasolinaa = nivelone.create_image(xg2,1,image = gas)
   
        #gasolina
        if(nivelone.coords(gasolina)[1] <= 2400):
            nivelone.move(gasolina,0,7)
            posxg = nivelone.coords(gasolina)[0]
            posyg = nivelone.coords(gasolina)[1]
            fxg = nivelone.coords(carrete1)[0]
            fyg = nivelone.coords(carrete1)[1]
            if( fxg >= posxg and fxg <= posxg + 34 and fyg >= posyg and fyg <= posyg + 58):
                nivelone.move(gasolina,0,200)
                pOne = pOne + 270
                                 

                 
            if( fxg <= posxg and fxg >= posxg - 34 and fyg <= posyg and fyg >= posyg - 58):
                nivelone.move(gasolina,0,200)
                pOne = pOne + 270
                                 
               
        if(nivelone.coords(gasolina)[1] > 2400):
            nivelone.delete(gasolina)
            xg = random.randint(165,457)
            gasolina = nivelone.create_image(xg,1,image = gas)

        #mancha1
        if(nivelone.coords(mancha1)[1] <= 900):
            nivelone.move(mancha1,0,9)
            posxm = nivelone.coords(mancha1)[0]
            posym = nivelone.coords(mancha1)[1]
            fxm = nivelone.coords(carrete1)[0]
            fym = nivelone.coords(carrete1)[1]
            if( fxm >= posxm and fxm <= posxm + 42 and fym >= posym and fym <= posym + 94):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,20,0)
                One = pOne - 17
                scoreOne = 0
                y = 2
                                               
            if( fxm <= posxm and fxm + 42 >= posxm  and fym <= posym and fym + 94 <= posym ):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,20,0)
                pOne = pOne - 17
                scoreOne = 0
                y = 2
                                
            if( fxm <= posxm and fxm >= posxm - 42 and fym <= posym and fym >= posym - 94):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,20,0)
                pOne = pOne - 17
                scoreOne = 0
                y = 2
                           
            if( fxm >= posxm and fxm + 42 <= posxm  and fym >= posym and fym + 94 >= posym ):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,20,0)
                pOne = pOne - 17
                scoreOne = 0
                y = 2

            else:
                y = 10
        if(nivelone.coords(mancha1)[1] > 900):
            nivelone.delete(mancha1)
            xm1 = random.randint(165,457)
            mancha1 = nivelone.create_image(xm1,1,image = mancha)
        #mancha2
        if(nivelone.coords(mancha2)[1] <= 900):
            nivelone.move(mancha2,0,9)
            posxmm = nivelone.coords(mancha2)[0]
            posymm = nivelone.coords(mancha2)[1]
            fxmm = nivelone.coords(carrete2)[0]
            fymm = nivelone.coords(carrete2)[1]
            if( fxmm >= posxmm  and fxm <= posxmm + 42 and fym >= posymm and fymm <= posymm + 94):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,20,0)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 2
                                               
            if( fxmm <= posxmm and fxmm + 42 >= posxmm  and fymm <= posymm and fymm + 94 <= posymm ):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,20,0)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 2
                                
            if( fxmm <= posxmm and fxmm >= posxmm - 42 and fymm <= posymm and fymm >= posymm - 94):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,20,0)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 2
                           
            if( fxmm >= posxmm and fxmm + 42 <= posxmm  and fymm >= posymm and fymm + 94 >= posymm ):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,20,0)
                pTwo = pTwo - 17
                scoreTwo = 0
                y = 2

            else:
                y = 10
        if(nivelone.coords(mancha2)[1] > 900):
            nivelone.delete(mancha2)
            xm2 = random.randint(860,1178)
            mancha2 = nivelone.create_image(xm2,1,image = mancha)
        
        

        #Limites
        if(pTwo <= 0 ):
            win2 = nivelone.create_image(300,350,image = win)
            lose2 = nivelone.create_image(1020,350,image = lose)
            break
        if(pOne <= 0):
            win2 = nivelone.create_image(1020,350,image = win)
            lose2 = nivelone.create_image(300,350,image = lose)
            break
            
        if(nivelone.coords(nivelonee)[1] >28000):
            xs = pTwo * 10
            xd = pOne * 10
            scoreOne = scoreOne + xd
            scoreTwo = scoreTwo + xs
            
            if(scoreOne > scoreTwo):
                win1 = nivelone.create_image(300,350,image = win)
                lose1 = nivelone.create_image(1020,350,image = lose)
                break
            
            if(scoreOne < scoreTwo):
                win2 = nivelone.create_image(1020,350,image = win)
                lose2 = nivelone.create_image(300,350,image = lose)
                break
                  
            
            
            
        v5.update()
        time.sleep(0.03)

#===========================================================================================================================================================#
                                                        #NIVEL 5 #

def nivel5():
    """
En esta  funcion el nivel de dificultad del nivel es muy dificil, en este sentido, se importan las imgenes necesarias para hacer que el nivel funcione
y mediante un "while" se hace que el nivel se mueva, y asi mismo, todos los objetos que hay en este(enemigos),incluyendo al jugador, se usa la herramienta random
para poder poner de forma aleatoria el lugar donde apareceran los enemigos
    """
    global Nivel5,mitad,carro2,v4,v5,namep1,namep2,nivelone,carrete1,h,minivan,runer,gas,fihter,bomba,win,lose,mancha,iz
    v4.iconify()
    v5 = Toplevel()
    v5.title("Survival Rate")
    v5.geometry("1366x768")
    nivelone = Canvas(v5,height = 768 , width = 1366)
    nivelonee = nivelone.create_image(683,387, image = Nivel5)
    carrete1 = nivelone.create_image(300,642, image = carro1)
    nivelonnee = nivelone.create_image(681,386, image = mitad)
    carrete2 = nivelone.create_image(1020,642,image = carro2)
    jugadorOne = Label(nivelone,  text = namep1.get(),bg = "Black",fg = "White",font = neon).place(x = 640, y = 80)
    jugadorTwo = Label(nivelone,  text = namep2.get(),bg = "Black",fg = "White",font = neon).place(x = 640, y = 470)
    xi = random.randint(165,457)
    xi2 = random.randint(860,1178)
    xii = random.randint(165,457)
    xii2 = random.randint(860,1178)
    xl = random.randint(165,457)
    xl2 = random.randint(860,1178)
    xg = random.randint(165,457)
    xg2 = random.randint(860,1178)
    xm = random.randint(165,457)
    xm2 = random.randint(860,1178)
    minivann = nivelone.create_image(xi,1,image = minivan)
    minivann2 = nivelone.create_image(xi2,1,image = minivan)
    minivanN = nivelone.create_image(xii,1,image = minivan)
    minivanN2 = nivelone.create_image(xii2,1,image = minivan)
    runner = nivelone.create_image(xl,1,image = runer)
    runner2 = nivelone.create_image(xl2,1,image = runer)
    gasolina = nivelone.create_image(xg,1,image = gas)
    gasolinaa = nivelone.create_image(xg2,1,image = gas)
    fighter = nivelone.create_image(300,1,image = fihter)
    fighter2 = nivelone.create_image(1020,1,image = fihter)
    mancha1 = nivelone.create_image(xm,1,image = mancha)
    mancha2 = nivelone.create_image(xm2,1,image = mancha)
    
    
        
    def keyup(e):
        """
        """
        global h
        if(e.keycode in h):
            h.pop(h.index(e.keycode))

    def keydown(e):
        """
        """
        global h
        if(not e.keycode in h):
            h.append(e.keycode)

    
    def key():
        """
        """
        global h
        #Player1
        if(nivelone.coords(carrete1)[0] > 130):
            if(65 in h):
                nivelone.move(carrete1,-7,0)
        if(nivelone.coords(carrete1)[0] < 467):
            if(68 in h):
                nivelone.move(carrete1,7,0)
        #Player2
        if(nivelone.coords(carrete2)[0] > 855):        
            if(74 in h):
                nivelone.move(carrete2,-7,0)
        if(nivelone.coords(carrete2)[0] < 1187):
            if(76 in h):
                nivelone.move(carrete2,7,0)
        nivelone.after(15,key)
                
    nivelone.bind("<KeyPress>", keydown)
    nivelone.bind("<KeyRelease>",keyup)
    nivelone.focus_set()
    key()
    
    nivelone.pack()
    pOne = 600
    pTwo = 600
    scoreOne = 0
    scoreTwo = 0
    y = 10
    
    while(True):
        nivelone.move(nivelonee,0,y)
        #Puntaje de la gasolina
        gasolina1 = Label(nivelone,text = pOne,bg = "Black",fg = "white",font = bit).place(x = 635, y = 220)
        gasolina2 = Label(nivelone,text = pTwo,bg = "Black",fg = "white",font = bit).place(x = 635, y = 590)
        pOne = pOne - 1 
        pTwo = pTwo - 1
        #Score
        score1 = Label(nivelone,text = scoreOne,bg = "Black",fg = "white",font = bit).place(x = 635, y = 340)
        score2 = Label(nivelone,text = scoreTwo,bg = "Black",fg = "white",font = bit).place(x = 635, y = 700)
        scoreOne = scoreOne + 1
        scoreTwo = scoreTwo + 1
        #minivan
        if(nivelone.coords(minivann)[1] <= 740):
            nivelone.move(minivann,0,9)
            posx = nivelone.coords(minivann)[0]
            posy = nivelone.coords(minivann)[1]
            fx = nivelone.coords(carrete1)[0]
            fy = nivelone.coords(carrete1)[1]
            if( fx >= posx and fx <= posx + 42 and fy >= posy and fy <= posy + 94):
                nivelone.move(minivann,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5
                                               
            if( fx <= posx and fx + 42 >= posx  and fy <= posy and fy + 94 <= posy ):
                nivelone.move(minivann,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5
                                
            if( fx <= posx and fx >= posx - 42 and fy <= posy and fy >= posy - 94):
                nivelone.move(minivann,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5
                           
            if( fx >= posx and fx + 42 <= posx  and fy >= posy and fy + 94 >= posy ):
                nivelone.move(minivann,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5

            else:
                y = 10
                           

                  
        if(nivelone.coords(minivann)[1] > 740):
            nivelone.delete(minivann)
            xi = random.randint(165,457)
            minivann = nivelone.create_image(xi,1,image = minivan)

        #minivan1.1
        if(nivelone.coords(minivanN)[1] <= 740):
            nivelone.move(minivanN,0,7)
            posx = nivelone.coords(minivanN)[0]
            posy = nivelone.coords(minivanN)[1]
            fx = nivelone.coords(carrete1)[0]
            fy = nivelone.coords(carrete1)[1]
            if( fx >= posx and fx <= posx + 42 and fy >= posy and fy <= posy + 94):
                nivelone.move(minivanN,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5
                                               
            if( fx <= posx and fx + 42 >= posx  and fy <= posy and fy + 94 <= posy ):
                nivelone.move(minivanN,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5
                                
            if( fx <= posx and fx >= posx - 42 and fy <= posy and fy >= posy - 94):
                nivelone.move(minivanN,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5
                           
            if( fx >= posx and fx + 42 <= posx  and fy >= posy and fy + 94 >= posy ):
                nivelone.move(minivanN,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5

            else:
                y = 10
                           

                  
        if(nivelone.coords(minivanN)[1] > 740):
            nivelone.delete(minivanN)
            xii = random.randint(165,457)
            minivanN = nivelone.create_image(xi,1,image = minivan)
            
        #minivan2
        if(nivelone.coords(minivann2)[1] <= 740):
            nivelone.move(minivann2,0,9)
            posxx = nivelone.coords(minivann2)[0]
            posyy = nivelone.coords(minivann2)[1]
            fxx = nivelone.coords(carrete2)[0]
            fyy = nivelone.coords(carrete2)[1]
            if( fxx >= posxx and fxx <= posxx + 42 and fyy >= posyy and fyy <= posyy + 94):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5
                                
            if( fxx <= posxx and fxx + 42 >= posxx  and fyy <= posyy and fyy + 94 <= posyy ):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5
                
            if( fxx <= posxx and fxx >= posxx - 42 and fyy <= posyy and fyy >= posyy - 94):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5
                                
            if( fxx >= posxx and fxx + 42 <= posxx  and fyy >= posyy and fyy + 94 >= posyy ):
                nivelone.move(minivann2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5

            else:
                y = 10
                       
                        
        if(nivelone.coords(minivann2)[1] > 740):
            nivelone.delete(minivann2)
            xi2 = random.randint(860,1178)
            minivann2 = nivelone.create_image(xi2,1,image = minivan)
        #minivan2.1
        if(nivelone.coords(minivann2)[1] <= 740):
            nivelone.move(minivanN2,0,7)
            posxx = nivelone.coords(minivanN2)[0]
            posyy = nivelone.coords(minivanN2)[1]
            fxx = nivelone.coords(carrete2)[0]
            fyy = nivelone.coords(carrete2)[1]
            if( fxx >= posxx and fxx <= posxx + 42 and fyy >= posyy and fyy <= posyy + 94):
                nivelone.move(minivanN2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5
                                
            if( fxx <= posxx and fxx + 42 >= posxx  and fyy <= posyy and fyy + 94 <= posyy ):
                nivelone.move(minivanN2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5
                
            if( fxx <= posxx and fxx >= posxx - 42 and fyy <= posyy and fyy >= posyy - 94):
                nivelone.move(minivanN2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5
                                
            if( fxx >= posxx and fxx + 42 <= posxx  and fyy >= posyy and fyy + 94 >= posyy ):
                nivelone.move(minivanN2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5

            else:
                y = 10
                       
                        
        if(nivelone.coords(minivanN2)[1] > 740):
            nivelone.delete(minivanN2)
            xii2 = random.randint(860,1178)
            minivanN2 = nivelone.create_image(xi2,1,image = minivan)
        #runner
        if(nivelone.coords(runner)[1] <= 740):
            if(nivelone.coords(runner)[0] <= 467 and nivelone.coords(runner)[0] >= 155):
                z = random.randint(-12,12)
                c = random.randint(1,9)
                nivelone.move(runner,z,c)
            if(nivelone.coords(runner)[0] > 467):
                z = random.randint(-12,0)
                c = random.randint(1,9)
                nivelone.move(runner,z,c)
            if(nivelone.coords(runner)[0] < 155):
                z = random.randint(0,12)
                c = random.randint(1,9)
                nivelone.move(runner,z,c)
            posxr = nivelone.coords(runner)[0]
            posyr = nivelone.coords(runner)[1]
            fxr = nivelone.coords(carrete1)[0]
            fyr = nivelone.coords(carrete1)[1]
            if( fxr >= posxr and fxr <= posxr + 45 and fyr >= posyr and fyr <= posyr + 82):
                nivelone.move(runner,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5                
            if( fxr <= posxr and fxr + 45 >= posxr  and fyr <= posyr and fyr + 82 <= posyr ):
                nivelone.move(runner,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5
            if( fxr <= posxr and fxr >= posxr - 45 and fyr <= posyr and fyr >= posyr - 82):
                nivelone.move(runner,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5                
            if( fxr >= posxr and fxr + 45 <= posxr  and fyr >= posyr and fyr + 82 >= posyr ):
                nivelone.move(runner,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5           

        if(nivelone.coords(runner)[1] >= 740):
            nivelone.delete(runner)
            xl = random.randint(165,457)
            runner = nivelone.create_image(xl,1,image = runer)
        #runner2
        if(nivelone.coords(runner2)[1] <= 740):
            if(nivelone.coords(runner2)[0] <= 1187 and nivelone.coords(runner2)[0] >= 855):
                z2 = random.randint(-12,12)
                c2 = random.randint(1,9)
                nivelone.move(runner2,z2,c2)
            if(nivelone.coords(runner2)[0] > 1187):
                z2 = random.randint(-12,0)
                c2 = random.randint(1,9)
                nivelone.move(runner2,z2,c2)
            if(nivelone.coords(runner2)[0] < 855):
                z2 = random.randint(0,12)
                c2 = random.randint(1,9)
                nivelone.move(runner2,z2,c2)
            posxrr = nivelone.coords(runner2)[0]
            posyrr = nivelone.coords(runner2)[1]
            fxrr = nivelone.coords(carrete2)[0]
            fyrr = nivelone.coords(carrete2)[1]
            if( fxrr >= posxrr and fxrr <= posxrr + 45 and fyrr >= posyrr and fyrr <= posyrr + 82):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5               
            if( fxrr <= posxrr and fxrr + 45 >= posxrr  and fyrr <= posyrr and fyrr + 82 <= posyrr ):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5
            if( fxrr <= posxrr and fxrr >= posxrr - 45 and fyrr <= posyrr and fyrr >= posyrr - 82):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5                
            if( fxrr >= posxrr and fxrr + 45 <= posxrr  and fyrr >= posyrr and fyrr + 82 >= posyrr ):
                nivelone.move(runner2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5
        if(nivelone.coords(runner2)[1] >= 740):
            nivelone.delete(runner2)
            xl2 = random.randint(860,1178)
            runner2 = nivelone.create_image(xl2,1,image = runer)


        #fighter
        if(nivelone.coords(fighter)[1] <= 1400):
            if(nivelone.coords(fighter)[0] < nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,5,5)
            if(nivelone.coords(fighter)[0] > nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,-5,5)
            if(nivelone.coords(fighter)[0] == nivelone.coords(carrete1)[0]):
                nivelone.move(fighter,0,5)
            posxf = nivelone.coords(fighter)[0]
            posyf = nivelone.coords(fighter)[1]
            fxf = nivelone.coords(carrete1)[0]
            fyf = nivelone.coords(carrete1)[1]
            if( fxf >= posxf and fxf <= posxf + 45 and fyf >= posyf and fyf <= posyf + 82):
                nivelone.move(fighter,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5                 
            if( fxf <= posxf and fxf + 45 >= posxf  and fyf <= posyf and fyf + 82 <= posyf ):
                nivelone.move(fighter,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5 
            if( fxf <= posxf and fxf >= posxf - 45 and fyf <= posyf and fyf >= posyf - 82):
                nivelone.move(fighter,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5                 
            if( fxf >= posxf and fxf + 45 <= posxf  and fyf >= posyf and fyf + 82 >= posyf ):
                nivelone.move(fighter,0,150)
                pOne = pOne - 19
                scoreOne = 0
                y = 5 
        if(nivelone.coords(fighter)[1] > 1400):
            nivelone.delete(fighter)
            xf = random.randint(165,457)
            fighter = nivelone.create_image(xf,1,image = fihter)

        #fighter2
        if(nivelone.coords(fighter2)[1] <= 1400):
            if(nivelone.coords(fighter2)[0] < nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,5,5)
            if(nivelone.coords(fighter2)[0] > nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,-5,5)
            if(nivelone.coords(fighter2)[0] == nivelone.coords(carrete2)[0]):
                nivelone.move(fighter2,0,5)
            posxff = nivelone.coords(fighter2)[0]
            posyff = nivelone.coords(fighter2)[1]
            fxff = nivelone.coords(carrete2)[0]
            fyff = nivelone.coords(carrete2)[1]
            if( fxff >= posxff and fxff <= posxff + 45 and fyff >= posyff and fyff <= posyff + 82):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5               
            if( fxff <= posxff and fxff + 45 >= posxff  and fyff <= posyff and fyff + 82 <= posyff ):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5
            if( fxff <= posxff and fxff >= posxff - 45 and fyff <= posyff and fyff >= posyff - 82):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5                
            if( fxff >= posxff and fxff + 45 <= posxff  and fyff >= posyff and fyff + 82 >= posyff ):
                nivelone.move(fighter2,0,150)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 5
        if(nivelone.coords(fighter2)[1] > 1400):
            nivelone.delete(fighter2)
            xf2 = random.randint(860,1178)
            fighter2 = nivelone.create_image(xf2,1,image = fihter)

        #gasolina2
        if(nivelone.coords(gasolinaa)[1] <= 2400):
            nivelone.move(gasolinaa,0,9)
            posxgg = nivelone.coords(gasolinaa)[0]
            posygg = nivelone.coords(gasolinaa)[1]
            fxgg = nivelone.coords(carrete2)[0]
            fygg = nivelone.coords(carrete2)[1]
            if( fxgg >= posxgg and fxgg <= posxgg + 34 and fygg >= posygg and fygg <= posygg + 58):
                nivelone.move(gasolinaa,0,200)
                pTwo = pTwo + 320
                                 
               
            if( fxgg <= posxgg and fxgg >= posxgg - 34 and fygg <= posygg and fygg >= posygg - 58):
                nivelone.move(gasolinaa,0,200)
                pTwo = pTwo + 320
                                 
             
            
        if(nivelone.coords(gasolinaa)[1] > 2400):
            nivelone.delete(gasolinaa)
            xg2 = random.randint(860,1178)
            gasolinaa = nivelone.create_image(xg2,1,image = gas)
   
        #gasolina
        if(nivelone.coords(gasolina)[1] <= 2400):
            nivelone.move(gasolina,0,9)
            posxg = nivelone.coords(gasolina)[0]
            posyg = nivelone.coords(gasolina)[1]
            fxg = nivelone.coords(carrete1)[0]
            fyg = nivelone.coords(carrete1)[1]
            if( fxg >= posxg and fxg <= posxg + 34 and fyg >= posyg and fyg <= posyg + 58):
                nivelone.move(gasolina,0,200)
                pOne = pOne + 320
                                 

                 
            if( fxg <= posxg and fxg >= posxg - 34 and fyg <= posyg and fyg >= posyg - 58):
                nivelone.move(gasolina,0,200)
                pOne = pOne + 320
                                 
               
        if(nivelone.coords(gasolina)[1] > 2400):
            nivelone.delete(gasolina)
            xg = random.randint(165,457)
            gasolina = nivelone.create_image(xg,1,image = gas)

        #mancha1
        if(nivelone.coords(mancha1)[1] <= 900):
            nivelone.move(mancha1,0,9)
            posxm = nivelone.coords(mancha1)[0]
            posym = nivelone.coords(mancha1)[1]
            fxm = nivelone.coords(carrete1)[0]
            fym = nivelone.coords(carrete1)[1]
            if( fxm >= posxm and fxm <= posxm + 42 and fym >= posym and fym <= posym + 94):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,22,0)
                One = pOne - 19
                scoreOne = 0
                y = 2
                                               
            if( fxm <= posxm and fxm + 42 >= posxm  and fym <= posym and fym + 94 <= posym ):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,22,0)
                pOne = pOne - 19
                scoreOne = 0
                y = 2
                                
            if( fxm <= posxm and fxm >= posxm - 42 and fym <= posym and fym >= posym - 94):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,22,0)
                pOne = pOne - 19
                scoreOne = 0
                y = 2
                           
            if( fxm >= posxm and fxm + 42 <= posxm  and fym >= posym and fym + 94 >= posym ):
                nivelone.move(mancha1,0,150)
                nivelone.move(carrete1,22,0)
                pOne = pOne - 19
                scoreOne = 0
                y = 2

            else:
                y = 10
        if(nivelone.coords(mancha1)[1] > 900):
            nivelone.delete(mancha1)
            xm1 = random.randint(165,457)
            mancha1 = nivelone.create_image(xm1,1,image = mancha)
        #mancha2
        if(nivelone.coords(mancha2)[1] <= 900):
            nivelone.move(mancha2,0,9)
            posxmm = nivelone.coords(mancha2)[0]
            posymm = nivelone.coords(mancha2)[1]
            fxmm = nivelone.coords(carrete2)[0]
            fymm = nivelone.coords(carrete2)[1]
            if( fxmm >= posxmm  and fxm <= posxmm + 42 and fym >= posymm and fymm <= posymm + 94):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,22,0)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 2
                                               
            if( fxmm <= posxmm and fxmm + 42 >= posxmm  and fymm <= posymm and fymm + 94 <= posymm ):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,22,0)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 2
                                
            if( fxmm <= posxmm and fxmm >= posxmm - 42 and fymm <= posymm and fymm >= posymm - 94):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,22,0)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 2
                           
            if( fxmm >= posxmm and fxmm + 42 <= posxmm  and fymm >= posymm and fymm + 94 >= posymm ):
                nivelone.move(mancha2,0,150)
                nivelone.move(carrete2,22,0)
                pTwo = pTwo - 19
                scoreTwo = 0
                y = 2

            else:
                y = 10
        if(nivelone.coords(mancha2)[1] > 900):
            nivelone.delete(mancha2)
            xm2 = random.randint(860,1178)
            mancha2 = nivelone.create_image(xm2,1,image = mancha)
        
        

        #Limites
        if(pTwo <= 0 ):
            win2 = nivelone.create_image(300,350,image = win)
            lose2 = nivelone.create_image(1020,350,image = lose)
            break
        if(pOne <= 0):
            win2 = nivelone.create_image(1020,350,image = win)
            lose2 = nivelone.create_image(300,350,image = lose)
            break
            
        if(nivelone.coords(nivelonee)[1] >28000):
            xs = pTwo * 10
            xd = pOne * 10
            scoreOne = scoreOne + xd
            scoreTwo = scoreTwo + xs
            
            if(scoreOne > scoreTwo):
                win1 = nivelone.create_image(300,350,image = win)
                lose1 = nivelone.create_image(1020,350,image = lose)
                break
            
            if(scoreOne < scoreTwo):
                win2 = nivelone.create_image(1020,350,image = win)
                lose2 = nivelone.create_image(300,350,image = lose)
                break 
            
            
            
        v5.update()
        time.sleep(0.03)


            
	
        
    
 

#====================================================================BOTONES===================================================================#

        
imgb1 = PhotoImage(file = "start.png")
imgb2 = PhotoImage(file = "instrucciones.png")
imgb3 = PhotoImage(file = "controles.png")
imgb4 = PhotoImage(file = "salir.png")
b1 = Button(v,image = imgb1 ,command = start,height=35,width = 110).place(x= 630,y=280)
b2 = Button(v,image = imgb2,command = instrucciones,height=35,width = 110).place(x= 630,y=360)
b3 = Button(v,image = imgb3,command = controles,height=35,width = 110).place(x= 630,y=440)
b4 = Button(v,image = imgb4,command = salir,height=35,width = 110).place(x= 630,y=520)





v.mainloop()

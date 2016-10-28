# -*- coding:utf-8 -*-

#Eduardo Garcia Asensio T2
#Javier Helguera Lopez T2

import gtk
import pygtk
pygtk.require("2.0")
import random
from os import remove
import os
import time

def golpe(fila,columna):       							#Cambia el valor de las casillas de la mancha( conjunto                                                  ¡
    for fil in range(fila-2,fila+3):               		#de casillas que seran alteradas) en la matriz interna.
        if -1<fil<num_fila:
            for col in range(columna-2,columna+3):
                if  -1<col<num_columna:
                    if matriz[fil][col]=="X":       
                        matriz[fil][col]="."
                    else: matriz[fil][col]="X"
    for fil in range (fila-2,fila+3,4):
        if -1<fil<num_fila:
            for col in range(columna-2,columna+3,4):
                if col>-1 and col<num_columna:
                    if matriz[fil][col]=="X":
                        matriz[fil][col]="."
                    else: matriz[fil][col]="X"
          

def golpeBoton(widget):      						 #Cambia el valor de las casillas de la mancha
    (fila,columna)=widget.posicion                   #creada a partir del boton pulsado, en la matriz interna.
    for fil in range(fila-2,fila+3):
        if -1<fil<num_fila:
            for col in range(columna-2,columna+3):
                if  -1<col<num_columna:
                    if matriz[fil][col]=="X":       
                        matriz[fil][col]="."
                    else: matriz[fil][col]="X"
    for fil in range (fila-2,fila+3,4):
        if -1<fil<num_fila:
            for col in range(columna-2,columna+3,4):
                if col>-1 and col<num_columna:
                    if matriz[fil][col]=="X":
                        matriz[fil][col]="."
                    else: matriz[fil][col]="X" 

    contenedor[0]+=1
    etiqueta_movimientos.set_label("Movimientos realizados: "+ str(contenedor[0]))
    imprimir_tablero()
    
    registroGolpes.append(fila)                            
    registroGolpes.append(columna) 
    boton_deshacer.set_sensitive(True)
    boton_invertir.set_sensitive(True)
    etiqueta_noticias.set_text(" ")
    comprobacion()

def genMnivel(widget,entrada_nivel):			#Genera el tablero acorde al nivel seleccionado
    for a in range(len(botones)):
			botones[a].set_visible(True)
    imagen.set_visible(False)
    try:
	nivel=int(entrada_nivel.get_text())
	
	if nivel>0:
		contenedor[2]=nivel
		del registroGolpes[:]
		etiqueta_noticias.set_text(" ")
		contenedor[1]=random.randrange(1,5)
		etiqueta_movimientos.set_label("Movimientos realizados: 0")
	
   		contenedor[0]=0
    		fila=0
    		for col in matriz:
			columna=0
			for fil in col:
				if fil=="X": matriz[fila][columna]="." 
				columna+=1 
			fila+=1 
		for a in range (100):
			botones[a].set_sensitive(True)
		boton_deshacer.set_sensitive(True)
		boton_reiniciar.set_sensitive(True)
		boton_invertir.set_sensitive(True)
	else: 
		etiqueta_noticias.set_text("Numero mayor que 0")
		exito=True
		for b in matriz:
        		for a in b:
            			if a!=".":  
					exito=False
		if exito==True:
			for a in range (len(botones)):
				botones[a].set_sensitive(False)
			imagen.set_from_file("200.gif")
			imagen.set_visible(True)
		
			for a in range(len(botones)):
				botones[a].set_visible(False)
			boton_deshacer.set_sensitive(False)
			boton_invertir.set_sensitive(False)
     
       
    
    	for a in range(nivel):
        	fil_aleatoria=random.randrange(0,num_fila,1)
        	col_aleatoria=random.randrange(0,num_columna,1)
        	golpe(fil_aleatoria,col_aleatoria)
		if contenedor[3]==True:
			while gtk.events_pending():
				gtk.main_iteration(gtk.FALSE)
			time.sleep(0.00001)
    			imprimir_tablero()
		else: imprimir_tablero()
    
    except: 
	etiqueta_noticias.set_text("No es un numero")
	exito=True
	for b in matriz:
        	for a in b:
            		if a!=".":  
				exito=False
	if exito==True:
		for a in range (len(botones)):
			botones[a].set_sensitive(False)
		imagen.set_from_file("200.gif")
		imagen.set_visible(True)
		
		for a in range(len(botones)):
			botones[a].set_visible(False)
		boton_deshacer.set_sensitive(False)
		boton_invertir.set_sensitive(False)
    if contenedor[3]==True:
	reiniciar(variable_inutil)		#este reiniciar sirve por si estas en modo animacion y mientras se genera el tablero clickas algun boton del juego, para que no se modifique la matriz inicial pensada por el juego
	etiqueta_noticias.set_text("")

def imprimir_tablero():									#Refleja en los botones la situacion de la matriz.
	contador=0
	for col in matriz:
		for fil in col:

			
			if fil==".": 
				botones[contador].set_label("")
				map = botones[contador].get_colormap() 
				color = map.alloc_color("black")
				style = botones[contador].get_style().copy()
				style.bg[gtk.STATE_NORMAL] = color
				botones[contador].set_style(style)
			if fil=="X": 
				botones[contador].set_label("")
				map = botones[contador].get_colormap()
				if contenedor[1]==1: 
					color = map.alloc_color("red")
				elif contenedor[1]==2: 
					color = map.alloc_color("gold")
				elif contenedor[1]==3: 
					color = map.alloc_color("green")
				elif contenedor[1]==4: 
					color = map.alloc_color("blue")
				style = botones[contador].get_style().copy()
				style.bg[gtk.STATE_NORMAL] = color
				botones[contador].set_style(style)
			contador+=1

def deshacer(widget):										#Hace una jugada atras
	try:                                                           
            golpe(registroGolpes[len(registroGolpes)-2],registroGolpes[len(registroGolpes)-1])
            imprimir_tablero()
            registroGolpes.pop()
            registroGolpes.pop()
		
        except: etiqueta_noticias.set_text("Ya estas en el tablero inicial")

def comprobacion():											#Comprueba si el tablero ha sido resuelto, y actualiza la
	exito=True												#lista de puntuaciones guardando la mejor obtenida hasta el
	for b in matriz:										#momento
        	for a in b:
            		if a!=".":  
				exito=False
	if exito==True:
		for a in range (len(botones)):
			botones[a].set_sensitive(False)
		imagen.set_from_file("winner200.gif")
		imagen.set_visible(True)
		
		for a in range(len(botones)):
			botones[a].set_visible(False)
		boton_deshacer.set_sensitive(False)
		boton_invertir.set_sensitive(False)
		comprobador=True
		try:
				if len(niveles_puntuaciones)!=0:		
					for a in niveles_puntuaciones[::2]:			
						if contenedor[2]==int(a):
							if contenedor[0]<int(niveles_puntuaciones[niveles_puntuaciones.index(a)+1]):
								niveles_puntuaciones[niveles_puntuaciones.index(a)+1]=contenedor[0]
								comprobador=False
							else: comprobador=False
				if comprobador==True:
					niveles_puntuaciones.append(contenedor[2])
					niveles_puntuaciones.append(contenedor[0])
				escribir_puntuacion()				
		except:
				if comprobador==True:
					niveles_puntuaciones.append(contenedor[2])
					niveles_puntuaciones.append(contenedor[0])
				escribir_puntuacion()

	
		
def reiniciar(widget):											#Vuelve al tablero inicial, para empezar de 0.
	imagen.set_visible(False)
	for a in range(len(botones)):
			botones[a].set_visible(True)
	if registroGolpes!=[]:
		for a in range (len(registroGolpes)/2):
			deshacer(variable_inutil)
			if contenedor[3]==True:
				while gtk.events_pending():
					gtk.main_iteration(gtk.FALSE)
				time.sleep(0.05)
		contenedor[0]=0
		etiqueta_movimientos.set_label("Movimientos realizados: "+ str(contenedor[0]))
		for a in range (100):
			botones[a].set_sensitive(True)
	else: etiqueta_noticias.set_text("Ya estas en el tablero inicial")
	
			
def puntuaciones(widget):									#Muestra en una etiqueta las mejores puntuaciones en sus
	etiqueta_movimientos.set_text("")						#respectivos niveles, en una etiqueta; activa el boton
	etiqueta_noticias.set_text("")							#de reiniciar puntuaciones, y el de vuelta al tablero
	boton_resetpuntu.set_sensitive(True)
	boton_atras.set_sensitive(True)	
	boton_puntuaciones.set_sensitive(False)
	boton_nivel.set_sensitive(False)
	boton_reiniciar.set_sensitive(False)
	boton_deshacer.set_sensitive(False)
	boton_invertir.set_sensitive(False)
	texto_etiqueta=""
	etiqueta_puntuaciones.set_visible(True)
	imagen.set_visible(False)
	for a in range(len(botones)):
		botones[a].set_visible(False)
	for a in range (len(niveles_puntuaciones)):
		niveles_puntuaciones[a]=int(niveles_puntuaciones[a])
	try:
		for a in range(1,max(niveles_puntuaciones[::2])+1):
			for b in niveles_puntuaciones[::2]:
				if a==b:
					texto_etiqueta=str(texto_etiqueta)+chr(13)+str(("Nivel "+str(a)+" : "+str(niveles_puntuaciones[niveles_puntuaciones.index(b)+1])+" movimientos."))
					etiqueta_puntuaciones.set_text(texto_etiqueta)
	except:a=0			

		
	for a in range (len(niveles_puntuaciones)):
		niveles_puntuaciones[a]=str(niveles_puntuaciones[a])
def leer_puntuaciones():                                         #Abre el fichero en modo lectura, lee la informacion
        	texto=open("puntuacionesGtk.txt",'r')				 #guaradada y la almacena en una lista.
		linea=texto.readline()
		linea=linea.split()
		texto.close()
		return linea


		
	
def escribir_puntuacion():										#Escribe en el fichero la lista con las mejores
	texto=open("puntuacionesGtk.txt",'w')						#puntuaciones y sus respectivos movimientos.
	for a in range(len(niveles_puntuaciones)):
		texto.write(str(niveles_puntuaciones[a]))
		texto.write(" ")
	texto.close()

def atras(widget):												#Sale del modo puntuaciones para volver al tablero
	exito=True
	for b in matriz:
        	for a in b:
            		if a!=".":  
				exito=False
	if exito==True:
		for a in range (len(botones)):
			botones[a].set_sensitive(False)
		imagen.set_from_file("200.gif")
		imagen.set_visible(True)
		
		for a in range(len(botones)):
			botones[a].set_visible(False)
		boton_deshacer.set_sensitive(False)
		boton_reiniciar.set_sensitive(False)
		boton_invertir.set_sensitive(False)	
	else:
		for a in range(len(botones)):
			botones[a].set_visible(True)
		boton_reiniciar.set_sensitive(True)
		boton_deshacer.set_sensitive(True)
		boton_invertir.set_sensitive(True)	
	boton_atras.set_sensitive(False)
	boton_resetpuntu.set_sensitive(False)
	boton_puntuaciones.set_sensitive(True)
	etiqueta_puntuaciones.set_text(" ")
	boton_nivel.set_sensitive(True)
	etiqueta_puntuaciones.set_visible(False)
	etiqueta_movimientos.set_text("Movimientos realizados: "+ str(contenedor[0]))
	etiqueta_noticias.set_text("")

def reiniciar_puntuaciones(widget):								#Resetea la lista de puntuaciones
	
	try:
		global niveles_puntuaciones
		remove ("puntuacionesGtkmod.txt")
		if niveles_puntuaciones==[]:
			etiqueta_puntuaciones.set_text("No hay puntuaciones"+chr(13)+ "          guardadas!")	
		else:
			niveles_puntuaciones=[]
			etiqueta_puntuaciones.set_text("Puntuaciones reseteadas!")
	except: 
		etiqueta_puntuaciones.set_text("No hay puntuaciones"+chr(13)+ "          guardadas!")	

def checable(widget):										#Lee si esta activado el tick para animar o no la creacion
	if contenedor[3]==False:								#del tablero
		contenedor[3]=True
	else: contenedor[3]=False

def invertir(widget):
	for b in range(0,10):										#momento
        	for a in range(0,10):
                    if matriz[b][a]=="X":
                        matriz[b][a]="."
		    else: matriz[b][a]="X"
			
	imprimir_tablero()
	

###################################################################################


matriz=[]												#Matriz interna
registroGolpes=[]										#Registro de coordenadas pulsadas
niveles_puntuaciones=[]									#Registro del nivel jugado con su mejor puntuacion
num_fila=10
num_columna=10
botones=[]												#Lista de botones

variable_inutil=0

contenedor=[0,1,0,True]									#Golpes,Aleatorio,Nivel,Tick

try:                                                    #Abre el fichero en modo lectura, sino existe lo crea.
        texto=open("puntuacionesGtk.txt",'r')
	texto.close()
	niveles_puntuaciones=leer_puntuaciones()
except: 
	texto=open("puntuacionesGtk.txt",'w')
        texto.close()



for x in range(num_fila):                      #Crea una matriz de listas acorde al numero de filas y columnas deseados.
        matriz.append(["."]*num_columna)

tabla = gtk.Table (num_fila+2,num_columna, homogeneous=True)			#Creas tabla y ventana principales
ventana = gtk.Window()
for i in range(0,num_fila):												#Crea los botones y les dota de coordenadas

	for j in range(0,num_columna):
	 
		boton = gtk.Button(str("."))
		botones.append(boton)
		boton.posicion=(i,j)
		boton.set_sensitive(False)
		boton.hide()
		boton.connect("clicked",golpeBoton)
		tabla.attach(boton,i,1+i,1+j,2+j)
		

etiqueta_noticias= gtk.Label("")										#Crea y coloca en la tabla las etiquetas,botones
tabla.attach(etiqueta_noticias,num_fila-2,num_fila,11,12)				#y demas elementos necesarios, poniendolos a la
																		#sensibilidad adecuada.
etiqueta_movimientos= gtk.Label("Movimientos realizados: "+ str(contenedor[0]))
tabla.attach(etiqueta_movimientos,5,7,11,12)

boton_invertir=gtk.Button("Invertir")
boton_invertir.connect("clicked",invertir)
tabla.attach(boton_invertir,7,9,11,12)
boton_invertir.set_sensitive(False)


boton_nivel= gtk.Button(str("Introducir Nivel"))
tabla.attach(boton_nivel,6,8,0,1)

boton_atras=gtk.Button("Atras")
boton_atras.set_sensitive(False)
boton_atras.connect("clicked",atras)
tabla.attach(boton_atras,0,1,11,12)

boton_resetpuntu=gtk.Button("Reiniciar Puntuaciones")
boton_resetpuntu.set_sensitive(False)
boton_resetpuntu.connect("clicked",reiniciar_puntuaciones)
tabla.attach(boton_resetpuntu,1,3,11,12)

boton_deshacer= gtk.Button(str("Deshacer"))
boton_deshacer.set_sensitive(False)
tabla.attach(boton_deshacer,num_fila-8,num_fila-6,0,1)
boton_deshacer.connect("clicked",deshacer)

boton_reiniciar= gtk.Button(str("Reiniciar nivel"))
boton_reiniciar.set_sensitive(False)
tabla.attach(boton_reiniciar,num_fila-10,num_fila-8,0,1)
boton_reiniciar.connect("clicked",reiniciar)

boton_puntuaciones= gtk.Button(str("Puntuaciones"))
tabla.attach(boton_puntuaciones,4,6,0,1)
boton_puntuaciones.connect("clicked",puntuaciones)

etiqueta_puntuaciones=gtk.Label()
tabla.attach(etiqueta_puntuaciones,0,10,0,10)

entrada_nivel=gtk.Entry()
entrada_nivel.set_text(str(0))
tabla.attach(entrada_nivel,8,10,0,1)

imagen=gtk.Image()
tabla.attach(imagen,0,10,1,11)

check=gtk.CheckButton("        Sin"+chr(13)+"Animacion")
tabla.attach(check,3,5,11,12)
check.connect("clicked",checable)

ventana.set_default_size(900,900)								#Define el tamaño de la ventana, la coloca en el centro,
ventana.connect ("destroy", gtk.main_quit)						#añade la tabla y termina el bucle gtk.main si se cierra
ventana.add(tabla)
ventana.set_title("Apagaluces")
ventana.set_position(gtk.WIN_POS_CENTER_ALWAYS)

ventana.show_all()
for a in range(len(botones)):
			botones[a].set_visible(False)
imagen.set_from_file("200.gif")									#Muestra el gif inicial
imagen.set_visible(True)
boton_nivel.connect("clicked",genMnivel,entrada_nivel)
imprimir_tablero()
gtk.main()

import pygame #importamos la libreria que nos permitira manejar graficos 

pygame.init() #inicializamos la libreria

#Colores

FONDO =(120, 80, 240)
BASE1 =(255, 200, 120)
BASE2 =(180, 80, 240)

NEGRO =(0, 0, 0)
MARRON =(180, 120, 55)
ROJO =(255, 0, 0)
NARANJA =(245, 150, 0)
AMARILLO =(255, 255, 20)
VERDE =(0, 255, 0)
AZUL =(50, 50, 255)
VIOLETA =(150, 0, 160)
GRIS =(120, 120, 120)
BLANCO =(255, 255, 255)
PLATA =(220, 220, 220)
ORO =(205, 170, 55)
OTRO =(120, 80, 240)

#Diccionarios de valores banda y tolerancia
BANDAS = {NEGRO: "Negro", MARRON:"Marron", ROJO:"Rojo", NARANJA: "Naranja", AMARILLO: "Amarillo", VERDE: "Verde", AZUL: "Azul", VIOLETA: "Violeta", GRIS: "Gris", BLANCO: "Blanco", PLATA: "Plata", ORO:"Oro"}
BANDAS_C = [NEGRO, MARRON, ROJO, NARANJA, AMARILLO, VERDE, AZUL, VIOLETA, GRIS, BLANCO]
BANDAS_4 = [NEGRO, MARRON, ROJO, NARANJA, AMARILLO, VERDE, AZUL, VIOLETA, PLATA, ORO]
BANDAS_T = (PLATA, ORO, ROJO)
TOLERANCIAS= (10,5,2)


T_VENTANA=(500,500) #Fijamos el las dimensiones de nuestra ventana

#texto
tamFuente=30
FUENTE=pygame.font.Font(None,tamFuente)
pos_texto=[50,400]

P_BOTON1=(50, 50)
P_BOTON2=(200, 50)
T_BOTON=(120,50)
P_TB1=(65,65)
P_TB2=(215,65)
texto_boton1=FUENTE.render("4 bandas",1,NEGRO)
texto_boton2=FUENTE.render("5 bandas",1,NEGRO)


#variables de la resistencia
ALTO=100
ANCHO=50
GAP=15
bandas=4
POS0=(80,200)
POS_T1=(POS0[0]-GAP*2,POS0[1]+150)
POS_T2=(POS_T1[0],POS_T1[1]+40)
POS_T3=(POS_T2[0],POS_T2[1]+40)


T_BANDA=(ANCHO,ALTO)
T_PUNTA=(ANCHO*2,ALTO+GAP*2)
T_CUERPO=((ANCHO+GAP)*5,ALTO)
P_CUERPO=POS0
P_PUNTA1=(P_CUERPO[0]-ANCHO*1.6, P_CUERPO[1]-GAP)
P_PUNTA2=(P_CUERPO[0]+T_CUERPO[0]-ANCHO/3, P_CUERPO[1]-GAP)
P_BANDA1=P_CUERPO
P_BANDA2=(P_BANDA1[0]+ANCHO+GAP, P_CUERPO[1])
P_BANDA3=(P_BANDA2[0]+ANCHO+GAP, P_CUERPO[1])
P_BANDA4=(P_BANDA3[0]+ANCHO+GAP, P_CUERPO[1])
P_BANDAT=(P_BANDA4[0]+ANCHO+GAP*2, P_CUERPO[1])

colorxbanda=[1, 0,0,0,0] #array de indices de color de banda

ventana = pygame.display.set_mode(T_VENTANA) #inicializamos la ventana
pygame.display.set_caption("Lector de Resistencias") #nombramos la ventana

clock=pygame.time.Clock()   #inicializamos la variable de actualizacion de pantalla
salir=False 
while salir == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir= True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos() #obtenemos la posicion del mouse en la ventana al hacer click
            #Aquí comprobaremos si estamos clickeando algun boton o banda.
            if pos[0]>P_BOTON1[0] and pos[1]>P_BOTON1[1] and pos[0]<P_BOTON1[0]+T_BOTON[0] and pos[1]<P_BOTON1[1]+T_BOTON[1] :
                bandas=4
            elif  pos[0]>P_BOTON2[0] and pos[1]>P_BOTON2[1] and pos[0]<P_BOTON2[0]+T_BOTON[0] and pos[1]<P_BOTON2[1]+T_BOTON[1]:
                bandas=5
            if not ((pos[0]<P_CUERPO[0] or pos[0]>P_CUERPO[0]+T_CUERPO[0]) or (pos[1]<P_CUERPO[1] or pos[1]>P_CUERPO[1]+T_CUERPO[1])):
                if pos[0]<P_BANDA1[0]+T_BANDA[0]:
                    colorxbanda[0]+=1
                    if colorxbanda[0]>=len(BANDAS_C):
                        colorxbanda[0]=0 
                elif pos[0]<P_BANDA2[0]+T_BANDA[0]:
                    colorxbanda[1]+=1
                    if colorxbanda[1]>=len(BANDAS_C):
                        colorxbanda[1]=0
                elif pos[0]<P_BANDA3[0]+T_BANDA[0]:
                    colorxbanda[2]+=1
                    if colorxbanda[2]>=len(BANDAS_C):
                        colorxbanda[2]=0
                elif pos[0]<P_BANDA4[0]+T_BANDA[0]:
                    colorxbanda[3]+=1
                    if colorxbanda[3]>=len(BANDAS_C):
                        colorxbanda[3]=0
                elif pos[0]<P_BANDAT[0]+T_BANDA[0]:
                    colorxbanda[4]+=1
                    if colorxbanda[4]>=len(BANDAS_T):
                        colorxbanda[4]=0


    ventana.fill((200,233,244)) #pantalla en blanco
    #dibujamos botones
    pygame.draw.rect(ventana, NEGRO, (P_BOTON1,T_BOTON),2 if bandas==5 else 4,8)
    pygame.draw.rect(ventana, NEGRO, (P_BOTON2,T_BOTON),2 if bandas==4 else 4,8)
    ventana.blit(texto_boton1,P_TB1)
    ventana.blit(texto_boton2,P_TB2)

    #dibujamos la resistencia
    color_resistencia=BASE1 if bandas==4 else BASE2
        #forma(ventana, color, posicion tamaño, borde)
    pygame.draw.ellipse(ventana, color_resistencia, [P_PUNTA1,T_PUNTA], 0)
    pygame.draw.ellipse(ventana, color_resistencia, [P_PUNTA2,T_PUNTA], 0)
    pygame.draw.rect(ventana, color_resistencia, [P_CUERPO, T_CUERPO], 0)
    pygame.draw.rect(ventana, BANDAS_C[colorxbanda[0]], [P_BANDA1, T_BANDA], 0)
    pygame.draw.rect(ventana, BANDAS_C[colorxbanda[1]], [P_BANDA2, T_BANDA], 0)
    pygame.draw.rect(ventana, BANDAS_C[colorxbanda[2]], [P_BANDA3, T_BANDA], 0)
    if bandas==5:
        pygame.draw.rect(ventana, BANDAS_4[colorxbanda[3]], [P_BANDA4, T_BANDA], 0)
    pygame.draw.rect(ventana, BANDAS_T[colorxbanda[4]], [P_BANDAT, T_BANDA], 0)
   
    
    
    if colorxbanda[3] == 8: 
        mult= -1
    elif colorxbanda[3] == 9:
        mult= -2
    else:
        mult=colorxbanda[3]
    
    valor=(colorxbanda[0]*10+colorxbanda[1])*(10**colorxbanda[2]) if bandas==4 else (colorxbanda[0]*100+colorxbanda[1]*10+colorxbanda[2])*(10**mult)
    if(valor>1000000):
        valor/=1000000
        unidad=" M"
    elif (valor>1000):
        valor/=1000
        unidad=" K"
    else:
        unidad=" "
    
    
    texto_colores=""
    for num in range(3):
        texto_colores+=BANDAS[BANDAS_C[colorxbanda[num]]] + " "
    if bandas==4:
        texto_colores+="          "
    else:
        texto_colores+=BANDAS[BANDAS_4[colorxbanda[3]]] + " "

    texto_colores+=BANDAS[BANDAS_T[colorxbanda[4]]]
    texto_lectura="El valor de la resistencia es de " + str(valor) + unidad + "Ohms"
    texto_lectura2="Y con una tolerancia del " + str(TOLERANCIAS[colorxbanda[4]]) + "%"
    epigrafe=FUENTE.render(texto_colores,1,NEGRO)
    epigrafe1=FUENTE.render(texto_lectura,1,NEGRO)
    epigrafe2=FUENTE.render(texto_lectura2,1,NEGRO)
    ventana.blit(epigrafe, POS_T1)
    ventana.blit(epigrafe1, POS_T2)
    ventana.blit(epigrafe2, POS_T3)
    
    pygame.display.flip()
    clock.tick(5)

            
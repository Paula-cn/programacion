"""
Created on Fri May  1 19:46:32 2020

@author: sofir
"""

import pygame #Se importa pygame para hacer la gráfica
class grafica(): #Crea la clase gráfica
    
    def inicio(self, contar): #Contar es el resultado numérico del test
        pygame.init() #Empieza pygame
        self.display = pygame.display.set_mode((500, 200)) #Crea la ventana de pygame de 500x200
        self.display.fill((255,255,255)) #La llena con color blanco
        while True: #Mantiene la ventana abierta
            ev = pygame.event.poll() #Busqua un evento
            if ev.type == pygame.QUIT: #Revisa si se presionó el botón cerrar
                break #Si se presionó, rompe el while y permite cerrar la ventana
            pygame.display.flip()
            self.cuadro(contar) #Llama la función cuadro
        
        pygame.quit() #Cierra pygame
        
    def cuadro(self, contar): 
        colores = [(0,182,12),(90,185,97),(47,131,195),(46,56,189)] #Los colores son verde oscuro, verde claro, azul claro y azul oscuro
        x = 10 #Para que haya un borde, la gráfica empieza en 10
        fuente = pygame.font.SysFont("Times New Roman",15, False, False) #Da estilo al texto con fuente, tamaño, sin itálica y sin negrita
        orientacion = ["Izquierda", "Centro izquierda", "Centro derecha", "Derecha"]#Lista de las cuatro orientaciones que arroja el test

#Como son cuatro orientaciones posible, se itera 4 veces: cambia la coordenada x de inicio y final, el color y el texto debajo de cada cuadro
        for i in range(4): 
            x2 = x + 99#x es donde inicia cada cuadro y x2 donde termina, el ancho del rectángulo es 99, así que se x2 = x+99
            pygame.draw.polygon(self.display, colores[i], [(x,20), (x,70),(x2,70),(x2,20)])#Dibuja los 4 rectángulos, uno al lado del otro
            texto_titulo = fuente.render("Su orientación política es:", False, (0,0,0))#Diseña el texto de título
            self.display.blit(texto_titulo, (10,0))#Crea el título de la gráfica encima de ella
            texto_orientacion = fuente.render(orientacion[i], False, (0,0,0))#Diseña el texto de la orientación e itera entre las 4 orientaciones políticas
            self.display.blit(texto_orientacion, (x,20))#Empieza el texto donde empieza cada rectángulo
            x = x2#El siguiente empieza donde termina el anterior

#A continuación se crea un círculo, un triángulo y un texto que señala donde queda la persona que toma el test, como el test va de 10 a 30 y la gráfica de 0 a 400, 1 en el test equivale a 20 en la gráfica
        if contar == 10: #Si el resultado del test es 10, al restarle 10 para volver a 0 y al multiplicarlo por 20, las figuras salen en el 0. Restándole solo 9 se evita eso.
            contar = (contar-9)*20
        else: #Si el resultado del test es mayor a 10
            contar = (contar-10)*20
        texto_resultado = fuente.render("Usted está aquí", False, (0,0,0)) #Pone estilo al texto
        pygame.draw.circle(self.display, (0,0,0), (contar,45), 5) #Pone el círculo en y = la mitad de la altura de la gráfica y x= equivalente del resultado en la gráfica
        pygame.draw.polygon(self.display, (0,0,0), [(contar,80), (contar+5,90),(contar-5,90)])#Pone el triángulo debajo de la gráfica en el mismo x del círculo
        self.display.blit(texto_resultado, (contar+20,75)) #Pone el texto en y= debajo de la gráfica y x= al lado del triángulo
        
import tkinter #Se importa tkinter para hacer el test
class test_politico(): #Crea la clase test político
        
    def __innit__(self, preguntas, respuestas, view): 
        self.preguntas = preguntas
        self.respuestas = respuestas
        self.view = view
        self.resultado = 0 #Inicia contador de resultado
        self.index = 0 #Inicia índice del cambio de preguntas y respuestas
    
    def cuestionario(self):
            preguntas = []#Crea la lista de las preguntas
            respuestas = []#Crea la lista de las respuestas
            archivo = open("questions.txt", "r")#Abre el archivo donde están las preguntas y respuestas

            for a in range (10):#Como hay 10 preguntas, se repite 10 veces
                    respuestasPorPregunta = []#Crea la lista de las respuestas de cada pregunta
                    preguntas.append(archivo.readline())#Añade las preguntas a la lista de preguntas
                    respuestasPorPregunta.append(archivo.readline())#Añade cada respuesta a la lista de respuestas de esa pregunta
                    respuestasPorPregunta.append(archivo.readline())
                    respuestasPorPregunta.append(archivo.readline())
                    respuestas.append(respuestasPorPregunta)#Añade la lista de respuestas de la pregunta a la lista más grande. Hace una lista de listas de respuestas
                    
            archivo.close()#Cierra el archivo cuando acaba el for
            return preguntas, respuestas#Devuelve la lista de preguntas y la lista de listas de respuestas
        
    
    def inicio_fin(self):#Crea el botón de inicio 
        tkinter.Button(ventana_inicial, text="Empezar el test", command = lambda *args: self.cambio()).pack()#Cuando se hace click en el botón entra a la función de cambio

        
        
    def hacerPregunta(self):
        self.view = tkinter.Tk()#Crea la ventana
        tkinter.Label(self.view, text=self.preguntas[self.index-1], wraplength = 500, width = 80, bg = ("snow")).pack()#Hace la pregunta
        #Crea los botones por pregunta, accede a la lista de respuestas por lista y al elemento de la lista, cuando se hace click en el botón va a la función opción con la letra correspondiente
        tkinter.Button(self.view, text=self.respuestas[self.index-1][0], anchor=tkinter.W, justify=tkinter.LEFT, padx=2, bg = ("linen"), command = lambda *args: (self.opcion('A')), wraplength = 500, width = 80).pack()
        tkinter.Button(self.view, text=self.respuestas[self.index-1][1], anchor=tkinter.W, justify=tkinter.LEFT, padx=2, bg = ("linen"), command = lambda *args: (self.opcion('B')), wraplength = 500, width = 80).pack()
        tkinter.Button(self.view, text=self.respuestas[self.index-1][2], anchor=tkinter.W, justify=tkinter.LEFT, padx=2, bg = ("linen"), command = lambda *args: (self.opcion('C')), wraplength = 500, width = 80).pack()

    def opcion(self, letra): #Esta función hace una equivalencia entre la opción y lo que se le suma al resultado
            if(letra == 'A'):
                self.resultado += 1
            elif(letra == 'B'):
                self.resultado += 2
            elif(letra == 'C'):
                self.resultado += 3
            self.cambio()#Al final, llama de nuevo a la función de cambio
        
    def cambio(self):
        if self.index == 10: #Si ya se llegó al final de la lista de preguntas, cierra la ventana y hace la gráfica
            self.view.destroy() #Cierra la ventana
            final = grafica() #Crea un objeto de clase gráfica
            final.inicio(self.resultado) #Hace la gráfica
            print ("Resultado final numérico: ", self.resultado)#Imprime el resultado numérico para comprobar la respuesta
        
        else: #Si el índice es menor a 10, cierra la ventana, aumenta el índice en 1 y hace la siguiente pregunta
            self.view.destroy()
            self.index += 1
            self.hacerPregunta()        
    
        
#Ejecución 
ventana_inicial = tkinter.Tk()#Crea una ventana inicial
view = tkinter.Frame(ventana_inicial, width=500, bg="white")#Parámetros para hacer el botón de inicio
orientacion = test_politico()#Crea un obtejo tipo test
preguntas, respuestas = orientacion.cuestionario()#Crea las listas del cuestionario 
orientacion.__innit__(preguntas, respuestas, view)#Crea los objetos con self.
orientacion.inicio_fin()#Llama a la función de inicio
ventana_inicial.mainloop()#Cierra
#Al final se debe cerrar manualmente la ventana inicial y la de la gráfica


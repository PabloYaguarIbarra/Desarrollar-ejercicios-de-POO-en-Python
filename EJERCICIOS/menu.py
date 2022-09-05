import os
import time

from POO.Cuenta import Cuenta
from paquete1.funciones_numericas import multiplicar,potenciar
from POO.Curso import *
from POO.Herencia import *
from POO.HerenciaMultiple import *
from POO.Polimorfismo import *
from POO.RelacionesClases import *


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Adios!")
c1 = True
while c1:
    print('1.Hola Mundo\n''2.Variables\n''3.Conversiones\n''4.Numero_Operaciones\n''5.Concatenacion\n''6.Cadenas\n''7.Tuplas\n''8.Listas\n''9.Diccionnarios\n''10.IngresoDatios\n''11.If_Else\n''12.Funciones\n''13.Operadpres_Logicos\n''14.Operadores_Ternarios\n''15.Range\n''16.For\n''17.If_In\n' '18.Factorial\n''19.While\n''20.Excepsiones\n''21.Generadores2\n''22.Generadores 2\n''23.Raise\n''24.Importacion de archivos externos\n''25.Constructor, Encapsulamiento y Metodo __str__\n''26.Metodo __Init__\n''27.Herencia\n''28.Herencia Multiple\n''29.Polimorfismo\n''30.Relaciones Clases\n''31.Salir')
    opc = input('Escoge Una Opcion: ')
    os.system("cls")
    if opc == '1':
        print('Hola Mundo')
        t = 5
        countdown(int(t))
    else:
        if opc == '2':
            nombre = 'Pablo'
            print(nombre)
            edad = 20
            print(edad)
            edad = True
            print(edad)
            sueldo = 0
            print(sueldo)
            t = 5
            countdown(int(t))
        else:
            if opc == '3':
                numero1 = "35"
                numero2 = "18"
                print(numero1 + numero2)
                num1 = int(numero1)
                num2 = int(numero2)
                print(num1 + num2)
                sueldo = 1200.43
                sueldoEntero = int(sueldo)
                print(sueldoEntero)
                valor = "4500.89"
                valorDecimal = float(valor)
                print(valorDecimal * 3)
                edad = 100
                print(len(str(edad)))
                for i in range(5):
                    print((i + 1) * "* ")
                t = 5
                countdown(int(t))
            else:
                if opc == '4':
                    num1 = 20
                    num2 = 4
                    print("Suma:", (num1 + num2))
                    print("Resta:", (num1 - num2))
                    print("Multiplicación:", (num1 * num2))
                    print("División:", (num1 / num2))
                    print("División Exacta:", (num1 // num2))
                    print("Potencia:", (num1 ** num2))
                    t = 5
                    countdown(int(t))
                else:
                    if opc == '5':
                        texto1 = "Hola"
                        texto2 = "Mundo"
                        textoFinal = texto1 + " " + texto2
                        print(textoFinal)
                        print("El saludo es: %s %s" % (texto1, texto2))
                        saludoFinal = "Saludo: {0} {1}".format(texto1, texto2)
                        print(saludoFinal)
                        saludoFinal2 = "Saludo: {y} {x}".format(x=texto2, y=texto1)
                        print(saludoFinal2)
                        t = 5
                        countdown(int(t))
                    else:
                        if opc == '6':
                            texto = "bienvenidos a mi deber"
                            print(texto)
                            print(texto.lower())
                            print(texto.upper())
                            print(texto.title())  # Convierte una cadena a un formato de título.
                            print(texto.find("al"))  # Posición donde encuentra la cadena o porción.
                            print(texto.count("e"))  # Cantidad de ocurrencias de una letra o porción.
                            textoFinal = texto.replace("e", "3")
                            print(textoFinal)
                            valor = texto.isnumeric()  # Arroja true o false dependiendo si es un número.
                            print(valor)
                            cadenaSeparada = texto.split(" ")
                            print(cadenaSeparada)
                            t = 5
                            countdown(int(t))
                        else:
                            if opc == '7':
                                tupla = (1, 2, 3)
                                print(tupla)
                                tupla2 = (7, "Oscar", True, 450.1, 16 + 7j, 15, "Felicidad", False)
                                print(tupla2)
                                tupla3 = (9, 3, (4, 5, 6))
                                print(tupla3)
                                print(tupla2[1])
                                print(tupla2[-1])  # Acceder al último elemento.
                                print(tupla2[0:4])
                                print(tupla2[-2])
                                a, b, c = tupla
                                print(a)
                                print(b)
                                print(c)
                                tuplaFinal = tupla + tupla3
                                print(tuplaFinal)
                                print(tuplaFinal.count(21))
                                print(tuplaFinal.index(3))
                                t = 5
                                countdown(int(t))
                            else:
                                if opc == '8':
                                    lista1 = ["Oscar", 25, 98.3, True, "Flavio", 56.3]
                                    print(lista1)
                                    print(lista1[:])
                                    print(lista1[2])
                                    print(lista1[-1])
                                    print(lista1[0:3])
                                    print(lista1[:2])
                                    print(lista1[3:])
                                    lista1.append("Pablo")
                                    print(lista1)
                                    lista1.insert(4, "Ecuador")
                                    print(lista1)
                                    lista1.extend(["Alejandro", 110, False])
                                    print(lista1)
                                    print(lista1.index("Flavio"))
                                    lista1.remove(56.3)
                                    print(lista1)
                                    lista1.pop()
                                    print(lista1)
                                    lista2 = ["Guayaquil", "Milagro"]
                                    lista3 = lista1 + lista2
                                    print(lista3)
                                    print(lista2 * 4)
                                    print("Pablo" in lista1)
                                    t = 5
                                    countdown(int(t))
                                else:
                                    if opc == "9":
                                        miDiccionario = {"España": "Madrid", "Perú": "Lima", "Alemania": "Berlín"}
                                        print(miDiccionario["Perú"])
                                        print(miDiccionario)
                                        miDiccionario["Venezuela"] = "Caracas"
                                        print(miDiccionario)
                                        miDiccionario["España"] = "Barcelona"
                                        print(miDiccionario)
                                        del miDiccionario["España"]
                                        print(miDiccionario)
                                        dic2 = {"García": "Oscar", 25: True, "Sueldo": 150.80}
                                        print(dic2[25])
                                        llaves = ("España", "Francia", "Inglaterra")
                                        dicPaises = {llaves[0]: "Madrid", llaves[1]: "París", llaves[2]: "Londres"}
                                        print(dicPaises)
                                        datosPersonales = {"Ape": "García",
                                                           "Anios": {1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014}}
                                        print(datosPersonales)
                                        print(datosPersonales["Anios"])
                                        print(datosPersonales.get('Apel', "Oscar"))
                                        print(datosPersonales.keys())
                                        valores = tuple(datosPersonales.values())
                                        print(valores)
                                        t = 5
                                        countdown(int(t))
                                    else:
                                        if opc == "10":
                                            nombre = input("Ingrese su nombre: ")
                                            edad = int(input("Ingrese su edad: "))
                                            sueldo = float(input("Ingrese su sueldo: "))
                                            print("Hola, " + nombre)
                                            edadFutura = edad + 20
                                            print("Tu edad es:", edad)
                                            print("Tu edad (dentro de 20 años) será:", edadFutura)
                                            print("Tu sueldo es:", sueldo)
                                            t = 5
                                            countdown(int(t))
                                        else:
                                            if opc == '11':
                                                edad = int(input("Ingrese su edad: "))
                                                if edad > 18:
                                                    print("Eres mayor de edad.")
                                                elif edad == 18:
                                                    print("Tienes 18 años!")
                                                else:
                                                    print("No eres mayor de edad.")
                                                t = 5
                                                countdown(int(t))
                                            else:
                                                if opc == "12":
                                                    def saludar():
                                                        print("Yaguar")
                                                        print("Pablo")
                                                        print("IwachuU")
                                                        return "Hola"
                                                    print(saludar())
                                                    def evaluarSueldoMinimo(sueldo):
                                                        if sueldo >= 850:
                                                            print("Cumples con el sueldo")
                                                        else:
                                                            print("Ganas menos que el sueldo mínimo")
                                                        evaluarSueldoMinimo(100)
                                                    t = 5
                                                    countdown(int(t))
                                                else:
                                                    if opc == "13":
                                                        distancia = 400
                                                        numeroHermanos = 3
                                                        salarioPadres = 3000
                                                        tieneBeneficio = False
                                                        if (distancia > 1000 and numeroHermanos > 2) or salarioPadres < 2000:
                                                            tieneBeneficio = True
                                                        print(not tieneBeneficio)
                                                        if (5 > 3) or (8 < 6):
                                                            print("Verdad")
                                                        t = 5
                                                        countdown(int(t))
                                                    else:
                                                        if opc == '14':
                                                            sexos = ("Hombre", "Mujer")
                                                            posicion = True
                                                            sexo = sexos[posicion]  # Mujer
                                                            print(sexo)
                                                            sexo = sexos[not posicion]  # Hombre
                                                            print(sexo)
                                                            t = 5
                                                            countdown(int(t))

                                                        else:
                                                            if opc == '15':
                                                                numeros = range(5)  # [0, 1, 2, 3, 4]
                                                                print("Rango de 5: ",numeros[1])
                                                                numeros1 = range(4, 10)  # [4, 5, 6, 7, 8, 9]
                                                                print("Un numero en el rango de 4 a 10: ",numeros1[5])
                                                                numeros2 = range(10, 100, 8)
                                                                print("Un numero en el rango de 10 a 100 a 8: ",numeros2[9])  # [10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98]
                                                                t = 5
                                                                countdown(int(t))
                                                            else:
                                                                if opc == "16":
                                                                    for i in range(1, 13):
                                                                        print("{0} x {1} es: {2}".format(i, i, (i * i)))
                                                                    for nom in ["Karen", "Oscar", "Héctor", "Leonardo"]:
                                                                        print(
                                                                            "Cantidad de letras de {0} es: {1}".format(
                                                                                nom, len(nom)))
                                                                    t = 5
                                                                    countdown(int(t))
                                                                else:
                                                                    if opc == "17":
                                                                        print("-- Materias --")
                                                                        print("Poo - Bdd - Estrucuta de D. - Administracion G.")
                                                                        curso = input("Ingrese el curso deseado: ")
                                                                        if curso in ("Poo - Bdd - Estrucuta de D. - Administracion G."):
                                                                            print("Curso {0} seleccionado.".format(curso))
                                                                        else:
                                                                            print("No existe ese curso...")
                                                                        t = 5
                                                                        countdown(int(t))
                                                                    else:
                                                                        if opc == "18":
                                                                            numero = int(
                                                                            input("Ingrese un número: "))
                                                                            factorial = 1
                                                                            for n in range(1, (numero + 1)):
                                                                                factorial = factorial * n
                                                                            print("El factorial de {0} es: {1}".format(numero, factorial))
                                                                            t = 5
                                                                            countdown(int(t))
                                                                        else:
                                                                            if opc == "19":
                                                                                inicio = 2
                                                                                while inicio <= 100:
                                                                                    print("Número par: {0}".format(inicio))
                                                                                    inicio += 2
                                                                                    print("Hemos terminado el bucle while.")
                                                                                t = 5
                                                                                countdown(int(t))
                                                                            else:
                                                                                if opc == "20":
                                                                                    numero1 = 20
                                                                                    numero2 = 2
                                                                                    # print("La división de {0} entre {1} es: {2}".format(numero1, numero2, (numero1 / numero2)))
                                                                                    try:
                                                                                        resultado = numero1 / numero2
                                                                                    # except:
                                                                                    except ZeroDivisionError:
                                                                                        print("No se puede dividir entre 0...")
                                                                                    finally:
                                                                                        print("Yo siempre aparezco.")
                                                                                    print("Aquí termina mi programa.")
                                                                                    t = 5
                                                                                    countdown(int(t))
                                                                                else:
                                                                                    if opc == "21":
                                                                                        def generadorMultiplos7(limite=10):
                                                                                            numero = 1
                                                                                            while numero <= limite:
                                                                                                yield numero * 7  # Ceder. La instrucción "yield" genera un objeto iterable.
                                                                                                numero = numero + 1
                                                                                        obtieneMultiplos7 = generadorMultiplos7(10)
                                                                                        print(next(obtieneMultiplos7))
                                                                                        print("Acá hay 300 líneas de código...")
                                                                                        print(next(obtieneMultiplos7))
                                                                                        print("Acá hay 1000 líneas de código...")
                                                                                        print(next(obtieneMultiplos7))
                                                                                        t = 5
                                                                                        countdown(int(t))
                                                                                    else:
                                                                                        if opc == "22":
                                                                                            def devuelveLenguajes(*lenguajes):
                                                                                                for leng in lenguajes:
                                                                                                    yield from leng
                                                                                            lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")
                                                                                            print(next(lenguajesObtenidos))
                                                                                            print(next(lenguajesObtenidos))
                                                                                            t = 5
                                                                                            countdown(int(t))
                                                                                        else:
                                                                                            if opc == "23":
                                                                                                def evaluarNota(nota):
                                                                                                    if nota < 0:
                                                                                                        raise ValueError("Valor incorrecto...")
                                                                                                        # raise ZeroDivisionError("Este mensaje es personalizado.")
                                                                                                    elif nota >= 16:
                                                                                                        print("Excelente")
                                                                                                    elif nota >= 11:
                                                                                                        print("Aprobado")
                                                                                                    else:
                                                                                                        print("Desaprobado")
                                                                                                evaluarNota(-7)
                                                                                                print("Este es el fin de mi programa.")
                                                                                                t = 5
                                                                                                countdown(int(t))
                                                                                            else:
                                                                                                if opc == "24":
                                                                                                    multiplicar()
                                                                                                    potenciar()
                                                                                                    t = 5
                                                                                                    countdown(int(t))
                                                                                                else:
                                                                                                    if opc=="25":
                                                                                                        curso1 = Curso("Matemática",5,"Ingeniería Civil")
                                                                                                        print(curso1)
                                                                                                        curso1.mostrarDatos()
                                                                                                        t = 5
                                                                                                        countdown(int(t))
                                                                                                    else:
                                                                                                        if opc=="26":
                                                                                                            cuenta1 = Cuenta("Oscar García",15000,"Soles")
                                                                                                            print(cuenta1.get_Saldo())
                                                                                                            print(cuenta1.get_Moneda())
                                                                                                            cuenta1.set_Moneda("Dólares")
                                                                                                            print(cuenta1.get_Moneda())
                                                                                                            t = 5
                                                                                                            countdown(int(t))
                                                                                                        else:
                                                                                                            if opc=="27":
                                                                                                                per1 = Persona("Torres","López","Juan")
                                                                                                                print(isinstance(per1,Estudiante))
                                                                                                                t = 5
                                                                                                                countdown(int(t))
                                                                                                            else:
                                                                                                                if opc=="28":
                                                                                                                    cX1 = ClaseX(15,21)
                                                                                                                    t = 5
                                                                                                                    countdown(int(t))
                                                                                                                else:
                                                                                                                    if opc =="29":
                                                                                                                        doc1 = Trabajador()
                                                                                                                        describirPersona(doc1)
                                                                                                                        t = 5
                                                                                                                        countdown(int(t))
                                                                                                                    else:
                                                                                                                        if opc=="30":
                                                                                                                            pais1 = Pais("Ecuador","Guillermo Lasso")
                                                                                                                            print(pais1)

                                                                                                                            ciudad1 = Ciudad("Milagro",150000,pais1)
                                                                                                                            print(ciudad1)

                                                                                                                            urba1 = Urbanizacion("María de los Angeles",ciudad1)
                                                                                                                            print(urba1)
                                                                                                                            t = 5
                                                                                                                            countdown(int(t))
                                                                                                                        else:
                                                                                                                            if opc == '31':
                                                                                                                                c1 = False








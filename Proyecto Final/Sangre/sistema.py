'''
Sistema de Sangre.
By Roger Urrutia 
Jose L Gonzalez M.

Concepto general, crear un sistema de donacion de sangre en la cual el donante de su informacion y se pueda ver si este es capaz 
de donarle a alguno de los usuarios quwe necesitan donacion. Para eso se realiza una evaluacion de los tipos de sangre que este puede aceptar.
'''

from collections import defaultdict 
# import pdb
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#Clases
class Donante():
    """Es la clase utilizada para definir a los donantes 

    Parameters:
        name(str): Nombre del donante
        age(num): Edad del donante
        b_type(str): Tipo de sangre del donante
        sex(str): Sexo del paciente (No en cantidad, sino su genero)
        """

    def __init__(self,name,age,b_type,sex):
        self.name=name
        self.age=age
        self.b_type=b_type
        self.sex=sex


class Donatario(Donante):
    """Define a un donatario de sangre en la base de datos
    """

    def __init__(self,name,age,b_type,sex):
        """Mismos datos que para un donante 
        Parameters:
            name(str): Nombre del donante
            age(num): Edad del donante
            b_type(str): Tipo de sangre del donante
            sex(str): Sexo del paciente (No en cantidad, sino su genero)
            """
        super().__init__(name,age,b_type,sex)

    def posible(self):
        """Define los posibles tipos de sangre que se pueden almacenar
        A+,A-,B+.B-,AB+,AB-,O+,O-"""
        if self.b_type=="A+":
            sangre_permitida=["A+","A-","O+","O-"]
        elif self.b_type=="O+":
            sangre_permitida=["O+","O-"]
        elif self.b_type=="B+":
            sangre_permitida=["B+","B-","O+","O-"]
        elif self.b_type=="AB+":
            sangre_permitida=["A+","A-","B+","B-","O+","O-","AB+","AB-"]
        elif self.b_type=="A-":
            sangre_permitida=["A-","O-"]
        elif self.b_type=="O-":
            sangre_permitida=["O-"]
        elif self.b_type=="B-":
            sangre_permitida=["B-","O-"]
        elif self.b_type=="AB-":
            sangre_permitida=["A-","B-","O-","AB-"]
        else:
            return f"La Sangre {self.b_type} no existe."
        return sangre_permitida

#Funciones 
def menu():
    """Manda el Menú \n
    Opciones:
        1: Añadir a un donante
        2: Añadir a un donatario
        3: Revisar la lista de donantes
        4: Revisar la lista de donatarios
        5: Realizar una transfusion
        6: Estadisticas
        7: Salir
    Returns:
        opc(num):Opcion del menu """
    print("\nBienvenido a el sistema de Donacion de Sangre. Elige la accion que deseas realizar.\n1.Añadir Donante de Sangre\n2.Añadir Donatario de Sangre\n3.Revisar lista de Donantes\n4.Revisar Lista de Donatarios\n5.Realizar una transfusion\n6.Estadisticas\n7.Salir")
    opc=int(input("Seleccionar: "))
    return opc

if __name__=="__main__":
    
    
    donantes=[]
    donatarios=[]
    sexoDonante=defaultdict(lambda:0)
    sexoDonatario=defaultdict(lambda:0)
    sangreDonante=defaultdict(lambda: 0)
    sangreDonatario=defaultdict(lambda: 0)
    
    while True:
        
        opc=menu()
        
        if opc==1: #Opcion 1 del menú añadir a un donante.
            cont=1
            while cont==1:
                print(f"Excelente, crearemos un nuevo donante de sangre. Actualmente hay {len(donantes)} donantes de Sangre.")
                name=input("Ingrese el nombre del donante: ")
                try:
                    age=int(input("Ingrese la edad del donante: "))
                except:
                    print("El valor introducido no es una edad. Comenzaremos nuevamente.")
                    break
                else:
                    if age<15:
                        print("Esta Persona es muy joven, no puede donar. Intentar añadir a otra persona.")
                        continue
                b_type=input("Ingrese el tipo de sangre del donante: ")
                if b_type.upper() not in ["A+","B+","O+","AB+","A-","B-","O-","AB-"]:
                    print("Sangre Invalida. Intente Nuevamente.")
                    continue
                else:
                    sangreDonante[b_type]+=1
                sex=input("Ingrese el sexo del donante: ")
                sexoDonante[sex]+=1
                try:
                    donantes.append(Donante(name,age,b_type,sex))
                except:
                    print("Parece ser que hubo algun error al momento de añadir al donante. Intenta Nuevamente.")
                else:
                    print("Donador añadido de manera exitosa.")
                cont=input("Desea añadir un nuevo donante? (si/no): ")
                if cont.lower()=="si":
                    cont=1
                else:
                    cont=0
        
        elif opc==2:#Opcion 2 del menú Añadir a un donatorio
            cont=1
            print(f"Excelente, crearemos un nuevo donatario de sangre. Actualmente hay {len(donatarios)} donatarios de Sangre.")
            while cont==1:
                name=input("Ingrese el nombre del donatario: ")
                try:
                    age=int(input("Ingrese la edad del donatario: "))
                except:
                    print("El valor introducido no es una edad. Comenzaremos nuevamente.")
                    break
                b_type=input("Ingrese el tipo de sangre del donatario: ")
                if b_type.upper() not in ["A+","B+","O+","AB+","A-","B-","O-","AB-"]:
                    print("Sangre Invalida. Intente Nuevamente.")
                    break
                sex=input("Ingrese el sexo del donatario: ")
                sexoDonatario[sex]+=1
                try:
                    donatarios.append(Donatario(name,age,b_type,sex))
                except:
                    print("Parece ser que hubo algun error al momento de añadir al donatario. Intenta Nuevamente.")
                else:
                    print("Donatario añadido de manera exitosa.")
                cont=input("Desea añadir un nuevo Donatario? (si/no): ")
                if cont.lower()=="si":
                    cont=1
                else:
                    cont=0
        
        elif opc==3:#Opcion 3 del menú Revisar la lista de donantes
            if len(donantes)>=1:
                print("Los donantes disponibles son: ")
                for donante in donantes:
                    print(f"\n{donante.name} con sangre tipo {donante.b_type}")
                print("\n"+("x"*20))
                for k,v in sangreDonante.items():
                    print(f"\nDe tipo de sangre {k} hay {v} personas.")
                print("\n"+("x"*20))
            else:
                print("\n"+("x"*20))
                print("\nNo hay ningun donante en la base de datos.")
                print("\n"+("x"*20))
        
        elif opc==4:#Opcion 4 del menú Revisar la lista de donatarios
            if len(donatarios)>=1:
                print("Los donatarios disponibles son: ")
                for donatario in donatarios:
                    print(f"\n{donatario.name} con sangre tipo {donatario.b_type}")
                print("\n"+("x"*20))
                for k,v in sangreDonatario.items():
                    print(f"\nDe tipo de sangre {k} hay {v} personas.")
                print("\n"+("x"*20))
            else:
                print("\n"+("x"*20))
                print("\nNo hay ningun donatario en la base de datos.")
                print("\n"+("x"*20))

        elif opc==5:#Opcion 5 del menú Realizar una transfusion
            print("\nSe realizara una transfusion. Es importante que los pacientes se encuentren en la base de datos.")
            
            while True:
                paciente_1=input("\nIngrese el nombre del donante o escriba q para salir: ")
                
                if paciente_1.lower()=="q":
                    break

                for donante in donantes:
                    if donante.name==paciente_1:
                        print("Donante encontrado.")
                        paciente_1=donante
                    else:
                        continue
                
                if paciente_1 not in donantes:
                    print("\nError")
                    break

                paciente_2=input("\nIngrese el nombre del donatario o escriba q para salir: ")
                
                if paciente_2.lower()=="q":
                    break

                for donatario in donatarios:
                    if donatario.name==paciente_2:
                        print("Donatario encontrado.")
                        paciente_2=donatario
                    else:
                        continue
                
                if paciente_2 not in donatarios:
                    print("\nError")
                    break

                if paciente_1.b_type in paciente_2.posible():
                    if paciente_1.sex.lower()=="femenino":
                        articulo="La"
                    else:
                        articulo="El"
                    print(f"{articulo} donante {paciente_1.name} puede donarle sin problemas a {paciente_2.name}")
                    index=donatarios.index(paciente_2)
                    delete=donatarios.pop(index)
                    print(f"{delete.name} ha sido removido de la lista de donatarios!")
                else:
                    print(f"Este donante {paciente_1.name} no puede donarle a {paciente_2.name}")
                    break
                
                continuar=input("Deseas continuar?(si/no): ")
                if continuar.lower()=="si":
                    continue
                else:
                    break
            
        elif opc==6:#opcion 6 del menú Mostrar estadistica. Se utiliza un modulo para poder mostrar en un cuadro estadistico a los donantes
            choose=int(input("Con gusto te mostramos las estadisticas. Elige las estadisticas que necesitas visualizar.\n1.Donantes\n2.Donatario"))
            #Estadisticas Donantes
            if choose==1:
                if len(donantes)>=1:
                    objects=[]
                    performance=[]
                    for k,v in sexoDonante.items():
                        objects.append(k)
                        performance.append(v)
                    
                    objects=tuple(objects)
                    y_pos=np.arange(len(objects))

                    plt.bar(y_pos,performance, align="center", alpha=0.5)
                    plt.xticks(y_pos,objects)
                    plt.ylabel("Cantidad de personas")
                    plt.title("Sexo de los donantes")
                    
                    plt.show()

                    objects=[]
                    performance=[]
                    for k,v in sangreDonante.items():
                        objects.append(k)
                        performance.append(v)
                    
                    objects=tuple(objects)
                    y_pos=np.arange(len(objects))

                    plt.bar(y_pos,performance, align="center", alpha=0.5)
                    plt.xticks(y_pos,objects)
                    plt.ylabel("Cantidad de personas")
                    plt.title("Tipo de Sangre de los donantes")
                    
                    plt.show()
                
                else:
                    print("No hay donantes en la base de Datos.")
            
            elif choose==2:
            #Estadisticas Donatarios
                if len(donatarios)>=1:
                    objects=[]
                    performance=[]
                    for k,v in sexoDonatario.items():
                        objects.append(k)
                        performance.append(v)
                    
                    objects=tuple(objects)
                    y_pos=np.arange(len(objects))

                    plt.bar(y_pos,performance, align="center", alpha=0.5)
                    plt.xticks(y_pos,objects)
                    plt.ylabel("Cantidad de personas")
                    plt.title("Sexo de los Donatarios")
                    
                    plt.show()

                    objects=[]
                    performance=[]
                    for k,v in sangreDonatario.items():
                        objects.append(k)
                        performance.append(v)
                    
                    objects=tuple(objects)
                    y_pos=np.arange(len(objects))

                    plt.bar(y_pos,performance, align="center", alpha=0.5)
                    plt.xticks(y_pos,objects)
                    plt.ylabel("Cantidad de personas")
                    plt.title("Sexo de los Donatarios")
                    
                    plt.show()
                
                else:
                    print("No hay donatarios en la base de Datos.")
        
        elif opc==7:#Opcion 7 del menú salir.
            print("\nGracias por utilizar la aplicacion.")
            break
        
        else:
            print("\n Opcion no valida.")


                







                    
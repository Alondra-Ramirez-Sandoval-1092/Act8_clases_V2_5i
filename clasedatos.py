class Informacion: 

    def mi_lista(self):
        lista_Nomperros=["boby","Dollar","fany"]
        for x in lista_Nomperros:
            print(x)

    def mi_tupla(self):
        tupla_Nomperros=("coco","rocko","chano")
        for x in tupla_Nomperros:
            print(x)            

    def mi_conjunto(self):
        conjunto_Nomperros={"negro","cafe","blanco"}
        for x in conjunto_Nomperros:
            print(x) 

    def mi_diccionario(self):
        diccionario_Nomperros={
            "nombre":"coco",
            "color":"cafe",
            "raza":"chihuahua"
            }
        for x,y in diccionario_Nomperros.items():
            print(x," : ",y)                     
# creando el objeto 

datos=Informacion() 
print("---Listado de nombre de perros---")
datos.mi_lista()
print("---Tupla de nombre de perros---")
datos.mi_tupla()
print("---Conjunto de colores de perros---")
datos.mi_conjunto()
print("---Diccionario de informacion del perro---")
datos.mi_diccionario()
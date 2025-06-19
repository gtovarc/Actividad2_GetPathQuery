#instalar el framework de fastapi 
#pip install fastapi

#instalacion del servidor de uvicorn
#pip install "uvicorn[standard]"

#instalacion del framework de fastapi 
#pip install fastapi[all]

#Importar el framework de fastapi
from fastapi import FastAPI, HTTPException

#Crear objeto a partir de la clase FastAPI
app = FastAPI()

#Utilizamos la (instancia) función get del framework FastAPI
@app.get("/imprimir")

#Crear la función asíncrona "impirmir"
async def imprimir():
    return "Hola mundo"

#Crear la función para Git
@app.get("/Git")
async def imprimir():
    return {"Git_curso: https://github.com/gtovarc/ModWeb0.git"}
#Activar el server de Uvicorn 
#uvicorn main:app --reload
#En el explorador utilizar la ip

#importar pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel, ValidationError

#Crear una lista de entidades con los siguientes atributos 
#{"id":3, "Nombre": "TOVAR CRUZ, GUADALUPE","Edad":"25"}
class Usuario(BaseModel):
    id: int
    Nombre: str
    Edad: int
    
#Crear una lista de usuarios
usuarios = [
    Usuario(id=1, Nombre="TOVAR CRUZ, GUADALUPE", Edad=25),
    Usuario(id=2, Nombre="TOVAR CRUZ, JUAN PABLO", Edad=22),
    Usuario(id=3, Nombre="TOVAR CRUZ, ELA LIZETH", Edad=12)
]

#definir la ruta para obtener todos los usuarios
@app.get("/usersclass/")
async def get_usuarios():
    return usuarios
#Colocar en el explorador la raíz /usersclass/

#---------------------------Actividad 1: API Solo Get ---------------------------------------------
import pandas as pd

#----------------------------------------------------------------------------------------------------------
#Ruta 1 = carrera/genero/promedio -----> 3 niveles
class Ruta1(BaseModel):
    nombre: str
    carrera: str
    genero: str
    promedio: float
   
#leer el csv 
df = pd.read_csv("BD_E6_v2.csv", sep=",", encoding="utf-8")    
        
#Definir la ruta para obtener los datos de Ruta1
@app.get("/carrera/genero/promedio")
async def get_ruta1(carrera: str = None, genero: str = None, promedio: float = None):
    ruta1_data = []
    for index, row in df.iterrows():
        if (carrera and row['Carrera'] != carrera):
            continue
        if (genero and row['Genero'] != genero):
            continue
        if (promedio and row['Promedio'] != promedio):
            continue
        try:
            usuario = Ruta1(
                nombre=row['Nombre'],
                carrera=row['Carrera'],
                genero=row['Genero'],
                promedio=row['Promedio']
            )
            ruta1_data.append(usuario.model_dump())
        except ValidationError as e:
            print(f"Error en la fila {index}: {e}")
    return ruta1_data

#----------------------------------------------------------------------------------------------------------
#Ruta 2 = matricula/edad/semestre -----> 3 niveles
class Ruta2(BaseModel):
    matricula: int
    edad: int
    semestre: int
#hay que leer el csv nuevamente
#df2 = pd.read_csv("BD_E6_v2.csv", sep=",", encoding="utf-8")    
 #No, puedo usar la misma lectura del csv, ya que es el mismo archivo


   
#Definir la ruta para obtener el set de datos de Ruta2
@app.get("/matricula/edad/semestre")
async def get_ruta2(matricula: int = None, edad: int =None, semestre: int = None):
    ruta2_data = []
    for index, row in df.iterrows():
        if (matricula and row['Matricula'] != matricula):
            continue
        if (edad and row['Edad'] != edad):
            continue
        if (semestre and row['Semestre'] != semestre):
            continue
        try:
            usuario = Ruta2(
                matricula=row['Matricula'],
                edad=row['Edad'],
                semestre=row['Semestre']
            )
            ruta2_data.append(usuario.model_dump())
        except ValidationError as e:
            print(f"Error en la fila {index}: {e}")    
    return ruta2_data   
                
  #----------------------------------------------------------------------------------------------------------
#Ruta 3 = matricula/edad/correo/genero -----> 4 niveles
class Ruta3(BaseModel):
    matricula: int
    edad: int
    correo: str
    genero: str
    
#Definir la ruta para obtener el set de datos de Ruta3
@app.get("/matricula/edad/correo/genero")
async def get_ruta3(matricula: int = None, edad: int = None, correo: str = None, genero: str = None):
    ruta3_data = []
    for index, row in df.iterrows():
        if (matricula and row['Matricula'] != matricula):
            continue
        if (edad and row['Edad'] != edad):
            continue
        if (correo and row['Correo'] != correo):
            continue
        if (genero and row['Genero'] != genero):
            continue
        try:
            usuario = Ruta3(
                matricula=row['Matricula'],
                edad=row['Edad'],
                correo=row['Correo'],
                genero=row['Genero']
            )
            ruta3_data.append(usuario.model_dump())
        except ValidationError as e:
            print(f"Error en la fila {index}: {e}")
    return ruta3_data    
#----------------------------------------------------------------------------------------------------------
#がんばって!         

#------------------------------------------------------------------------------------------------------------
#Clase 18/Junio/2025
#Python filter()
#@app.get("/carrera/genero/promedio/{pmedio}")
#async def get_ruta1 (pmedio: float):
#    ruta1_data_n = filter(lambda ruta1_data: ruta1_data.promedio == pmedio,ruta1_data)
#    try:
#        return list(ruta1_data_n)[0]
#    except:
#        return {"error": "No se encontraron datos con el promedio especificado."}
    
#------------------------------------------------------------------------------------------------------------

@app.get("/usersclass/{id}")
async def usersclass(id:int):
    users = filter (lambda usuarios: usuarios.id == id, usuarios)
    try:
        return list(users)[0]
    except:
        return {"error": "No se encontraron datos con el id especificado."}
    

#-------------------------------------------------------------------------------------------------------------
#---------Actividad 2: Get por PATH y Query------------------------------------------------

# Parte 1: Crear una lista de 50 usuarios con los registros del csv ------------------------

df_1 = pd.read_csv("BD_E6_v2.csv", sep=",", encoding="utf-8")
lista_alumnos = df_1.values.tolist()

# Parte 2: Implementar 1 filtro con la función get por cada uno de los campos de la listac--------------------------------
@app.get("/alumnos/{matricula}")
async def get_alumno(matricula: int):
    alumnos = filter(lambda alumno: alumno[0] == matricula, lista_alumnos)
    try:
        return list(alumnos)[0]
    except:
        return {"error": "No se encontraron datos con la matrícula especificada."}
    
 #Parte 3: Implementar 10 filtros con la función get usando query combinando los campos de la lista -----------------------------------

# Lista completa de alumnos (sin filtros)
@app.get("/alumnos/")
async def get_alumnos():
    return lista_alumnos

#Lista de alumnos por edad
@app.get("/alumnos/edad/")
async def get_alumnos_edad(edad: int):
    alumnos = filter(lambda alumno: alumno[2] == edad, lista_alumnos)
    try:
        return list(alumnos)
    except:
        return {"error": "No se encontraron datos con la edad especificada."}
    
 #Lista de alumnos por semestre
@app.get("/alumnos/semestre/")
async def get_alumnos_semestre(semestre: int):
    alumnos = filter(lambda alumno: alumno[9] == semestre, lista_alumnos)
    try:
        return list(alumnos)
    except:
        return {"error": "No se encontraron datos con el semestre especificado."}
 
 #Lista de alumnos por promedio
@app.get("/alumnos/promedio/")
async def get_alumnos_promedio(promedio: float):
    alumnos = filter(lambda alumno: alumno[8] == promedio, lista_alumnos)
    try:
        return list(alumnos)
    except:
        return {"error": "No se encontraron datos con el promedio especificado."}   
    
 #Lista de alumnos por genero
@app.get("/alumnos/genero/")
async def get_alumnos_genero(genero: str):
    alumnos = filter(lambda alumno: alumno[6] == genero, lista_alumnos)
    try:
        return list(alumnos)
    except:
        return {"error": "No se encontraron datos con el género especificado."}   
    
 #Lista de alumnos por genero y edad
@app.get("/alumnos/genero/edad/")
async def get_alumnos_genero_edad(genero: str, edad: int):
    alumnos = filter(lambda alumno: alumno[6] == genero and alumno[2] == edad, lista_alumnos)
    try:
        return list(alumnos)
    except:
        return {"error": "No se encontraron datos con el género y la edad especificados."}

#Lista de alumnos por genero y semestre
@app.get("/alumnos/genero/semestre/")
async def get_alumnos_genero_semestre(genero: str, semestre: int):
    alumnos = filter(lambda alumno: alumno[6] == genero and alumno[9] == semestre, lista_alumnos)
    try:
        return list(alumnos)
    except:
        return {"error": "No se encontraron datos con el género y el semestre especificados."}
 
 #Lista de alumnos por genero y promedio
@app.get("/alumnos/genero/promedio/")
async def get_alumnos_genero_promedio(genero: str, promedio: float):
    alumnos = filter(lambda alumno: alumno[6] == genero and alumno[8] == promedio, lista_alumnos)
    try:
        return list(alumnos)
    except:
        return {"error": "No se encontraron datos con el género y el promedio especificados."}
    
   
#Lista de alumnos por edad y semestre
@app.get("/alumnos/edad/semestre/")
async def get_alumnos_edad_semestre(edad: int, semestre: int):
    alumnos = filter(lambda alumno: alumno[2] == edad and alumno[9] == semestre, lista_alumnos)
    try:
        return list(alumnos)
    except:
        return {"error": "No se encontraron datos con la edad y el semestre especificados."}
    
#Lista de alumnos por edad, semestre y promedio
@app.get("/alumnos/edad/semestre/promedio/")
async def get_alumnos_edad_semestre_promedio(edad: int, semestre: int, promedio: float):
    alumnos = filter(lambda alumno: alumno[2] == edad and alumno[9] == semestre and alumno[8] == promedio, lista_alumnos)
    try:
        return list(alumnos)
    except:
        return {"error": "No se encontraron datos con la edad, el semestre y el promedio especificados."}

#Lista de alumnos por genero, semestre y promedio
@app.get("/alumnos/genero/semestre/promedio/")
async def get_alumnos_genero_semestre_promedio(genero: str, semestre: int, promedio: float):
    alumnos = filter(lambda alumno: alumno[6] == genero and alumno[9] == semestre and alumno[8] == promedio, lista_alumnos)
    try:
        return list(alumnos)
    except:
        return {"error": "No se encontraron datos con el género, el semestre y el promedio especificados."}
    
                    
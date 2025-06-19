## Actividad 2: Get Path y Query

**1  -  /alumnos/{matricula}**

Parámetros:
```json
matricula (int)
```

Respuesta:
```json
[ 
202163318, 
"TOVAR CRUZ, GUADALUPE", 
25, 
"Ciencias de la computación", 
"Licenciatura", 
"Ing. Tecnologias de la Información", 
"Masculino", 
"guadalupe.tovarc@alumno.buap.mx", 
9.3, 
8 
]
```
---
**2 - /alumnos/edad/**

Parámetros:
```json
edad (int)
```

Respuesta:
```json
 [
    202132799,
    "ANZURES MORALES, ENRIQUE",
    22,
    "Ciencias de la computación",
    "Licenciatura",
    "Ing. Ciencias Computación",
    "Masculino",
    "enrique.anzures@alumno.buap.mx",
    7,
    8
  ]
```
---
**3 - /alumnos/semestre/**

Parámetros:
```json
semestre (int)
```
Respuesta: 
```json
 [
    202132799,
    "ANZURES MORALES, ENRIQUE",
    22,
    "Ciencias de la computación",
    "Licenciatura",
    "Ing. Ciencias Computación",
    "Masculino",
    "enrique.anzures@alumno.buap.mx",
    7,
    8
  ]
```
---
**4 - /alumnos/promedio/**

Parámetros:
```json
promedio (int)
```
Respuesta: 
```json
 [
    202132799,
    "ANZURES MORALES, ENRIQUE",
    22,
    "Ciencias de la computación",
    "Licenciatura",
    "Ing. Ciencias Computación",
    "Masculino",
    "enrique.anzures@alumno.buap.mx",
    7,
    8
  ]
```
---
**5 - /alumnos/genero/**

Parámetros:
```json
genero (string)
```
Respuesta: 
```json
 [
    202132799,
    "RODRIGUEZ SALVADOR, MARIA",
    21,
    "Ciencias de la computación",
    "Licenciatura",
    "Ing. Ciencias Computación",
    "Femenino",
    "maria.rodriguezs@alumno.buap.mx",
    8,
    9
  ]
```
---
**6 - /alumnos/genero/edad/**

Parámetros:
```json
genero (string)
edad (int)
```
Respuesta: 
```json
 [
    202132799,
    "RODRIGUEZ SALVADOR, MARIA",
    21,
    "Ciencias de la computación",
    "Licenciatura",
    "Ing. Ciencias Computación",
    "Femenino",
    "maria.rodriguezs@alumno.buap.mx",
    8,
    9
  ]
```
---
**7 - /alumnos/genero/semestre/**

Parámetros:
```json
genero (string)
semestre (int)
```
Respuesta: 
```json
 [
    202132799,
    "RODRIGUEZ SALVADOR, MARIA",
    21,
    "Ciencias de la computación",
    "Licenciatura",
    "Ing. Ciencias Computación",
    "Femenino",
    "maria.rodriguezs@alumno.buap.mx",
    8,
    9
  ]
```
---
**8 - /alumnos/genero/promedio/**

Parámetros:
```json
genero (string)
promedio (int)
```
Respuesta: 
```json
 [
    202132799,
    "RODRIGUEZ SALVADOR, MARIA",
    21,
    "Ciencias de la computación",
    "Licenciatura",
    "Ing. Ciencias Computación",
    "Femenino",
    "maria.rodriguezs@alumno.buap.mx",
    8,
    9
  ]
```
---
**9 - /alumnos/edad/semestre/**

Parámetros:
```json
edad (int)
semestre (int)
```
Respuesta: 
```json
 [
    202132799,
    "RODRIGUEZ SALVADOR, MARIA",
    21,
    "Ciencias de la computación",
    "Licenciatura",
    "Ing. Ciencias Computación",
    "Femenino",
    "maria.rodriguezs@alumno.buap.mx",
    8,
    9
  ]
```
---
**10 - /alumnos/edad/semestre/promedio/**

Parámetros:
```json
edad (int)
semestre (int)
promedio (int)
```
Respuesta: 
```json
 [
    202132799,
    "RODRIGUEZ SALVADOR, MARIA",
    21,
    "Ciencias de la computación",
    "Licenciatura",
    "Ing. Ciencias Computación",
    "Femenino",
    "maria.rodriguezs@alumno.buap.mx",
    8,
    9
  ]
```
---
**11 - /alumnos/genero/semestre/promedio/**

Parámetros:
```json
genero (string)
semestre (int)
promedio (int)
```
Respuesta: 
```json
 [
    202132799,
    "RODRIGUEZ SALVADOR, MARIA",
    21,
    "Ciencias de la computación",
    "Licenciatura",
    "Ing. Ciencias Computación",
    "Femenino",
    "maria.rodriguezs@alumno.buap.mx",
    8,
    9
  ]
```
---

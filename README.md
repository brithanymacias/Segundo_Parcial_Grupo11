# Sistema Municipal de Gestión de Trámites 📋
### Proyecto POO – Segundo Parcial  
### Grupo 11: Gestión de Servicios de Municipio / Trámites  

## 👥 Integrantes
- Collaguari Israel  
- Macias Brithany  

---

# 📌 Descripción del Proyecto

Es una aplicación de escritorio desarrollada en **Python** para la gestión administrativa de **trámites vinculados a ciudadanos**.  
Este proyecto se destaca por la implementación de una **Arquitectura por Capas**, lo que garantiza un código organizado, mantenible, escalable y seguro.

---

## 🏗 Características Principales

- **CRUD Completo**: Crear, Leer, Actualizar y Eliminar trámites.
- **Gestión de Ciudadanos**: Asociación de datos personales (Cédula, Nombre y Apellido) a cada trámite.
- **Búsqueda Inteligente**: Recuperación de información mediante el código de trámite.
- **Validaciones Robustas**:
  - Control de tipos de datos  
  - Longitud de campos  
  - Verificación de campos obligatorios  
- **Interfaz Gráfica Moderna**: Desarrollada con **Qt Designer** y **PySide6**.

---

## 🛠️ Arquitectura del Software

El sistema no es un script monolítico, sino una aplicación estructurada siguiendo **buenas prácticas de ingeniería de software**.

### 1️⃣ Arquitectura por Capas (Layered Architecture)

El código está organizado en paquetes lógicos que separan claramente las responsabilidades:

- **Dominio**  
  Contiene las entidades del negocio como `Tramite` y `Ciudadano`.

- **Datos**  
  Capa de persistencia encargada de la comunicación con **SQL Server**.

- **Servicios**  
  Implementa la lógica de negocio y actúa como intermediaria entre la UI y la capa de datos.

- **UI**  
  Contiene los archivos de interfaz gráfica generados con **Qt Designer** y la lógica de interacción con el usuario.


### 2️⃣ Patrones de Diseño Implementados

- **DAO (Data Access Object)**  
  Implementado en `tramite_DAO.py`.  
  Encapsula el acceso a la base de datos y desacopla la lógica de negocio de la persistencia.

- **Singleton**  
  Implementado en `conexion.py`.  
  Garantiza una única instancia de conexión a la base de datos durante la ejecución del sistema, optimizando recursos.

- **DTO / VO (Data Transfer Object / Value Object)**  
  Uso de objetos para transferir datos entre capas sin exponer directamente la estructura de la base de datos.


### 3️⃣ Seguridad

- **Prevención de Inyección SQL**  
  Uso estricto de **consultas parametrizadas** en todas las sentencias SQL.

- **Manejo de Excepciones**  
  Implementación de bloques `try-except` para capturar:
  - Errores de conexión
  - Errores de integridad referencial
  - Errores de ejecución en la base de datos

---

## 🗄️ Base de Datos

El sistema utiliza **SQL Server** como gestor de base de datos.  
La estructura se crea mediante el archivo:

- `schema.sql`

Este script contiene:
- Creación de la base de datos
- Creación de tablas
- Datos iniciales de prueba

---

## ▶️ Ejecución del Proyecto

1. Clonar el repositorio desde GitHub.
2. Ejecutar el archivo `schema.sql` en SQL Server.
3. Abrir el proyecto en **PyCharm**.
4. Ejecutar el archivo `main.py`.

---

## 🔗🎥 Enlace del vídeo

https://drive.google.com/file/d/1dkR1bHyQQohtF56lGcaF4lbKnvw1vIOi/view?usp=drivesdk

---

## 📸 Capturas del programa

## Función Insertar (Nuevo)

![WhatsApp Image 2026-02-08 at 17 37 59](https://github.com/user-attachments/assets/020b4ccc-b9f9-47aa-a72f-922af48fd529)
![WhatsApp Image 2026-02-08 at 17 35 47](https://github.com/user-attachments/assets/c1561da8-8a25-4b72-9f61-b050661705a6)
![WhatsApp Image 2026-02-08 at 17 36 03](https://github.com/user-attachments/assets/9ad0e760-93c5-4147-96f7-41f80fb0c04c)

## Función Buscar

![WhatsApp Image 2026-02-08 at 17 29 43](https://github.com/user-attachments/assets/6c544c9d-48fc-4ce1-9c25-3abfafd1a99d)
![WhatsApp Image 2026-02-08 at 17 29 17](https://github.com/user-attachments/assets/16b694c5-ddd5-4499-a2e7-71514f9b10c1)

## Función Actualizar

![WhatsApp Image 2026-02-08 at 17 30 55](https://github.com/user-attachments/assets/c462f583-4f5e-43e7-96a4-d0974eb607b2)
![WhatsApp Image 2026-02-08 at 17 31 35](https://github.com/user-attachments/assets/fe711076-1d60-4cad-806e-47b2b1733c87)
![WhatsApp Image 2026-02-08 at 17 31 53](https://github.com/user-attachments/assets/2394f9d5-87bd-4a00-947d-287a180a809c)
![WhatsApp Image 2026-02-08 at 17 32 23](https://github.com/user-attachments/assets/cbb823f0-8238-4156-8381-785571935f97)


## Función Eliminar

![WhatsApp Image 2026-02-08 at 17 33 37](https://github.com/user-attachments/assets/6d40af75-c473-4744-8e4d-c791f8fdd529)
![WhatsApp Image 2026-02-08 at 17 34 00](https://github.com/user-attachments/assets/d82e6273-eb7d-454a-835f-9b46992a9345)
![WhatsApp Image 2026-02-08 at 17 34 18](https://github.com/user-attachments/assets/64919990-ddf0-42c1-ac53-fd094bb85d34)

## Validaciones de algunos campos vacíos

![WhatsApp Image 2026-02-08 at 17 39 09](https://github.com/user-attachments/assets/0b5db484-ec90-49e0-beb9-9e468a7e13c0)
![WhatsApp Image 2026-02-08 at 17 39 22](https://github.com/user-attachments/assets/52767db7-f3bb-4351-8f47-60c48eff722c)
![WhatsApp Image 2026-02-08 at 17 39 50](https://github.com/user-attachments/assets/ac749f5c-e729-40a1-9933-adc88ef49011)
![WhatsApp Image 2026-02-08 at 17 40 05](https://github.com/user-attachments/assets/db945cc7-6e48-49f0-b3e0-d77aefb43ea5)







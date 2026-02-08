# Sistema Municipal de Gestión de Trámites 📋
### Proyecto POO – Segundo Parcial  
### Grupo 11: Gestión de Servicios de Municipio / Trámites  

## 👥 Integrantes
- Collaguari Israel  
- Macias Brithany  

---

# 📌 Descripción del Proyecto

Aplicación de escritorio desarrollada en **Python** para la gestión administrativa de **trámites vinculados a ciudadanos**.  
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


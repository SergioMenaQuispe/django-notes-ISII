Alumno: JESUS BRUNO CHANCAYAURI SONCCO

# TÉCNICAS DE REFACTORIZACIÓN

## Número 1
Primer error que suele ser muy común es el sgte:

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/8e789592-013c-4696-82da-0fd5920294f4)

SonarLint lo detecta:

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/7404de14-ec45-4704-a902-6394b614fde3)

>[!NOTE]
>### Regla: Class names should comply with a naming convention (python:S101)
>Esta regla plantea un problema cuando el nombre de una clase no coincide con una expresión regular proporcionada.
>La expresión regular predeterminada permite la convención "CapWords" y "snake_case" en minúsculas. La guía de estilo PEP-8 recomienda usar la convención "CapWords" en todos los casos, pero también acepta la convención "snake_case" cuando la clase se usa principalmente como invocable (por ejemplo: decorador, administrador de contexto, etc.).

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/0e71a8f3-6635-40d8-a2bb-4af7726e2a4e)

Refactorizando:

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/92480754-fcc4-4017-9c0c-b74cd4a93d0d)


## Número 2
A continuación se muestra el error generado:

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/bc57ced9-5024-4829-a016-337c340d429f)


SonarLint lo detecta:

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/f7d256b7-5e39-4c73-af1e-111a84beb2bb)


>[!NOTE]
>### String literals should not be duplicated (python:S1192)
>En su lugar, utilice constantes para reemplazar los literales de cadena duplicados. Se puede hacer referencia a las constantes desde muchos lugares, pero solo es necesario actualizarlas en un solo lugar.
>La sugerencia de SonarLint se basa en las buenas prácticas de programación para mejorar la legibilidad, reducir la duplicación de código y facilitar el mantenimiento.

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/4f86c1fa-0ce2-4015-b4c3-589941eb5282)


Refactorizando:

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/96d14d95-c9f1-4c92-bbc4-63fd9b63382e)


# CASOS DE PRUEBA
Para ejecutar los casos de prueba se uso Selenium. Esta herramienta, se utiliza comúnmente para la automatización de pruebas funcionales en aplicaciones web. Permite simular las acciones del usuario en un navegador, como hacer clic en enlaces, llenar formularios, y verificar resultados.
## CASO DE PRUEBA 1 : TestUsuarioExistente
Se probó el comportamiento cuando al momento de querer registrarse, los datos corresponden a una cuenta ya existente.
Por ejemplo: Anteriormente se creo una cuenta con los sgtes datos:
- username: 123
- password: 123

Ahora se hará el testeo y veremos los resultados a continuación:

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/eba26af6-a7d0-4b99-9875-5fb268d59781)

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/b35dbe58-7389-44c8-a1f9-34748d3488b6)

La salida en consola:

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/8383f772-d463-4d82-8b9c-305a0ace2431)

## CASO DE PRUEBA 2 : TestPasswordsDiferentes
Se probó el comportamiento cuando al momento de querer registrarse, la contraseña que se pide no es la misma, a la contraseña que se vuelve a pedir.
Por ejemplo: Se llena los inputs con los sgtes datos:
- username: Bruno
- password1 (primera vez que se digita): 123
- password2 (segunda vez que se digita): 321

Ahora se hará el testeo y veremos los resultados a continuación:

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/e5e0c5ed-b288-4ffd-9a61-380a27b44e2d)

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/4f9f9757-f7b0-48ab-8e19-9b3470ef2df6)


La salida en consola, se muestran ambos testeos (el actual y el anteriormente explicado):

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/9265ab5b-cd17-457c-b027-ba2f6200a41d)

# MÓDULOS Y CONTEXTOS DELIMITADOS IDENTIFICADOS

## Módulos:
### Módulo de Autenticación:
Funciones: Signup, Registro de usuarios, Login, Logout.

Responsabilidad: Gestionar la autenticación y autorización de usuarios.
### Módulo de Gestión de Tareas:
Funciones: Task Model, Formulario de Tareas, Crear tareas, Listar tareas, Obtener Tarea,
Actualizar tarea, Completar y eliminar tarea, Listar tareas completadas.

Responsabilidad: Administrar el ciclo de vida de las tareas, desde su creación hasta su
finalización y eliminación.

### Módulo de Presentación y Templates:
Funciones: Templates y condicionales.

Responsabilidad: Manejar la presentación de la interfaz de usuario, renderizar vistas y
aplicar lógica condicional para mostrar información de manera dinámica.

## Contextos Delimitados:
### Contexto de Autenticación:
Agrupa todas las funcionalidades relacionadas con el registro, inicio de sesión y gestión de
sesiones de usuario.
### Contexto de Gestión de Tareas:
Engloba todas las funcionalidades relacionadas con la creación, edición, visualización y
gestión de tareas.
### Contexto de Presentación y UI:
Se centra en la presentación visual de la aplicación, la manipulación de templates y la lógica
condicional para la renderización de vistas.

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/99931412-bb05-4103-b619-891b506a55e1)

# MICROSERVICIOS IDENTIFICADOS

## Microservicio de Autenticación y Usuarios:
AuthService: Gestiona el registro, autenticación, autorización y manejo de sesiones de usuario.
UserProfileService: Administra los perfiles y datos de usuario, incluyendo la configuración y
preferencias asociadas.
## Microservicio de Gestión de Tareas:
TaskService: Maneja todas las operaciones relacionadas con las tareas, como la creación, edición,
visualización, actualización, completado y eliminación de tareas.
## Microservicio de Presentación y UI:
PresentationService: Se encarga de la presentación visual de la aplicación, gestionando la
renderización de vistas, la manipulación de templates y la lógica condicional para mostrar
información de manera dinámica.
## Microservicio de Comunicación y Integración:
CommunicationService: Facilita la comunicación y la integración entre los diferentes microservicios
y componentes de la aplicación, asegurando una interacción fluida y coherente entre los diferentes
servicios.
## Microservicio de Configuración y Gestión de Datos:
ConfigurationService: Administra la configuración global de la aplicación, permitiendo la
personalización y adaptación de funcionalidades según las preferencias y necesidades del usuario
o del sistema.

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/87840475/b5000e9e-b583-415e-ad4c-5d9bb5569999)


Estos microservicios representan unidades funcionales independientes que pueden ser
desarrolladas, desplegadas y escaladas de manera individual, permitiendo una mayor flexibilidad,
adaptabilidad y mantenibilidad en el desarrollo y operación de tu aplicación.


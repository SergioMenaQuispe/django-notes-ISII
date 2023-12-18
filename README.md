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

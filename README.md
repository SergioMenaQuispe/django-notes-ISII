<<<<<<< HEAD
<<<<<<< HEAD
# Pasos para iniciar proyecto
=======
# Gestor de Tareas

Este proyecto es una aplicación web para la gestión de tareas personales. Permite a los usuarios crear, organizar y priorizar sus tareas diarias de manera efectiva.

## Características

- Registro e inicio de sesión de usuarios.
- Creación y gestión de tareas personales.
- Marcar tareas como importantes.
- Visualizar y editar tareas pendientes.
- Registrar tareas completadas con fecha de finalización.
- Navegación intuitiva a través de un menú de usuario.

## Contribuciones Específicas (Branch - Saul Arturo Condori Machaca)

### Tareas Públicas (Public Tasks)

Mi contribución principal al proyecto fue el desarrollo de la funcionalidad "Tareas Públicas" (Public Tasks). Esta característica permite a los usuarios marcar sus tareas como públicas, haciéndolas accesibles a todos los usuarios de la plataforma. Fomenta la colaboración y transparencia, y añade una dimensión comunitaria a la gestión de tareas.

### Implementación de Casos de Prueba

Además, implementé varios casos de prueba para asegurar la funcionalidad y robustez de la aplicación. Estos tests incluyen:

- Pruebas para la creación de tareas, tanto con datos válidos como inválidos.
- Verificación del funcionamiento correcto del formulario de creación de tareas.
- Tests para la lógica de visualización y manejo de tareas públicas.

Estos casos de prueba fueron fundamentales para mantener la calidad y estabilidad del software durante el desarrollo.

## Tecnologías Utilizadas

- Django (Framework de Python para desarrollo web)
- SQLite (Base de datos)
- HTML/CSS (Frontend)
- Bootstrap (Framework de CSS)

## Instalación y Ejecución
>>>>>>> rama-Saul

Primero tener descargado sqlite e iniciar el ejecutable de sqlite3.
[Link de descarga del .zip](https://www.sqlite.org/2023/sqlite-tools-win-x64-3440200.zip)

<<<<<<< HEAD

=======
>>>>>>> rama-Saul
1. `pip install -r requirements.txt`
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. `python manage.py createsuperuser`
5. `python manage.py runserver`
6. Ingresar a tu navegador en el puerto 8000 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

<<<<<<< HEAD

# FEATURE PROGRESS BAR 

Se agrego el feature de una barra de progreso de tareas completadas y por completar.

```python

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    tasks_completed = Task.objects.filter(user=request.user, datecompleted__isnull=False)

    count_completed = tasks_completed.count()
    count_not_completed = tasks.count()

    return render(request, 'tasks.html', {"tasks": tasks, "count_total": count_completed + count_not_completed, "count_completed": count_completed})


@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    
    tasks_not_completed = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    count_not_completed = tasks_not_completed.count()
    count_completed = tasks.count()
    
    return render(request, 'tasks.html', {"tasks": tasks, "count_total": count_completed + count_not_completed, "count_completed": count_completed})

```

### Test

Se hizo una prueba de test para comprobar que la barra de progreso exista.


```python
class TasksTestCase(LiveServerTestCase):
    def setUp(self):
        # Configuración del navegador Selenium (puedes ajustar según tus necesidades)
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Ejecución en modo sin cabeza para pruebas en segundo plano
        self.selenium = webdriver.Chrome(options=chrome_options)
        self.selenium.implicitly_wait(10)  # Espera implícita de 10 segundos
        super(TasksTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TasksTestCase, self).tearDown()

    def test_tasks_page(self):
        # Crear un usuario y tareas para ese usuario
        user = User.objects.create_user(username='testuser', password='testpass')
        Task.objects.create(user=user, description='Task 1')

        # Acceder a la página de tareas con Selenium
        self.selenium.get(f'{self.live_server_url}/signup/')
        self.selenium.find_element(By.NAME, 'username').send_keys('mena3')
        self.selenium.find_element(By.NAME, 'password1').send_keys('123qweop')
        self.selenium.find_element(By.NAME, 'password2').send_keys('123qweop')
        self.selenium.find_element(By.NAME, 'password2').send_keys(Keys.ENTER)
    
        # Verificar que la página de tareas se carga correctamente
        self.assertIn('tasks', self.selenium.find_element(By.CSS_SELECTOR, "h1").text.lower())
        
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'progress'))
        )

        # Verificar que la tarea se muestra en la página
        progress_bar = self.selenium.find_element(By.TAG_NAME, 'progress')
        self.assertIsNotNone(progress_bar, 'Progress bar not found')


        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.ID, 'progress-message'))
        )

        progress_message = self.selenium.find_element(By.ID, 'progress-message')
        self.assertIn('Tasks completed 0/0', progress_message.text)
```


# MODELO DE DOMINIO

El modelo de dominio se centra en el dominio de "Task", del cual se extienden otros modelos como "TaskAdmin", "TaskForm", y "TaskConfig", y también otro modelo "User" que administras las tasks.

![Alt text](image.png)

## MÓDULO AUTH

Se agrego el módulo de "auth", en el que se incluyeron funciones como el "sigin", "signout", y "signup".

```python

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)  # Replace LoginFailure with login
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('tasks')

@login_required
def signout(request):
    logout(request)
    return redirect('home')


```
=======
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


>>>>>>> rama-Bruno
=======
>>>>>>> rama-Saul

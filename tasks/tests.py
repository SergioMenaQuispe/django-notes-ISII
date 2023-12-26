<<<<<<< HEAD
from django.test import TestCase
# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .models import Task  # Reemplaza 'your_app' con el nombre real de tu aplicación

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
=======
# Create your tests here.

from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

# Test para la vista de Registro

# Comprobamos si el comportamiento es el adecuado cuando se intenta registrar
# un usuario, ya existente
class TestUsuarioExistente(TestCase, LiveServerTestCase):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    title = driver.title

    def setUp(self):
        # Iniciamos el navegador y configuramos
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-extensions')
        self.driver.get('http://127.0.0.1:8000/signup/')

    def tearDown(self) -> None:
        return super().tearDown()

    def test_form(self):
        # Intentamos registrarnos
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.ID, 'id_username'))).send_keys('123')
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.ID, 'id_password1'))).send_keys('123')
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.ID, 'id_password2'))).send_keys('123')
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/form/div/button'))).click()
        
        # Extraemos el mensaje de error generado
        error = self.driver.find_element(by=By.ID, value='error')
        # Guardamos el texto de eso mensaje
        resultado = error.text
        # Comprobamos si el contenido del mensaje es el esperado
        self.assertEqual(resultado, 'El usuario ya esta registrado.')


class TestPasswordsDiferentes(TestCase, LiveServerTestCase):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    title = driver.title

    def setUp(self):
        # Iniciamos el navegador y configuramos
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-extensions')
        self.driver.get('http://127.0.0.1:8000/signup/')

    def tearDown(self) -> None:
        return super().tearDown()

    def test_form(self):
        # Intentamos registrarnos
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.ID, 'id_username'))).send_keys('Bruno')
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.ID, 'id_password1'))).send_keys('123')
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.ID, 'id_password2'))).send_keys('321')
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/form/div/button'))).click()
        
        # Extraemos el mensaje de error generado
        error = self.driver.find_element(by=By.ID, value='error')
        # Guardamos el texto de eso mensaje
        resultado = error.text
        # Comprobamos si el contenido del mensaje es el esperado
        self.assertEqual(resultado, 'Las contraseñas no coinciden.')


if __name__ == '__main__':
    # Ejecutar las pruebas
    unittest.main()
>>>>>>> rama-Bruno

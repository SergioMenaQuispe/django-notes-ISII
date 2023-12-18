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


if __name__ == '__main__':
    # Ejecutar las pruebas
    unittest.main()
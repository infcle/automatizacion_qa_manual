from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Opciones para Firefox (modo normal)
options = webdriver.FirefoxOptions()
# options.add_argument("--headless")  # Descomenta para modo sin interfaz

# Iniciar navegador Firefox
driver = webdriver.Firefox(options=options)

# Navegar a la página de login
driver.get("https://practicetestautomation.com/practice-test-login/")

# Localizar los campos de formulario
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "submit")

# Ingresar credenciales válidas
username_input.send_keys("student")
password_input.send_keys("Password123")
login_button.click()

# Esperar para que cargue la siguiente página
time.sleep(3)

# Verificar el resultado
success_message = driver.find_element(By.TAG_NAME, "h1").text
assert success_message == "Logged In Successfully", "❌ Error: el login falló"

print("✅ Login exitoso")

# Cerrar navegador
driver.quit()

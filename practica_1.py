from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login_test(username, password):
    # Configuración del navegador Firefox
    options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")  # Ejecutar sin abrir la ventana
    driver = webdriver.Firefox(options=options)

    # Navegar a la página
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Llenar formulario
    driver.find_element(By.ID, "username").send_keys("student_")
    driver.save_screenshot("username_filled.png")  # Captura de pantalla del campo username
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.save_screenshot("password_filled.png")  # Captura de pantalla del campo password
    time.sleep(1)  # Esperar un segundo para ver los cambios
    driver.find_element(By.ID, "submit").click()

    # Esperar hasta que ocurra algo: éxito o error
    try:
        # Caso éxito: buscar el h1 con el mensaje
        success_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        ).text

        assert success_message == "Logged In Successfully", "❌ Error: mensaje de éxito inesperado"
        driver.save_screenshot("login_success.png")  # Captura de pantalla del mensaje de éxito
        print("✅ Login exitoso")

    except:
        # Caso error: buscar el div con id=error
        try:
            error_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "error"))
            ).text
            driver.save_screenshot("login_error.png")  # Captura de pantalla del mensaje de error
            print(f"❌ Login fallido: {error_message}")
        except:
            print("❌ Login fallido y no se encontró mensaje de error visible.")

    finally:
        driver.quit()


# caso1 = ("student", "Password123")  # Credenciales correctas
login_test("student", "Password123")
# caso2 = ("incorrectUser", "Password123")  # Contraseña incorrecta
login_test("incorrectUser", "Password123")
# caso3 = ("student", "incorrectPassword")  # Usuario incorrecto    
login_test("student", "incorrectPassword")
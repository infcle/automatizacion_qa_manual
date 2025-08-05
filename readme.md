# Selenium + Firefox | Login Test

Este proyecto automatiza una prueba de login en la siguiente página de práctica:  
🔗 https://practicetestautomation.com/practice-test-login/

Usa **Selenium**, **Python** y **Firefox** para validar credenciales correctas.

---

## 📦 Requisitos

- Python 3.7+
- Firefox instalado
- GeckoDriver compatible con tu versión de Firefox:
  👉 https://github.com/mozilla/geckodriver/releases

---

## 🚀 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/selenium-firefox-login-test.git
cd selenium-firefox-login-test
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. para pruebas no funcionales

```bash
pip install locust
```

---

Para locus se lo hace correr con el siguiente comando

```bash
locust -f no_funcional.py
```

entrar al <http://localhost:8089>

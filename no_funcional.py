from locust import HttpUser, task, between
# carga a la pagina https://the-internet.herokuapp.com/
class NoFuncional(HttpUser):
    # wait_time = between(1, 5)

    @task
    def authenticate(self):
        payload = {
            "username": "tomsmith",
            "password": "SuperSecretPassword"
        }
        self.client.post("/authenticate", json=payload)

    @task
    def login(self):        
        self.client.get("/login")
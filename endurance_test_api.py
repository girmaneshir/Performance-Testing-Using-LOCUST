from locust import HttpUser, task, between

class EnduranceTest(HttpUser):
    wait_time = between(1, 2)

    @task
    def endurance_test(self):
        self.client.get("/users")

    @task
    def create_user(self):
        self.client.post("/users", json={"name": "Endurance Test User"})
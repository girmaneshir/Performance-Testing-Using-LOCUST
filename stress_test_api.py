from locust import HttpUser, task, between,events

class StressTest(HttpUser):
    wait_time = between(0, 1)  # No wait time for stress testing

    @task
    def stress_test(self):
        self.client.get("/users")

    @task
    def create_user(self):
        self.client.post("/users", json={"name": "Stress Test User"})

    @task
    def update_user(self):
        self.client.put("/users/1", json={"name": "Updated Stress User"})

    @task
    def delete_user(self):
        self.client.delete("/users/1")

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("Starting Stress Test")
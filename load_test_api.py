from locust import HttpUser, task, between, events

class UserApiUser(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def create_user(self):
        self.client.post("/users", json={"name": "User Load Test"})

    @task(2)
    def retrieve_users(self):
        self.client.get("/users")

    @task(3)
    def update_user(self):
        self.client.put("/users/1", json={"name": "Updated User Load Test"})

    @task(4)
    def delete_user(self):
        self.client.delete("/users/1")

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("Starting Load Test")
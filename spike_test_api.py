from locust import HttpUser, task, between

class SpikeTest(HttpUser):
    wait_time = between(1, 5)

    @task
    def spike_test_create(self):
        self.client.post("/users", json={"name": "Spike Test User"})

    @task
    def spike_test_retrieve(self):
        self.client.get("/users")
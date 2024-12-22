from locust import HttpUser, task, between
import random

# Define the date range for random date generation (from 2000 to 2023)
START_YEAR = 2000
END_YEAR = 2023

# Function to generate a random date
def get_random_date():
    year = random.randint(START_YEAR, END_YEAR)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Keep it simple; February has at most 28 days
    return f"{year}-{month:02d}-{day:02d}"

class UserBehavior(HttpUser):
    wait_time = between(1, 5)  # Simulate user wait time between tasks

    @task
    def load_random_age(self):
        random_date = get_random_date()  # Generate a random date
        response = self.client.get(f"/age/{random_date}")  # Make a GET request
        if response.status_code == 200:
            print(f"Success: Retrieved data for date {random_date}")
        else:
            print(f"Failed: Status code {response.status_code} for date {random_date}")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000  # Minimum wait time between requests (in milliseconds)
    max_wait = 5000  # Maximum wait time between requests (in milliseconds)
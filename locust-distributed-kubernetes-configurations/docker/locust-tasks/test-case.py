from locust import HttpUser, task, between


class TestCase(HttpUser):

    @task
    def get(self):
        self.client.get("www.google.com")

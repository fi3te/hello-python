import logging

from locust import HttpLocust, TaskSet, task, constant

logger = logging.getLogger(__name__)


class DemoBehaviour(TaskSet):
    @task()
    def get_users(self):
        self.client.get("/user")


class DemoUser(HttpLocust):
    task_set = DemoBehaviour
    wait_time = constant(1)

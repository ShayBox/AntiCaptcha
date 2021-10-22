from time import sleep
import requests


class AntiCaptcha:
    def __init__(self, client_key):
        self.base_url = "https://api.anti-captcha.com/"
        self.headers = {"Content-Type": "Application/json"}
        self.client_key = client_key

    def _post(self, endpoint: str, data: object):
        """Make requests to api.anti-captcha.com

        Args:
            endpoint (str): API Endpoint
            data (object): API Payload

        Raises:
            Exception: API Error

        Returns:
            Response: Request Response
        """

        url = self.base_url + endpoint
        data.update({"clientKey": self.client_key})
        response = requests.post(url, data, headers=self.headers)
        json = response.json()
        if not hasattr(json, "errorId") or json.errorId == 0:
            return json
        else:
            raise Exception(json)

    def create_task(self, data: object):
        """Create Task

        Args:
            data (object): createTask Payload

        Returns:
            Response: Request Response
        """

        return self._post("createTask", data)

    def get_task(self, task_id: str):
        """Get

        Args:
            task_id (str): API Task ID

        Returns:
            Response: Request Response
        """

        return self._post("getTaskResult", {"taskId": task_id})

    def get_result(self, task_id: str, sleep_seconds: float = 5):
        """Wait for result

        Args:
            task_id (str): API Task ID
            sleep_seconds (float, optional): Amount of time to sleep between checks. Defaults to 5.

        Raises:
            Exception: API Error

        Returns:
            Response: Request Response
        """

        json = {}
        while json.status == "processing":
            json = self.get_task(task_id)
            sleep(sleep_seconds)
        if not hasattr(json, "errorId") or json.errorId == 0:
            return json
        else:
            raise Exception(json)

    def get_token(self, task_id: str, sleep_seconds: float = 5):
        """Get result token

        Args:
            task_id (str): API Task ID
            sleep_seconds (float, optional): Amount of time to sleep between checks. Defaults to 5.

        Returns:
            str: API Result Token
        """

        return self.get_result(task_id, sleep_seconds).solution.token

    def solve(self, data: object):
        """All-in-one function to get token

        Args:
            data (object): createTask Payload

        Returns:
            str: API Token
        """

        json = self.create_task(data)
        token = self.get_token(json.taskId)
        return token

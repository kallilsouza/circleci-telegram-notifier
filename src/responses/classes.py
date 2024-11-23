import json


class HttpResponse:
    status_code: int
    data: dict

    def __init__(self, status_code: int, data: dict) -> None:
        self.status_code = status_code
        self.data = data

    def send(self):
        return {
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
            },
            "statusCode": self.status_code,
            "body": json.dumps(self.data),
        }

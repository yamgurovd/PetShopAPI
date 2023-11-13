import requests
from requests import Request, Response
from src.logger import Logger
import allure
from pathlib import Path

loger = Logger(file_name="src/logs/request_log.log")


class HttpClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.api_client = requests.session()

    def send_request(self, request: Request) -> Response:
        request = request
        request.url = self.base_url + request.url

        loger.add_request(
            method=request.method,
            user_agent=request.headers.get("User-Agent", "testDefault"),
            accept_encoding=request.headers.get("Accept-Encoding", "testDefault"),
            accept=request.headers.get("Accept", "testDefault"),
            connection=request.headers.get("Connection", "testDefault"),
            content_type=request.headers.get("Content-Type", "testDefault"),
            cookie=request.headers.get("Cookie", "testDefault"),
            content_length=request.headers.get("Content-Length", "testDefault"),
            url=request.url,
        )
        request = self.api_client.prepare_request(request)

        response = self.api_client.send(request)

        loger.add_response(
            code=response.status_code,
            user_agent=response.headers.get("User-Agent", "testDefault"),
            accept_encoding=response.headers.get("Accept-Encoding", "testDefault"),
            accept=response.headers.get("Accept", "testDefault"),
            connection=response.headers.get("Connection", "testDefault"),
            content_type=response.headers.get("Content-Type", "testDefault"),
            cookie=response.headers.get("Cookie", "testDefault"),
            content_length=response.headers.get("Content-Length", "testDefault"),
            response_data=response.json()
        )

        Path("src/logs/request_log.log")
        allure.attach.file(
            "src/logs/request_log.log",
            name=None,
            attachment_type=allure.attachment_type.TEXT
        )


        return response

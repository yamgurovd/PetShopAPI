class Logger:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_log_to_file(self, data: str) -> any:
        with open(self.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    def add_request(self,
                    url: str,
                    method: str,
                    user_agent: str,
                    accept_encoding: str,
                    accept: str,
                    connection: str,
                    content_type: str,
                    cookie: dict,
                    content_length: str):
        data_to_add = "\n-------------\n"
        data_to_add += f"curl -X {method}\n"
        data_to_add += f"-H 'User-Agent: {user_agent}'\n"
        data_to_add += f"-H 'Accept-Encoding: {accept_encoding}'\n"
        data_to_add += f"-H 'Accept: {accept}'\n"
        data_to_add += f"-H 'Connection: {connection}'\n"
        data_to_add += f"-H 'Content-Type: {content_type}'\n"
        data_to_add += f"-H 'Cookie: {cookie}'\n"
        data_to_add += f"-H 'Content-Length: {content_length}'\n"
        data_to_add += f"-cookie {cookie}\n"
        data_to_add += f"{url}\n"

        self.write_log_to_file(data_to_add)

    def add_response(self,
                     code: int,
                     user_agent: str,
                     response_data: dict,
                     accept_encoding: str,
                     accept: str,
                     connection: str,
                     content_type: str,
                     cookie: dict,
                     content_length: str
                     ):
        data_to_add = f"\nStatus code: {code}\n"
        data_to_add += f"Response data: {response_data}\n"
        data_to_add += f"Response headers:\n"
        data_to_add += f"-H 'User-Agent: {user_agent}'\n"
        data_to_add += f"-H 'Accept-Encoding: {accept_encoding}'\n"
        data_to_add += f"-H 'Accept: {accept}'\n"
        data_to_add += f"-H 'Connection: {connection}'\n"
        data_to_add += f"-H 'Content-Type: {content_type}'\n"
        data_to_add += f"-H 'Cookie: {cookie}'\n"
        data_to_add += f"-H 'Content-Length: {content_length}'\n"

        self.write_log_to_file(data_to_add)

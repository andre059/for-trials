from http.server import HTTPServer, BaseHTTPRequestHandler
import time
from urllib.parse import urlparse, parse_qs


# Определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сет


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """

        self.send_response(200)  # Отправка кода ответа
        self.send_header('Content-type', 'text/plain')  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(b'Hello, World wide web!\n')  # Тело ответа

        # run()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    webServer.server_close()
    print("Server stopped.")

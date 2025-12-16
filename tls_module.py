import ssl
import socket

class TLSModule:
    @staticmethod
    def test_tls_connection(host="google.com"):
        context = ssl.create_default_context()
        with socket.create_connection((host, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                return {
                    "protocol": ssock.version(),
                    "cipher": ssock.cipher()
                }

import http.server
import socketserver
import os
import socket

# Definir o diretório onde estão os arquivos do site
DIRECTORY = "C:\\Users\\johnk\\Desktop\\versao2"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Garantir que o caminho esteja correto e serve todos os arquivos
        path = super().translate_path(path)
        # Adicionar o diretório ao caminho
        return os.path.join(DIRECTORY, os.path.relpath(path, os.getcwd()))

def run_server():
    # Obter o endereço IP local do servidor
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print(f"Endereço IP local: {local_ip}")
    print(f"Servidor HTTP iniciado em http://{local_ip}:{PORT}/")
    
    # Criar e iniciar o servidor HTTP
    handler = CustomHTTPRequestHandler
    with socketserver.ThreadingTCPServer(('', PORT), handler) as httpd:
        httpd.serve_forever()

# Definir a porta do servidor
PORT = 5000

# Rodar o servidor
if __name__ == "__main__":
    run_server()

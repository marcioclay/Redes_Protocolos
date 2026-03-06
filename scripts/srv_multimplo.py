import socket
import threading

def handle_client(con, cliente):
    print(f'>>> Conectado por: {cliente}')
    while True:
        try:
            msg = con.recv(1024)
            if not msg: break
            
            mensagem_recebida = msg.decode('UTF-8')
            print(f"[{cliente}] enviou: {mensagem_recebida}")

            # Simulando a resposta da IA (Aqui entrará a lógica do Gemini/GPT)
            resposta = f"Olá, sou uma cientista. Você disse: {mensagem_recebida}"
            
            con.send(resposta.encode('UTF-8'))
        except:
            break
    print(f"<<< Conexão encerrada com {cliente}")
    con.close()

HOST = '0.0.0.0' # Permite conexões de qualquer IP na rede
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen()

print(f"Servidor de IA rodando na porta {PORT}...")

while True:
    con, cliente = tcp.accept()
    # Cria uma nova Thread para cada cliente
    thread = threading.Thread(target=handle_client, args=(con, cliente))
    thread.start()
    print(f"Total de conexões ativas: {threading.active_count() - 1}")

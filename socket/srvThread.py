import socket
import threading

HOST = ''  # Endereco IP do Servidor e o endereco atual do computador
PORT = 5000  # Porta que o Servidor na maquina

def handle_client(conn, addr):
    print('Conectado por', addr)
    while True:
        msg = conn.recv(1024)
        msg = msg.decode('UTF-8')
        print(addr, msg)

        msg = input(">> Digite a Mensagem: ")
        msg = msg.encode('UTF-8')
        conn.send(msg)

def main():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(10)

    print(">>> Aguardando Conexão")
    while True:
        conn, addr = tcp.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()

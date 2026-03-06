import socket

# Substitua pelo IP real do computador servidor na rede da escola
HOST = '127.0.0.1' 
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

try:
    tcp.connect(dest)
    print("Conectado ao Sistema de IA das Pioneiras!")
    
    while True:
        msg = input(">> Pergunte algo à cientista (ou 'sair'): ")
        if msg.lower() == 'sair': break
        
        tcp.send(msg.encode('UTF-8'))
        
        resposta = tcp.recv(1024)
        print(f"Resposta: {resposta.decode('UTF-8')}")

except Exception as e:
    print(f"Erro ao conectar: {e}")
finally:
    tcp.close()

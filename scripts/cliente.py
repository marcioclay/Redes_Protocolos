import socket

HOST = '127.0.0.1'  # Endereco IP do Servidor (loopback)
PORT = 5000  # Porta que o Servidor esta usando (identifica qual a aplicacao)
# Cria o socket do cliente
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)  # Forma a tupla de host, porta
tcp.connect(dest)  # Estabelece a conexao

while True:
	msg = input(">> Digite a mensagem: ")
	msg = msg.encode('UTF-8')  # Codifica a mensagem para UTF-8
	tcp.send(msg)  # Envio a mensagem para o servidor
	# Recebe mensagem servidor
	msg = tcp.recv(1024)
	msg = msg.decode('UTF-8')
	print(dest, msg)
# ---------------- fim do protocolo --------------

tcp.close()  # fecha a conexao com o servidor


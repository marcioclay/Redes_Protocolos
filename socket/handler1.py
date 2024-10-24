# Abrir o arquivo no modo de leitura
arquivo = open("dados.txt", "r")

# Ler a primeira linha
linha1 = arquivo.readline().strip()

# Ler a segunda linha
linha2 = arquivo.readline().strip()

# Exibir o conteúdo das duas linhas
print("Conteúdo da primeira linha:", linha1)
print("Conteúdo da segunda linha:", linha2)

# Fechar o arquivo
arquivo.close()

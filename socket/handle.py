def dados(msg):
    if msg=="marcio":
        f = open('dados.txt', 'r',encoding='utf-8')
        print(f.read())
        f.close()
    else:
        print("errado")
msg="gustavo"
dados(msg)

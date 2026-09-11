from conexao import conectar

conexao = conectar()
cursor = conexao.cursor()

nome_produto = input("Digite o nome do produto que deseja cadastrar: ")
valor = int(input("Digite o valor do produto: "))

comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'

cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()
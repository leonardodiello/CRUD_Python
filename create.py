from conexao import conectar

conexao = conectar()
cursor = conexao.cursor()

nome_produto = "Farofa"
valor = 4

comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'

cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()
from conexao import conectar

conexao = conectar()
cursor = conexao.cursor()

nome_produto = "Água"
valor = 1

comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'

cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
from conexao import conectar

conexao = conectar()
cursor = conexao.cursor()

nome_produto = "Farofa"

comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'

cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
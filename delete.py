from conexao import conectar

conexao = conectar()
cursor = conexao.cursor()

nome_produto = input("Digite o nome do produto que deseja deletar: ")

comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'

cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
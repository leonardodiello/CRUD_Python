from conexao import conectar

conexao = conectar()
cursor = conexao.cursor()

nome_produto = input("Digite o nome do produto que deseja atualizar: ")
valor = int(input("Digite o novo valor do produto: "))

comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'

cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
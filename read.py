from conexao import conectar

conexao = conectar()
cursor = conexao.cursor()

comando = 'SELECT * FROM vendas'
cursor.execute(comando)

resultado = cursor.fetchall()

for linha in resultado:
    print(f'ID: {linha[0]} | Nome do Produto: {linha[1]} | Valor: {linha[2]}')

cursor.close()
conexao.close()
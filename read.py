from conexao import conectar

conexao = conectar()
cursor = conexao.cursor()

comando = 'SELECT * FROM vendas'
cursor.execute(comando)

resultado = cursor.fetchall()
print(resultado)

cursor.close()
conexao.close()
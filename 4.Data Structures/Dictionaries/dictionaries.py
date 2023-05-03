# Dictionaries
    # Utiliza index no formato keys e Values
    # Aceita string, integer, float, boolean...

aluno = {
    'nome': 'Ana', 
    'idade': 16, 
    'nota_final': 'A', 
    'aprovação': True, 
    'Materias': ['Java', 'Python', 'SQL']
}

print(aluno)
print(aluno['nome'])
print(aluno.get('Materias', 'Não existe'))
print()

aluno['nome'] = 'Jose'
print(aluno)

aluno.update({'nome': 'Bruno', 'nota_final': 'B'})
print(aluno)

aluno.update({'endereco': 'Rua A'})
print(aluno)

print(aluno.get('sobrenome', 'Não existe'))

del aluno['idade']
print(aluno)
print()

print(aluno.items())
print(aluno.keys())
print(aluno.values())
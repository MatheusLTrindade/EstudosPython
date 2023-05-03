# Python Object-Oriented Programming

# Classes
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class (instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar

    # Class: Frutas
    # Objects: Abacate, Banana...


# Criar a classe
class Funcionarios:
    
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

# Criar objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')

# Print
print(usuario1.nome)
print(usuario2.nome)
print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario2))

# Criar os parametros do usuario1
    # usuario1.nome = 'Elena'
    # usuario1.sobrenome = 'Cabral'
    # usuario1.data_nascimento = '12/01/2009'

# Criar os parametros do usuario2
    # usuario2.nome = 'Carol'
    # usuario2.sobrenome = 'Silva'
    # usuario2.data_nascimento = '15/10/2005'

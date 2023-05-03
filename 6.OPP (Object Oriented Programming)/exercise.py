# Python Object-Oriented Programming

# Classes
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class (instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar

from datetime import datetime

# Criar a classe
class Funcionarios:
    
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        return ano_atual - self.ano_nascimento

# Criar objeto
usuario1 = Funcionarios('Elena', 'Cabral', 2009)
usuario2 = Funcionarios('Carol', 'Silva', 2005)
usuario3 = Funcionarios('Murilo', 'Trindade', 2017)

# Print
print(Funcionarios.nome_completo(usuario2))
print(Funcionarios.idade_funcionario(usuario3))

from modelos.personagens.personagem import Personagem

#cria a calsse arqueiro com atributos da classe pai mais o atributo proprio 
class Arqueiro(Personagem):
    def __init__(self, nome, idade, porte, vida, poder):
        super().__init__(nome, idade, porte, vida, poder, flecha)
        
    def atacar(self):
        ataque = self._poder + self._flecha
        return ataque
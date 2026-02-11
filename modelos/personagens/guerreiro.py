from modelos.personagens.personagem import Personagem

#herda atributos da classe pai e adicona atributo proprio 
class Guerreiro(Personagem):
    def __init__(self, nome, idade, porte, vida, poder, soco):
        super().__init__(nome, idade, porte, vida, poder)
        self._soco = soco

    def atacar(self):
        ataque = self._poder + self._soco
        return ataque
        
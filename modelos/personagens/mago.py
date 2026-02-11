
from modelos.personagens.personagem import Personagem

#classe mago com atributos herdados da classe pai e atributos proprios
class Mago(Personagem):
    def __init__(self, nome, idade, porte, poder, vida, magia):
        super().__init__(nome, idade,  porte, vida, poder)
        self._magia = magia

    def __str__(self):
        return f'Mago | {self._nome} | {self._idade} | {self._poder} | {self._vida} '

    def atacar(self):
        ataque = self._poder + self._magia 
        return ataque

    
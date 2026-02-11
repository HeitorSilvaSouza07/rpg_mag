
from abc import ABC, abstractmethod
#cria uma classe desporagem como classe pai e define atriubutos basicos para os outros personagens 
class Personagem():
    def __init__(self, nome, idade, porte, vida, poder, defesa ):
        self._nome = nome
        self._idade = idade   
        self._porte_fisico = porte
        self.vida = vida
        self._poder = poder
        self._defesa = defesa
     
    @abstractmethod
    def atacar(self):
        pass

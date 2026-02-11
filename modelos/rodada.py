#define as informacoes de cada rodada e como elas serão slavas
class Rodada():
    
    #define os atributos de cada rodada 
    def __init__(self, nome_atacante, nome_atacado, dano, vida_atual_atacado):
        self._nome_atacante = nome_atacante
        self._nome_atacado = nome_atacado
        self._dano = dano 
        self._vida_atual_atacado = vida_atual_atacado

    #como as rodadas serão salvas na lista de rodadas
    def __str__(self):
        return f'Personagem atacado: {self._nome_atacado} | Personagem que está atacando: {self._nome_atacante} | Dano recebido pelo atacado: {self._dano} | Vida atual do atacado: {self._vida_atual_atacado} '
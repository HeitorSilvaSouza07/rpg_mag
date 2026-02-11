#importação de bibliotecas e classes de arquivo para manipulação do sistema e funcionamneto do jogo 
import random
from modelos.personagens.arqueiro import Arqueiro
from modelos.personagens.mago import Mago
from modelos.personagens.guerreiro import Guerreiro
from modelos.rodada import Rodada

#meio para controle e regras do jogo 
class Sistema():
    
    #define o que a classe precisa para salvar as rodadas e os danos de cada personagem
    def __init__(self):
        self._rodada = []
        self._vida_personagens = []
    
    #define os dados e se o valor do dado bate de frente com a defesa do outro  jogado, tambem salva o que aconteceu nesssa rodada
    def embate(self, atacante, atacado):
        valor_dado = random.randint(1, 20)
        if valor_dado > atacado._defesa:
            dano = atacante.atacar()
            atacado.vida -= dano
            rodada = Rodada(atacante._nome, atacado._nome, dano, atacado._vida )
            self._rodada.append(rodada)

    #toda rodado atraves dessa função é exibido a vida dos tres personagens em jogo        
    def registrar_vida_jogador(self, jogador_1, jogador_2, Jogador_3):
        registro = {'Nome1' : jogador_1._nome ,'Dano1' : jogador_1.vida,'Nome2' : jogador_2,'Dano2' : jogador_2.vida , 'Nome3' : Jogador_3._nome ,'Dano3' : Jogador_3.vida}
        self._vida_personagens.clear()
        self._vida_personagens.append(registro)

    #lista o que aconteceu em cada rodade de forma organizada e em texto enformando quyem atacou, quem foi atacado e o dano que foi causado 
    def listar_rodada(self):
        for item in self._rodada:
            print(f'{item._nome_atacante} atacou {item._nome_atacado} e deu dano de {item._dano} pontos de vida ao jogador')

    #acessa a lista de vida de personagem e imprime o quanto cada jogador está
    def listar_vida_jogadores(self):
        for vidas in self._vida_personagens:
            print(f'O {vidas['Nome1']} tem {vidas['Dano1']} pontos de vida, o {vidas['Nome2']} tem {vidas['Dano2']} pontos de vida, O {vidas['Nome3']} tem {vidas['Dano3']} de vida,')

import sys
import math
import pygame
from pygame import QUIT

import construtor
import calcula_centro

# Define as dimensões da janela
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Cria a janela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Computação Gráfica')

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (135, 236, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BROWN = (92, 52, 23)
STEEL = (143, 143, 189)
GRAY = (105, 105, 105)

# Limpa a janela com a cor de fundo
screen.fill(WHITE)

coordenadas_iniciais_sabre = [(100, 400), (85, 400), (85, 100), (100, 100)]
coordenadas_iniciais_orelha_esq = [(250, 310), (270, 270), (185, 265)]
coordenadas_iniciais_orelha_dir = [(270, 350), (250, 270), (415, 265)]


def desenhar_sw():
    pygame.init()

    pygame.draw.polygon(screen, GREEN, coordenadas_iniciais_sabre)
    pygame.draw.circle(screen, GREEN, (93, 103), 8)

    #yoda (quase)
    desenhar_yoda()

    ##cano
    cano_fim, centro = desenha_cano()
    ##detalhes
    desenha_detalhes(cano_fim, centro)

    # Atualiza a janela
    pygame.display.flip()

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


def desenhar_yoda():
    pygame.draw.circle(screen, GREEN, (300, 300), 60)  # cabeça
    pygame.draw.polygon(screen, GREEN, coordenadas_iniciais_orelha_esq)
    pygame.draw.polygon(screen, GREEN, coordenadas_iniciais_orelha_dir)
    pygame.draw.circle(screen, WHITE, (325, 290), 10)  # olho esq
    pygame.draw.circle(screen, BLACK, (325, 290), 5)  # iris esq
    pygame.draw.circle(screen, WHITE, (275, 290), 10)  # olho dir
    pygame.draw.circle(screen, BLACK, (275, 290), 5)  # iris dir
    pygame.draw.polygon(screen, BLACK, ([275, 330], [325, 330], [325, 327], [275, 327]))  # boca


def desenha_detalhes(cano_fim, centro):
    detalhe_menor = construtor.aplicar_translacao(0, 280, cano_fim)
    detalhe_fim = construtor.aplicar_escala(1, 0.3, centro, detalhe_menor)
    pygame.draw.polygon(screen, BLACK, detalhe_fim)
    detalhe_baixo = construtor.aplicar_translacao(-10, 63, detalhe_fim)
    detalhe_escala = construtor.aplicar_escala(0.35, 0.8, centro, detalhe_baixo)
    pygame.draw.polygon(screen, BLACK, detalhe_escala)
    detalhe_baixo2 = construtor.aplicar_translacao(12, 63, detalhe_fim)
    detalhe_escala2 = construtor.aplicar_escala(0.35, 0.8, centro, detalhe_baixo2)
    pygame.draw.polygon(screen, BLACK, detalhe_escala2)


def desenha_cano():
    centro = calcula_centro.calcular_centro_quadrado(coordenadas_iniciais_sabre)
    cano = construtor.aplicar_translacao(0, 680, coordenadas_iniciais_sabre)
    cano_fim = construtor.aplicar_escala(1, 0.2, centro, cano)
    pygame.draw.polygon(screen, GRAY, cano_fim)
    return cano_fim, centro

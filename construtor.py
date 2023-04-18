import sys
import math
import pygame
from pygame import QUIT
import calcula_centro
import construtor_yoda

#atribuição de constantes

triang1_points = [(80, 420), (220, 420), (150, 350)] #define coordenadas base do 1 objeto triangulo
quad1_points = [(100, 400), (200, 400), (200, 500), (100, 500)] #define coordenadas base do 1 objeto quadrilátero
# Define as dimensões da janela
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

    # Cria a janela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Computação Gráfica')

    # Define as cores
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (135, 236, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BROWN = (92, 52, 23)

    # Limpa a janela com a cor de fundo
screen.fill(SKY_BLUE)


def aplicar_escala(valor_escala_x, valor_escala_y, centro_objeto, points_obj):
    obj_escala_points = []
    for x, y in points_obj:
        # Calcula as coordenadas em relação ao centro do objeto
        x_rel = x - centro_objeto[0]
        y_rel = y - centro_objeto[1]
        # Aplica a escala
        x_escala = x_rel * valor_escala_x
        y_escala = y_rel * valor_escala_y
        # Calcula as coordenadas finais com base no centro do objeto
        x_final = x_escala + centro_objeto[0]
        y_final = y_escala + centro_objeto[1]
        obj_escala_points.append((x_final, y_final))
    return obj_escala_points


def aplicar_translacao(desloc_x, desloc_y, coordenadas_obj):

    obj2_points = [((x + desloc_x), (y + desloc_y)) for x, y in coordenadas_obj]

    return obj2_points


def aplicar_rotacao(angulo_rotacao, centro_objeto, pontos_objeto):
    # Converte o ângulo de rotação de graus para radianos
    angulo_rad = math.radians(angulo_rotacao)
    obj_rotacao_points = []
    for x, y in pontos_objeto:
        # Calcula as coordenadas relativas ao centro do objeto
        x_rel = x - centro_objeto[0]
        y_rel = y - centro_objeto[1]
        # Aplica a rotação usando as fórmulas de rotação em 2D
        x_rotacao = x_rel * math.cos(angulo_rad) - y_rel * math.sin(angulo_rad)
        y_rotacao = x_rel * math.sin(angulo_rad) + y_rel * math.cos(angulo_rad)
        # Calcula as coordenadas finais com base no centro do objeto
        x_final = x_rotacao + centro_objeto[0]
        y_final = y_rotacao + centro_objeto[1]
        obj_rotacao_points.append((x_final, y_final))
    return obj_rotacao_points


def construtor():
    pygame.init()

    desenhar_obj_base()
    #yoda = escala.desenhar_yoda(screen, GREEN)

    #aplica transformações para porta e desenha
    centro_quad1 = calcula_centro.calcular_centro_quadrado(quad1_points)
    quad2_points = aplicar_escala(0.2, 0.4, centro_quad1, quad1_points)
    quad2_points = aplicar_translacao(-20, 30, quad2_points)
    pygame.draw.polygon(screen, BROWN, quad2_points)

    #aplica transformações para chao e desenha
    quad3_points = aplicar_escala(13, 3, (150, 450), quad1_points)
    quad3_points = aplicar_translacao(500, 200, quad3_points)
    pygame.draw.polygon(screen, GREEN, quad3_points)

    # aplica transformações para janela e desenha
    quad4_points = aplicar_escala(0.4, 0.2, (150, 450), quad1_points)
    quad4_points = aplicar_translacao(20, 20, quad4_points)
    pygame.draw.polygon(screen, BLUE, quad4_points)

    centro_circulo = (0, 0)
    raio_circulo = 20
    angulos = [120, 130, 140, 150, 160]

    # Laço de repetição para criar 5 triângulos em posições diferentes próximas ao objeto circular
    for i in range(5):
        angulo = angulos[i]
        # Cálculo das coordenadas de translação em relação ao objeto circular
        x = centro_circulo[0] + (raio_circulo * math.cos(math.radians(angulo)))
        y = centro_circulo[1] - (raio_circulo * math.sin(math.radians(angulo)))
        centro = calcula_centro.calcular_centro_triangulo(triang1_points)
        triang2_points_transladado = aplicar_translacao(-centro[0], -centro[1], triang1_points)
        triang2_points_escalonado = aplicar_escala(0.15, 0.4, centro, triang2_points_transladado)
        triang2_points_rotacionado = aplicar_rotacao(angulo, centro, triang2_points_escalonado)
        triang2_points_translacao_inversa = aplicar_translacao(centro[0], centro[1], triang2_points_rotacionado)
        triang2_points_translacao_posicao = aplicar_translacao(x, y, triang2_points_translacao_inversa)
        triang2_fim = aplicar_translacao(-350, -820, triang2_points_translacao_posicao)
        pygame.draw.polygon(screen, YELLOW, triang2_fim)

    # desenha maçaneta
    pygame.draw.circle(screen, WHITE, (125, 480), 3)

    # Atualiza a janela
    pygame.display.flip()

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


def desenhar_obj_base():
    # Desenha os objetos base
    pygame.draw.polygon(screen, WHITE, quad1_points)
    pygame.draw.polygon(screen, BROWN, triang1_points)
    pygame.draw.circle(screen, YELLOW, (0, 0), 50)

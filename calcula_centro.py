def calcular_centro_triangulo(coord_base):
    # Calcular o centro do triângulo
    centro_x = (coord_base[0][0] + coord_base[1][0] + coord_base[2][0]) / 3
    centro_y = (coord_base[0][1] + coord_base[1][1] + coord_base[2][1]) / 3

    return centro_x, centro_y


def calcular_centro_quadrado(coord_base):
    # Calcular o centro do quadrado
    centro_x = (coord_base[0][0] + coord_base[1][0] + coord_base[2][0] + coord_base[3][0]) / 4
    centro_y = (coord_base[0][1] + coord_base[1][1] + coord_base[2][1] + coord_base[3][1]) / 4

    return centro_x, centro_y

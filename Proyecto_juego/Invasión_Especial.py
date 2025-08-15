import pygame
import random
import math
from pygame import mixer
import io
# Inicializar pygame
pygame.init()

# Crear pantalla
largo = 800
ancho = 600
pantalla = pygame.display.set_mode((largo, ancho))

def fuente_bytes(fuente):
    with open(fuente,"rb") as f:
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)


# Título e ícono
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("astronave.png")
fondo = pygame.image.load("fondo.jpg")
pygame.display.set_icon(icono)
#importamos la fuente

# Agregar música
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# Variable puntuación
puntuacion = 0
fuente_como_bytes = fuente_bytes("FreeSansBold.ttf")
fuente = pygame.font.Font(fuente_como_bytes, 32)
texto_x = 10
texto_y = 10

# Texto final
fuente_final = pygame.font.Font(fuente_como_bytes, 50)
def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (173, 200))

# Mostrar puntuación
def mostrar_puntuacion(x, y):
    texto = fuente.render(f"Puntuación : {puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

# Jugador
img_jugador = pygame.image.load("astronave prota.png")
jugador_x = largo / 2 - 38
jugador_y = ancho - 100
jugador_x_cambio = 0
velocidad = 0.4

# Enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# Balas
balas = []
img_bala = pygame.image.load("bala.png")

def disparar_bala(x, y):
    pantalla.blit(img_bala, (x + 16, y + 10))

def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt((x_1 - x_2) ** 2 + (y_2 - y_1) ** 2)
    return distancia < 27

# Bucle principal
se_ejecuta = True
juego_terminado = False

while se_ejecuta:
    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -velocidad
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = +velocidad
            if evento.key == pygame.K_SPACE and not juego_terminado:
                mixer.Sound("disparo.mp3").play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)

        if evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                jugador_x_cambio = 0

    jugador_x += jugador_x_cambio
    jugador_x = max(0, min(jugador_x, 736))

    if not juego_terminado:
        for e in range(cantidad_enemigos):
            if enemigo_y[e] > 460:
                juego_terminado = True
                break

            enemigo_x[e] += enemigo_x_cambio[e]

            if enemigo_x[e] <= 0:
                enemigo_x_cambio[e] = 0.5
                enemigo_y[e] += enemigo_y_cambio[e]
            elif enemigo_x[e] >= 736:
                enemigo_x_cambio[e] = -0.5
                enemigo_y[e] += enemigo_y_cambio[e]

            for bala in balas[:]:
                if hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"]):
                    mixer.Sound("Golpe.mp3").play()
                    balas.remove(bala)
                    puntuacion += 1
                    enemigo_x[e] = random.randint(0, 736)
                    enemigo_y[e] = random.randint(20, 200)
                    break

            enemigo(enemigo_x[e], enemigo_y[e], e)

        for bala in balas[:]:
            bala["y"] += bala["velocidad"]
            disparar_bala(bala["x"], bala["y"])
            if bala["y"] < 0:
                balas.remove(bala)

    jugador(jugador_x, jugador_y)
    mostrar_puntuacion(texto_x, texto_y)

    if juego_terminado:
        texto_final()

    pygame.display.update()


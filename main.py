import pygame 
import sys

# Inicializar pygame
pygame.init()

# Definir tableta de colores 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
RED = (255, 0, 0)

# Definir el tamaño de la ventana
ANCHO = 600
LARGO = 400
pantalla = pygame.display.set_mode((ANCHO, LARGO))
pygame.display.set_caption("Juego de preguntas")

# Fuente
fuente = pygame.font.SysFont("Arial", 24)

# Preguntas y opciones
pregunta = "¿Cuál es la capital de Francia?"
opciones = ["A. Berlín", "B. Madrid", "C. Paris", "D. Roma"]
respuesta_correcta = "C"

def mostrar_texto(texto: str, x: int, y: int, color: tuple) -> None:
    """ 
    Muestra el texto renderizado en pantalla
    """
    texto_renderizado = fuente.render(texto, True, color)
    pantalla.blit(texto_renderizado, (x, y))

def dibujar_recuadro_pregunta():
    """ 
    Dibuja el recuadro de la pregunta en la pantalla
    """
    pygame.draw.rect(pantalla, BLUE, (50, 50, ANCHO - 100, 100), 3)
    mostrar_texto(pregunta, 60, 60, BLACK)


# Funcion para dibujar opciones
def dibujar_opciones(seleccion = None, hover = None) -> list:
    posiciones = []
    for i, opcion in enumerate(opciones):
        rectangulo_opciones = pygame.Rect(50, 160 + i * 60, ANCHO - 100, 50)
        
        # Si la opción es la seleccionada, pintamos el fondo de azul
        if seleccion == chr(65 + i):  # 'A' == 65, 'B' == 66, etc.
            pygame.draw.rect(pantalla, BLUE, rectangulo_opciones)  # Rellenar opción con azul
        # Si el mouse está sobre la opción (hover), también pintamos el fondo de azul
        elif hover == chr(65 + i):
            pygame.draw.rect(pantalla, BLUE, rectangulo_opciones)
        else:
            pygame.draw.rect(pantalla, WHITE, rectangulo_opciones)  # Rellenar con blanco para opciones no seleccionadas
        
        # Dibujar el borde del recuadro (siempre visible)
        pygame.draw.rect(pantalla, BLUE, rectangulo_opciones, 3)  # Borde azul
        
        mostrar_texto(opcion, 60, 170 + i * 60, BLACK)
        posiciones.append(rectangulo_opciones)
    
    return posiciones



corriendo = True
seleccion = None  # Inicializar la variable de selección
mostrar_resultado = False  # Variable para mostrar el resultado (Correcto/Incorrecto)
resultado = ""  # Mensaje de resultado
hover_opcion = None # Variable para almacenar la opción sobre la que está el mouse

while corriendo:
    pantalla.fill(WHITE)
    
    # Comprobación de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si el clic fue con el botón izquierdo del mouse (código 1)
            if event.button == 1:  # 1 es el botón izquierdo del mouse
                mouse_x, mouse_y = event.pos  # Obtener las coordenadas del clic
                
                # Comprobar en qué opción se hizo clic
                for i, rect in enumerate(posiciones):
                    if rect.collidepoint(mouse_x, mouse_y):
                        seleccion = chr(65 + i)  # Asigna "A", "B", "C", o "D" según la opción clickeada
                        break

        if event.type == pygame.MOUSEMOTION:
            # Detectar sobre qué opción está el mouse (hover)
            mouse_x, mouse_y = event.pos  # Obtener las coordenadas del mouse
            hover_opcion = None  # Resetear la opción hover
            for i, rect in enumerate(posiciones):
                if rect.collidepoint(mouse_x, mouse_y):
                    hover_opcion = chr(65 + i)  # Asigna la opción sobre la que está el mouse
                    break
    
    # Identificar la respuesta después de que el usuario seleccione una opción
    if seleccion and not mostrar_resultado:
        if seleccion == respuesta_correcta:
            resultado = "¡Respuesta Correcta!"
        else:
            resultado = "Respuesta Incorrecta"
        
        mostrar_resultado = True  # Cambiar el estado para mostrar el resultado
    
    # Mostrar la pregunta y opciones si no se ha mostrado el resultado
    if not mostrar_resultado:
        dibujar_recuadro_pregunta()
        posiciones = dibujar_opciones(seleccion, hover_opcion)  # Pasar hover_opcion al dibujar opciones
    
    # Si mostrar_resultado es True, significa que el jugador ya ha seleccionado una opción y se debe mostrar el resultado
    else:
        mostrar_texto(resultado, ANCHO // 2 - 100, LARGO // 2, RED)
        pygame.display.flip()
        pygame.time.delay(1000)  # 1 segundo para mostrar el resultado antes de reiniciar
        
        # Reiniciar el estado para permitir la siguiente selección
        mostrar_resultado = False  # Volver a permitir que se seleccionen opciones
        seleccion = None  # Limpiar la selección anterior
    
    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()
sys.exit()

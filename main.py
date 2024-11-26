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
    # toma la cadena de texto y la convierte en una superficie renderizada (es decir, una representación gráfica) que Pygame puede dibujar en la pantalla.
    texto_renderizado = fuente.render(texto, True, color)
    # La función blit de Pygame dibuja (o coloca) una superficie sobre otra
    # se está dibujando la superficie del texto (texto_renderizado) en la pantalla
    pantalla.blit(texto_renderizado, (x,y))

def dibujar_recuadro_pregunta():
    """ 
    Dibuja el recuadro de la pregunta en la pantalla
    """
    pygame.draw.rect(pantalla, BLUE, (50, 50, ANCHO - 100, 100), 3)
    mostrar_texto(pregunta, 60, 60, BLACK)

# Funcion para dibujar opciones

def dibujar_opciones(seleccion = None) -> list:
    
    posiciones = []
    
    for i, opcion in enumerate(opciones):
        # enumerate(opciones): enumerate recorre la lista opciones
        # devuelve un índice i y el valor de cada opción. (indice, valor)
        """ 
        Se crea un objeto pygame.Rect que representa un rectángulo en la pantalla. Este rectángulo se usa para definir la posición (coordenadas X y Y) y las dimensiones (ancho y alto) del recuadro que rodeará el texto de la opción.
        """
        """ 
        * (50, 160 + i * 60) establece las coordenadas donde empieza el rectángulo, asegurando que cada opción esté separada verticalmente (espaciada 60 píxeles de la anterior).
        * ANCHO - 100 y 50 definen el ancho del rectángulo (con un margen de 50 píxeles a cada lado) y la altura de 50 píxeles.
        """
        rectangulo_opciones = pygame.Rect(50, 160 + i * 60, ANCHO - 100, 50)
        
        # Si la opcion es la seleccionada, pintamos el fondo de azul
        """ 
        chr(65 + i) convierte el número 65 (que corresponde al carácter 'A') y lo ajusta para que, en cada iteración, se obtenga la letra correspondiente ('A', 'B', 'C', etc.).
        """
        if seleccion == chr(65 + i): # # 'A' == 65, 'B' == 66, etc.
            pygame.draw.rect(pantalla, BLUE, rectangulo_opciones) # Rellena opcion con azul
        else:
            pygame.draw.rect(pantalla, WHITE, rectangulo_opciones)  # Rellenar con blanco para opciones no seleccionadas
        
        # Dibujar el borde del recuadro (siempre visible)
        pygame.draw.rect(pantalla, BLUE, rectangulo_opciones, 3) # Borde azul
        
        mostrar_texto(opcion, 60, 170 + i * 60, BLACK)
        """ 
        opcion: Es el texto de la opción (por ejemplo, "A. Berlín").
        * 60: La posición horizontal (X) en la que se muestra el texto dentro del recuadro (fija en 60).
        * 170 + i * 60: La posición vertical (Y) donde se coloca el texto. Similar a los recuadros, se usa i para espaciar las opciones verticalmente. Se inicia en 170 píxeles y luego se añaden 60 píxeles por cada opción.
        * BLACK: Es el color del texto, que en este caso es negro (debe estar definido previamente en el código).
        """
        posiciones.append(rectangulo_opciones)
    return posiciones

corriendo = True
seleccion = None  # Inicializar la variable de selección
respuesta_muestra = False  # Variable para verificar si la respuesta ha sido mostrada

while corriendo:
    
    pantalla.fill(WHITE)
    
    # Mostrar recuadro de la pregunta
    dibujar_recuadro_pregunta()
    
    # Mostrar opciones y obtener sus posiciones
    posiciones = dibujar_opciones(seleccion)
    
    # Verificar la respuesta después de que el usuario seleccione una opción
    if seleccion:
        if seleccion == respuesta_correcta:
            mostrar_texto("¡Respuesta Correcta!", 200, LARGO - 50, RED)
        else:
            mostrar_texto("Respuesta Incorrecta.", 200, LARGO - 50, RED)
        
        # Establecer un pequeño retraso antes de resetear la selección
        pygame.display.flip()
        pygame.time.delay(1000)  # 1000 ms = 1 segundo
        
        # Reiniciar a la seleccion
        seleccion = None
    
    
    
    # Comprobación de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si el clic fue con el boton izquierdo del mouse (código 1)
            if event.button == 1: # 1 es el botón izquierdo del mouse
                mouse_x, mouse_y = event.pos # Obtener las coordenadas del clic
                
                # Comprobar en que opcion se hizo clic:
                for i, rect in enumerate(posiciones):
                    if rect.collidepoint(mouse_x, mouse_y):
                        seleccion = chr(65 + i) # Asigna "A", "B", "C", o "D" según la opción clickeada
                        break
    
    
    # Actualizar la pantalla
    pygame.display.flip()
    
pygame.quit()
sys.exit()

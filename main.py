import machine
import ili9341
import time

# 1. Configuración de pantalla (VSPI)
spi = machine.SPI(2, baudrate=40000000, sck=machine.Pin(18), mosi=machine.Pin(23))
display = ili9341.Display(spi, dc=machine.Pin(21), rst=machine.Pin(22), cs=machine.Pin(5))

# 2. Definición de colores para el Castillo
COLOR_FONDO = ili9341.color565(20, 20, 30) # Azul muy oscuro (Noche)
COLOR_TEXTO = ili9341.color565(255, 255, 255) # Blanco
COLOR_ORO = ili9341.color565(255, 215, 0) # Dorado para logros

def mostrar_bienvenida():
    display.clear(COLOR_FONDO)
    
    # Ahora que tenemos glcdfont, el texto NO dará error
    # Estructura: draw_text(x, y, texto, fuente, color)
    # Importamos la fuente aquí mismo
    import glcdfont
    
    display.draw_text(40, 50, "EL CASTILLO", glcdfont, COLOR_ORO)
    display.draw_text(20, 100, "Bienvenido, Caballero", glcdfont, COLOR_TEXTO)
    display.draw_text(20, 130, "Esperando cartucho...", glcdfont, COLOR_TEXTO)
    
    print("Castillo renderizado con éxito.")

# Ejecutar el inicio
mostrar_bienvenida()

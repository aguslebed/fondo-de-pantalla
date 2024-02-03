import os
import random
import ctypes 


carpeta = "C:\\Users\\alebe\\Desktop\\Fondo de pantalla\\Fotos"

os.chdir(carpeta)

formatoImagenes = ["jpg","png","jpeg"]
listaImagenes = [imagen for imagen in os.listdir() if imagen.endswith(tuple(formatoImagenes))]


ctypes.windll.user32.SystemParametersInfoW(20, 0, "image.jpg" , 0)

SPI_SETDESKWALLPAPER = 20
imagen = os.path.join(os.getcwd(), random.choice(listaImagenes))
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imagen , 0)
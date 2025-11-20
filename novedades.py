class novedades:
    def __init__(self, clasificacion, tema):
        self.clasificacion = clasificacion
        self.tema = tema
        
    def cambiar_clasificacion(self):
        print(f"cambiando la clasificacion de clasificacion {self.clasificacion} por {self.tema}")
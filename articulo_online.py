class articulo_online:
    def __init__(self, tema):
       self.tema = tema
       
    def publicar(self):
        print(f"publicando el libro del tema {self.tema}")
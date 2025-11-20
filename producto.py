class producto:
    def __init__(self, precio, titulo, autor, editorial, año_de_edicion, preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.año_de_edicion = año_de_edicion
        self.preferencias = preferencias
        
    def vender(self):
        print(f"el libro {self.titulo} se vende en {self.precio}")
        
    def comprar(self):
         print("el libro ha sido comprado")
         
    def ver_catalogo(self):
        print(f"abriendo catalogo de preferencias en el area de {self.preferencias}")
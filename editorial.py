class editorial:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        
    def vender(self):
        print(f" el producto ha sido vendido a {self.nombre}, con telefono {self.telefono} y llegara a la direccion {self.direccion}")
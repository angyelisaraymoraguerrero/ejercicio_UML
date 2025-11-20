class usuario:
    def __init__(self, nombre, apellido, n_cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.n_cuenta = n_cuenta
        self.direccion = direccion
        self.login = login
        self.password = password
        
    def enviar_sugerencia(self):
        print(f"usuario {self.nombre} su sugerencia ha sido enviada con exito")
        
    def leer(self):
        print(f"sus datos de la cuenta {self.n_cuenta} han sido leidos con exito")
        
    def comprar(self):
        print("su compra se esta realizando...")
        
    def vender(self):
        print("su venta se esta realizando...")
        
    def realizar_reclamacion(self):
        print("muy pronto podra reclamar los articulos que ha comprado y/o el dinero de las ventas que ha realizado")
        

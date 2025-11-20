class Procesador:
    def mandar_datos_de_venta(self):
        print ("enviando datos de venta")
        
    def mandar_articulo_online(self):
        print("enviando articulo online")
        
    def envia_sugerencias_administrador(self):
        print("enviando sugerencias al administrador")
        
    def modificar_stock(self):
        pregunta = int(input("si desea modificarlo ingrese 1"))
        if pregunta == 1:
            print("el stick esta siendo modificado")
        else:
            print("el stick no se ha modificado")
        
    def realizar_cobro(self):
        print("el cobro esta siendo realizado")
    
    def realizar_pago(self):
        print("el pago esta siendo realizado")
        
    def actualizar_catalogo(self):
        print("el catalogo esta siendo actualizado")
        
    def realiza_busqueda(self):
        print("buscando....")
        
        
        
        
        
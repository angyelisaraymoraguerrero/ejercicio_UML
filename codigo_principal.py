from usuario import usuario
from servidor import servidor
from indexador import Indexador
from procesador import Procesador
from producto import producto
from recolector import recolector
from hilo import hilo
from editorial import editorial
from libro import libro
from revista import revista
from articulo_de_segunda_mano import articulos_de_segunda_mano
from novedades import novedades
from articulo_online import articulo_online


u = usuario("Angyeli", "Mora", "010010101", "av 23 casa #16", "usuario", "0101" )
u.enviar_sugerencia()
u.leer()
u.comprar()
u.vender()
u.realizar_reclamacion()

s = servidor()
s.mostrar_pagina()
s.enviar_sugerencia()
s.enviar_datos_de_compra()
s.enviar_datos_de_venta()

i = Indexador()
i.actualiza_almacen()
i.envia_resultado_busqueda()

p = Procesador()
p.mandar_datos_de_venta()
p.mandar_articulo_online()
p.envia_sugerencias_administrador()
p.modificar_stock()
p.realizar_cobro()
p.actualizar_catalogo()
p.realiza_busqueda()

r = recolector()
r.envia_novedades()

h = hilo()
h.buscar_novedades()

e = editorial("Angyeli", "av 23", "32000000")
e.vender()


pr = producto("50000", "sigue mi voz", "Ariana Godoy", "paginas de magia", "2020", " romance")
pr.vender()
pr.comprar()
pr.ver_catalogo()

l = libro("romance")

re = revista("romance")

Ar_seg = articulos_de_segunda_mano("romance", "terror", "pancrasio")

nov = novedades("romance", "psicologia")
nov.cambiar_clasificacion()

ar_online = articulo_online("romance")
ar_online.publicar()





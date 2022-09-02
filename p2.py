def leer_archivo(lista, palabra):
	for frase in lista:
		if palabra in frase:
			return True
	return False

print(leer_archivo(['chau eres', 'pedro pascal hola'],'hola')) #return True
print(leer_archivo(['chau eres', 'pedro pascal'],'hola')) #return False

def buscar_palabra(texto, palabra):
	words = texto.split()
	cont = 0
	for p in words:
		if p == palabra:
			cont += 1
	if cont > 0:
		return (1,cont)
	return (0,0)

print(buscar_palabra('hola como estas hola', 'hola')) # return (1,2)
print(buscar_palabra('hola como estas hola', 'xyz')) # return (0,0)
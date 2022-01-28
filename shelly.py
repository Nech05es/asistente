#Python 3.10.0#
#Asistente virtual #

dic = {}#<-- diccionario de palabras de palabras 
list_c = 0
lista =  ['gestos/cara.txt']#<-- lista de caras
num = 0
play = True
while play:
	with open(lista[num],'r') as cara:
		#hacer que se ejecute solo una vez
		if list_c <= 0:
			print(cara.read())
			list_c += 1
			_input = input('--> ')
			if _input == 'hola':
				list_c -= 1
			#@-->validar para responder<--@#	


def numero_primo(numero): #Tenemos la función definida
    if numero < 2: #Si el número de la función es menor a 2, no será primo automáticamente
        print('No es primo') #Por definición matemática, ver nota_1 en la página web
        return

    for i in range(2, int(numero ** 0.5) + 1): #Un iterable ('i') en un rango de 2 hasta la raíz del número + 1
        if numero % i == 0: #Su el resiudo de Numero entre el iterable 'i' es 0...
            print('No es primo') #No será primo
            return
    print('Es primo') #En todos los demás casos será primo

numero_primo(2)
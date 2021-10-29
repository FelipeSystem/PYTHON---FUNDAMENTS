# La barra invertida (\) tiene un significado muy especial cuando 
#se usa dentro de las cadenas, es llamado el carácter de escape.
#La letra n colocada después de la barra invertida proviene de la palabra newline (nueva linea).
print("La Witsi Witsi Araña\nsubió a su telaraña.\n")
print()    
print("Vino la lluvia\ny se la llevó.")

#La función print() pone un espacio entre los argumentos emitidos por iniciativa propia cuando esta separada por coma
print("La Witsi Witsi Arañar" , "subió" , "a su telaraña.")

#Como puedes ver, el argumento de palabra clave end determina los caracteres que la función print() envía a la salida una vez que llega al final de sus argumentos posicionales.
#El comportamiento predeterminado refleja la situación en la que el argumento de la palabra clave end se usa implícitamente de la siguiente manera: end="\n".
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")
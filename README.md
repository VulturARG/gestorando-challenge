# Gestorando-challenge

Un laboratorio está desarrollando un robot capaz de interactuar con personas.
Para que la interacción con éste sea lo más natural posible, es necesario que el artefacto sea capaz de detectar los
sentimientos de las personas que lo rodean.

En una primera etapa el laboratorio decide simplificar esta tarea de la siguiente forma: dado un diccionario en donde
cada palabra posee un puntaje entre -10 y 10 el robot analizará la “positividad” de diversos textos.
Las palabras con mayor puntaje son aquellas que los seres humanos comúnmente consideran positivas.
Por ejemplo: la palabra “fantástico” tiene puntaje 10 y “destestable” tiene -10. 

Nuestra tarea es desarrollar un algoritmo que, dado este diccionario y un texto, nos diga qué tan positivo es este
último, hallando el promedio de la positividad de las palabras.
Cualquier palabra que no se halle en el diccionario tendrá el valor 0.

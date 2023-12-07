# Día 4: Raspas ---
La góndola te lleva hacia arriba. Extrañamente, sin embargo, el suelo no parece estar subiendo contigo; no estás escalando una montaña. Mientras el círculo de Snow Island retrocede debajo de ti, ¡de repente aparece toda una nueva masa de tierra sobre ti! La góndola te lleva a la superficie de la nueva isla y se detiene en la estación.

Al salir de la góndola, lo primero que notas es que el aire aquí es mucho más cálido que en Snow Island. También es bastante húmedo. ¿Es aquí donde está la fuente de agua?

Lo siguiente que notas es a un Elfo sentado en el suelo al otro lado de la estación en lo que parece ser un montón de tarjetas cuadradas y coloridas.

"¡Oh! ¡Hola!" El Elfo corre emocionado hacia ti. "¿En qué puedo ayudarte?" Le preguntas por las fuentes de agua.

"No estoy seguro; solo opero el ascensor de la góndola. Aunque suena como algo que podríamos tener, ¡esto es Island Island, después de todo! Apuesto a que el jardinero lo sabría. Sin embargo, él está en una isla diferente, la pequeña rodeada de agua, no la flotante. Realmente necesitamos idear un mejor esquema de nombres. Mira: si me ayudas con algo rápido, te prestaré mi bote y podrás visitar al jardinero. Recibí todas estas tarjetas de raspado como regalo, pero no puedo averiguar qué he ganado."

El Elfo te lleva hacia el montón de tarjetas coloridas. Allí descubres docenas de tarjetas de raspado, todas con su cubierta opaca ya rasgada. Al coger una, parece que cada tarjeta tiene dos listas de números separadas por una barra vertical (|): una lista de números ganadores y luego una lista de números que tienes. Organizas la información en una tabla (tu entrada de rompecabezas).

Según ha podido averiguar el Elfo, tienes que descubrir qué números que tienes aparecen en la lista de números ganadores. La primera coincidencia hace que la tarjeta valga un punto y cada coincidencia después de la primera duplica el valor de esa tarjeta.

Por ejemplo:

Tarjeta 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53
Tarjeta 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Tarjeta 3: 1 21 53 59 44 | 69 82 63 72 16 21 14 1
Tarjeta 4: 41 92 73 84 69 | 59 84 76 51 58 5 54 83
Tarjeta 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Tarjeta 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
En el ejemplo anterior, la tarjeta 1 tiene cinco números ganadores (41, 48, 83, 86 y 17) y ocho números que tienes (83, 86, 6, 31, 17, 9, 48 y 53). ¡De los números que tienes, cuatro de ellos (48, 83, 17 y 86) son números ganadores! Eso significa que la tarjeta 1 vale 8 puntos (1 por el primer acierto y luego se duplica tres veces por cada uno de los tres aciertos después del primero).

La tarjeta 2 tiene dos números ganadores (32 y 61), por lo que vale 2 puntos.
La tarjeta 3 tiene dos números ganadores (1 y 21), por lo que vale 2 puntos.
La tarjeta 4 tiene un número ganador (84), por lo que vale 1 punto.
La tarjeta 5 no tiene números ganadores, por lo que no vale ningún punto.
La tarjeta 6 no tiene números ganadores, por lo que no vale ningún punto.
Entonces, en este ejemplo, el montón de tarjetas de raspado del Elfo vale 13 puntos.

Toma asiento en el gran montón de tarjetas coloridas. ¿Cuántos puntos valen en total?

## Parte Dos ---
Justo cuando estás a punto de informar tus hallazgos al Elfo, uno de ustedes se da cuenta de que las reglas en realidad han estado impresas en la parte posterior de cada tarjeta todo este tiempo.

No existe tal cosa como "puntos". En lugar de eso, las tarjetas rasca y gana solo te hacen ganar más tarjetas rasca y gana igual al número de números ganadores que tengas.

Específicamente, ganas copias de las tarjetas rasca y gana debajo de la tarjeta ganadora igual al número de coincidencias. Entonces, si la tarjeta 10 tuviera 5 números coincidentes, ganarías una copia de cada una de las tarjetas 11, 12, 13, 14 y 15.

Las copias de las tarjetas rasca y gana se puntúan como las tarjetas rasca y gana normales y tienen el mismo número de tarjeta que la tarjeta que copiaron. Entonces, si ganas una copia de la tarjeta 10 y tiene 5 números coincidentes, entonces ganaría una copia de las mismas tarjetas que la tarjeta original 10 ganó: tarjetas 11, 12, 13, 14 y 15. Este proceso se repite hasta que ninguna de las copias te haga ganar más tarjetas. (Las tarjetas nunca te harán copiar una tarjeta más allá del final de la tabla).

Esta vez, el ejemplo anterior va de manera diferente:

Tarjeta 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Tarjeta 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Tarjeta 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Tarjeta 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Tarjeta 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Tarjeta 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
La tarjeta 1 tiene cuatro números coincidentes, por lo que ganas una copia de cada una de las siguientes cuatro tarjetas: tarjetas 2, 3, 4 y 5.
Tu tarjeta original 2 tiene dos números coincidentes, por lo que ganas una copia de cada una de las tarjetas 3 y 4.
Tu copia de la tarjeta 2 también gana una copia de las tarjetas 3 y 4.
Tus cuatro instancias de la tarjeta 3 (una original y tres copias) tienen dos números coincidentes, por lo que ganas cuatro copias cada una de las tarjetas 4 y 5.
Tus ocho instancias de la tarjeta 4 (una original y siete copias) tienen un número coincidente, por lo que ganas ocho copias de la tarjeta 5.
Tus catorce instancias de la tarjeta 5 (una original y trece copias) no tienen números coincidentes y no ganan más tarjetas.
Tu única instancia de la tarjeta 6 (una original) no tiene números coincidentes y no gana más tarjetas.
Una vez que todas las tarjetas originales y las copias han sido procesadas, terminas con 1 instancia de la tarjeta 1, 2 instancias de la tarjeta 2, 4 instancias de la tarjeta 3, 8 instancias de la tarjeta 4, 14 instancias de la tarjeta 5 y 1 instancia de la tarjeta 6. ¡En total, esta pila de tarjetas rasca y gana te hace terminar con 30 tarjetas rasca y gana en última instancia!

Procesa todas las tarjetas rasca y gana originales y copiadas hasta que no ganes más tarjetas rasca y gana. ¿Incluyendo el conjunto original de tarjetas rasca y gana, cuántas tarjetas rasca y gana en total terminas teniendo?
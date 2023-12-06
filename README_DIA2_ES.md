# Día 2: Enigma del Cubo ---
¡Eres lanzado alto en la atmósfera! El punto más alto de tu trayectoria apenas roza la superficie de una gran isla flotando en el cielo. Aterrizas suavemente en una mullida pila de hojas. Hace bastante frío, pero no ves mucha nieve. Un elfo corre hacia ti para saludarte.

El elfo explica que has llegado a la Isla de la Nieve y se disculpa por la falta de nieve. Estará encantado de explicarte la situación, pero es un poco lejos, así que tienes algo de tiempo. No reciben muchos visitantes aquí arriba; ¿te gustaría jugar a un juego mientras tanto?

Mientras caminas, el elfo te muestra una bolsa pequeña y algunos cubos que son rojos, verdes o azules. Cada vez que juegas este juego, él esconde una cantidad secreta de cubos de cada color en la bolsa, y tu objetivo es descubrir información sobre la cantidad de cubos.

Para obtener información, una vez que una bolsa ha sido cargada con cubos, el elfo meterá la mano en la bolsa, cogerá un puñado de cubos al azar, te los mostrará y luego los devolverá a la bolsa. Él hará esto varias veces en cada juego.

Juegas varias partidas y registras la información de cada juego (tu entrada de puzles). Cada juego está listado con su número de identificación (como el 11 en Juego 11: ...) seguido de una lista separada por punto y coma de subconjuntos de cubos que fueron revelados de la bolsa (como 3 azules, 5 verdes, 4 azules).

Por ejemplo, el registro de algunos juegos podría verse así:

```
Juego 1: 3 azules, 4 rojos; 1 rojo, 2 verdes, 6 azules; 2 verdes
Juego 2: 1 azul, 2 verdes; 3 verdes, 4 azules, 1 rojo; 1 verde, 1 azul
Juego 3: 8 verdes, 6 azules, 20 rojos; 5 azules, 4 rojos, 13 verdes; 5 verdes, 1 rojo
Juego 4: 1 verde, 3 rojos, 6 azules; 3 verdes, 6 rojos; 3 verdes, 15 azules, 14 rojos
Juego 5: 6 rojos, 1 azul, 3 verdes; 2 azules, 1 rojo, 2 verdes
```

En el juego 1, se revelan tres conjuntos de cubos de la bolsa (y luego se vuelven a poner). El primer conjunto es de 3 cubos azules y 4 cubos rojos; el segundo conjunto es de 1 cubo rojo, 2 cubos verdes y 6 cubos azules; el tercer conjunto es solo de 2 cubos verdes.

El elfo quiere saber primero qué juegos habrían sido posibles si la bolsa solo contuviera 12 cubos rojos, 13 cubos verdes y 14 cubos azules.

En el ejemplo anterior, los juegos 1, 2 y 5 habrían sido posibles si la bolsa hubiera estado cargada con esa configuración. Sin embargo, el juego 3 habría sido imposible porque en un momento el elfo te mostró 20 cubos rojos a la vez; de manera similar, el juego 4 también habría sido imposible porque el elfo te mostró 15 cubos azules a la vez. Si sumas los ID de los juegos que habrían sido posibles, obtienes 8.

Determina qué juegos habrían sido posibles si la bolsa hubiera sido cargada solo con 12 cubos rojos, 13 cubos verdes y 14 cubos azules. ¿Cuál es la suma de los ID de esos juegos?

## Parte Dos ---
¡El elfo dice que han dejado de producir nieve porque no están recibiendo agua! No está seguro de por qué se detuvo el agua; sin embargo, puede mostrarte cómo llegar a la fuente de agua para que lo compruebes por ti mismo. ¡Está justo ahí adelante!

Mientras continúas tu caminata, el elfo plantea una segunda pregunta: en cada juego que jugaste, ¿cuál es la menor cantidad de cubos de cada color que podría haber estado en la bolsa para hacer posible el juego?

Considera nuevamente los juegos de ejemplo mencionados anteriormente:

Juego 1: 3 azules, 4 rojos; 1 rojo, 2 verdes, 6 azules; 2 verdes
Juego 2: 1 azul, 2 verdes; 3 verdes, 4 azules, 1 rojo; 1 verde, 1 azul
Juego 3: 8 verdes, 6 azules, 20 rojos; 5 azules, 4 rojos, 13 verdes; 5 verdes, 1 rojo
Juego 4: 1 verde, 3 rojos, 6 azules; 3 verdes, 6 rojos; 3 verdes, 15 azules, 14 rojos
Juego 5: 6 rojos, 1 azul, 3 verdes; 2 azules, 1 rojo, 2 verdes
En el juego 1, el juego podría haberse jugado con un mínimo de 4 cubos rojos, 2 verdes y 6 azules. Si algún color tuviera incluso un cubo menos, el juego habría sido imposible.
El juego 2 podría haberse jugado con un mínimo de 1 rojo, 3 verdes y 4 azules.
El juego 3 debe haberse jugado con al menos 20 rojos, 13 verdes y 6 azules.
El juego 4 requirió al menos 14 rojos, 3 verdes y 15 azules.
El juego 5 no necesitaba menos de 6 rojos, 3 verdes y 2 azules en la bolsa.
El poder de un conjunto de cubos es igual al producto de los números de cubos rojos, verdes y azules. El poder del conjunto mínimo de cubos en el juego 1 es 48. En los juegos 2-5 fue 12, 1560, 630 y 36, respectivamente. Sumar estos cinco poderes produce la suma 2286.

Para cada juego, encuentra el conjunto mínimo de cubos que debe haber estado presente. ¿Cuál es la suma del poder de estos conjuntos?
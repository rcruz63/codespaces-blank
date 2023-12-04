# Día 3: Relaciones de Engranajes ---
Tú y el Elfo finalmente llegan a una estación de teleférico; él dice que el teleférico te llevará hasta la fuente de agua, pero este es el punto hasta donde él puede llevarte. Entras.

No tardáis mucho en encontrar los teleféricos, pero parece haber un problema: no se están moviendo.

"¡Aaah!"

Te giras para ver a un Elfo ligeramente grasiento con una llave inglesa y una expresión de sorpresa. "¡Perdón, no esperaba a nadie! El teleférico no está funcionando en este momento; aún pasará un tiempo antes de que pueda arreglarlo." Ofreces tu ayuda.

El ingeniero explica que parece faltar una parte del motor en el motor, pero nadie puede averiguar cuál es. Si sumas todos los números de las partes en el esquema del motor, debería ser fácil descubrir qué parte falta.

El esquema del motor (tu entrada del puzle) consiste en una representación visual del motor. Hay muchos números y símbolos que realmente no comprendes, pero al parecer cualquier número adyacente a un símbolo, incluso en diagonal, es un "número de parte" y debería incluirse en tu suma. (Los puntos (.) no cuentan como un símbolo.)

Aquí tienes un ejemplo del esquema del motor:

```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```

En este esquema, dos números no son números de parte porque no están adyacentes a un símbolo: 114 (arriba a la derecha) y 58 (en el centro a la derecha). Todos los demás números están adyacentes a un símbolo y, por lo tanto, son números de parte; su suma es 4361.

Por supuesto, el esquema del motor real es mucho más grande. ¿Cuál es la suma de todos los números de las partes en el esquema del motor?

## Parte Dos ---
¡El ingeniero encuentra la pieza perdida e instala en el motor! A medida que el motor cobra vida, te subes al teleférico más cercano, finalmente listo para ascender hacia la fuente de agua.

Sin embargo, no pareces estar yendo muy rápido. ¿Quizás algo sigue mal? Afortunadamente, el teleférico tiene un teléfono etiquetado como "ayuda", así que lo coges y el ingeniero responde.

Antes de que puedas explicar la situación, ella sugiere que mires por la ventana. Allí está el ingeniero, sosteniendo un teléfono en una mano y saludando con la otra. Vas tan despacio que ni siquiera has salido de la estación. Sales del teleférico.

La pieza faltante no fue el único problema; uno de los engranajes en el motor está mal. Un engranaje es cualquier símbolo * que esté adyacente exactamente a dos números de parte. Su relación de engranaje es el resultado de multiplicar esos dos números juntos.

Esta vez, debes encontrar la relación de engranaje de cada engranaje y sumarlos todos para que el ingeniero pueda determinar qué engranaje necesita ser reemplazado.

Considera nuevamente el mismo esquema del motor:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
En este esquema, hay dos engranajes. El primero está en la parte superior izquierda; tiene los números de parte 467 y 35, por lo que su relación de engranaje es 16345. El segundo engranaje está en la parte inferior derecha; su relación de engranaje es 451490. (El * adyacente a 617 no es un engranaje porque solo está adyacente a un número de parte). Sumando todas las relaciones de engranajes se obtiene 467835.

¿Cuál es la suma de todas las relaciones de engranajes en el esquema de tu motor?
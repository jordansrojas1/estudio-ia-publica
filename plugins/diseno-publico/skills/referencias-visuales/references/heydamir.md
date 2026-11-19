# heydamir.design, desarmado

> **Autor y titular:** Damir, diseñador de producto — https://heydamir.design
> El diseño, los textos, las imágenes y los videos del sitio son obra de su autor.
> Este archivo solo describe, con fines educativos, decisiones de diseño observables
> en el sitio público (medidas el 2026-11-01; el sitio puede haber cambiado).
> No hay afiliación ni respaldo del autor. Análisis original: Jordan Rojas.

Portafolio personal construido con Next.js y Tailwind.

## Tokens

```css
:root {
  /* Oscuro CÁLIDO, no negro. Ahí está medio efecto. */
  --bg:        #151413;   /* rgb(21, 20, 19) */
  --surface:   #302D2A;   /* tarjetas, botón secundario */
  --text:      #EFE9DE;   /* crema, nunca #fff */
  --text-2:    rgb(239 233 222 / .64);
  --text-3:    rgb(239 233 222 / .40);

  --radius:      28px;    /* tarjetas */
  --radius-pill: 9999px;  /* botones */

  --ease: cubic-bezier(.22, 1, .36, 1);  /* conocida como easeOutQuint */
}
```

Tipografía: **Inter Tight**, un solo peso visible (500) en los titulares.
Interlineado de **1.1** y espaciado entre letras de **-0.012em**. Titular apretado,
cuerpo suelto. No hay una fuente decorativa aparte: el carácter sale del espaciado y
del color.

Acento: un solo naranja, usado **una vez**: en la última palabra del titular y en el
brillo del botón principal. Nada más lo lleva.

## Layout

```
pantalla completa, sin scroll de la página
├── columna izquierda (~42 %, quieta)
│   ├── foto + nombre + "disponible para proyectos"
│   ├── titular (2 líneas, la última palabra en acento)
│   ├── subtítulo en --text-2
│   └── dos botones: uno principal, uno secundario
└── columna derecha (~58 %, galería que se desplaza)
    └── 25 tarjetas con video, una sola columna
```

## Movimiento

```css
/* tarjeta al pasar el cursor */
transition: translate .5s var(--ease), box-shadow .5s var(--ease);
/* botones */
transition: transform .16s var(--ease), opacity .15s;
```

Dos velocidades y nada más: **160 ms** para lo que responde al dedo, **500 ms** para
lo que se desplaza. La misma curva en todo.

## Los tres trucos

1. **La vitrina es video, no imagen.** Cada tarjeta es un clip corto del proyecto en
   movimiento. Es lo que hace que el sitio se sienta vivo.
2. **Oscuro cálido + crema.** #151413 sobre #EFE9DE en vez de #000 sobre #fff.
   Mismo contraste alto (más de 15:1), cero frialdad.
3. **Señal de que hay alguien.** Un estado "disponible" y la hora local. Convierte un
   sitio en una persona que atiende.

## Qué no copiar

- La galería con scroll simulado: es cara de mantener y pelea con los lectores de
  pantalla y con el teclado. Una entidad pública no puede permitírselo.
- Sus textos, su posicionamiento, sus videos ni su composición literal.
- 25 videos en una página: en conexiones lentas (muchos municipios) es inviable.

## Qué sí sirve para una entidad pública

- **Un solo color de acento por pantalla**, usado para lo único que la persona tiene
  que hacer (por ejemplo, "Radicar mi solicitud").
- **Dos velocidades de movimiento y una curva.** Orden que se siente, aunque no se vea.
- **La señal de que hay alguien**, traducida: "Atención hoy de 8:00 a. m. a 4:00 p. m."
  o "Tiempo de respuesta: 15 días hábiles".
- **Colores suaves en vez de negro y blanco puros**, sin perder contraste.

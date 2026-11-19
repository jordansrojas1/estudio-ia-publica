# admin-OS, desarmado

> **Autor y titular:** lroy-stack — https://github.com/lroy-stack/admin-os
> Proyecto de código abierto bajo licencia MIT. Demo: https://admin-os.lr0y.dev
> Este archivo no copia código del proyecto: describe y comenta, con fines
> educativos, las decisiones que sus autores publicaron en sus documentos de diseño
> (ADR y hoja de temas), leídos en noviembre de 2026. No hay afiliación ni respaldo
> de los autores. Análisis original: Jordan Rojas.

Panel de gestión para negocios pequeños. Next.js, React, Tailwind y shadcn/ui.

**Por qué está aquí.** No por cómo se ve, sino por **cómo decide**: cada color tiene
escrito su criterio de accesibilidad, y las discusiones de diseño se cierran con
medidas. Esa disciplina es exactamente la que necesita una entidad pública.

## Lo que enseña

### 1. Separar los roles de los colores concretos
Un archivo define **roles** (fondo, texto, tarjeta, borde, aviso…) y otro, más
pequeño, define los **colores** de cada tema. Cambiar de tema es cambiar cinco
valores, no rehacer todo. Para una entidad: el día que cambie la imagen institucional,
se cambia una hoja, no cien páginas.

### 2. Donde hay texto que leer, la transparencia se vuelve casi sólida
Sus menús usan "cristal" con un relleno del 94–96 %, para que lo que hay detrás nunca
compita con el texto. Regla útil: los efectos van donde no estorban la lectura.

### 3. Respeta a quien no quiere transparencias
Tiene un bloque `prefers-reduced-transparency` que vuelve opacas las superficies sin
perder la jerarquía visual. Es el primo de `prefers-reduced-motion`, y muy pocos
sitios lo tienen.

### 4. Cerrar una discusión midiendo (su ADR 0002)
Evaluaron un efecto de refracción "de lujo" y lo **rechazaron después de medirlo**:
pesaba +12,1 KB y cambiaba apenas el 0,2 % de los píxeles. "Imperceptible lado a
lado". Quitaron la dependencia y dejaron escrito por qué.

### 5. Contraste citado, no afirmado
Cada regla lleva su fuente: WCAG 2.2 criterio 1.4.3 (4,5:1 para texto), 1.4.11 (3:1
para elementos que no son texto) y 1.4.1 (un estado nunca depende solo del color).
Y cuando no pudieron verificar una fuente, lo dicen.

## Qué no copiar

- **El código**, salvo que se respete su licencia MIT (mantener el aviso de copyright).
  Aquí se trasplantan ideas, no archivos.
- **La madurez**: era un proyecto muy joven, de un solo mantenedor. Excelente para
  leer; para depender de él en una entidad, todavía no.

## Qué sí sirve para una entidad pública

- Escribir, junto a cada decisión de diseño, **la norma o el criterio que la justifica**
  (WCAG 2.1 AA, Resolución 1519 de 2020).
- Dejar escrito también **lo que se rechazó y por qué**.
- Medir antes de comprar un efecto, una librería o una herramienta.

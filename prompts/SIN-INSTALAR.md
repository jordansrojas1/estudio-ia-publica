# Prompts para usar el kit sin instalar nada

Copia uno, cambia lo que está entre [corchetes] y pégalo en ChatGPT, Gemini,
Copilot o Claude.

> Recuerda: **cero datos personales reales**. Usa entidades y personas ficticias.

---

## 1. Crear una pieza ciudadana

```
Actúa como diseñador de servicios públicos digitales. Crea UN SOLO archivo HTML
(con el CSS y el JavaScript dentro, sin librerías externas) que explique a la
ciudadanía el trámite [NOMBRE DEL TRÁMITE] de [ENTIDAD FICTICIA].
Público principal: [QUIÉN LO VA A LEER].

Contenido:
- Un titular que diga el beneficio para la persona, no el nombre del trámite.
- Una entrada de dos frases.
- Tres cifras clave (plazos, costos o requisitos) que cuenten solas al aparecer.
- De 3 a 5 pasos numerados, cada uno empezando con un verbo.
- Una lista de chequeo interactiva con barra de progreso (que no envíe nada).
- Tres preguntas frecuentes desplegables.
- Un aviso que diga que es un ejemplo ficticio y cite la norma de cada plazo.

Reglas de diseño (obligatorias):
- Contraste de 4,5:1 o más en todo el texto (WCAG 2.1 AA, Resolución 1519 de 2020).
- Un solo color de acento, solo para el botón principal y la frase clave.
- Solo dos duraciones de animación (160 ms y 500 ms) y una sola curva:
  cubic-bezier(.22, 1, .36, 1).
- Un bloque @media (prefers-reduced-motion: reduce) que apague el movimiento.
- Enlace "Saltar al contenido", foco visible y que funcione con teclado y en celular.
- Lenguaje claro: frases de menos de 25 palabras y nada de siglas sin explicar.

Marca con [VERIFICAR] cualquier dato que no te haya dado yo.
Al final, dime cómo abrir el archivo.
```

---

## 2. Revisar si una página se lee bien

```
Actúa como auditor de accesibilidad web. Te voy a pegar el CSS (o el HTML) de una
página. Haz esto:

1. Lista cada color de texto y calcula su relación de contraste contra el fondo,
   con la fórmula de luminancia relativa de WCAG 2.1.
2. Di cuáles NO llegan a 4,5:1 (texto normal) o 3:1 (texto grande).
3. Para cada uno que falle, dime dónde se usa, si es texto que alguien necesita
   leer, y propón el color más parecido que sí cumpla.
4. Cuenta cuántas duraciones y curvas de animación distintas hay, y propón dejar
   solo dos duraciones y una curva.
5. Dime si falta el bloque prefers-reduced-motion.

Escribe para alguien que no es programador: primero un resumen de tres líneas,
luego las tablas. Aclara que tus cálculos conviene confirmarlos con el verificador
de WebAIM (https://webaim.org/resources/contrastchecker/).

Este es el código:
[PEGA AQUÍ EL CSS O EL HTML]
```

---

## 3. Aprender de un sitio bien hecho

```
Quiero aprender de un sitio con buen diseño: [ENLACE O NOMBRE DEL SITIO].
Analízalo como lo haría un diseñador, sin copiarlo:

1. Paleta (fondo, texto, acento) y por qué funciona.
2. Tipografía: tamaños, interlineado, espaciado.
3. Movimiento: cuántas velocidades y qué sensación dan.
4. Los dos o tres "trucos" que lo hacen verse bien.
5. Qué NO deberíamos copiar en una entidad pública, y por qué.
6. Qué SÍ podríamos aplicar en [MI ENTIDAD O PROYECTO], respetando WCAG 2.1 AA.

Cita siempre el sitio como fuente y recuerda que su diseño pertenece a sus autores.
```

---

*Prompts del kit* estudio-ia-publica *de Jordan Rojas, CC BY 4.0.*
*Curso IA Generativa para la Gestión Pública, Universidad de los Andes.*

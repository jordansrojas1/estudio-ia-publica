# Ejemplos

| Archivo | Qué es |
|---|---|
| `pieza-ciudadana-derecho-de-peticion.html` | Lo que produce la habilidad `pieza-ciudadana`. Descárgalo y ábrelo con doble clic. Alcaldía **ficticia**. |
| `sitio-para-auditar/estilos.css` | La hoja de estilos de un portal ficticio, con los errores típicos, para practicar `auditar-diseno`. |

## Ejercicio de 10 minutos

1. Abre `sitio-para-auditar/estilos.css`, copia todo su contenido y pégaselo a
   Claude con: *"Usa la habilidad auditar-diseno: ¿se lee bien?"*
2. Deberías encontrar **5 de 6 colores** que no llegan a 4,5:1, **7 duraciones** y
   **6 curvas** de animación distintas, y que falta `prefers-reduced-motion`.
3. Pídele el CSS corregido y vuelve a auditarlo.

Pista: el gris de los requisitos (`#A0A0A0`) es el hallazgo más grave. Es texto que
la ciudadanía necesita para hacer el trámite.

# Guía de instalación, paso a paso

No necesitas saber programar. Elige **un solo camino** y sigue los pasos en orden.

| Camino | Para quién | Qué necesitas | Tiempo |
|---|---|---|---|
| 🟢 **A. Claude en el navegador** | La mayoría. **Empieza aquí.** | Una cuenta de Claude (sirve la gratuita) | 5 minutos |
| 🔵 **B. Claude Code** | Quien ya usa Claude Code o quiere probarlo | Plan pago de Claude (Pro o superior) | 10 minutos |
| ⚪ **C. Sin instalar nada** | Quien usa ChatGPT, Gemini o Copilot | Cualquier chat de IA | 1 minuto |

```mermaid
flowchart LR
    I([¿Qué usas?]) --> A[Claude en el navegador<br/>o en la app]
    I --> B[Claude Code<br/>en la terminal]
    I --> C[ChatGPT, Gemini<br/>o Copilot]
    A --> A1[Descarga el ZIP] --> A2[Súbelo en<br/>Personalizar → Habilidades] --> L([¡Listo!])
    B --> B1[Agrega el marketplace] --> B2[Instala diseno-publico] --> L
    C --> C1[Copia un prompt<br/>de prompts/SIN-INSTALAR.md] --> L
```

> **Antes de empezar, dos reglas del curso:**
> 1. **Nunca pegues datos personales reales** (cédulas, nombres de ciudadanos,
>    teléfonos, direcciones) en ninguna IA. Usa datos ficticios.
> 2. Todo lo que produzca la IA **se revisa** antes de usarse en la entidad.

---

## 🟢 Camino A: Claude en el navegador (recomendado)

Funciona en [claude.ai](https://claude.ai) y en la aplicación de escritorio de Claude.

### Paso 1. Descarga la habilidad

Haz clic en la que quieras. El archivo `.zip` se descarga solo. **No lo
descomprimas.**

| Habilidad | Para qué | Descarga |
|---|---|---|
| ⭐ **pieza-ciudadana** | Crear una página para explicar un trámite o una política | [pieza-ciudadana.zip](https://github.com/jordansrojas1/estudio-ia-publica/raw/main/descargas/pieza-ciudadana.zip) |
| **auditar-diseno** | Revisar si una página se lee bien y si sus animaciones están ordenadas | [auditar-diseno.zip](https://github.com/jordansrojas1/estudio-ia-publica/raw/main/descargas/auditar-diseno.zip) |
| **referencias-visuales** | Aprender de sitios bien diseñados | [referencias-visuales.zip](https://github.com/jordansrojas1/estudio-ia-publica/raw/main/descargas/referencias-visuales.zip) |

Si es tu primera vez, empieza solo con **pieza-ciudadana**.

### Paso 2. Activa la ejecución de código

1. Entra a [claude.ai](https://claude.ai) con tu cuenta.
2. Abre **Configuración** (Settings) → **Capacidades** (Capabilities).
3. Activa **Ejecución de código y creación de archivos** (Code execution and file creation).

> Las habilidades necesitan esta opción. Sin ella, no aparecen.

### Paso 3. Sube la habilidad

1. Ve a **Personalizar** (Customize) → **Habilidades** (Skills).
2. Haz clic en **+** → **Crear habilidad** (Create skill) → **Subir una habilidad** (Upload a skill).
3. Elige el `.zip` que descargaste en el paso 1.
4. La habilidad aparece en tu lista. Comprueba que esté **activada**.

Repite el paso 3 con cada `.zip` que quieras sumar.

> Los nombres de los menús pueden cambiar con el tiempo. Si no los encuentras,
> mira la [guía oficial de Anthropic sobre habilidades](https://support.claude.com/en/articles/12512180-use-skills).

### Paso 4. Pruébala

Abre un chat nuevo y pega esto:

```
Usa la habilidad pieza-ciudadana para crear una página que explique, en lenguaje
claro, cómo pedir un certificado de residencia en una alcaldía ficticia llamada
Villa Esperanza. Público: adultos mayores.
```

Claude te devuelve un archivo `.html`. Descárgalo y ábrelo con **doble clic**: se
abre en tu navegador. 🎉

---

## 🔵 Camino B: Claude Code

Claude Code requiere un plan **Pro, Max, Team o Enterprise** (el plan gratuito no
lo incluye).

### Paso 1. Instala Claude Code (si aún no lo tienes)

Abre la terminal:
- **Mac**: presiona `Cmd + Espacio`, escribe *Terminal* y presiona Enter.
- **Windows**: abre el menú Inicio, escribe *PowerShell* y presiona Enter.

Copia y pega el comando de tu sistema, y presiona Enter:

**Mac o Linux**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell)**
```powershell
irm https://claude.ai/install.ps1 | iex
```

Cierra la terminal, ábrela de nuevo y escribe `claude`. La primera vez te pide
iniciar sesión en el navegador.

> ¿Prefieres no usar la terminal? La **aplicación de escritorio de Claude** trae
> Claude Code en su pestaña *Code*. Guía oficial: https://code.claude.com/docs/en/setup

### Paso 2. Agrega este kit

Dentro de Claude Code, escribe estas dos líneas, una por una:

```
/plugin marketplace add jordansrojas1/estudio-ia-publica
```

```
/plugin install diseno-publico@estudio-ia-publica
```

Si Claude Code te pregunta si confías en el marketplace, responde que sí.

### Paso 3. Pruébalo

Escribe:

```
/diseno-publico:pieza-ciudadana Crea una página que explique cómo pedir un
certificado de residencia en una alcaldía ficticia llamada Villa Esperanza.
```

Y después, para revisar lo que acabas de crear:

```
/diseno-publico:auditar-diseno Revisa la página que acabas de crear y dime, en
lenguaje sencillo, si todo el texto se lee bien.
```

### Para actualizar el kit más adelante

```
/plugin marketplace update estudio-ia-publica
```

---

## ⚪ Camino C: sin instalar nada

Abre [`prompts/SIN-INSTALAR.md`](prompts/SIN-INSTALAR.md), copia el prompt que
quieras y pégalo en ChatGPT, Gemini, Copilot o Claude. Funciona igual de bien para
practicar; solo pierdes las mediciones automáticas de contraste.

---

## ¿Algo salió mal?

| Me pasa esto | Haz esto |
|---|---|
| No veo **Habilidades** en el menú | Activa *Ejecución de código* (Camino A, paso 2) y recarga la página |
| Al subir el ZIP sale un error | No lo descomprimas ni lo renombres. Descárgalo de nuevo desde el enlace |
| Claude no usa la habilidad | Nómbrala en tu mensaje: "Usa la habilidad pieza-ciudadana para…" |
| `claude` no se reconoce en la terminal | Cierra y vuelve a abrir la terminal. Si sigue, mira la guía oficial de instalación |
| El `.html` se ve como texto raro | Guárdalo con extensión `.html` y ábrelo con Chrome, Edge, Firefox o Safari |
| Dice que falta Python | Solo afecta las mediciones automáticas. Pide a Claude que calcule el contraste "a mano", o instala Python desde https://www.python.org |

¿Sigues con dudas? Pregunta en el grupo del curso o escríbele al profesor.

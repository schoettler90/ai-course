# Pensum del Curso: Agentes de IA — De Cero a Creador

Un curso de ~20 horas para principiantes sobre IA y Agentes de IA, estructurado en 10 clases de aproximadamente 2 horas cada una.
Cada clase contiene múltiples lecciones con explicaciones de conceptos, casos de estudio del mundo real, ejercicios prácticos guiados, desafíos independientes y cuestionarios.

---

## Mapa del Curso de un Vistazo

| Clase | # | Lección | Horas | Módulo | Herramientas / Frameworks |
|-------|---|--------|-------|--------|---------------------|
| 1 | 01 | Bienvenida: La IA en el Mundo Real | 1h | Fundamentos | Claude Code (demo) |
| 1 | 02 | Una Breve Historia de la IA | 1h | Fundamentos | — |
| 2 | 03 | Cómo Funcionan los LLMs | 2h | Fundamentos | ChatGPT, Claude.ai, Gemini |
| 3 | 04 | Uso de APIs de LLM y Salidas Estructuradas | 1h | LLMs en Código | SDK de Anthropic, SDK de OpenAI |
| 3 | 05 | Herramientas y MCP | 1h | LLMs en Código | SDK de Anthropic, JSON, MCP |
| 4 | 06 | RAG: Conceptos e Implementación | 2h | RAG | LangChain, Chroma |
| 5 | 07 | Claude Code: Arquitectura y Diseño de Agentes | 2h | Agentes y Código | Claude Code |
| 6 | 08 | Antigravity: Construir una Aplicación Simple | 2h | Agentes de Código | Antigravity |
| 7 | 09 | Claude Cowork: Análisis de Datos y Documentos | 2h | Agentes de Código | Claude Cowork |
| 8 | 10 | OpenClaw: IA Local y Agentes Personales | 2h | IA Local | OpenClaw, Ollama |
| 9 | 11 | OpenClaw: Construir un Agente de Marketing | 2h | IA Local | OpenClaw |
| 10 | 12 | Agentes No-Code con N8N | 2h | Avanzado | N8N |

---

## Clase 1 — Fundamentos (2 horas)

### Lección 01 — Bienvenida: La IA en el Mundo Real
**Tema:** ¿Para quién es este curso y por qué es importante ahora?

**Temas:**
- Introducción: antecedentes del instructor, motivación para el curso
- ¿Qué es la IA? ¿Qué es un agente de IA? (definiciones intuitivas, sin jerga)
- Casos de uso en el mundo real: la IA en la vida diaria, los negocios, la ciencia y la creatividad
- Demo en vivo: Claude Code como un agente de vanguardia en acción
- Visión general del viaje del curso por delante

**Términos clave del glosario:** IA, Agente, LLM, Claude Code

---

### Lección 02 — Una Breve Historia de la IA
**Tema:** ¿Cómo llegamos aquí? De perceptrones a agentes.

**Temas:**
- IA temprana y sistemas basados en reglas (décadas de 1950 a 1980)
- Machine Learning (Aprendizaje Automático): enseñando a las computadoras a partir de datos
- Redes neuronales y el auge del aprendizaje profundo (deep learning)
- GPUs: el hardware que lo cambió todo
- AlexNet y el momento ImageNet (2012)
- Redes Neuronales Convolucionales (CNNs) y visión por computadora
- La arquitectura Transformer: *"Attention Is All You Need"* (2017)
- Leyes de Escalado (Scaling Laws): más grande es mejor (hasta cierto punto)
- GPT-2, GPT-3, GPT-4 y la revolución de los LLMs
- Dónde estamos hoy: modelos fundacionales y agentes de IA

**Términos clave del glosario:** Machine Learning, Red Neuronal, Deep Learning, GPU, AlexNet, CNN, Transformer, Leyes de Escalado, GPT, Modelo Fundacional

---

## Clase 2 — LLMs, Ingeniería de Prompts e IA Multimodal (2 horas)

### Lección 03 — Cómo Funcionan los LLMs
**Tema:** Entender cómo funcionan los grandes modelos de lenguaje y empezar a usar las principales herramientas de IA.

**Temas:**
- Tokens: cómo el texto se convierte en números
- La ventana de contexto: lo que el modelo puede "ver"
- Pre-entrenamiento vs. fine-tuning vs. RLHF
- Por qué los modelos alucinan — y qué hacer al respecto
- Prompts del sistema (System prompts) y cómo moldean el comportamiento
- Recorrido por ChatGPT, Claude.ai y Gemini
- IA Multimodal: yendo más allá del texto (imágenes, audio y documentos)
- **Ejercicio:** Resolver las mismas tres tareas en las tres herramientas y comparar los resultados

**Términos clave del glosario:** Token, Ventana de Contexto, Fine-tuning, RLHF, Alucinación, System Prompt, ChatGPT, Claude, Gemini, Multimodal

---

## Clase 3 — APIs de LLM, Salidas Estructuradas y Herramientas (2 horas)

### Lección 04 — Uso de APIs de LLM y Salidas Estructuradas
**Tema:** Yendo más allá de la interfaz de chat — hablando con los modelos en código y obteniendo resultados confiables.

**Temas:**
- ¿Qué es una API y por qué usarla programáticamente?
- Obtención de claves API: OpenAI, Anthropic, Google
- Tu primera llamada a la API en Python
- Estructura de la solicitud: mensajes, roles, selección de modelo
- Manejo de respuestas y errores
- Conciencia de costos: tokens, precios, límites de tasa
- Por qué el texto no estructurado es difícil de usar en el código
- Salidas estructuradas: pedir a los modelos que respondan en JSON
- Analizando y validando respuestas estructuradas
- **Ejercicio:** Construir un script en Python que consulte la API de Claude y devuelva datos estructurados en JSON

**Términos clave del glosario:** API, Token, LLM, Cliente, Salida Estructurada, JSON

---

### Lección 05 — Herramientas y MCP
**Tema:** Dando a los LLMs la capacidad de actuar — y conectándolos a todo.

**Temas:**
- Llamada de herramientas (function calling): dando a los modelos la capacidad de actuar
- Definiendo herramientas: nombre, descripción, parámetros
- Analizando y usando los resultados de llamadas de herramientas
- El problema antes de MCP: cada integración de herramientas era única y frágil
- ¿Qué es MCP (Model Context Protocol)? Hosts, clientes y servidores explicados
- Cómo MCP estandariza las conexiones de herramientas a través de agentes y modelos
- Servidores MCP integrados: sistema de archivos, búsqueda web, bases de datos, GitHub, Slack
- Uso de MCP con Claude Code: configuración y uso práctico
- MCP vs. llamada de herramientas cruda: cuándo usar cada uno
- **Ejercicio:** Construir un agente que llame herramientas, luego configurar Claude Code con servidores MCP para hacer la misma tarea con menos código
- **Desafío:** Construir y registrar un servidor MCP personalizado simple

**Términos clave del glosario:** Llamada de Herramientas, Herramienta, API, MCP

---

## Clase 4 — Generación Aumentada por Recuperación (RAG) (2 horas)

### Lección 06 — RAG: Conceptos e Implementación
**Tema:** Basar la IA en tus propios datos — entiéndelo, luego constrúyelo.

**Temas:**
- El problema: los LLMs tienen un límite de conocimiento y pueden alucinar hechos
- ¿Qué es RAG? La tubería de recuperar y luego generar
- Embeddings (Incrustaciones): convirtiendo texto en vectores
- Similitud semántica: encontrando fragmentos relevantes por significado, no por palabras clave
- Bases de datos vectoriales: Chroma, Pinecone, Weaviate
- Estrategias de chunking (fragmentación): cómo dividir documentos de manera efectiva
- Introducción a LangChain: ¿por qué usar un framework?
- Cargando y fragmentando documentos en LangChain
- Creando embeddings y almacenándolos en una base de datos vectorial
- Ensamblando la cadena RAG: recuperador + LLM
- **Ejercicio:** Construir un bot de preguntas y respuestas sobre un conjunto de archivos PDF o de texto
- **Desafío:** Añadir un componente de memoria para que el bot rastree el historial de la conversación

**Términos clave del glosario:** RAG, Embedding, Base de Datos Vectorial, Alucinación, Ventana de Contexto, LangChain, Memoria

---

## Clase 5 — Claude Code: Arquitectura y Diseño de Agentes (2 horas)

### Lección 07 — Claude Code: Arquitectura y Diseño de Agentes
**Tema:** Entender qué son los agentes, luego construir uno con Claude Code.

**Temas:**
- *Arquitectura del Agente:*
  - La diferencia entre un chatbot y un agente
  - Los cuatro componentes de un agente: percepción, memoria, razonamiento, acción
  - El bucle agéntico (agentic loop) en detalle
  - Tipos de memoria: en contexto, externa (RAG), persistente
  - Tipos de herramientas: búsqueda, ejecución de código, E/S de archivos, APIs
  - Modos de fallo de los agentes: bucles infinitos, llamadas a herramientas alucinadas, desbordamiento del contexto
  - Caso de estudio del mundo real: un agente que automatiza una tarea de investigación de múltiples pasos
- *Introducción a Claude Code:*
  - ¿Qué es Claude Code y en qué se diferencia de Copilot o ChatGPT?
  - Instalación y configuración
  - Cómo Claude Code lee archivos, ejecuta comandos y usa herramientas
  - El modelo de permisos: lo que Claude puede y no puede hacer por defecto
  - Primera sesión: navegando y entendiendo una base de código
  - **Ejercicio:** Usar Claude Code para refactorizar un pequeño proyecto en Python
- *Análisis Profundo de Claude Code — Memoria, CLAUDE.md y Habilidades (Skills):*
  - `CLAUDE.md`: dando a Claude memoria e instrucciones específicas del proyecto
  - Archivos `CLAUDE.md` globales vs. a nivel de proyecto
  - Habilidades (Skills): flujos de trabajo reutilizables como comandos de barra (slash commands)
  - Escribiendo tu propia habilidad para una tarea repetitiva
  - Tipos de memoria en Claude Code: en contexto, basada en archivos, externa
  - Mejores prácticas para sesiones de agentes de larga duración
  - **Ejercicio:** Escribir un `CLAUDE.md` para un proyecto real y crear una habilidad personalizada

**Términos clave del glosario:** Agente, Bucle Agéntico, Memoria, Herramienta, Orquestación, Claude Code, CLAUDE.md, Habilidades

---

## Clase 6 — Agentes de Código en la Práctica (2 horas)

### Lección 08 — Antigravity: Construir una Aplicación Simple
**Tema:** Ponerlo todo junto — escribir y enviar una aplicación funcional usando un agente de código de IA.

**Temas:**
- Resumen: qué es Antigravity y cómo encaja en el panorama de los agentes de código
- Configuración de un proyecto de Antigravity desde cero
- Traducción de una idea de función a una descripción de tarea amigable para agentes
- Iteración con el agente: revisando diffs, aprobando cambios, dando retroalimentación
- Manejo del contexto del proyecto: GEMINI.md, base de conocimiento y habilidades
- Depuración (Debugging) con un agente de IA: leyendo errores, guiando correcciones
- Cuándo intervenir vs. dejar que el agente se ejecute
- Envío (Shipping): vista previa local, despliegue básico (ej. sitio estático o API simple)
- **Ejercicio:** Construir y desplegar una pequeña aplicación web o herramienta CLI de tu elección, guiada completamente por Antigravity
- **Desafío:** Añadir una característica que el agente no había planeado originalmente e iterar hasta su finalización

**Términos clave del glosario:** Antigravity, Agente, GEMINI.md, Habilidades, Herramienta, Bucle Agéntico

---

## Clase 7 — Claude Cowork: Análisis de Datos y Documentos (2 horas)

### Lección 09 — Claude Cowork: Análisis de Datos y Documentos
**Tema:** Usar el espacio de trabajo colaborativo de Claude para analizar documentos y datos reales — no se requiere código.

**Temas:**
- ¿Qué es Claude Cowork (Proyectos de claude.ai)? Compartiendo contexto a través de una conversación
- Subiendo y trabajando con archivos PDF, Word, hojas de cálculo y CSVs
- Haciendo preguntas matizadas a través de múltiples documentos
- Extracción de datos estructurados: tablas, datos clave, resúmenes
- Intérprete de Código en Claude: generando y ejecutando Python para análisis de datos
- Construcción de un flujo de trabajo repetible de revisión de documentos (ej. contratos, informes)
- Generación de gráficos, resúmenes pivote e informes escritos a partir de datos en bruto
- Caso de estudio del mundo real: un equipo automatizando informes de negocios semanales
- **Ejercicio:** Subir un conjunto mixto de documentos (PDF + CSV), extraer ideas clave y producir un informe resumido estructurado
- **Desafío:** Diseñar un flujo de trabajo de prompts repetible que un colega no técnico podría ejecutar por sí mismo

**Términos clave del glosario:** Claude Cowork, Salida Estructurada, Llamada de Herramientas, Intérprete de Código, Notebook, RAG

---

## Clase 8 — OpenClaw: IA Local y Agentes Personales (2 horas)

### Lección 10 — OpenClaw: IA Local y Agentes Personales
**Tema:** Ejecutar IA en tu propia máquina y automatizar tareas personales con OpenClaw.

**Temas:**
- *Fundamentos de la IA Local:*
  - ¿Por qué ejecutar IA localmente? Privacidad, costo, control y uso sin conexión
  - Modelos locales: Ollama, LM Studio y la ejecución de modelos de pesos abiertos (open-weight)
  - Compensaciones: capacidad vs. privacidad vs. costo
- *OpenClaw:*
  - OpenClaw: asistente de IA personal con integración a aplicaciones de mensajería
  - Configuración y ajustes
  - Memoria persistente y habilidades
  - Automatización del navegador y acceso al sistema de archivos
  - Conexión a modelos locales o en la nube
  - **Ejercicio:** Configurar OpenClaw y automatizar una tarea personal a través de Telegram o Slack

**Términos clave del glosario:** OpenClaw, Memoria, Herramienta, Agente, Habilidades, Ollama

---

## Clase 9 — OpenClaw: Construir un Agente de Marketing (2 horas)

### Lección 11 — OpenClaw: Construir un Agente de Marketing
**Tema:** Agencia local avanzada — construyendo un asistente de marketing listo para producción.

**Temas:**
- Definiendo un agente complejo multi-herramienta: búsqueda web, automatización del navegador y acceso a archivos locales
- Diseño del flujo de trabajo: investigación → planificación → generación → revisión
- Uso de habilidades (skills) para inteligencia específica de la tarea
- Conectando OpenClaw a conjuntos de datos locales específicos
- Ajuste (fine-tuning) del modelo de interacción para redacción (copy) de marketing y estrategia
- **Ejercicio:** Construir un agente de marketing que investigue a un competidor, planifique una campaña y redacte tres publicaciones para redes sociales
- **Desafío:** Añadir una habilidad que le permita al agente analizar el sentimiento de la marca usando automatización del navegador

**Términos clave del glosario:** OpenClaw, Agente, Habilidades, Herramienta, Orquestación, Memoria

---

## Clase 10 — Agentes No-Code con N8N (2 horas)

### Lección 12 — Agentes No-Code con N8N
**Tema:** Construir potentes flujos de trabajo de IA sin escribir una sola línea de código.

**Temas:**
- ¿Qué es N8N? Automatización visual de flujos de trabajo vs. agentes basados en código
- Conceptos de N8N: nodos, disparadores (triggers), flujos de trabajo y credenciales
- Conectando N8N a LLMs: nodos de OpenAI, Claude y Gemini
- Nodo de Agente de IA: dando a N8N la capacidad de razonar y usar herramientas
- Herramientas integradas: búsqueda web, solicitudes HTTP, ejecución de código, manejo de archivos
- Encadenando flujos de trabajo: uso de sub-flujos de trabajo como herramientas para un agente padre
- Memoria en N8N: memoria de sesión y almacenamiento persistente
- Auto-hospedaje (Self-hosting) vs. N8N Cloud: opciones de privacidad y despliegue
- **Ejercicio:** Construir un flujo de trabajo de agente de IA que monitoree una fuente de noticias, resuma los artículos y envíe un resumen diario por correo electrónico
- **Desafío:** Añadir un paso RAG — almacenar resúmenes de artículos en un almacén vectorial y dejar que el agente responda preguntas sobre noticias pasadas

**Términos clave del glosario:** N8N, Agente, Bucle Agéntico, Herramienta, Orquestación, Memoria, Automatización de Flujos de Trabajo

*Las lecciones están intercaladas: concepto → ejercicio guiado → desafío independiente. Cada lección termina con un breve cuestionario referenciando el glosario.*

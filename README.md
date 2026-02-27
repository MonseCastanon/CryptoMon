# 🪙 CryptoMon

> Plataforma web para explorar el mundo de las criptomonedas — precios en tiempo real, noticias, videos y una guía para quienes están comenzando.


## ✨ ¿Qué es CryptoMon?

CryptoMon es una aplicación web construida con **Python y Flask** que reúne en un solo lugar todo lo que necesitas para adentrarte al mundo crypto: precios actualizados, noticias del mercado, videos educativos y una guía práctica de inversión responsable.

El proyecto nació como una forma de combinar dos pasiones — el **desarrollo backend con arquitectura limpia** y el ecosistema de las **finanzas descentralizadas** — en una herramienta real y funcional.


## 🚀 Funcionalidades

| Sección | Descripción |
|---|---|
| 📈 **Top Criptos** | Ranking en tiempo real con precio, variación 24h y market cap via CoinGecko API |
| 📰 **Noticias** | Artículos recientes del mercado crypto via NewsAPI |
| 🎬 **Videos** | Buscador de contenido educativo via YouTube Data API |
| 📖 **Guía crypto** | Sección educativa: qué es una cripto, cómo iniciar, consejos de riesgo |
| 👩‍💻 **Sobre mí** | Página de presentación del proyecto y su desarrolladora |


## 🛠️ Stack tecnológico

- **Backend:** Python · Flask · Jinja2
- **Frontend:** Bootstrap 5 · CSS personalizado · Orbitron + Exo 2 (Google Fonts)
- **APIs externas:**
  - [CoinGecko API](https://www.coingecko.com/en/api) — precios y datos de mercado
  - [NewsAPI](https://newsapi.org/) — noticias en tiempo real
  - [YouTube Data API v3](https://developers.google.com/youtube/v3) — búsqueda de videos


## 📁 Estructura del proyecto

```
CryptoMon/
├── app/
│   ├── routes/
│   │   ├── home.py
│   │   ├── crypto.py
│   │   ├── news.py
│   │   ├── videos.py
│   │   └── about.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── images/
│   └── templates/
|       ├── errors/
|       |   ├── 404.html
│       |   └── 500.html
│       ├── base.html
│       ├── index.html
│       ├── crypto_dashboard.html
│       ├── news.html
│       ├── videos.html
│       └── about.html
├── .env
├── requirements.txt
└── run.py
```

## ⚙️ Instalación y uso

```bash
# 1. Clona el repositorio
git clone https://github.com/MonseCastanon/CryptoMon.git
cd CryptoMon

# 2. Crea y activa un entorno virtual
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Configura tus variables de entorno
cp .env.example .env
# Edita .env con tus API keys

# 5. Ejecuta la aplicación
flask run
```

## 🔑 Variables de entorno

Crea un archivo `.env` en la raíz con las siguientes claves:

```env
COINGECKO_API_KEY=tu_api_key
NEWS_API_KEY=tu_api_key
YOUTUBE_API_KEY=tu_api_key
SECRET_KEY=una_clave_secreta
```

## 🎨 Diseño

La interfaz usa una paleta neón con fondo oscuro donde cada sección tiene su propio color de acento:

- 🔵 **Purple** `#00f7ff` — navegación y precios
- 🟢 **Verde neón** `#39ff14` — pasos y videos
- 🔴 **Pink** `#ff2d78` — advertencias y noticias
- 🟡 **Amarillo** `#ffe600` — datos de mercado


## 👩‍💻 Autora

**Monse Castañon**
Desarrolladora enfocada en backend y arquitectura limpia. Apasionada por sistemas financieros, criptomonedas y tecnología moderna.

<br>

> [!WARNING]
> Este proyecto es de carácter educativo. Nada de lo mostrado en la plataforma debe considerarse asesoramiento financiero.

<br>

# 🤖 LangChain FastAPI Agent

[![Python](https## 📚 **Dokumentacija**

| Fajl | Opis |
|------|------|
| [📋 UPUTSTVO.md](./UPUTSTVO.md) | Detaljno uputstvo za instalaciju i korišćenje |
| [⚡ QUICK_REF.md](./QUICK_REF.md) | Brze komande i reference |
| [🛠️ TROUBLESHOOTING.md](./TROUBLESHOOTING.md) | Rešavanje čestih problema |
| [🔒 SECURITY.md](./SECURITY.md) | Bezbednosne mere i najbolje prakse |
| [🚨 GIT_PODSETNIK.md](./GIT_PODSETNIK.md) | Sigurni Git workflow |
| [📝 CONTRIBUTING.md](./CONTRIBUTING.md) | Vodič za doprinošenje projektu |
| [📊 CHANGELOG.md](./CHANGELOG.md) | Istorija promena i verzija |

## 🛡️ **Bezbednosne Funkcionalnosti**

- **🔐 API Key Protection** - `.env` fajlovi nisu u git-u
- **⚡ Rate Limiting** - Zaštita od zloupotreb (10 req/min po IP)
- **✅ Input Validation** - Validacija svih korisničkih unosa
- **🛡️ CORS Protection** - Kontrolisani cross-origin pristup
- **📝 Security Logging** - Praćenje svih sigurnosnih događaja
- **🔍 Automated Security Checks** - Pre-commit security scanning
- **❌ Error Handling** - Sigurne error poruke
- **🎛️ Environment Isolation** - Virtual environment setup

## 🚀 **API Endpoints**

### `POST /ask`
Pošaljite poruku AI agentu i dobijte odgovor sa memory kontekstom.

**Request:**
```json
{
  "prompt": "Hello! How can you help me?",
  "session_id": "user123"
}
```

**Response:**
```json
{
  "reply": "Hello! I'm an AI assistant that can help you with various tasks...",
  "session_id": "user123", 
  "status": "success"
}
```

### `GET /health`
Proveri status aplikacije i AI agent-a.

**Response:**
```json
{
  "status": "healthy",
  "agent_status": "working",
  "timestamp": 1752305667.9753249
}
```

### `GET /docs`
Interactive API documentation (Swagger UI) - dostupno na `http://localhost:8000/docs`

## 🎯 **Production Deployment**

Za produkcijsku upotrebu:

```bash
# 1. Set production environment
export ENVIRONMENT=production

# 2. Use Gunicorn instead of Uvicorn
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# 3. Enable API key authentication
export API_KEY="your-secure-api-key"

# 4. Use HTTPS reverse proxy (nginx/traefik)
# 5. Set up monitoring and logging
```

Detaljnije u [SECURITY.md](./SECURITY.md).shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-orange.svg)](https://python.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Security](https://img.shields.io/badge/Security-Enhanced-red.svg)](./SECURITY.md)

> **Sigurna AI agent aplikacija sa memory funkcionalnostima, izgrađena sa FastAPI i LangChain.**

Ovaj projekat demonstrira kako kreirati production-ready AI agent API sa naprednim bezbednosnim merama, conversation memory sistemom i kompletnom dokumentacijom.

## ✨ **Ključne Funkcionalnosti**

- 🤖 **GPT-4 AI Agent** sa intelligent conversation handling
- 💾 **Session-based Memory** - pamti kontekst razgovora po korisnicima
- 🛡️ **Advanced Security** - input validation, rate limiting, CORS zaštita
- 📡 **REST API** - production-ready FastAPI endpoints
- 🔒 **API Key Protection** - sigurno upravljanje secret-ima
- 📊 **Health Monitoring** - health check endpoints
- 🚀 **Easy Deployment** - automated scripts i Docker support
- 📚 **Kompletna Dokumentacija** - step-by-step uputstva

## 🎯 **Use Cases**

- **Customer Support Bots** - AI podrška sa memory
- **Personal AI Assistants** - pametan pomoćnik
- **Educational Chatbots** - interaktivno učenje
- **Business Process Automation** - automatizacija zadataka
- **API Integration** - dodavanje AI u postojeće aplikacije

## 🛠️ Instalacija

1. **Kloniraj/kopiraj kod**
2. **Instaliraj dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Konfiguriši environment:**
   - Kopiraj `.env.example` u `.env`
   - Dodaj svoj OpenAI API ključ u `.env`:
     ```
     OPENAI_API_KEY="sk-your-actual-openai-api-key"
     ```

## � Dokumentacija

- **📋 [UPUTSTVO.md](./UPUTSTVO.md)** - Kompletno uputstvo za korišćenje
- **⚡ [QUICK_REF.md](./QUICK_REF.md)** - Brze komande i reference
- **🛠️ [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)** - Rešavanje problema
- **🔒 [SECURITY.md](./SECURITY.md)** - Bezbednosne mere i preporuke

## 🚀 **Brzo Pokretanje**

### **Preduslovi**
- Python 3.8+
- OpenAI API ključ ([dobij ovde](https://platform.openai.com/api-keys))

### **Instalacija**

```bash
# 1. Kloniraj repository
git clone https://github.com/your-username/langchain-fastapi-agent.git
cd langchain-fastapi-agent

# 2. Kreiraj virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# ili: venv\Scripts\activate  # Windows

# 3. Instaliraj dependencies
pip install -r requirements.txt

# 4. Konfiguriši environment
cp .env.example .env
# Edituj .env i dodaj svoj OpenAI API ključ:
# OPENAI_API_KEY="sk-your-openai-api-key-here"

# 5. Pokreni aplikaciju
./start.sh
```

### **Brzi Test**
```bash
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello! How are you?", "session_id": "demo"}'
```

**Odgovor:**
```json
{
  "reply": "Hello! I'm doing well, thank you for asking. How can I help you today?",
  "session_id": "demo",
  "status": "success"
}
```

## 🏗️ **Arhitektura**

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Web Client    │───▶│   FastAPI App    │───▶│  LangChain     │
│                 │    │                  │    │  Agent         │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
                       ┌──────────────────┐    ┌─────────────────┐
                       │  Security Layer  │    │   OpenAI API    │
                       │  Rate Limiting   │    │   GPT-4         │
                       │  Input Validation│    │                 │
                       └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
                       ┌──────────────────┐    ┌─────────────────┐
                       │  Session Memory  │    │   Response      │
                       │  Conversation    │    │   Generation    │
                       │  History         │    │                 │
                       └──────────────────┘    └─────────────────┘
```

## 📖 API Dokumentacija

### Endpointi

- **GET** `/` - Osnovne informacije
- **GET** `/health` - Detaljni health check
- **POST** `/ask` - Pošalji poruku AI agentu

### Korišćenje

**Osnovni zahtev:**
```bash
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Hello! How are you?",
    "session_id": "user123"
  }'
```

**Sa API ključem (ako je omogućen):**
```bash
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-api-key" \
  -d '{
    "prompt": "Hello! How are you?", 
    "session_id": "user123"
  }'
```

**Odgovor:**
```json
{
  "reply": "Hello! I'm doing well, thank you for asking. How can I help you today?",
  "session_id": "user123",
  "status": "success"
}
```

## 🔒 Bezbednost

Aplikacija uključuje nekoliko bezbednosnih mera:

1. **Input validation** - ograničenja na dužinu i sadržaj
2. **Rate limiting** - maksimalno 10 zahteva po minuti po IP adresi
3. **CORS zaštita** - kontrolisani pristup iz web aplikacija
4. **Error handling** - sigurni error poruke
5. **Logging** - praćenje svih zahteva

Za produkciju, pogledaj `SECURITY.md` za dodatne preporuke.

## 🔧 Konfiguracija

### Environment Variables

```bash
# Obavezno
OPENAI_API_KEY="sk-your-openai-api-key"

# Opciono
API_KEY="your-service-api-key"  # Za zaštićeni pristup
ENVIRONMENT="production"        # Za produkciju
LOG_LEVEL="INFO"               # Nivo logovanja
```

## 📁 Struktura Projekta

```
langchain_fastapi_agent/
├── main.py              # FastAPI aplikacija
├── agent.py             # LangChain AI agent logika
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (PRIVATNO!)
├── .env.example         # Template za .env
├── .gitignore          # Git ignore fajl
├── start.sh            # Start script
├── security_check.sh   # 🛡️ Sigurnosna provera pre commit-a
├── commit_helper.sh    # 🚀 Helper za sigurne commit-ove
├── README.md           # Osnovna dokumentacija
├── UPUTSTVO.md         # Detaljno uputstvo
├── QUICK_REF.md        # Brze komande
├── GIT_PODSETNIK.md    # 🚨 Git commit podsetnik
├── SECURITY.md         # Bezbednosni vodič
├── TROUBLESHOOTING.md  # Rešavanje problema
└── venv/               # Python virtual environment
```

## 🐛 Troubleshooting

### Česti problemi:

1. **"Incorrect API key"**
   - Proveri da li je API ključ pravilno postavljen u `.env`
   - Ukloni navodnike iz API ključa ako nisu potrebni

2. **"Too many requests"**
   - Sačekaj minut pre ponovnog slanja zahteva
   - Rate limiting je postavljen na 10 zahteva po minuti

3. **CORS greške**
   - Dodaj svoj domain u `allow_origins` listu u `main.py`

### Logs

Aplikacija loguje sve zahteve. Proveri terminal/konzolu za detaljne informacije.

## 🚀 Produkcijska Deployment

Za produkciju:

1. Postavi `ENVIRONMENT=production` u `.env`
2. Omogući API key autentifikovanje
3. Koristi HTTPS
4. Implementiraj Redis za rate limiting
5. Dodaj monitoring i alerting

Detaljnije u `SECURITY.md`.

## 🤝 **Contributing**

Doprinosi su dobrodošli! Molimo pročitajte [CONTRIBUTING.md](./CONTRIBUTING.md) za detalje o našem kodu ponašanja i procesu slanja pull request-ova.

### **Kako doprineti:**
1. 🍴 Fork repository
2. 🔧 Kreiraj feature branch (`git checkout -b feature/amazing-feature`)
3. 📝 Commit-uj izmene (`git commit -m 'Add amazing feature'`)
4. 🚀 Push-uj na branch (`git push origin feature/amazing-feature`)
5. 🔀 Otvori Pull Request

## 📄 **Licenca**

Ovaj projekat je licenciran pod MIT licencom - pogledaj [LICENSE](./LICENSE) fajl za detalje.

## 🙏 **Zahvalnice**

- [LangChain](https://python.langchain.com/) - Za fantastičan AI framework
- [FastAPI](https://fastapi.tiangolo.com/) - Za moderne Python web API
- [OpenAI](https://openai.com/) - Za GPT-4 model
- Open source zajednici za inspiraciju i podršku

## 📞 **Podrška**

- 📖 **Dokumentacija**: Pogledaj [DOCS_INDEX.md](./DOCS_INDEX.md)
- 🐛 **Bug reports**: Otvori issue sa detaljnim opisom
- 💡 **Feature requests**: Diskutuj u Issues sekciji
- 🔧 **Problemi**: Konsultuj [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)

---

**⭐ Ako ti se sviđa ovaj projekat, daj mu zvezdu na GitHub-u!**

**Napravljen sa ❤️ za AI i developer zajednicu**

# LangChain FastAPI Agent

Sigurna AI agent aplikacija sa memory funkcionalnostima, izgrađena sa FastAPI i LangChain.

## 🚀 Funkcionalnosti

- ✅ **AI Chat Agent** sa GPT-4 modelom
- ✅ **Conversation Memory** - čuva kontekst razgovora po sesijama
- ✅ **Input Validation** - validacija unosa i ograničenja
- ✅ **Rate Limiting** - ograničavanje broja zahteva (10/minut po IP)
- ✅ **CORS podrška** - za web aplikacije
- ✅ **Opciono API Key autentifikovanje** 
- ✅ **Logging** - praćenje zahteva i grešaka
- ✅ **Health Check** endpointi
- ✅ **Error Handling** - sigurno rukovanje greškama

## 📋 Zahtevi

- Python 3.8+
- OpenAI API ključ

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

## 🚀 Brzo Pokretanje

```bash
# 1. Pokreni aplikaciju
./start.sh

# 2. Testiraj API
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Zdravo!", "session_id": "test"}'

# 3. Za Git commit (UVEK sa sigurnosnom proverom):
git add .
./security_check.sh  # ← OBAVEZNO!
git commit -m "opis"
```

Detaljno uputstvo je u [UPUTSTVO.md](./UPUTSTVO.md).  
**🚨 Git podsetnik:** [GIT_PODSETNIK.md](./GIT_PODSETNIK.md)

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

## 🤝 Doprinos

Molimo da testirate aplikaciju i prijavite greške ili predloge za poboljšanje.

## 📄 Licenca

MIT License

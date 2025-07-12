# 🚀 LangChain FastAPI Agent - Kompletno Uputstvo

## 📋 Kratak Pregled

Ovaj projekat je sigurna AI agent aplikacija koja koristi:
- **FastAPI** - za REST API
- **LangChain** - za AI agent logiku
- **OpenAI GPT-4** - za odgovore
- **Memory sistem** - pamti razgovor po sesijama

## 🗂️ Struktura Projekta

```
langchain_fastapi_agent/
├── main.py              # FastAPI aplikacija (REST API)
├── agent.py             # LangChain AI agent sa memory
├── requirements.txt     # Python dependencies
├── .env                 # Privatni API ključevi (NIKAD u git!)
├── .env.example         # Template za .env
├── .gitignore          # Git ignore fajl
├── start.sh            # Script za pokretanje
├── README.md           # Osnovna dokumentacija
├── SECURITY.md         # Bezbednosni vodič
├── UPUTSTVO.md         # Ovaj fajl - detaljan vodič
└── venv/               # Python virtual environment
```

## 🛠️ Instalacija i Setup (Korak po Korak)

### 1. Kloniraj/kopiraj kod
```bash
# Ako kloniraš iz git-a:
git clone <repository-url>
cd langchain_fastapi_agent

# Ili ako kopirajś lokalno:
cd langchain_fastapi_agent
```

### 2. Kreiraj i aktiviraj virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Na macOS/Linux
# ili
venv\Scripts\activate    # Na Windows
```

### 3. Instaliraj dependencies
```bash
pip install -r requirements.txt
```

### 4. Konfiguriši environment varijable
```bash
# Kopiraj template
cp .env.example .env

# Edituj .env i dodaj svoj OpenAI API ključ:
OPENAI_API_KEY="sk-your-actual-openai-api-key"
```

## 🚀 Pokretanje Aplikacije

### Metoda 1: Koristi script (preporučeno)
```bash
./start.sh
```

### Metoda 2: Aktiviraj venv pa pokreni
```bash
source venv/bin/activate
uvicorn main:app --reload
```

### Metoda 3: Direktno sa punom putanjom
```bash
/Users/dennzy/langchain_fastapi_agent/venv/bin/python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 🌐 Pristupne Tačke

- **API:** http://localhost:8000
- **Dokumentacija:** http://localhost:8000/docs  
- **Health Check:** http://localhost:8000/health

## 📡 Korišćenje API-ja

### Osnovni zahtev
```bash
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Zdravo! Kako si?",
    "session_id": "korisnik123"
  }'
```

### Odgovor
```json
{
  "reply": "Zdravo! Dobro sam, hvala. Kako mogu da ti pomognem?",
  "session_id": "korisnik123", 
  "status": "success"
}
```

### Test memory funkcionalnosti
```bash
# Prvi zahtev
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Moje ime je Marko", "session_id": "test"}'

# Drugi zahtev (testira da li pamti)
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Kako se zovem?", "session_id": "test"}'
```

## 🔒 Bezbednosne Funkcionalnosti

### Automatski Aktivne:
1. **Input Validation** - proverava dužinu i format
2. **Rate Limiting** - max 10 zahteva/minut po IP
3. **CORS zaštita** - kontrolisani pristup
4. **Error Handling** - sigurne error poruke
5. **Logging** - praćenje svih zahteva

### Opciono (za dodatnu bezbednost):
Dodaj u `.env`:
```bash
API_KEY="moj-tajni-kljuc-123"
```

Zatim koristi:
```bash
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer moj-tajni-kljuc-123" \
  -d '{"prompt": "Poruka", "session_id": "test"}'
```

## 🐛 Česti Problemi i Rešenja

### Problem: "command not found: uvicorn"
**Rešenje:** Aktiviraj virtual environment ili koristi punu putanju
```bash
source venv/bin/activate
# ili
/Users/dennzy/langchain_fastapi_agent/venv/bin/python -m uvicorn main:app --reload
```

### Problem: "Incorrect API key"
**Rešenje:** Proveri .env fajl
```bash
cat .env  # Proveri da li je API ključ tu
```

### Problem: "Too many requests"
**Rešenje:** Sačekaj minut (rate limiting)

### Problem: CORS greške
**Rešenje:** Dodaj svoj domain u `main.py` u `allow_origins` listu

## 🔧 Development

### Pokretanje u development modu
```bash
uvicorn main:app --reload --log-level debug
```

### Dodavanje novih funkcionalnosti
1. Edituj `agent.py` za AI logiku
2. Edituj `main.py` za API endpoints
3. Dodaj nove dependencies u `requirements.txt`

### Testiranje
```bash
# Health check
curl http://localhost:8000/health

# Basic test
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "test", "session_id": "test"}'
```

## 📦 Deployment

### Za produkciju:
1. Postavi `ENVIRONMENT=production` u `.env`
2. Koristi Gunicorn umesto Uvicorn
3. Aktiviraj API key autentifikovanje
4. Koristi HTTPS
5. Implementiraj Redis za rate limiting

### Deployment komande:
```bash
# Instaliraj production dependencies
pip install gunicorn

# Pokreni sa Gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 🚨 Važne Napomene

### ⚠️ NIKAD ne commit-uj:
- `.env` fajl (sadrži API ključeve)
- `__pycache__/` folder
- `venv/` folder
- Log fajlove

### ✅ UVEK commit-uj:
- `.env.example` (template)
- Source kod (`.py` fajlovi)
- `requirements.txt`
- Dokumentaciju

### 🔐 Pre svakog commit-a:
```bash
./security_check.sh  # OBAVEZNO! Proverava API ključeve
git add .
git commit -m "opis"
```

### 🔐 Bezbednost:
- Nikad ne deli svoj OpenAI API ključ
- U produkciji koristi HTTPS
- Regularno ažuriraj dependencies

## 📞 Podrška

### Log fajlovi:
```bash
# Proveri logs u terminalu gde radi server
# Ili dodaj file logging u aplikaciju
```

### Debugging:
```bash
# Pokreni sa debug modom
uvicorn main:app --reload --log-level debug
```

### Korisni linkovi:
- FastAPI dokumentacija: https://fastapi.tiangolo.com/
- LangChain dokumentacija: https://python.langchain.com/
- OpenAI API: https://platform.openai.com/docs/

---

**Napravljen:** 12 July 2025  
**Verzija:** 1.0.0  
**Status:** Production Ready 🚀

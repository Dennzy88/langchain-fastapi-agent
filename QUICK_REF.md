# 🚀 Quick Reference - Brze Komande

## ⚡ Pokretanje

```bash
# Najlakši način:
./start.sh

# Ili aktiviraj venv pa pokreni:
source venv/bin/activate && uvicorn main:app --reload

# Ili direktno:
/Users/dennzy/langchain_fastapi_agent/venv/bin/python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 🧪 Brzi Testovi

```bash
# Health check
curl http://localhost:8000/health

# Osnovni test
curl -X POST "http://localhost:8000/ask" -H "Content-Type: application/json" -d '{"prompt": "Zdravo!", "session_id": "test"}'

# Memory test
curl -X POST "http://localhost:8000/ask" -H "Content-Type: application/json" -d '{"prompt": "Zapamti: volim kafu", "session_id": "test"}'
curl -X POST "http://localhost:8000/ask" -H "Content-Type: application/json" -d '{"prompt": "Šta volim?", "session_id": "test"}'
```

## 🔧 Development

```bash
# Instaliraj nove pakete
source venv/bin/activate
pip install paket_ime
pip freeze > requirements.txt

# Debug mode
uvicorn main:app --reload --log-level debug

# Proveri status servera
ps aux | grep uvicorn
```

## 🛡️ Bezbednost

```bash
# Proveri .env
cat .env

# Aktiviraj API key zaštitu
echo 'API_KEY="moj-secret-123"' >> .env

# Test sa API key
curl -X POST "http://localhost:8000/ask" -H "Content-Type: application/json" -H "Authorization: Bearer moj-secret-123" -d '{"prompt": "test", "session_id": "test"}'
```

## 📁 Fajlovi

```bash
# Važni fajlovi:
main.py         # FastAPI server
agent.py        # AI agent logika  
.env           # API ključevi (PRIVATNO!)
requirements.txt # Dependencies
start.sh       # Start script

# Dokumentacija:
README.md      # Osnovno
UPUTSTVO.md    # Detaljno
SECURITY.md    # Bezbednost
QUICK_REF.md   # Ovaj fajl
```

## 🚨 Troubleshooting

```bash
# Server ne startuje
ps aux | grep uvicorn  # Proveri da li već radi
kill $(ps aux | grep uvicorn | awk '{print $2}')  # Ugasi

# API ključ problemi
echo $OPENAI_API_KEY  # Proveri environment
cat .env  # Proveri fajl

# Rate limiting
# Sačekaj 1 minut između zahteva
```

## 📦 Git - SIGURNI COMMIT WORKFLOW

```bash
# 🛡️ OPCIJA 1: Manuelno (OBAVEZNA PROCEDURA):
git add .
./security_check.sh  # ← OBAVEZNO! Proverava API ključeve
git commit -m "opis izmena"
git push

# 🚀 OPCIJA 2: Koristi helper script (lakše):
./commit_helper.sh  # Automatski radi sve gore + podsetnike

# Prvi put setup:
git init
git add .
./security_check.sh
git commit -m "Initial commit"

# PAŽNJA: .gitignore štiti .env fajl!
# NIKAD ne commit-uj bez security_check.sh!
```

## 🌐 Korisni URL-ovi

- http://localhost:8000 - API
- http://localhost:8000/docs - Swagger dokumentacija  
- http://localhost:8000/health - Health check
- http://localhost:8000/redoc - ReDoc dokumentacija

# 🛠️ Troubleshooting Guide

## 🚨 Česti Problemi

### 1. "command not found: uvicorn"
**Uzrok:** Virtual environment nije aktiviran  
**Rešenje:**
```bash
# Opcija 1: Aktiviraj venv
source venv/bin/activate
uvicorn main:app --reload

# Opcija 2: Koristi punu putanju
/Users/dennzy/langchain_fastapi_agent/venv/bin/python -m uvicorn main:app --reload

# Opcija 3: Koristi script
./start.sh
```

### 2. "Incorrect API key provided"
**Uzrok:** Neispravan ili nedostaje OpenAI API ključ  
**Rešenje:**
```bash
# Proveri .env fajl
cat .env

# Treba da izgleda ovako:
# OPENAI_API_KEY="sk-your-api-key-here"

# Ako nema, dodaj:
echo 'OPENAI_API_KEY="sk-your-key-here"' > .env
```

### 3. "Port 8000 is already in use"
**Uzrok:** Server već radi  
**Rešenje:**
```bash
# Pronađi proces
ps aux | grep uvicorn

# Ugasi proces
kill PID_BROJ

# Ili ugasi sve uvicorn procese
pkill -f uvicorn
```

### 4. "Too many requests" (429 error)
**Uzrok:** Rate limiting (više od 10 zahteva/minut)  
**Rešenje:** Sačekaj 1 minut

### 5. Server se ne pokreće
**Dijagnoza:**
```bash
# Proveri Python
python --version

# Proveri dependencies
pip list | grep fastapi

# Proveri sintaksu
python -m py_compile main.py
python -m py_compile agent.py
```

### 6. JSON validation errors
**Uzrok:** Loš format JSON-a u curl zahtevima  
**Rešenje:**
```bash
# Ispravan format:
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "test", "session_id": "test"}'

# NE:
curl ... -d "{'prompt': 'test'}"  # Jednostruki navodnici
curl ... -d "{prompt: test}"      # Nema navodnike
```

### 7. CORS errors (iz web aplikacije)
**Rešenje:** Dodaj svoj domain u `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://tvoj-domain.com"],
    # ...
)
```

### 8. Memory ne radi (ne pamti razgovor)
**Uzrok:** Različiti session_id  
**Rešenje:** Koristi isti session_id za istu konverzaciju

### 9. Spor odgovor
**Mogući uzroci:**
- Sporna internet veza
- OpenAI API preopterećen
- Veliki prompt (skrati ga)

### 10. "Šta znače git oznake A, M, D?"
**Objašnjenje:** Oznake u git status-u  
**Rešenje:** Pogledaj [GIT_OZNAKE.md](./GIT_OZNAKE.md) za kompletno objašnjenje

```bash
# Kratko:
# M = Modified (izmenjeno)
# A = Added (dodano) 
# D = Deleted (obrisano)
# ?? = Untracked (novi fajl)
```

## 🔍 Debugging

### Pokretanje sa više detalja:
```bash
uvicorn main:app --reload --log-level debug
```

### Provera varijabli:
```bash
# Proveri environment varijable
env | grep OPENAI

# Ili u Python-u:
python -c "import os; print(os.getenv('OPENAI_API_KEY'))"
```

### Test API poziva:
```bash
# Osnovno
curl -v http://localhost:8000/

# Sa detaljima
curl -v -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "test", "session_id": "debug"}'
```

## 📞 Kada se obratiti za pomoć

Ako ništa od navedenog ne pomaže, priloži:

1. **Error poruku** (ceo tekst)
2. **Korake koji su doveli do greške**
3. **Python verziju:** `python --version`
4. **OS informacije:** `uname -a` (macOS/Linux) ili `ver` (Windows)
5. **Log iz terminala** gde se pokreće server

## 🚀 Quick Fix Checklist

- [ ] Virtual environment aktiviran?
- [ ] OpenAI API ključ u .env fajlu?
- [ ] Port 8000 slobodan?
- [ ] Internet konekcija radi?
- [ ] Dependencies instalirani?
- [ ] JSON format ispravan?
- [ ] Session ID konzistentan?

**90% problema se reši sa ovih 7 provera!**

# 📚 Dokumentacijski Index

Dobrodošli u LangChain FastAPI Agent projekat! Evo kompletnog vodića kroz dokumentaciju:

## 🚀 Za Početnike

1. **[README.md](./README.md)** - Počni ovde! Kratak pregled projekta
2. **[UPUTSTVO.md](./UPUTSTVO.md)** - Detaljno uputstvo korak po korak
3. **[QUICK_REF.md](./QUICK_REF.md)** - Brze komande za svakodnevno korišćenje

## 🔧 Za Developere

4. **[TROUBLESHOOTING.md](./TROUBLESHOOTING.md)** - Kada nešto ne radi
5. **[SECURITY.md](./SECURITY.md)** - Bezbednosne mere i best practices
6. **[GIT_PODSETNIK.md](./GIT_PODSETNIK.md)** - 🚨 OBAVEZNO pre svakog commit-a!

## 📁 Konfiguracijski Fajlovi

6. **[.env.example](./.env.example)** - Template za environment varijable
7. **[.gitignore](./.gitignore)** - Git ignore lista (štiti privatne fajlove)
8. **[requirements.txt](./requirements.txt)** - Python dependencies
9. **[start.sh](./start.sh)** - Script za pokretanje aplikacije

## 🏃‍♂️ Brzi Start (TL;DR)

```bash
# 1. Kopiraj template i dodaj svoj API ključ
cp .env.example .env
# Edituj .env i dodaj: OPENAI_API_KEY="sk-your-key"

# 2. Pokreni
./start.sh

# 3. Testiraj
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello!", "session_id": "test"}'

# 4. SIGURNI GIT WORKFLOW:
git add .
./security_check.sh  # ← OBAVEZNO!
git commit -m "opis"
```

## 📖 Čitanje po Redosledu

### Prvi put koristiš:
1. README.md → UPUTSTVO.md → Pokreni aplikaciju

### Svakodnevno korišćenje:
1. QUICK_REF.md → start.sh → Radi!

### Kad ima problema:
1. TROUBLESHOOTING.md → SECURITY.md → Pitaj za pomoć

### Za deployment:
1. SECURITY.md → Production sekcija u UPUTSTVO.md

## 🎯 Najvažniji Fajlovi

| Fajl | Svrha | Kada čitaš |
|------|-------|------------|
| **README.md** | Brzi pregled | Prvi put |
| **UPUTSTVO.md** | Kompletno uputstvo | Za setup |
| **QUICK_REF.md** | Brze komande | Svakodnevno |
| **TROUBLESHOOTING.md** | Rešavanje problema | Kad ne radi |

## 🔗 Direktni Linkovi na Bitne Sekcije

- [Instalacija](./UPUTSTVO.md#%EF%B8%8F-instalacija-i-setup-korak-po-korak)
- [Pokretanje](./UPUTSTVO.md#-pokretanje-aplikacije)
- [API Korišćenje](./UPUTSTVO.md#-korišćenje-api-ja)
- [Bezbednost](./SECURITY.md#bezbednosne-funkcionalnosti)
- [Česti Problemi](./TROUBLESHOOTING.md#-česti-problemi)

## 💡 Saveti

- **Bookmark**: QUICK_REF.md za brze komande
- **Print**: TROUBLESHOOTING.md za debug sesije  
- **🚨 ZAPAMTI**: GIT_PODSETNIK.md - UVEK pre commit-a!
- **Share**: README.md sa kolegama
- **Study**: SECURITY.md za produkciju

---

**Happy coding!** 🚀  
*Svi fajlovi su ažurirani: 12 July 2025*

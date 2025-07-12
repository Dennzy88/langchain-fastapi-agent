# 🚨 GIT COMMIT PODSETNIK

## ⚠️ OBAVEZNA PROCEDURA - NIKAD NE PRESKAČAJ!

```bash
git add .
./security_check.sh  # ← OBAVEZNO! Proverava API ključeve  
git commit -m "opis izmena"
git push
```

## 🛡️ ZAŠTO JE BITNO:

- **`security_check.sh`** proverava da li slučajno commit-uješ API ključeve
- **Blokira commit** ako nadje opasnost
- **Štiti te** od curenja privatnih podataka na GitHub

## 🚫 NIKAD:

```bash
git add .
git commit -m "opis"  # ❌ BEZ security_check.sh!
```

## ✅ UVEK:

```bash
git add .
./security_check.sh   # ✅ SA sigurnosnom proverom!
git commit -m "opis"
```

## 📋 Checklist Pre Commit-a:

- [ ] `git add .`
- [ ] `./security_check.sh` (čeka da vidiš ✅)
- [ ] `git commit -m "opis"`
- [ ] `git push`

---

**ZAPAMTI: Jedan security_check.sh sprečava katastrofu!** 🛡️

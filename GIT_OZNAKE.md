# 📊 Git Status Oznake - Objašnjenje

## 🔤 Šta Znače Git Oznake?

### **Git Status Kategorije:**

#### 🟢 **"Changes to be committed"** (Staged)
- Fajlovi koji su **dodani** sa `git add`
- **Spremni za commit**
- Označeni sa:
  - `new file:` - novi fajl
  - `modified:` - izmenjeni fajl  
  - `deleted:` - obrisani fajl

#### 🟡 **"Changes not staged for commit"** (Modified)
- Fajlovi koji su **izmenjeni** ali NISU dodani sa `git add`
- **Trebaš `git add` pre commit-a**
- Označeni sa:
  - `modified:` - fajl je menjan nakon poslednjeg `git add`

#### 🔴 **"Untracked files"** (Novi)
- **Potpuno novi fajlovi** koje git ne prati
- **Trebaš `git add` da ih dodaš**
- Nema posebnih oznaka, samo lista fajlova

## 📋 **Tvoj Trenutni Status:**

```
🟢 STAGED (ready for commit):
   - .env.example, .gitignore, README.md, itd.
   
🟡 MODIFIED (needs git add):
   - DOCS_INDEX.md, QUICK_REF.md, README.md, security_check.sh
   
🔴 UNTRACKED (new files):
   - GIT_PODSETNIK.md, commit_helper.sh
```

## 🎯 **Dodatne Git Oznake (u drugim komandama):**

### **`git log --oneline`** oznake:
- `A` = Added (dodano)
- `M` = Modified (izmenjeno)  
- `D` = Deleted (obrisano)
- `R` = Renamed (preimenovano)
- `C` = Copied (kopirano)

### **`git diff`** oznake:
- `+` = Dodana linija
- `-` = Obrisana linija
- `@@` = Lokacija izmene

### **Merge conflict oznake:**
- `<<<<<<< HEAD` = Tvoja verzija
- `=======` = Separator
- `>>>>>>> branch` = Druga verzija

## 🚀 **Kako Rešiti Tvoj Status:**

```bash
# Dodaj sve izmenjene i nove fajlove
git add .

# Proveri bezbednost
./security_check.sh

# Napravi commit
git commit -m "Dodao dokumentaciju i sigurnosne skriptove"
```

## 💡 **Korisni Git Status Saveti:**

```bash
# Kratka verzija statusa
git status -s

# Prikaži i ignored fajlove
git status --ignored

# Samo fajlovi (bez poruka)
git status --porcelain
```

## 🔍 **Git Status Legend:**

| Oznaka | Značenje |
|--------|----------|
| `??` | Untracked (novi fajl) |
| `A` | Added (staged novi fajl) |
| `M` | Modified (staged izmena) |
| ` M` | Modified (not staged) |
| `MM` | Modified (staged i not staged) |
| `D` | Deleted |
| `R` | Renamed |

---

**Zapamti: Git status ti govori šta treba da uradiš pre commit-a!** 📝

#!/bin/bash
# 🛡️ SIGURNOSNA PROVERA - Pre Git Commit

echo "🔍 Proveram sigurnost pre commit-a..."

# Proveri da li se .env fajl slučajno dodaje u git
if git ls-files --cached | grep -q "^\.env$"; then
    echo "🚨 PAŽNJA! .env fajl je u git staging area!"
    echo "❌ STOP! Ne commit-uj - sadrži API ključeve!"
    exit 1
fi

# Proveri da li ima pravih API ključeva u fajlovima koji se commit-uju
staged_files=$(git diff --cached --name-only)
for file in $staged_files; do
    if [ -f "$file" ]; then
        # Proveri za dugačke API ključeve (ne template)
        if grep -q "sk-[a-zA-Z0-9]\{40,\}" "$file" 2>/dev/null; then
            echo "🚨 OPASNOST! Pravi API ključ u: $file"
            echo "❌ STOP! Ne commit-uj - sadrži pravi API ključ!"
            exit 1
        fi
        # Dodatna provera za OpenAI project ključeve
        if grep -q "sk-proj-[a-zA-Z0-9]" "$file" 2>/dev/null; then
            echo "🚨 OPASNOST! OpenAI API ključ u: $file"
            echo "❌ STOP! Ne commit-uj!"
            exit 1
        fi
    fi
done

echo "✅ Sigurnosna provera prošla - bezbedno za commit!"
exit 0

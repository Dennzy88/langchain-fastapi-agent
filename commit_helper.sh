#!/bin/bash
# 🚨 Git Commit Helper - Sa Podsetnikima

echo ""
echo "🚨 ==============================================="
echo "    GIT COMMIT BEZBEDNOSNI PROTOKOL"
echo "==============================================="
echo ""
echo "📋 CHECKLIST:"
echo "   1. ✅ Izmene gotove"
echo "   2. ⏳ Dodavanje fajlova..."

git add .

echo "   3. 🔍 Sigurnosna provera..."
echo ""

# Pokreni sigurnosnu proveru
if ./security_check.sh; then
    echo ""
    echo "   4. ✅ Sigurnosna provera prošla!"
    echo ""
    echo "💬 Unesi commit poruku:"
    read -p "   > " commit_message
    
    if [ -n "$commit_message" ]; then
        git commit -m "$commit_message"
        echo ""
        echo "🎉 USPEŠNO! Commit je napravljen."
        echo ""
        echo "📤 Da push-uješ sada? (y/n)"
        read -p "   > " push_choice
        
        if [ "$push_choice" = "y" ] || [ "$push_choice" = "Y" ]; then
            git push
            echo ""
            echo "🚀 GOTOVO! Sve je poslato na GitHub."
        else
            echo ""
            echo "✋ OK, možeš push-ovati kasnije sa: git push"
        fi
    else
        echo ""
        echo "❌ Nema commit poruke. Prekidamo."
    fi
else
    echo ""
    echo "🛑 COMMIT BLOKIRAN!"
    echo "   Sigurnosna provera je našla problem."
    echo "   Proveri gore šta treba popraviti."
fi

echo ""
echo "==============================================="
echo ""

#!/bin/bash
# Автоматическое обновление GitHub репозитория

# Проверяем, есть ли аргумент для сообщения коммита
if [ -z "$1" ]; then
  msg="Автоматическое обновление $(date '+%Y-%m-%d %H:%M:%S')"
else
  msg="$1"
fi

echo "Добавляем изменения..."
git add .

echo "Создаем коммит..."
git commit -m "$msg"

echo "Отправляем на GitHub..."
git push origin main

echo "✅ Готово!"

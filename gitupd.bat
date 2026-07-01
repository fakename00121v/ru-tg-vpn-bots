@echo off
chcp 65001 >nul
echo Git Auto Reset and Push

git config --global user.email "no-reply@localhost"
git config --global user.name "maxikvin"

echo Инициализация Git
git init
git branch -m main

echo Привязываем к GitHub
git remote add origin https://github.com/fakename00121v/ru-tg-vpn-bots.git

echo Добавляем файлы...
git add .

echo Сохраняем изменения
git commit -m "Auto reset and push %date% %time%"

echo Отправляем на GitHub
git push -u origin main --force
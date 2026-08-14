from datetime import datetime
def readme_update(rmefile, inputtxt, sort1):
    dnow = datetime.now().strftime("%Y-%m-%d %H:%M")
    text = f"""# ru-tg-vpn-bots

[![Support](https://img.shields.io/badge/Поддержать-CloudTips-blue)](https://pay.cloudtips.ru/p/4ea26bd3)
[![Python](https://img.shields.io/badge/Python-3.14-yellow)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-GPLv3-green)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Open Source](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://opensource.org)

Сборник VPN из Telegram. Инструмент для фильтрации и очистки: разделяет @username и https, удаляет дубликаты и мусор.

Боты и реферальные ссылки ищутся вручную и автообновления списка нет.

💰 **Поддержать проект:** https://pay.cloudtips.ru/p/4ea26bd3 - коплю на новый ПК.

| Категория | Ссылка |
| :---: | :---: |
| **Боты** | [`bots.md`](https://github.com/fakename00121v/ru-tg-vpn-bots/blob/main/output/bots.md) |
| **Ссылки** | [`links.md`](https://github.com/fakename00121v/ru-tg-vpn-bots/blob/main/output/links.md) |
| **Другое** | [`others.md`](https://github.com/fakename00121v/ru-tg-vpn-bots/blob/main/output/others.md) |

## Бонусы🎁
| Бонус | Ссылка |
| :---: | :---: |
| **VPN-клиенты и конфиги** | [`vpnc.md`](https://github.com/fakename00121v/ru-tg-vpn-bots/blob/main/bonus/vpnc.md) |
| **Полезные ссылки** | [`coollinks.md`](https://github.com/fakename00121v/ru-tg-vpn-bots/blob/main/bonus/coollinks.md) |
| **Прокси для telegram** | [`tgproxy.md`](https://github.com/fakename00121v/ru-tg-vpn-bots/blob/main/bonus/tgproxy.md) |

## Статистика записей в input.txt
| Тип | Значение |
| :---: | :---: |
| Время | {dnow} |
| Всего | {inputtxt} |
| Уникальных | {sort1} |

## Как это работает

1. **`scripts/sort.py`** — читает указанный файл, разделяет строки на ботов, ссылки и прочее, удаляет дубликаты и сохраняет в указанную папку.
2. **`scripts/txttomd.py`** — конвертирует полученные `.txt` файлы в удобные `.md` с кликабельными ссылками.
3. **`scripts/с.py`** - считает всего количество записей в input.txt
4. **`scripts/rmeupd.py`** - обновляет README.md
5. **`app.py`** — запускает всю цепочку автоматически.

---

### Отказ от ответственности
*   Данный репозиторий является **инструментом для обработки списков** и **коллекцией общедоступных ссылок**, собранных вручную из открытых источников.
*   Я **не являюсь автором** и **не поддерживаю** ботов, VPN-сервисы и конфиги, ссылки на которые приведены здесь. Вся ответственность за их использование лежит на конечном пользователе.
*   Я не гарантирую работоспособность, безопасность или легальность любого из перечисленных ресурсов. Используйте их на свой страх и риск.

---

#### Поддерживаю инициативу [Keep Android Open](https://keepandroidopen.org).
* Я за свободный и открытый Android.
"""
    with open(rmefile, 'w', encoding='utf-8') as file:
        file.write(text)
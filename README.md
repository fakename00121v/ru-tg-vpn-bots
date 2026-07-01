# ru-tg-vpn-bots

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.14-yellow" alt="Python 3.14">
  </a>
  <a href="https://www.gnu.org/licenses/gpl-3.0.html">
    <img src="https://img.shields.io/badge/License-GPLv3-green" alt="License GPLv3">
  </a>
  <a href="https://opensource.org">
    <img src="https://badges.frapsoft.com/os/v2/open-source.png?v=103" alt="Open Source">
  </a>
</p>

Сборник VPN из Telegram. Инструмент для фильтрации и очистки: разделяет @username и https, удаляет дубликаты и мусор.

Боты и реферальные ссылки ищутся вручную и автообновления списка нет.

| Категория | Ссылка |
|-|-|
| **Боты** | [`bots.md`](https://github.com/fakename00121v/ru-tg-vpn-bots/blob/main/output/bots.md) |
| **Ссылки** | [`links.md`](https://github.com/fakename00121v/ru-tg-vpn-bots/blob/main/output/links.md) |
| **Другое** | [`others.md`](https://github.com/fakename00121v/ru-tg-vpn-bots/blob/main/output/others.md) |

## Бонусы🎁
| Бонус | Ссылка | Источник |
|-|-|-|
| **vpn-клиент (Android)** | [`nekobox`](https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/latest) | [`MatsuriDayo/NekoBoxForAndroid`](https://github.com/MatsuriDayo/NekoBoxForAndroid) |
| **конфиг vpn-клиента (Android)** | [`nekobox_backup.json`](https://github.com/fakename00121v/ru-tg-vpn-bots/blob/main/bonus/nekobox_backup.json) | [`igareck/vpn-configs-for-russia`](https://github.com/igareck/vpn-configs-for-russia) |
| **полезные ссылки** | [`coollinks.md`](https://github.com/fakename00121v/ru-tg-vpn-bots/blob/main/bonus/coollinks.md) | [`fakename00121v/ru-tg-vpn-bots`](https://github.com/fakename00121v/ru-tg-vpn-bots) |
| **прокси для telegram** | [`tgproxy.md`](https://github.com/fakename00121v/ru-tg-vpn-bots/blob/main/bonus/tgproxy.md) | [`fakename00121v/ru-tg-vpn-bots`](https://github.com/fakename00121v/ru-tg-vpn-bots) |

## Статистика записей в input.txt
| Тип | Значение |
|-|-|
| Время | 2026-07-02 00:13:06.635917 |
| Всего | 144 |
| Уникальных | 144 |

## Как это работает

1. **`scripts/sort.py`** — читает указанный файл, разделяет строки на ботов, ссылки и прочее, удаляет дубликаты и сохраняет в указанную папку.
2. **`scripts/txttomd.py`** — конвертирует полученные `.txt` файлы в удобные `.md` с кликабельными ссылками.
3. **`scripts/с.py`** - считает всего количество записей в input.txt
4. **`scripts/rmeupd.py`** - обновляет README.md
5. **`gitupd.bat`** - обновляет файлы на гитхабе
6. **`app.py`** — запускает всю цепочку автоматически.

---

### Отказ от ответственности
*   Данный репозиторий является **инструментом для обработки списков** и **коллекцией общедоступных ссылок**, собранных вручную из открытых источников.
*   Я **не являюсь автором** и **не поддерживаю** ботов, VPN-сервисы и конфиги, ссылки на которые приведены здесь. Вся ответственность за их использование лежит на конечном пользователе.
*   Я не гарантирую работоспособность, безопасность или легальность любого из перечисленных ресурсов. Используйте их на свой страх и риск.

---

#### Поддерживаю инициативу [Keep Android Open](https://keepandroidopen.org).
* Я за свободный и открытый Android.

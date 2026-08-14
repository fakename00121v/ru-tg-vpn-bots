#Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
# Этот код был создан при помощи искусственного интеллекта
import os

def convert_txt_to_md(input_folder='output'):
    """
    Конвертирует .txt файлы в .md с кликабельными ссылками
    """
    
    # Показываем где мы сейчас и что ищем
    current_folder = os.getcwd()
    full_path = os.path.join(current_folder, input_folder)
    
    print(f"📂 Текущая папка: {current_folder}")
    print(f"🔍 Ищем папку: {full_path}")
    print(f"📁 Папка существует? {os.path.exists(full_path)}")
    print()
    
    # Файлы для конвертации
    files_to_convert = {
        'bots.txt': 'VPN Боты из Telegram',
        'links.txt': 'Реферальные ссылки на VPN',
        'others.txt': 'Что то'
    }
    
    found_any = False
    
    for txt_file, title in files_to_convert.items():
        txt_path = os.path.join(input_folder, txt_file)
        
        # Проверяем, существует ли файл
        if not os.path.exists(txt_path):
            print(f"❌ Не найден: {txt_path}")
            continue
        
        found_any = True
        
        # Читаем .txt файл
        with open(txt_path, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        
        print(f"✅ Найден {txt_file} ({len(lines)} строк)")
        
        # Создаем .md файл
        md_path = os.path.join(input_folder, txt_file.replace('.txt', '.md'))
        
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f'# {title}\n\n')
            f.write(f'Всего записей: **{len(lines)}**\n\n')
            f.write('---\n\n')
            
            for line in lines:
                if not line.strip():
                    continue
                    
                if line.startswith('t.me/') or line.startswith('@'):
                    clean_line = line.replace('@', 't.me/') if line.startswith('@') else line
                    f.write(f'- [`{line}`](https://{clean_line})\n')
                elif line.startswith('https://'):
                    f.write(f'- {line}\n')
                else:
                    f.write(f'- {line}\n')
        
        print(f"   ✅ Создан: {md_path}")
        print()
    
    if not found_any:
        print("\n❌ НИ ОДНОГО ФАЙЛА НЕ НАЙДЕНО!")
        print("\nРешение:")
        print("1. Убедитесь, что папка 'output' существует в той же папке, что и скрипт")
        print("2. Или укажите правильный путь:")
        print("   convert_txt_to_md('путь/к/вашей/папке')")
        print()
        print("Содержимое текущей папки:")
        for item in os.listdir(current_folder):
            print(f"   - {item}")
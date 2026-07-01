#Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
# Этот код был создан при помощи искусственного интеллекта

def remove_duplicates(input_file, output_dir='output', convert_to_tme=False):
    """
    Обрабатывает файл и разделяет строки по категориям
    
    Args:
        input_file: входной файл
        output_dir: папка для сохранения результатов
        convert_to_tme: если True, преобразует @username в t.me/username
    """
    import os
    
    # Создаем папку, если её нет
    os.makedirs(output_dir, exist_ok=True)
    
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    
    # Фильтруем и очищаем строки
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            cleaned_lines.append(line)
    
    # Разделяем по категориям
    bots = []
    links = []
    others = []
    
    for line in cleaned_lines:
        if line.startswith('@'):
            if convert_to_tme:
                # Преобразуем @username в t.me/username
                username = line[1:]  # убираем @
                tme_link = f't.me/{username}'
                bots.append(tme_link)
            else:
                bots.append(line)
        elif line.startswith('https://'):
            links.append(line)
        else:
            others.append(line)
    
    # Удаляем дубликаты в каждой категории
    bots_unique = list(set(bots))
    links_unique = list(set(links))
    others_unique = list(set(others))
    
    # Сохраняем в файлы
    bots_file = os.path.join(output_dir, 'bots.txt')
    links_file = os.path.join(output_dir, 'links.txt')
    others_file = os.path.join(output_dir, 'others.txt')
    
    with open(bots_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(bots_unique))
    
    with open(links_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(links_unique))
    
    with open(others_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(others_unique))
    
    # Выводим статистику
    print(f"Обработано строк: {len(cleaned_lines)}")
    print(f"Ботов (@): {len(bots_unique)} -> сохранено в {bots_file}")
    print(f"Ссылок: {len(links_unique)} -> сохранено в {links_file}")
    print(f"Прочих строк: {len(others_unique)} -> сохранено в {others_file}")
    vsego = len(bots_unique) + len(links_unique) + len(others_unique)
    
    return {
        'bots': bots_unique,
        'links': links_unique,
        'others': others_unique,
        'vsego': vsego
    }

# Использование
# Без преобразования
#remove_duplicates('input.txt', 'output')

# С преобразованием @ в t.me/
#remove_duplicates('input.txt', 'output', convert_to_tme=False)
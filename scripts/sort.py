#Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
# Этот код был создан при помощи искусственного интеллекта

def remove_duplicates(input_file, output_dir='output', convert_to_tme=False):
    import os
    import re
    
    os.makedirs(output_dir, exist_ok=True)
    
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            cleaned_lines.append(line)
    
    # Словарь для группировки по username
    bot_dict = {}  # username -> {'bots': [], 'links': []}
    pure_links = []
    others = []
    
    def extract_username(text):
        if text.startswith('@'):
            return text[1:]
        match = re.search(r't\.me/([a-zA-Z0-9_]+)', text)
        return match.group(1) if match else None
    
    for line in cleaned_lines:
        # Строки с vpn: или promo: → сразу в others
        if 'vpn:' in line or 'promo:' in line:
            others.append(line)
            continue
        
        username = extract_username(line)
        
        if username:
            # Это бот или ссылка на бота
            if username not in bot_dict:
                bot_dict[username] = {'bots': [], 'links': []}
            
            if line.startswith('@'):
                bot_dict[username]['bots'].append(line)
            elif line.startswith('https://') or line.startswith('http://'):
                if '?' in line:
                    bot_dict[username]['links'].append(line)
                else:
                    others.append(line)
        elif line.startswith('https://') or line.startswith('http://'):
            pure_links.append(line)
        else:
            others.append(line)
    
    # Формируем итоговые списки
    final_bots = []
    final_links = []
    
    for username, data in bot_dict.items():
        if data['links']:
            # Если есть рефералки → берём ТОЛЬКО ПЕРВУЮ
            final_links.append(data['links'][0])
        else:
            # Если рефералок нет → боты в bots
            if convert_to_tme:
                final_bots.append(f't.me/{username}')
            else:
                final_bots.extend(data['bots'])
    
    # Удаляем дубликаты
    bots_unique = list(set(final_bots))
    links_unique = list(set(final_links + pure_links))
    others_unique = list(set(others))
    
    bots_file = os.path.join(output_dir, 'bots.txt')
    links_file = os.path.join(output_dir, 'links.txt')
    others_file = os.path.join(output_dir, 'others.txt')
    
    with open(bots_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(bots_unique))
    
    with open(links_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(links_unique))
    
    with open(others_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(others_unique))
    
    vsego = len(bots_unique) + len(links_unique) + len(others_unique)
    
    print(f"Обработано строк: {len(cleaned_lines)}")
    print(f"Ботов: {len(bots_unique)} -> сохранено в {bots_file}")
    print(f"Ссылок (реферальных): {len(links_unique)} -> сохранено в {links_file}")
    print(f"Прочих строк: {len(others_unique)} -> сохранено в {others_file}")
    
    return {
        'bots': bots_unique,
        'links': links_unique,
        'others': others_unique,
        'vsego': vsego
    }

# Использование
# remove_duplicates('input.txt', 'output', convert_to_tme=False)
# ВАЖНО: Этот скрипт добавляет мои личные реферальные ссылки
# (из файла ../blocks/1.txt) в начало списка ссылок.
# Это делается для поддержки проекта. Все остальные ссылки сохраняются.
import os, shutil
import random
from scripts.c import *
from scripts.sort import *
from scripts.rmeupd import *
from scripts.txttomd import *

def patch_links(priority_file, links_file):
    if not os.path.exists(priority_file):
        return False
    if not os.path.exists(links_file):
        return False
    with open(priority_file, 'r', encoding='utf-8') as f:
        priority_lines = f.read().splitlines()
    priority_links = []
    for line in priority_lines:
        line = line.strip()
        if line and (line.startswith('https://') or line.startswith('http://')):
            priority_links.append(line)
    random.shuffle(priority_links)
    with open(links_file, 'r', encoding='utf-8') as f:
        all_links = f.read().splitlines()
    all_links = [line for line in all_links if line.strip()]
    priority_set = set(priority_links)
    remaining_links = [link for link in all_links if link not in priority_set]
    new_links = priority_links + remaining_links
    with open(links_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_links))
    return True

try:
    result = remove_duplicates('input.txt', 'output', convert_to_tme=False)
    vsego = result['vsego']
    
    total = count_lines('input.txt')
    readme_update('README.md', total, vsego)

    patch_links('../blocks/1.txt', 'output/links.txt')
    convert_txt_to_md('output')

    os.remove('output/others.txt')
    os.remove('output/bots.txt')
    os.remove('output/links.txt')

    shutil.rmtree("scripts/__pycache__")
    
    os.system('gitupd.bat')
    if os.path.exists(".git"):
        os.system('rmdir /s /q .git')    
    if os.path.exists('README.md'):
        os.remove('README.md')
    if os.path.exists("output"):
        shutil.rmtree("output")
except Exception as e:
    print("Error")
    print(e)
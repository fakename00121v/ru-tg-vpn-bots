import os, shutil
from scripts.c import *
from scripts.sort import *
from scripts.txttomd import *
from scripts.rmeupd import *

try:
    result = remove_duplicates('input.txt', 'output', convert_to_tme=False)
    vsego = result['vsego']
    
    convert_txt_to_md('output')
    os.remove('output/others.txt')
    os.remove('output/bots.txt')
    os.remove('output/links.txt')
    shutil.rmtree("scripts/__pycache__")
    
    total = count_lines('input.txt')
    readme_update('README.md', total, vsego)

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
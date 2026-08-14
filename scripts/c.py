def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return 0
    except Exception as e:
        print(f"Ошибка при чтении {file_path}: {e}")
        return 0
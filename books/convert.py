import json
import os

# Папка с исходными JSON
INPUT_DIR = "books"
# Папка для сохранения новых JSON (можно перезаписать старые)
OUTPUT_DIR = "books/converted"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Проходим по всем JSON-файлам в INPUT_DIR
for filename in os.listdir(INPUT_DIR):
    if not filename.endswith(".json"):
        continue

    input_path = os.path.join(INPUT_DIR, filename)

    with open(input_path, "r", encoding="utf-8") as f:
        old_data = json.load(f)

    # Определяем название книги (можно задать вручную или брать из старого JSON)
    book_title = old_data.get("title", os.path.splitext(filename)[0])

    # Преобразуем главы
    chapters = []
    for key in sorted(old_data.keys(), key=lambda x: int(x) if x.isdigit() else x):
        if key == "title":
            continue  # Пропускаем поле title, если есть
        chapter = old_data[key]
        # если список, берём первый элемент
        chapter_data = chapter[0] if isinstance(chapter, list) else chapter
        chapters.append({
            "title": chapter_data.get("title", f"Глава {key}"),
            "content": "<p>" + chapter_data.get("content", "").replace("\n\n", "</p><p>") + "</p>"
        })


    new_data = {
        "title": book_title,
        "chapters": chapters
    }

    output_path = os.path.join(OUTPUT_DIR, filename)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)

    print(f"{filename} → {output_path} преобразован")


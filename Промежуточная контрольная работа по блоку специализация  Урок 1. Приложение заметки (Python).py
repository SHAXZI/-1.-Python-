import json
import os

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NotesApp:
    def __init__(self, file_name="notes.json"):
        self.file_name = file_name
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}

    def save_notes(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.notes, file, ensure_ascii=False, indent=4)

    def create_note(self, title, content):
        if title in self.notes:
            print("Заметка с таким названием уже существует.")
        else:
            self.notes[title] = content
            self.save_notes()
            print("Заметка успешно создана.")

    def list_notes(self):
        if not self.notes:
            print("Нет доступных заметок.")
        else:
            print("Список заметок:")
            for title in self.notes:
                print(f"- {title}")

    def read_note(self, title):
        if title in self.notes:
            print(f"Заметка: {title}\n{self.notes[title]}")
        else:
            print("Заметка с таким названием не найдена.")

    def edit_note(self, title, new_content):
        if title in self.notes:
            self.notes[title] = new_content
            self.save_notes()
            print("Заметка успешно отредактирована.")
        else:
            print("Заметка с таким названием не найдена.")

    def delete_note(self, title):
        if title in self.notes:
            del self.notes[title]
            self.save_notes()
            print("Заметка успешно удалена.")
        else:
            print("Заметка с таким названием не найдена.")

def main():
    app = NotesApp()

    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Просмотреть список заметок")
        print("3. Прочитать заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название заметки: ")
            content = input("Введите содержимое заметки: ")
            app.create_note(title, content)
        elif choice == "2":
            app.list_notes()
        elif choice == "3":
            title = input("Введите название заметки: ")
            app.read_note(title)
        elif choice == "4":
            title = input("Введите название заметки: ")
            new_content = input("Введите новое содержимое заметки: ")
            app.edit_note(title, new_content)
        elif choice == "5":
            title = input("Введите название заметки: ")
            app.delete_note(title)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

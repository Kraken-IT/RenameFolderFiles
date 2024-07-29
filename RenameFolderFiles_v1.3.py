import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def change_extension_and_copy_files(src_folder, dest_folder):
    try:
        # Получаем список всех файлов в исходной папке
        files = os.listdir(src_folder)
        
        # Проходим по каждому файлу
        for file_name in files:
            # Создаем полный путь к файлу
            full_file_path = os.path.join(src_folder, file_name)
            
            # Проверяем, является ли объект файлом
            if os.path.isfile(full_file_path):
                # Разделяем имя файла и его расширение
                base_name, ext = os.path.splitext(file_name)
                
                # Создаем новое имя файла с расширением .jpg
                new_file_name = base_name + ".jpg"
                new_file_path = os.path.join(dest_folder, new_file_name)
                
                # Копируем файл в целевую папку с новым именем
                shutil.copy2(full_file_path, new_file_path)
        
        messagebox.showinfo("Hazır", "Bütün faylların adları dəyişdirildi və digər qovluğa kopyalandı")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

def select_src_folder():
    src_folder = filedialog.askdirectory(title="Dəyişiləcək fayllar olan qovluğu seçin")
    if src_folder:
        src_folder_var.set(src_folder)

def select_dest_folder():
    dest_folder = filedialog.askdirectory(title="Haraya kopyalansın?")
    if dest_folder:
        dest_folder_var.set(dest_folder)

def start_process():
    src_folder = src_folder_var.get()
    dest_folder = dest_folder_var.get()
    if src_folder and dest_folder:
        change_extension_and_copy_files(src_folder, dest_folder)
    else:
        messagebox.showwarning("Diqqət", "Zəhmət olmasa hər iki qovluğu seçin.")

# Создаем главное окно
root = tk.Tk()
root.title("Dəyişiklik .jpg və kopyalanma")
root.geometry("500x300")

# Переменные для хранения путей папок
src_folder_var = tk.StringVar()
dest_folder_var = tk.StringVar()

# Создаем и размещаем виджеты
label = tk.Label(root, text="Hansı qovluqdakı fayllarda sonluq .jpg olacaq?")
label.pack(pady=10)

src_button = tk.Button(root, text="Dəyişdiriləcək fayllar qovluğu", command=select_src_folder)
src_button.pack(pady=5)

src_label = tk.Label(root, textvariable=src_folder_var)
src_label.pack(pady=5)

dest_button = tk.Button(root, text="Dəyişilən faylların yerləşdiyi qovluq", command=select_dest_folder)
dest_button.pack(pady=5)

dest_label = tk.Label(root, textvariable=dest_folder_var)
dest_label.pack(pady=5)

start_button = tk.Button(root, text="İcra edilsin", command=start_process)
start_button.pack(pady=20)

# Подпись
signature_label = tk.Label(root, text="Kraken-IT", font=("Arial", 10), fg="grey")
signature_label.pack(side=tk.BOTTOM, pady=10)

# Запускаем главный цикл приложения
root.mainloop()

import pandas as pd
import os

# Получаем путь к текущему каталогу
current_directory = os.getcwd()

# Создаем полный путь к файлу
file_path = os.path.join(current_directory, 'BD.xlsx')

# Загружаем данные из файла Excel
df = pd.read_excel(file_path)

print(df)
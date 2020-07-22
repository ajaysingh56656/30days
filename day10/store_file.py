import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_dir = os.path.join(BASE_DIR, 'images')

os.makedirs(file_dir, exist_ok=True)

my_images = range(0, 12)

for i in my_images:
    fName = f'{i}.txt'
    file_path = os.path.join(file_dir, fName)
    if os.path.exists(file_path):
        print(f'Skipped {fName}')
        continue
    with open(file_path, 'w') as f:
        f.write(f'Hello World {i}')

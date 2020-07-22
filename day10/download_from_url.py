import os
import requests
import shutil  # For big item download

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOADS_DIR = os.path.join(BASE_DIR, 'downloads')
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

download_img_path = os.path.join(DOWNLOADS_DIR, '1.jpg')
url = 'https://images.unsplash.com/photo-1562155847-c05f7386b204'

# A small item
r = requests.get(url, stream=True)
r.raise_for_status()  # raise error if somthing went wrong
with open(download_img_path, 'wb') as f:
    f.write(r.content)

dl_filename = os.path.basename(url)
new_dl_path = os.path.join(DOWNLOADS_DIR, f'{dl_filename}.jpg')
# For Big Item
with requests.get(url, stream=True) as r:
    with open(new_dl_path, 'wb') as file_obj:
        shutil.copyfileobj(r.raw, file_obj)

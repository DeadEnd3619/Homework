from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

app = Flask(__name__)

def download_image(url, folder_path):
    try:
        responce = requests.get(url, stream=True)
        if (responce.status_code==200):
            file_name = url.split('/')[-1]
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'wb') as file:
                for chunk in responce.iter_content(1024):
                    file.write(chunk)
            print(f'image downloaded: {file_name}')
        else:
            print(f'failed to download image from: {url}:{e}')
    except Exception as e:
        print(f'Error downloading image from: {url}:{e}')
def crawl_images(url, folder_path):
    image_paths = []
    try:
        responce = requests.get(url)
        if (responce.status_code==200):
            soup = BeautifulSoup(responce.text, 'html.parser')
            img_tags = soup.find_all(['img', 'video'])
            for img_tag in img_tags:
                img_url = img_tag.get('src')
                img_url = urljoin(url, img_url)
                download_image(img_url, folder_path)
                file_name = img_url.split('/')[-1]
                image_paths.append(os.path.join(folder_path, file_name))
    except Exception as e:
        print(f'Error crawling images from: {url}:{e}')
    return image_paths




@app.route('/', methods=['GET', 'POST'])
def index():
    image_urls = []
    if request.method == 'POST':
        url = request.form['url']
        folder_path = 'C:/Users/Ckirkl439/Downloads/WASD'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        image_urls = crawl_images(url, folder_path)
        return render_template('index.html', image_urls=image_urls)
    return render_template('index.html', image_urls=image_urls)
if __name__ == '__main__':
    app.run(debug=True)
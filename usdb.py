import time
import requests
from bs4 import BeautifulSoup
import os

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {save_path}")
    else:
        print(f"Failed to retrieve image from {url}")

def main():
    baseurl = 'https://usdb.animux.de/'
    page = '?link=detail&id=1322'
    url = baseurl + page
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        download_link = None
        for tr in soup.find_all('tr', class_='list_tr1'):
            a_tag = tr.find('a', href=True)
            if a_tag and 'gettxt' in a_tag['href']:
                download_link = a_tag['href']
                break

        # import webbrowser
        # if download_link:
        #     # webbrowser.open(baseurl + download_link)
        #     webbrowser.open_new(baseurl + download_link)
        # if download_link:
        #     from selenium import webdriver

        #     driver = webdriver.Chrome()
        #     driver.get("http://www.google.com/")
        #     driver.close()

        class_list_tr1 = soup.find_all('tr', class_='list_tr1')
        cover_row = None
        for tr in class_list_tr1:
            if 'Cover' in tr.text:
                cover_row = tr
                break

        if cover_row:
            cover_image = cover_row.find('img')
        else:
            cover_image = None

        # with open('page_content.html', 'w', encoding='utf-8') as file:
        #     file.write(soup.prettify())
        # print("Page content successfully written to page_content.html")

        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.text.strip()
            title = title.split('-')[1] + '-' + title.split('-')[2]
            title = title.strip()
            print(f"Page title: {title}")
        else:
            print("Title not found in the head section.")
    
        import os
        if title:
            folder_path = os.path.join(os.getcwd(), title)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Folder created: {folder_path}")

        if cover_image and 'src' in cover_image.attrs:
            image_url = cover_image['src']
            if not image_url.startswith('http'):
                image_url = 'https://usdb.animux.de/' + image_url
            
            save_path = os.path.join(folder_path, f'{title} [CO].jpg')
            download_image(image_url, save_path)
        else:
            print("Cover image not found on the page.")
    else:
        print(f"Failed to retrieve the webpage: {url}")

if __name__ == "__main__":
    main()
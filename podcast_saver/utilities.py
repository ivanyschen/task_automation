import os

import requests
from bs4 import BeautifulSoup
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def get_episodes():
    url = 'https://talkpython.fm/episodes/all'
    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print err
        yield
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='table table-hover episodes')
    tbody = table.find('tbody')
    table_rows = tbody.find_all('tr')
    for row in table_rows:
        table_data = row.find_all('td')
        episode_number = table_data[0].text.encode('utf-8')
        episode_date = table_data[1].text.encode('utf-8')
        episode_title = table_data[2].text.encode('utf-8')
        episode_guest = table_data[3].text.encode('utf-8')
        episode_page_url = 'https://talkpython.fm' + table_data[2].find('a')['href'].encode('utf-8')
        yield (episode_number, episode_date, episode_title, episode_guest, episode_page_url)


def get_mp3_url(episode_page_url):
    title = episode_page_url.split('/')
    title = '/'.join(title[-2:])
    mp3_url = "https://talkpython.fm/episodes/download/{}.mp3".format(title)
    return mp3_url


def download_mp3(mp3_url, file_name, destination_directory):
    response = requests.get(mp3_url)
    path_to_new_file = os.path.join(destination_directory, file_name) + '.mp3'
    with open(path_to_new_file, 'a') as new_file:
        new_file.write(response.content)
    print("Saved {} to {}".format(file_name, destination_directory))
    return path_to_new_file


def drive_authentication():
    drive_auth = GoogleAuth()
    drive_auth.LocalWebserverAuth()
    drive = GoogleDrive(drive_auth)
    return drive


def create_folder(drive, new_folder_name, parent_folder=None):
    new_folder = drive.CreateFile({'title': '{}'.format(new_folder_name),
                                   'mimeType': 'application/vnd.google-apps.folder'})
    if parent_folder is not None:
        new_folder['parents'] = [{u'id': parent_folder['id']}]
    new_folder.Upload()
    print('created folder {}'.format(new_folder_name))
    return new_folder


def upload_to_gdrive(drive, local_file, parent_folder=None):
    local_file_name = os.path.basename(local_file)
    new_file = drive.CreateFile({'title': local_file_name,})
    new_file['parents'] = [parent_folder] if parent_folder else []
    new_file.SetContentFile(local_file)
    new_file.Upload()
    print("Uploaded {}".format(local_file_name))
    return


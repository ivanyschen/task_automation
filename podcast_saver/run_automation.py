import utilities as util


drive = util.drive_authentication()
drive_folder_to_save = util.create_folder(drive, 'Talk Python to Me')

podcast_episodes = util.get_episodes()
for eps_number, _, eps_title, _, eps_url in podcast_episodes:
    eps_mp3_url = util.get_mp3_url(eps_url)
    mp3_file_name = '-'.join([eps_number, eps_title])
    path_to_new_file = util.download_mp3(eps_mp3_url, mp3_file_name, 'podcasts')
    util.upload_to_gdrive(drive, path_to_new_file, parent_folder=drive_folder_to_save)
# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/utils.ipynb (unless otherwise specified).

__all__ = ['logger', 'download_gdrive']


# Cell
import os
import gdown
import logging


logger = logging.getLogger()
logger.setLevel("INFO")


# Cell
def download_gdrive(url=None, file_id=None, file_name=None, data_folder=None,
                    extract_all=False, **kwargs):
    assert url or file_id, "Either google drive download url or file id must be specified."
    base_url = "https://drive.google.com/uc?id={file_id}"
    if url:
        file_id, is_download_link = gdown.parse_url.parse_url(url)
    elif file_id:
        url = base_url.format(file_id=file_id)

    # folder to save this particular file
    data_folder = data_folder if data_folder else file_id
    data_folder = os.path.join(get_data_root(), data_folder)
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    file_name = file_name if file_name else "gdrive_{file_id}.zip"
    file_path = os.path.join(data_folder, file_name)
    if not os.path.exists(file_path):
        logging.info("Start to download files on Google Drive...")
        downloaded_file_path = gdown.download(url, **kwargs)
        os.rename(downloaded_file_path, file_path)

    if extract_all:
        logging.info("Extracting zip file...")
        files = gdown.extractall(file_path)
        return file_path, files
    else:
        return file_path
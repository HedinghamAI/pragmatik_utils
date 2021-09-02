import os
import requests
import logging
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


def __download_img(url, file_path):
    try:
        if os.path.exists(file_path):
            return
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(file_path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        else:
            logging.error("failed to get image: {}".format(file_path))
    except Exception as e:
        logging.error(e)


def fetch_images(image_list):
    """Download a list of images using ThreadPoolExecutor
    Parameters:
        image_urls: list(tuple(file_name, image_url))
    """
    with tqdm(total=len(image_list)) as pbar:
        with ThreadPoolExecutor(max_workers=8) as ex:
            futures = [ex.submit(__download_img, url, file_name) for file_name, url in image_list]
            for future in as_completed(futures):
                # result = future.result()
                pbar.update(1)

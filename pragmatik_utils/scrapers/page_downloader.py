import os
import requests
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


def __download_page(url, file_path):
    try:
        if os.path.exists(file_path):
            return
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(file_path, 'w') as f:
                f.write(r.text)
        else:
            logging.error("failed to get image: {}".format(file_path))
    except Exception as e:
        logging.error(e)


def fetch_pages(page_list):
    """Download a list of pages using ThreadPoolExecutor
    Parameters:
        image_urls: list(tuple(file_name, image_url))
    """
    with tqdm(total=len(page_list)) as pbar:
        with ThreadPoolExecutor(max_workers=3) as ex:
            futures = [ex.submit(__download_page, url, file_name) for file_name, url in page_list]
            for future in as_completed(futures):
                # result = future.result()
                pbar.update(1)


if __name__ == '__main__':
    fetch_pages([("page.html", "https://google.com")])

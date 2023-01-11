import zipfile
import os
import requests

ZIP_PATH = "downloads/firefox.zip"
DIST_PATH = "downloads/"
URL = "https://ftp.mozilla.org/pub/firefox/nightly/2022/12/2022-12-01-16-18-29-mozilla-central/firefox-109.0a1.en-US.win32.zip"


def download():
    print("Baixando Firefox 109.0a1...\n")
    response = requests.get(URL)
    open(ZIP_PATH, "wb").write(response.content)


def unzip():
    print("Extraindo Firefox 109.0a1...\n")
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(DIST_PATH)


def install():
    if not os.path.exists("downloads/firefox"):
        download()
        unzip()

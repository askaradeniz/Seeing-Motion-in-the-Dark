import requests
import os

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

if not os.path.isdir("checkpoint"):
    os.makedirs("checkpoint")

print('Dowloading Model..')
download_file_from_google_drive('1zqFFB8UfuAdIJrrtL1RvG2tj52BEldWa', 'checkpoint/model.ckpt.data')
download_file_from_google_drive('1WdELGbiRDma4QjoRxQgvkBdvvl-5_vhm', 'checkpoint/model.ckpt.data-00000-of-00001')
download_file_from_google_drive('1yZ7LhgUdr2CeXIBWciB1Du5xVE2sEMZf', 'checkpoint/model.ckpt.index')
download_file_from_google_drive('1P7d4HYZx5cyJQYze8Jx6f1mLXhwq58c0', 'checkpoint/checkpoint')






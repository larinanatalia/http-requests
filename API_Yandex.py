
class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        import requests
        import json
        path_list = self.file_path.split('/')
        pic_name = path_list[-1]
        headers = {'Authorization': 'OAuth ++++++++++++++'}
        params = {'path': pic_name}
        resp = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                headers=headers, params=params)
        resp_get = resp.json()
        with open(self.file_path, 'rb') as f:
            resp_put = requests.put(str(resp_get['href']), files={"file": f})
        return 'File added'



naruto = YaUploader('C:/Users/79035/Desktop/py-33/hw-http/photos/naruto_1.jpg')
naruto.upload()

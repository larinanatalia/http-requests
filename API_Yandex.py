
class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        import requests
        import json
        path_list = self.file_path.split('/')
        pic_name = path_list[-1]
        headers = {'Authorization': 'OAuth ++++++++++++++++'}
        params = {'path': pic_name}
        resp = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                headers=headers, params=params)
        resp_get = resp.json()
        if resp.status_code == 200:
            with open(self.file_path, 'rb') as f:
                resp_put = requests.put(str(resp_get['href']), files={"file": f})
                print('File added')
        else:
            print(resp_get['message'])


if __name__ == '__main__':
    uploader = YaUploader('')
    result = uploader.upload()



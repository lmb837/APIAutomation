import requests, json


class SendMethod:
    def get(url, params, headers):
        res = requests.get(url=url, params=params, headers=headers)
        return res

    def postByJson(url, params, headers):
        res = requests.post(url=url, data=params, headers=headers)
        return res

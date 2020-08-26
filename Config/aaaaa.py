# -*-coding:utf-8-*-
def get(url, params=None, **kwargs):


    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs)


def post(url, data=None, json=None, **kwargs):



    return request('post', url, data=data, json=json, **kwargs)
import requests


def lang_popular(url):
    popularity_dict = {}# мне больше нравится словарь, но в задании просили список)
    popularity_list = [] # сделала и список, и словарь :)
    for i in lang_list:
        lang_i = []
        response = requests.get(url, params='q=language:'+i)
        response_dict = response.json()
        popularity_dict[i] = response_dict['total_count']
        lang_i.append(i)
        lang_i.append(response_dict['total_count'])
        popularity_list.append(lang_i)
    print(popularity_dict)
    print(popularity_list)

lang_list = ['python', 'c++', 'java',
             'javascript', 'ruby', 'c#']

url = 'https://api.github.com/search/repositories'

lang_popular(url)

import urllib.request


class GetDataFromUrl(object):
    def __init__(self, url):
        self.url = url

    def get_url_data(self):

        request = urllib.request.Request(self.url)
        response = urllib.request.urlopen(request)
        data = response.read()
        data = data.decode('utf-8')
        return data


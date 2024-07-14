import dj_database_url

def parse(url):
    if isinstance(url, bytes):
        url = url.decode('utf-8')
    return dj_database_url.parse(url)

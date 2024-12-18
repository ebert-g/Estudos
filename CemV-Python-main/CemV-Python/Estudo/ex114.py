import urllib.request


def check_website_accessibility(url):
    try:
        urllib.request.urlopen(url)
        return True
    except urllib.request.URLError:
        return False


# Example usage:
url = 'https://www.youtube.com/watch?v=8jAykqxIeqw&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=139'
if check_website_accessibility(url):
    print(f'{url} is accessible.')
else:
    print(f'{url} is not accessible.')
print(urllib.request.urlopen(url).read)
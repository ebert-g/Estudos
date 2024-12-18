import requests

def check_website_exists(domain):
    url = "http://" + domain
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

if check_website_exists("https://www.youtube.com/watch?v=8jAykqxIeqw&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=139"):
    print("The website exists.")
else:
    print("The website does not exist.")
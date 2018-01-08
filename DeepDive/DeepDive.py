import requests
from bs4 import BeautifulSoup

visited = []

def get_links(url):
    visited.append(url)
    print(url)

    try:
        response = requests.get(url)
    except:
        print("Request failed!")
        return []

    if response.status_code != 200:
        print("Unexpected status code!")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    links = []

    for x in soup.find_all("a", href=True):
        link = x["href"]

        if link.startswith("/"):
            base = ""
            slashes = 0

            for y in url:
                if y == "/":
                    slashes += 1

                if slashes == 3:
                    break

                base += y

            link = base + link
        
        links.append(link)

    return links

if __name__ == "__main__":
    print("Enter initial URL: ", end="")
    initUrl = input()

    remaining = get_links(initUrl)

    while remaining:
        for x in get_links(remaining.pop()):
            if x not in remaining and x not in visited:
                remaining.append(x)

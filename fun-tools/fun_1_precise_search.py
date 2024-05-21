import requests
from bs4 import BeautifulSoup


def is_product(product):
    query = product.replace(' ', '+')
    query = '"' + query + '"'
    add = '&sca_esv=396701017a0fe9d3&sca_upv=1&sxsrf=ADLYWIKWgdKR0hofOSCSRshq3fR-z5vDMA%3A1715482705794&ei=UTBAZqCXMMvK1e8Pw_C8gAk&ved=0ahUKEwjgg7CKj4eGAxVLZfUHHUM4D5AQ4dUDCBE&uact=5&oq=%22%E6%96%B0%E8%83%BD%E6%BA%90%E6%B1%BD%E8%BD%A6%E7%94%B5%E6%B1%A0%22&gs_lp=Egxnd3Mtd2l6LXNlcnAiFyLmlrDog73mupDmsb3ovabnlLXmsaAiMgYQABgeGA8yBhAAGB4YDzIGEAAYHhgPMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIESP8FUABYAHAAeACQAQCYAeIBoAHiAaoBAzItMbgBA8gBAPgBAvgBAZgCAaAC5QGYAwCSBwMyLTGgB8kC&sclient=gws-wiz-serp'
    URL = f"https://www.google.com/search?q={query}&as_q={query}&tbs=li:1"
    print(URL)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    resp = requests.get(URL, headers=headers)
    decoded_text = resp.text
    results = []
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        # print(soup)

        for g in soup.find_all('div', class_='tF2Cxc'):
            title = g.find('h3').text
            link = g.find('a')['href']
            item = {
                "title": title,
                "link": link
            }
            results.append(item)
        print(results)
    else:
        print("Failed to fetch search results")

    return True if len(results) >= 1 else False


query = '"新能源汽车电池"'
query = '"高档数控机床用变频智能电动执行器（电动夹爪）"'
query = '"CAE—多学科设计集成与优化"'
res = []
for query in ["新能源汽车电池", "高档数控机床用变频智能电动执行器（电动夹爪）", "CAE—多学科设计集成与优化"]:
    res.append(is_product(query))

print(res)
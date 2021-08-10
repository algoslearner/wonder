# from googlesearch import search
from bs4 import BeautifulSoup
from requests import get


def search(term, num_results=20, lang="en", proxy=None):
    usr_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.100 Safari/537.36'}

    def fetch_results(search_term, number_results, language_code):
        escaped_search_term = search_term.replace(' ', '+')

        google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results+1,
                                                                              language_code)
        proxies = None
        if proxy:
            if proxy[:5]=="https":
                proxies = {"https":proxy} 
            else:
                proxies = {"http":proxy}
        
        response = get(google_url, headers=usr_agent, proxies=proxies)    
        response.raise_for_status()

        return response.text

    def parse_results(raw_html):
        soup = BeautifulSoup(raw_html, 'html.parser')
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:
            link = result.find('a', href=True)
            title = result.find('h3')
            if link and title:
                yield link['href']

    html = fetch_results(term, num_results, lang)
    return list(parse_results(html))

# search io
query = input("Enter your search query: ")
#store query and search results in output.txt file
output_file = open("output.txt", 'w')
print("***********************", file=output_file)
print(query, file=output_file)
print("***********************", file=output_file)

# for i in search(query, tld="com", lang='en', num=10, stop=10, pause=2):
# 	print(i, file=output_file)
for i in search(query):
	print(i, file=output_file)
print("***********************", file=output_file)
output_file.close()

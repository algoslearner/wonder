import requests
from bs4 import BeautifulSoup

search_term = input("Enter your search term : ")
escaped_search_term = search_term.replace(' ', '+')
number_results = 10
language_code='en'

google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results+1,language_code)
response = requests.get(google_url)
# print(response.content)

#write response to a file
#output_file = open("output_html.txt",'w')
#print(response.content, file=output_file)
#output_file.close()

#html parsing using beautifulsoup
soup = BeautifulSoup(response.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
output_file_parsed = open("output_html.txt",'w')
print(soup.prettify(), file=output_file_parsed)
output_file_parsed.close()

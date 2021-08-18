import requests

# get the API KEY here: https://developers.google.com/custom-search/v1/overview
API_KEY = "AIzaSyBe_rpbTPsQrB_dmTCuSCpIBN8jc0ar-P0"

# get your Search Engine ID on your CSE control panel
SEARCH_ENGINE_ID = "3b0a0eb2b684072d2"

# the search query you want
query = input("Enter your Google search query :" )

# using the first page
page = 1

# constructing the URL
# doc: https://developers.google.com/custom-search/v1/using_rest
# calculating start, (page=2) => (start=11), (page=3) => (start=21)
start = (page - 1) * 10 + 1
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

# make the API request
# using requests' json() method to automatically parse the returned JSON data to a Python dictionary
data = requests.get(url).json()

# output json data to textfile
output_file = open("outputJSON.txt", 'w')
for i in data:
	print(i, file=output_file)
for i in data:
	print(data[i], file=output_file)
output_file.close()

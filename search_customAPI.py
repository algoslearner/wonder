import requests
import urllib.parse as urlparse

query = input("Enter your Google search query :" )
params = {
	"key": "AIzaSyBe_rpbTPsQrB_dmTCuSCpIBN8jc0ar-P0",
	"cx": "3b0a0eb2b684072d2",
	"q": query,
	"start": 0
}
gcse_base_url = "https://www.googleapis.com/customsearch/v1"
url_parts = list(urlparse.urlparse(gcse_base_url))
url_parts[4] = urlparse.urlencode(params)
gcse_url = urlparse.urlunparse(url_parts)

data = requests.get(gcse_url).json()
items = data["items"]

# output json data to textfile
output_file = open("outputJSON.txt", 'w')
for i in data:
	print(i, file=output_file)
for i in data:
	print(data[i], file=output_file)
output_file.close()

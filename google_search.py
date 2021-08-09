try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

# to search
query = "active volcano"

#store query and search results in output.txt file
output_file = open("output.txt", a)
print("***********************", file=output_file)
print(query, file=output_file)
print("***********************", file=output_file)

for i in search(query, tld="com", lang='en', num=10, stop=10, pause=2):
	print(i, file=output_file)
print("***********************", file=output_file)
f.close()

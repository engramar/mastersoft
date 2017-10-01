import urllib.request

# Load the data from remote location (URL)
file = urllib.request.urlopen("https://gist.githubusercontent.com/twielfaert/a0972bf366d9aaf6cb1206c16bf93731/raw/dde46ad1fa41f442971726f34ad03aaac85f5414/Donna-Tartt-The-Goldfinch.csv")
f = file.read()

# Transform the bitstream into strings
text = f.decode(encoding='utf-8',errors='ignore')

# Split this single string at the end of lines
lines = text.split("\n")

# Initalising the dictionary
reviews = {}

# Filling the dictionary
for line in lines:
  l = line.strip().split("\t")
  
  # These are just training wheels to see more clearly what goes into the dictionary
  score = l[0] 
  id = l[1]
  title = l[2]
  review = l[3]
  
  reviews[id] = {"score" : score, "title" : title, "review" : review}

count = 0  
for key, val in reviews.items():
    print (reviews[key]["score"],reviews[key]["title"])
    count = count + 1

print(count)

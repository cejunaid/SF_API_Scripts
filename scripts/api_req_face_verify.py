import requests

# Read the query and verification images
img_files = [('qfile', open('test_imgs/1.jpg', 'rb')), ('vfile', open('test_imgs/2.jpeg', 'rb'))]
url = "https://api.sensusfuturis.com/api/v1/faces/verify"




# Create the POST request
headers = {
            
            "Authorization": "Token <replace with token>",
            }

response = requests.post(url, files=img_files, headers=headers)
# Print the response
print(f"Response: {response.text}")

import requests
import cv2
import json


class SFAPI():
    def __init__(self) -> None:
        self.url = "https://api.sensusfuturis.com/api/v1/appearance_embedding"
        
    def appearance_embedding(self, image_path):
        # Read the image
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        
        # Create the POST request
        headers = {
                    "Authorization": "Token <replace with token>"
                  }
        files = {'file': image_data}
        response = requests.post(self.url, files=files, headers=headers)
        return response.text
    
if __name__ =='__main__':
    sf_api = SFAPI()
    
    pe_resp = sf_api.appearance_embedding('test_imgs/r1.webp')
    print(pe_resp)
    
    #display person detections on image
    resp = json.loads(pe_resp)
    pboxes = resp['person_locations']
    
    img = cv2.imread('test_imgs/r1.webp')
    
    # Blue color in BGR
    color = (255, 0, 0)
    
    # Line thickness of 2 px
    thickness = 2
    
    for pb in pboxes:
        pb = list(map(int, pb))
        img = cv2.rectangle(img, (pb[0], pb[1]), (pb[2], pb[3]), color, thickness)
    # Displaying the image 
    cv2.imshow("Person Detection", img)
    cv2.waitKey(0)     

    print('All done!')
    
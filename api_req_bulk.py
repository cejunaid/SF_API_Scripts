import requests
import json
import os
from tqdm import tqdm



class SFAPI():
    def __init__(self) -> None:
        self.fd_url = "https://api.sensusfuturis.com/api/v1/face_detector"

    def face_detector(self, image_path):
        # Read the image
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        
        # Create the POST request
        headers = {"content-type": "application/octet-stream",
                "content-Disposition": "attachment; filename='img.jpg'",
                "Authorization": "Token <replace with token>"
                }

        response = requests.post(self.fd_url, data=image_data, headers=headers)
        return response.text
    
if __name__ =='__main__':
    sf_api = SFAPI()
    f = open('image_list.txt', 'r')
    all_image_paths = f.readlines()
    f.close()
    
    
    all_fd_resp = {}
    
    for image_path in tqdm(all_image_paths):
        image_path = image_path.replace('\n', '')
        fd_resp = sf_api.face_detector(image_path)
        all_fd_resp[os.path.basename(image_path)] = json.loads(fd_resp) 
        
   
    
    with open('bulk_face_detector_response.json', 'w') as f:
        f.writelines(json.dumps(all_fd_resp))
        
    print('All done!')
import requests




class SFAPI():
    def __init__(self) -> None:
        self.url = "https://api.sensusfuturis.com/api/v1/faces/detector"

    def face_detector(self, image_path):
        # Read the image
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        
        # Create the POST request
        headers = {
                "Authorization": "Token <replace with token>",
                }

        files = {'file': image_data}
        response = requests.post(self.url, files=files, headers=headers)
        return response.text
    
if __name__ =='__main__':
    sf_api = SFAPI()
    
    fe_resp = sf_api.face_detector('test_imgs/1.jpg')
    print(fe_resp)
        
    print('All done!')
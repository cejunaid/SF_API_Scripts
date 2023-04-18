import requests




class SFAPI():
    def __init__(self) -> None:
        self.fd_url = "https://api.sensusfuturis.com/api/v1/face_embedding"

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
    
    fd_resp = sf_api.face_detector('test_imgs/1.jpg')
    print(fd_resp)
        
    print('All done!')
    
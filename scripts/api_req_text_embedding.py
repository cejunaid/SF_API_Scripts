import requests
import numpy as np
import json


class SFAPI():
    def __init__(self) -> None:
        self.url = "https://api.sensusfuturis.com/api/v1/people/text/embedding"
        
        
    def text_embedding(self, sentences):
        # Read the image
        
        # Create the POST request
        headers = {
                    "Authorization": "Token <replace with token>",
                  }
        form_data = {}
        form_data["sentences"] =  sentences
        
        response = requests.post(self.url, data=form_data, headers=headers)
        return response.text
    
if __name__ =='__main__':
    sf_api = SFAPI()
    sentence = "A person wearing blue jeans and red shirt"
    ts = ['A man in red shirt and black pants and black shoes.', 
		'A man in red tshirt and black pants and black shoes.',
		'A man in red t-shirt and black pants and black shoes.',
		'A man in reddish t-shirt and black pants and black shoes.',
		'A man in reddish color t-shirt and black pants and black shoes.',
		'A man in scarlet t-shirt and black pants and black shoes.',
		]
    ts = [
        'A person wearing yellow hoodie with green pattern and gray trousers',
        'A person wearing gray shirt, blue jeans and blue shoes. he is holding an orange handbook',
        'An old man is wearing white and black lines shirt under a coat. he is wearing a green cap and holding a cane.',
        'A person wearing green hoodie with white lines.',
        'A person wearing orange top and blue jeans is holding an umbrella',
        'A person wearing white coat and black trouser',
        'A girl wearing a floral scarf '
        
        ]
    text_resp = sf_api.text_embedding('::'.join(ts))
    
    ad = json.loads(text_resp)
    text_feat = np.array(ad['text_embeddings'])
    
    print('All done!')
    
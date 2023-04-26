import ast
import numpy as np
import heapq
import cv2
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image






class L2V():
    def __init__(self) -> None:
            
        #load all the appearance features
        self.all_appearance_data =np.load('path_to_appearance_features.npy', allow_pickle=True)
        
        self.all_pd_data = np.load('path_to_person_detection.npy', allow_pickle=True).tolist()
        
    
    def get_l2v(self, lang_feat, frame_nr, sentence):
        
        
        pd = self.all_pd_data[frame_nr]
        vis = np.array(self.all_appearance_data[frame_nr])
        lang = np.expand_dims(np.array(lang_feat), axis=0)
        
        #get cosine similarity
        z = cosine_similarity(vis, Y=lang)
        
        #get matching index of person detection
        max_idx = np.argmax(z)
        
        #get the matched person detection for diplaying purpose
        matched_pd = pd[max_idx]
        
        
    

if __name__ == '__main__':
    sentences = [
        'A person wearing yellow hoodie with green pattern and gray trousers',
        'A person wearing gray shirt, blue jeans and blue shoes. he is holding an orange handbook',
        'An old man is wearing white and black lines shirt under a coat. he is wearing a green cap and holding a cane.',
        'A person wearing green hoodie with white lines.',
        'A person wearing orange top and blue jeans is holding an umbrella',
        'A person wearing white coat and black trouser',
        'A girl wearing a floral scarf '
        
        ]
    
    
    
    l2v = L2V()
    all_lang_data = np.load('path_to_lang_features.npy', allow_pickle=True).tolist()
    
    #get matching result
    l2v.get_l2v(all_lang_data[0], 220, sentences[0])
    
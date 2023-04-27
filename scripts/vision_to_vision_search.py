import ast
import numpy as np
import heapq
import cv2
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image






class V2V():
    def __init__(self) -> None:
            
        #load all the vision features
        self.all_vision_data =np.load('path_to_vision_features.npy', allow_pickle=True)
        
        self.all_pd_data = np.load('path_to_person_detections.npy', allow_pickle=True).tolist()
        
    
    def get_v2v(self, vision_feat, frame_nr):
        
        
        pd = self.all_pd_data[frame_nr]
        all_vision_features = np.array(self.all_vision_data[frame_nr])
        vision_query = np.expand_dims(np.array(vision_feat), axis=0)
        
        #get cosine similarity
        z = cosine_similarity(all_vision_features, Y=vision_query)
        
        #get matching index of person detection
        max_idx = np.argmax(z)
        
        #get the matched person detection for diplaying purpose
        matched_pd = pd[max_idx]
        
        
    

if __name__ == '__main__':
    
    
    v2v = V2V()
    
    
    #get matching result
    v2v.get_v2v("<query_vision_feat>", 220)
    
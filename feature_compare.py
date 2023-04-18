import torch
from sklearn.metrics.pairwise import cosine_similarity

def compare_features(feature1, feature2):
        #since the feature response from out API is a list of feature containing 512 floating point numbers, we need to convert it to a tensor.
        f1 = torch.Tensor(feature1)
        if len(f1.shape) == 1:
            f1 = f1.unsqueeze(0)
        f2 = torch.Tensor(feature2)
        if len(f2.shape) == 1:
            f2 = f2.unsqueeze(0)
        
        result = cosine_similarity(f1, f2)
        return result
    
list_feat1 = [-0.013276094570755959, 0.004762198776006699, -0.014785194769501686, -0.04084409028291702]
list_feat2 = [0.044945213943719864, 0.03469116985797882, -0.014785194769501686, -0.04084409028291702]

#get feature cosine similarity
feature_similarity = compare_features(list_feat1, list_feat2)
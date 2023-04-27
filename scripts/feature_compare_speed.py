import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import datetime

tic = datetime.datetime.now()
feat_array1 = np.random.rand(17000,512)
feat_array2 = np.random.rand(1,512)
z = cosine_similarity(feat_array1, Y=feat_array2)
toc = datetime.datetime.now()
delta = toc - tic

print('{}ms'.format(int(delta.total_seconds() * 1000)))

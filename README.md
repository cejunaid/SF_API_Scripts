<img src="https://sensusfuturis.com/images/logo.png" >
# SF_APIs
Scripts for using Sensus Futuris APIs

Please check the sample codes in scripts to call various Sensus Futuris APIs.

## Face Detection API - Version 1.0
Detect human faces in an image, return face rectangles. 
* Supported image types are JPG/ JPEG, PNG, WEBP, BMP.
* Max image file pixel size is 1000.
* Max file upload size is 2.5Mb. 

### Response 200
Json response containing list of face rectangles
```
{
    "face_locations": [
        [
        100,
        84,
        261,
        285
        ],
        [..]
    ]
}
```

The coordinates in face rectangle can be displayed as in the following example.

<p align="center">
  <img src="face_detector_result.png" alt="" width="650">
</p>

## Face Embedding API - Version 1.0
Detect human faces in an image, return face rectangles and embeddings against each detected face. 
* Supported image types are JPG/ JPEG, PNG, WEBP, BMP.
* Max image file pixel size is 1000.
* Max file upload size is 2.5Mb. 

### Response 200
Json response containing list of face rectangles and embeddings
```
{
    "face_locations": [
        [
        100,
        84,
        261,
        285
        ],
        [..]
    ],
    "face_embeddings": [
        [   
        -0.013276094570755959,
        0.004762198776006699,
        -0.014785194769501686,
        -0.04084409028291702,
        0.044945213943719864,
        0.03469116985797882,
        .
        .
        .
        ],
        [...]
    ]
}
```
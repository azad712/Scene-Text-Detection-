# Scene Text Generation

This project finds the text present in a video https://www.youtube.com/watch?v=_pHZqBQYRQ4&t=277s 
The video is divided processed into frames, and then each frame passes through a deep learning module
which is CRAFT (Character-Region Awareness For Text detection based) and I have used their pretrained model. After then easyOCR is used to extract text  and stored in excel sheet. Frame rate is 1 fps and I have included results only upto 504 frames.

In thi github repository, One result is shown in frame no. 199, input frame image is frame_199.jpeg,  image with bounding boxes is res_frame_199.jpg, bounding box coordinates is in image res_frame_199.txt, with it's correosponding output images of text recognition and cropped image of
that text recognition in res_bounding boxes 0.jpeg and res_bounding_boxes 1.jpeg. In the excel sheet file updated_extracted_text.xsls, entry number 666, has extracted shop name CHAIPOINT with corresponding entry and exit time stamps.

Since character recognition and matching task is difficult, so I have relaxed condition of character matching to
have matched first and last character and one character matching in between and have excluded common words like 
"in", "the", "floor", etc 

#  Challenges encountered :

Scene text detection is a difficult problem, it's challenging for text to be identified under blurry, occluded and 
lightening conditions. 

# Future scope 

1. There is shortage of scene text datasets, that needs to be created. Roboflow is one of the tools
 for manually annoatating datasets. https://roboflow.com/
2. New or novel Deep learning architecure can be developed especially for scene text recognition, along with traditional image processing techniques. CRAFT, CRNN and vision transformers
   are not fully accurate
3. For character recognition, new or novel deep learning models should be tried and experimented. Clustering techniques, semi supervised learning techniques can be given thought for further experimentation. 

# Video processing is present in file called Scene Text Generation Processing.ipynb

# Following is details from CRAFT 


# The project uses CRAFT based text detector
## https://github.com/clovaai/CRAFT-pytorch
## CRAFT: Character-Region Awareness For Text detection
Official Pytorch implementation of CRAFT text detector | [Paper](https://arxiv.org/abs/1904.01941) | [Pretrained Model](https://drive.google.com/open?id=1Jk4eGD7crsqCCg9C9VjCLkMN3ze8kutZ) | [Supplementary](https://youtu.be/HI8MzpY8KMI)

**[Youngmin Baek](mailto:youngmin.baek@navercorp.com), Bado Lee, Dongyoon Han, Sangdoo Yun, Hwalsuk Lee.**
 
Clova AI Research, NAVER Corp.


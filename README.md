# Scene Text Generation

This project finds the text present in a video https://www.youtube.com/watch?v=_pHZqBQYRQ4&t=277s 
The video is divided processed into frames, and then each frame passes through a deep learning module
which is CRAFT (Character-Region Awareness For Text detection based) and I have used their pretrained model. After then easyOCR is used to extract text  and stored in excel sheet. Frame rate is 1 fps and I have included results only upto 504 frames.

One result is shown in frame no. 199, image with bounding boxes is res_frame_199.jpg, bounding box coordinates is in image res_frame_199.txt, with it's correosponding output images of text recognition and cropped image of
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
3. For character recognition, new or novel deep learning models should be tried and experimented

# Video processing is present in file called Scene Text Generation Processing.ipynb

# Following is details from CRAFT 


# The project uses CRAFT based text detector
## https://github.com/clovaai/CRAFT-pytorch
## CRAFT: Character-Region Awareness For Text detection
Official Pytorch implementation of CRAFT text detector | [Paper](https://arxiv.org/abs/1904.01941) | [Pretrained Model](https://drive.google.com/open?id=1Jk4eGD7crsqCCg9C9VjCLkMN3ze8kutZ) | [Supplementary](https://youtu.be/HI8MzpY8KMI)

**[Youngmin Baek](mailto:youngmin.baek@navercorp.com), Bado Lee, Dongyoon Han, Sangdoo Yun, Hwalsuk Lee.**
 
Clova AI Research, NAVER Corp.

### Sample Results

### Overview
PyTorch implementation for CRAFT text detector that effectively detect text area by exploring each character region and affinity between characters. The bounding box of texts are obtained by simply finding minimum bounding rectangles on binary map after thresholding character region and affinity scores. 

<img width="1000" alt="teaser" src="./figures/craft_example.gif">

## Updates
**13 Jun, 2019**: Initial update
**20 Jul, 2019**: Added post-processing for polygon result
**28 Sep, 2019**: Added the trained model on IC15 and the link refiner


## Getting started
### Install dependencies
#### Requirements
- PyTorch>=0.4.1
- torchvision>=0.2.1
- opencv-python>=3.4.2
- check requiremtns.txt
```
pip install -r requirements.txt
```

### Training
The code for training is not included in this repository, and we cannot release the full training code for IP reason.


### Test instruction using pretrained model
- Download the trained models
 
 *Model name* | *Used datasets* | *Languages* | *Purpose* | *Model Link* |
 | :--- | :--- | :--- | :--- | :--- |
General | SynthText, IC13, IC17 | Eng + MLT | For general purpose | [Click](https://drive.google.com/open?id=1Jk4eGD7crsqCCg9C9VjCLkMN3ze8kutZ)
IC15 | SynthText, IC15 | Eng | For IC15 only | [Click](https://drive.google.com/open?id=1i2R7UIUqmkUtF0jv_3MXTqmQ_9wuAnLf)
LinkRefiner | CTW1500 | - | Used with the General Model | [Click](https://drive.google.com/open?id=1XSaFwBkOaFOdtk4Ane3DFyJGPRw6v5bO)

* Run with pretrained model
``` (with python 3.7)
python test.py --trained_model=[weightfile] --test_folder=[folder path to test images]
```

The result image and socre maps will be saved to `./result` by default.

### Arguments
* `--trained_model`: pretrained model
* `--text_threshold`: text confidence threshold
* `--low_text`: text low-bound score
* `--link_threshold`: link confidence threshold
* `--cuda`: use cuda for inference (default:True)
* `--canvas_size`: max image size for inference
* `--mag_ratio`: image magnification ratio
* `--poly`: enable polygon type result
* `--show_time`: show processing time
* `--test_folder`: folder path to input images
* `--refine`: use link refiner for sentense-level dataset
* `--refiner_model`: pretrained refiner model


## Links
- WebDemo : https://demo.ocr.clova.ai/
- Repo of recognition : https://github.com/clovaai/deep-text-recognition-benchmark

## Citation
```
@inproceedings{baek2019character,
  title={Character Region Awareness for Text Detection},
  author={Baek, Youngmin and Lee, Bado and Han, Dongyoon and Yun, Sangdoo and Lee, Hwalsuk},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={9365--9374},
  year={2019}
}
```

## License
```
Copyright (c) 2019-present NAVER Corp.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

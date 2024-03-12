# -*- coding: utf-8 -*-
import os
import numpy as np
import cv2
import imgproc
from PIL import Image

# borrowed from https://github.com/lengstrom/fast-style-transfer/blob/master/src/utils.py
def get_files(img_dir):
    imgs, masks, xmls = list_files(img_dir)
    return imgs, masks, xmls

def list_files(in_path):
    img_files = []
    mask_files = []
    gt_files = []
    for (dirpath, dirnames, filenames) in os.walk(in_path):
        for file in filenames:
            filename, ext = os.path.splitext(file)
            ext = str.lower(ext)
            if ext == '.jpg' or ext == '.jpeg' or ext == '.gif' or ext == '.png' or ext == '.pgm':
                img_files.append(os.path.join(dirpath, file))
            elif ext == '.bmp':
                mask_files.append(os.path.join(dirpath, file))
            elif ext == '.xml' or ext == '.gt' or ext == '.txt':
                gt_files.append(os.path.join(dirpath, file))
            elif ext == '.zip':
                continue
    # img_files.sort()
    # mask_files.sort()
    # gt_files.sort()
    return img_files, mask_files, gt_files

def saveResult(img_file, img, boxes, dirname='./result/', verticals=None, texts=None):
        """ save text detection result one by one
        Args:
            img_file (str): image file name
            img (array): raw image context
            boxes (array): array of result file
                Shape: [num_detections, 4] for BB output / [num_detections, 4] for QUAD output
        Return:
            None
        """
        img = np.array(img)
        #print("type of parameter boxes is ", type(boxes), " with the dimensions are ", boxes.shape)
        # make result file list
        filename, file_ext = os.path.splitext(os.path.basename(img_file))

        # result directory
        res_file = dirname + "res_" + filename + '.txt'
        res_img_file = dirname + "res_" + filename + '.jpg'

        print("res_img_file", res_img_file)

        if not os.path.isdir(dirname):
            os.mkdir(dirname)

        with open(res_file, 'w') as f:
            index  = 0
            # Specify the folder path
            #folder_path = dirname + "res_" + filename
            folder_path = dirname + "res_" + filename


            # Create the folder
            os.makedirs(folder_path, exist_ok=True)
            for i, box in enumerate(boxes):
                b = box
                #print("The box b is ", b)
                poly = np.array(box).astype(np.int32).reshape((-1))
                strResult = ','.join([str(p) for p in poly]) + '\r\n'
                f.write(strResult)

                poly = poly.reshape(-1, 2)
                #print("type of parameter box is ", type(box), " with the dimensions are ", box.shape)
                #print("type of poly is is ", type(poly), " with the dimensions are ", poly.shape)
                poly_res_img_file = "res_bounding_boxes " + str(index)  + '.jpg'
                path1 = os.path.join(folder_path, poly_res_img_file)
                #poly_res_img_file = path1 + "res_bounding_boxes " + str(index)  + '.jpg'
                #print(path1)
                #pil_image = Image.fromarray(poly)
                print("The cropped text save path is ", path1)
                # Now you can use pil_image for further processing or save it to a file
                #pil_image.save(pil_image)  # Example: save the image as PNG file
                #x_min, y_min = box[0]
                #x_max, y_max = box[1]
                #print(" x_min, y_min are", x_min, y_min)
                #print("x_max, y_max are ", x_max, y_max )

                # Convert the coordinates to integers
                b = np.int0(b)

                # Extract the bounding box region from the image
                x_min = np.absolute(np.min(b[:, 0]))
                x_max = np.absolute(np.max(b[:, 0]))
                y_min = np.absolute(np.min(b[:, 1]))
                y_max = np.absolute(np.max(b[:, 1]))
                #print("range for x is ", x_min, x_max)
                #print("range for y is ", y_min, y_max)
                cropped_image = img[int(y_min):int(y_max), int(x_min):int(x_max)]
                # Save result bb in an image
                #print("The type of cropped image is " , type(cropped_image))
                cv2.imwrite(path1, cropped_image)
                cv2.polylines(img, [poly.reshape((-1, 1, 2))], True, color=(0, 0, 255), thickness=2)
                ptColor = (0, 255, 255)
                if verticals is not None:
                    if verticals[i]:
                        ptColor = (255, 0, 0)

                if texts is not None:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    font_scale = 0.5
                    cv2.putText(img, "{}".format(texts[i]), (poly[0][0]+1, poly[0][1]+1), font, font_scale, (0, 0, 0), thickness=1)
                    cv2.putText(img, "{}".format(texts[i]), tuple(poly[0]), font, font_scale, (0, 255, 255), thickness=1)
                index +=1
        # Save result image
        cv2.imwrite(res_img_file, img)


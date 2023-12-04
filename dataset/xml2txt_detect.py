import xml.etree.ElementTree as ET
import pickle
import os
from os import listxattr, getcwd
from os.path import join
import glob

print("5")
classes = ['holothurian', 'echinus', 'scallop', 'starfish']


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_name):
    in_file = open('/home/xls1/桌面/train/label/train/' + image_name[:-3] + 'xml')
    out_file = open('/home/xls1/桌面/train/labels/train/' + image_name[:-3] + 'txt', 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            print(cls)
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


print("1")
wd = getcwd()
print("2")
if __name__ == '__main__':
    for image_path in glob.glob("/home/xls1/桌面/train/images/train/*.jpg"):
        image_name = image_path.split('/')[-1]

        convert_annotation(image_name)
        print("3")

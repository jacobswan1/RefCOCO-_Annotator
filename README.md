# RefCOCO+_Annotator
A image-level attributes (filling) annotation tool written in Python Tkinter. 
<p float="center">
  <img src="/GUI.png" width="250" />
</p>

## Dataset preparation:
We use the RefCOCO+ (https://github.com/lichengunc/refer) as our basic dataset which contains a comprehensive annotation on both instance level label, as well as attributes like: color, materials, locations and so forth. 

To prepare the dataset, download COCO train_2014 (http://cocodataset.org/#download) images in local and revise the "image_root" directory accordingly.

image_root = '/path/to/your/coco/train2014/images'

## Contents:
ca_annotations:<pre>Output dictionary h5py file <filename, attributes one-hot> </pre>

counterfactual_grounding:<pre> <filename, attribute tokens, bboxes> </pre>

counterfactual_grounding contains 1765 image names in COCO2014 train dataset, possible attribute tokens (extracted from coco caption), and the associated bounding boxes.

## Usage
1. Preparing the images and set the root directory.
2. Prepare the original annotation h5py file.
3. Run the scripy by: <pre>
python3 Annotator.py
</pre>

## How it works?
The ca_annotations is for storing the <image, attributes> pairs.

counterfactual_grounding got the validation/testing files from RefCOCO+ and their textual grounding annotations. For every new image, we select the attributes and store the <image, attributes> to ca_annotations file. In the same time the image from ca_annotations got removed. 

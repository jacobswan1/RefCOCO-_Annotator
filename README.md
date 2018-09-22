# RefCOCO+_Annotator
This script is for annotating the image-level attributes in RefCOCO+ dataset:
<p float="center">
  <img src="/GUI.png" width="250" />
</p>

## Dataset preparation:
We use the RefCOCO+ (https://github.com/lichengunc/refer) as our basic dataset which contains a comprehensive annotation on both instance level label, as well as attributes like: color, materials, locations and so forth. 

To prepare the dataset, download COCO train_2014 (http://cocodataset.org/#download) images in local and revise the "image_root" directory accordingly.

image_root = '/media/drive1/Data/refer/data/images'

## Files:
ca_annotations:<pre>Output dictionary h5py file <filename, attributes one-hot> </pre>

counterfactual_grounding:<pre> <filename, attributestokens, bboxes> </pre>

counterfactual_grounding contains 1765 image names in COCO2014 train dataset, possible attribute tokens (extracted from coco caption), and the associated bounding boxes.


## How it works?
The ca_annotations is for storing the <image, attributes> pairs.

counterfactual_grounding got the validation/testing files from RefCOCO+ and their textual grounding annotations. For every new image, we select the attributes and store the <image, attributes> to ca_annotations file. In the same time the image from ca_annotations got removed. 

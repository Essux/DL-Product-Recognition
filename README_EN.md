# Product identification for EAFIT's Warehousing Lab

## Description
Tool for product identification in EAFIT's Warehousing Lab. These products are dummy objects that are very similar between each other and given their size it is not possible to use barcodes. This software would therefore demonstrate product identification to replace barcodes. This project just contains the code for the training and construction of a neural network, the code of the web application that uses the model can be found [here](https://github.com/hamax97/Product-Recognition).

![prods_ex_2](/images/prods_ex_2.PNG?raw=true "prods_ex_2")

## Network Architecture
The selected architecture is based in *Inception v3* removing the top layers and initializing the weights with those of a pretrained network with the ImageNet dataset. At the top of the network, there is a dense layer of 100 neruons and a Softmax layer with 60 outputs.

![architecture](/images/arch.png?raw=true "architecture")

## Code Architecture
The code is divided in the components: Data processing, Preprocessing, Training and Postprocessing.

### Data processing
This module contains the scripts `preprocess` and `split_data`. `preprocess` resizes the images to a resolution of 299x299px and `split_data` splits the dataset in the directories `train`, `dev` y `test`.

### Preprocessing
Processing contains the code for the data generators used to train the model. The generator uses the following *Data augmentation* techniques:

* Rotation
* Shift
* Shear
* Zoom
* Horizontal and vertical flips

### Training
This module contains the model definition and training cycle. The cycle consists of 100 epochs with a *Learning Rate Decay* of 0.8 for every 5 iterations without improvement.

### Postprocessing
Used to process the vector obtained from the softmax layer and obtain the predicted class and the predicted image.

## Members
* Juan José Suarez Estrada - jsuare32@eafit.edu.co
* Juan Manuel Ciro Restrepo - jcirore@eafit.edu.co

## Caffe Hands on Tutorial by Jinfagang

> This caffe tutorial written by Jinfagang-Master in CSU, if you have any question about this post please contact me via WeChat: jintianiloveu ,if you repost this blog, please keep this original mark, thanks very much!

## Notes
the most important 3files
* caffe_path_gen.py
* caffe_create_lmdb.sh
* caffe_make_mean.sh

before using this 3 files please make sure this requirments:
1. You must have caffe build in your home path, that is you gonna have **~/caffe**
2. After get train.txt test.txt alongside the script directory, please **mkdir a data/** folder, and place your txts into it.
3. The caffe_path_gen.py must run with python3.+ type **python3** in your terminal not python
4. After you got train.txt replace your

## Download Data and Source Code:
I upload data to BaiduYun, you can download fome [here](https://pan.baidu.com/s/1eRJcRVO), and all source code you can get from my Github Repository [here](https://github.com/jinfagang/CaffeHandsOn.git), if you like this, you can just clik the star and give me some inspire!

## Part 1 Get Your Data First

**Step 1** Generate the image name file

Run caffe_path_gen.py in your terminal, just type:
```
python3 caffe_path_gen.py -train=/home/jfg/Documents/PythonSpace/caffe_cat_and_dog/image_data -shuffle=True
```
-shuffle is optional, because caffe can do this too.
In this tutorial we only have train data in image_data folder, we don't have test image, so we just generate the train image path, and manully divide them into train and test. But if you have test data folder, you also can type:
```
python3 caffe_path_gen.py -train=/home/jfg/Documents/PythonSpace/caffe_cat_and_dog/image_data_train -test=/home/jfg/Documents/PythonSpace/caffe_cat_and_dog/image_data_test -valid=/home/jfg/Documents/PythonSpace/caffe_cat_and_dog/image_data_valid

```
the valid data only generate image path without labels.
After this, you gonna have **train.txt**, **words.txt**.

**Step 2** Split train.txt into to train.txt and test.txt

**Before split please remove the path just make it like this:**
```
狗/34.jpg 1
猫/365.jpg 0
狗/119.jpg 1
猫/185.jpg 0
猫/112.jpg 0
猫/272.jpg 0
猫/366.jpg 0
猫/194.jpg 0
猫/213.jpg 0
猫/507.jpg 0
狗/396.jpg 1
猫/299.jpg 0
猫/264.jpg 0
猫/156.jpg 0
狗/427.jpg 1
狗/359.jpg 1
狗/458.jpg 1
狗/184.jpg 1
狗/435.jpg 1
猫/450.jpg 0
猫/400.jpg 0
狗/216.jpg 1
狗/258.jpg 1
猫/181.jpg 0
猫/40.jpg 0
```
But stay with the class prefix
OK, in this step, you gonna manully split train.txt into train and test, but this is very simple. just cut and paste into a test.txt file, and just do it, don't think too much.

**Step 3** Generate Caffe LMDB data file
First mkdir a `data` folder just inside the project directory, and place train.txt and test.txt into it.
And then open caffe_create_lmdb.sh and just edit the following two lines:
```
TRAIN_DATA_ROOT=/home/jfg/Documents/PythonSpace/caffe_cat_and_dog/image_data/
VAL_DATA_ROOT=/home/jfg/Documents/PythonSpace/caffe_cat_and_dog/image_data/
```
this two root it's your images original path, in this tutorial, we do not have valid data, so it's the same path, but it doesn't matter.This two line is suitable with your train and test file generate method.
If you have test data in another folder, make sure this two line is correctly direct into your image original position, otherwise caffe cannot find image.
**Simply edit two lines, leave other along.**
Then type:
```
bash caffe_create_lmdb.sh
```
Tip: Anything wrong, check you mkdir a data folder, and have train.txt and test.txt in it.
OK, after this, you gonna have two new folder in your data folder, that is:`caffe_train_lmdb` and `caffe_val_lmdb`, this is what we need to feed into caffe net and it is nothing with your original image anymore! It's complete and clean! Do not warry about path wrong anymore! Very nice!

**Step 4** Generate Mean Binary File
This step is very easy, don't change anything ,just type this in your terminal:
```
bash caffe_make_mean.sh
```
And you gonna have `caffe_mean.binaryproto` file in your data folder.

## Part 2 Get Your prototxt , It's simple!

After part 1 , you already have your data, just finish 80% work. 20% to go. Next, we gonna using solver folder. In this folder we have a solver.prototxt and a train_test.prototxt.
solver.prototxt is the net pramas setting file.
train_test.prototxt is the net structure setting file and your lmdb data feed into net in here.
```
layer {
  name: "cifar"
  type: "Data"
  top: "data"
  top: "label"
  include {
    phase: TRAIN
  }
  transform_param {
    mean_file: "/home/jfg/Documents/PythonSpace/caffe_cat_and_dog/data/caffe_mean.binaryproto"
  }
  data_param {
    source: "/home/jfg/Documents/PythonSpace/caffe_cat_and_dog/data/caffe_train_lmdb"
    batch_size: 100
    backend: LMDB
  }
}
layer {
  name: "cifar"
  type: "Data"
  top: "data"
  top: "label"
  include {
    phase: TEST
  }
  transform_param {
    mean_file: "/home/jfg/Documents/PythonSpace/caffe_cat_and_dog/data/caffe_mean.binaryproto"
  }
  data_param {
    source: "/home/jfg/Documents/PythonSpace/caffe_cat_and_dog/data/caffe_val_lmdb"
    batch_size: 100
    backend: LMDB
  }
}
```
This 2 layer is data feed layer, so you have to change your data path in here.Make sure it correct.
Open solver.prototxt, find this 2 and edit it:
```
net: "/home/jfg/Documents/PythonSpace/caffe_cat_and_dog/solver/cifar10_quick_train_test.prototxt"
snapshot_prefix: "/home/jfg/Documents/PythonSpace/caffe_cat_and_dog/model_snapshot/cifar10"

```
net: it is your train_test.prototxt file postion, snapshot_prefix is your save model path and prefix name, we place all saved models into a model_snapshot folder with prefix cifar10.

## Part 3 Train Your Data!
The rest is easy, just type:
```
bash train_caffenet.sh

```

## Part 4 Predict your image
 Last but not the least, try this in your terminal:
 ```
 caffe/build/examples/cpp_classification/classification.bin ~/Documents/PythonSpace/caffe_cat_and_dog/solver/caffenet_deploy.prototxt ~/Documents/PythonSpace/caffe_cat_and_dog/model_snapshot/caffenet_iter_16315.caffemodel ~/Documents/PythonSpace/caffe_cat_and_dog/data/caffe_mean.binaryproto ~/Documents/PythonSpace/caffe_cat_and_dog/words.txt ~/Pictures/dog.jpeg
 ```
 the params in order is: your deply.prototxt file, your caffemodel file, your mean binary file, your words.txt file, your image.
 deploy.protxt is the save net structure of train_val.prototxt, but with out train data announce.
 And the result could be this:
 ```
 0.55 'Cat 0'
 0.45 'Dog 1'
 ```

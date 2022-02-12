# Fruit recognition system

This *fruit recognition system* allows you to get information about different fruits in real time. You'll be provided with information about its **name** and **size**.

## Recognition system

This recognition system has been developed based on a simple **IA model** which has been extremely helpful when classifying different fruits. Such IA model was created by using [Teachable Machine](https://teachablemachine.withgoogle.com/), an online tool that allows you to create models by uploading a few photos of each class.

The result will be shown in the top left corner!

## Size

I'd like to point out that when it comes to computing the *size* of the piece of fruit, this system ensures **invariance** not only to rotation but to position and distance, as well. For that, we've used a **minimum rotated bounding box** (invariance to rotation) and an **Aruco marker** whose size is known (in this case 5x5 cm). If you want to give it a shot, you can find the Aruco marker that I've used on this repository.

![Aruco marker](./CVProject/Images/aruco.jpeg)

In the first place, the size will be computed in *pixels*. Nevertheless, the results are shown in *cm*.

### Installations required to measure objects with Aruco Marker

Not only do you have to install OpenCV, but we need to use a library called Contrib, too.

```bash
pip install opencv-contrib-python
```


## Installation and dependencies

The execution of this project calls for several packages you need to intall before getting it running.

### Numpy

If you use pip, you can install NumPy with:

```bash
pip install numpy
```

### Cv2

So as to install the main module:

```bash
pip install opencv-python
```
### cvzone

You can simply use pip:

```bash
pip install cvzone
```

## Usage

1.- In order to get it running, open up the *main.py* file and execute it.

2.- Subsequently, your webcam will be activated and a little window will show up to show you what the webcam is capturing.

3.- Set your webcam facing down so as to capture the fruit (I personally recommend you put the fruit on a piece of paper in blank to avoid different issues) and put the Aruco marker just next to it.

Here's an example:

![Aruco marker](./CVProject/Images/Screenshot_1.png)
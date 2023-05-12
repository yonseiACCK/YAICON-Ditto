<img src="https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/DITTO.png" width = "900" >


# DITTO: Doodle to Image Web Project

Team Members: 박지호, 박찬혁, 안정우, 이수민, 장윤호, 최정우

- This is [ControlNet](https://github.com/lllyasviel/ControlNet)(Latent Diffusion) Web Application Project
- Our model generates high quality Image from prompt guided Doodle.
- To enhance the Doodle to Image performance, we fine-tuned ControlNet using `SDU Caption` dataset.

~~ 시연 결과/영상


## 1. ControlNet

## Train
***Our goal is to generate high-quality image from even more doodling sketch.***<br/>
We trained preatrained scribble-to-image ControlNet.(epoch~~ time~~ ~~)

### Dataset
To train ControlNet on sketch control, caption, sketch and target image are required.  <br/>
We used `SBU Captions` dataset, which is large-scale dataset that contains 860K image-text pairs. <br/>

### Edge Detection
To obtain Doodle of the target image, we have tested several edge detectors. <br/>
We have chose [`PhotoSketch`](https://github.com/mtli/PhotoSketch), which was most human-like doodle.

<img src = "https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/edgedetect1.png" width = "800" align = "center">

## 2. Web


## How to Run

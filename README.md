# 11785 Project: Towards Improving Object Detection with End-to-End Transformers

Convolutional neural networks have been proven to be extremely effective for end-to-end object detection tasks. Lately, the onset of transformers has opened new dimensions in improving the performance of the existing object detection networks. Although the application of transformers has been in natural language processing predominantly, recent research works have suggested that they are capable of achieving comparable, if not better, performance on computer vision problems while requiring substantially smaller number of parameters. In this project, we will develop pure transformer networks by replacing traditional CNN backbone architecture with a visual transformer classifier in DETR for object detection and measure their effectiveness on popular large-scale datasets.

## Requirements
1. Python 3.6+
2. Pytorch 1.8+

# Run

To perform training and inference
```
!git clone https://github.com/tusharvatsa32/VisTransformers
```
```
runner
	- notebooks
		- DETR
			- run DETR_modified_train.ipyn 
```


## Performance of ViT vs ResNet

<img src="https://raw.githubusercontent.com/tusharvatsa32/VisTransformers/main/docs/plot1.jpeg" alt="drawing" width="400"/> <img src="https://raw.githubusercontent.com/tusharvatsa32/VisTransformers/main/docs/plot2.jpeg" alt="drawing" width="400"/>


## Team Members
1. Tushar Vatsa : tvatsa
2. Rituraj Singh: riturajs
3. Wallace Dalmet: wdalmet
4. Vivek Aswal: vaswal

### [FB DETR](https://github.com/facebookresearch/detr)







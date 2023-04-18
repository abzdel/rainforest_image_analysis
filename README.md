[![Makefile CI](https://github.com/abzdel/rainforest_image_analysis/actions/workflows/makefile.yml/badge.svg)](https://github.com/abzdel/rainforest_image_analysis/actions/workflows/makefile.yml)

# Algorithmic Rainforest Image Analysis
Sampling and algorithmic analysis of rainforest drone videos. For Rainforest Engineering class at Duke University.

# Architectural Diagram - Frame Sampling
![frame sampling program drawio](https://user-images.githubusercontent.com/55398496/232870522-3984e84a-da30-4487-9fdc-be6cbdaf7c63.png)


# Architectural Diagram - Clustering

![color segmentation diagram drawio](https://user-images.githubusercontent.com/55398496/232870532-bed17fa2-62d4-499f-9ba4-86d59b974ad8.png)


# How to Run the App

1) Clone the repo
```python
git clone https://github.com/abzdel/rainforest_image_analysis.git
```
2) Setup - Install the required packages
```python
make install
```
3) Run the application

We can run the sampling + segmentation steps in one invocation by calling the *sample_and_segment* bash script.
```python
chmod +x sample_and_segment.sh
sample_and_segment.sh {video or folder of videos}
```

Alternatively, if we only want to sample frames, we only need to run *sample_frames.py*
```python
python sample_frames.py {video or folder of videos}
```

Or, if we only want to run clustering on our already sampled frames
```python
python clustering.py {path to image or folder of images}
```

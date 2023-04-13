# rainforest_image_analysis
Sampling and algorithmic analysis of rainforest drone videos. For Rainforest Engineering class at Duke University.


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
python clustering.py {path to image}
```


<br>
After this, we simply select the matchup we want and get our predicted total score (score from both teams combined)

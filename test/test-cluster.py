import os
import sys


def test_incorrect_path():
    # assert that the output of "python sample_frames.py" is "Incorrect number of arguments"
    assert os.system("python clustering.py") != 0, "incorrect number of arguments"


def test_incorrect_path_mp4():
    assert (
        os.system("python clustering.py short-vid-demo.mp4") != 0
    ), "should not work with mp4 files that exist"


def test_correct_folder():
    assert (
        os.system("python clustering.py results-test") == 0
    ), "should work with folder that exists"


def test_correct_file():
    assert (
        os.system("python clustering.py results-test/framesshort-vid-demo/frame_0.jpg")
        == 0
    ), "should work with jpg files that exist"

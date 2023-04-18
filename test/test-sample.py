import os
import sys


def test_incorrect_path():
    # assert that the output of "python sample_frames.py" is "Incorrect number of arguments"
    assert os.system("python sample_frames.py") == 1, "incorrect number of arguments"


def test_file_not_exists():
    assert (
        os.system("python sample_frames.py not_exist.jpg") == 1
    ), "file should not exist"


def test_wrong_filetype():
    assert (
        os.system("python sample_frames.py results-test/frame_0.txt") == 1
    ), "file should not be a txt"


def test_correct_folder():
    assert (
        os.system("python sample_frames.py short-vid-demo.mp4") == 0
    ), "should work with mp4 files that exist"


def test_mp4_not_exist():
    assert (
        os.system("python sample_frames.py not_exist.mp4") == 1
    ), "should not work with mp4 files that don't exist"

import os
import sys
import cv2


def get_filetype(filename):
    """Determines the type of a given file
    If the file is a video, it returns the video type
    If the file is a directory, it returns dir"""

    if os.path.isdir(filename):
        return "dir"
    elif os.path.isfile(filename):
        # split filename then return after .
        filename_tuple = os.path.splitext(filename)
        return filename_tuple[1].lower()
    else:
        return None


def get_video_info(video):
    """Returns a tuple of video info
    (fps, width, height)"""
    fps = video.get(cv2.CAP_PROP_FPS)
    return fps


def sample_video(video, filename, sample_rate=2, start_min=0, start_sec=0):
    """Samples a video file at a given sample rate
    Returns a list of frames"""
    fps = get_video_info(video)
    frame_id = int(fps * (start_min * 60 + start_sec))

    spaced_frames = []
    initial_frame = frame_id

    # calculate total frames
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # create loop to get entire video's frames
    it = 0
    while True:
        new_frame = initial_frame + it * (
            fps * sample_rate
        )  # save a frame every sample_rate seconds
        spaced_frames.append(int(new_frame))

        it += 1
        # check to see if we've reached the end of the video
        if new_frame > total_frames:
            break

    # save spaced_frames to local dir
    for f_num in spaced_frames:
        # check if we've reached the end of the video
        # may occasionally go past the end of the video on edge cases
        # instead of fixing it, I'm just adding another conditional :(
        if f_num > total_frames:
            break

        print(f"saving frame {f_num} from {filename}")
        video.set(cv2.CAP_PROP_POS_FRAMES, f_num)
        ret, frame = video.read()

        # if folder doesnt exist, create it
        if not os.path.exists(f"results/frames{filename[:-4]}"):
            os.makedirs(f"results/frames{filename[:-4]}")

        # make sure to make new dir for each experiment
        cv2.imwrite(
            f"results/frames{filename[:-4]}/frame_{f_num}.jpg",
            frame,
        )
    print(f"frames successfully sampled from {filename}")


def process_folder(dirname):
    """Processes a folder of videos
    Saves each image to a new folder"""
    # count records of videos in dirname
    for i, filename in enumerate(os.listdir(dirname)):
        # get filetype
        filetype = get_filetype(filename)

        # if video, process it
        if filetype == ".mp4":
            # load in video
            video = cv2.VideoCapture(filename)
            sample_video(
                video,
                filename,
                sample_rate=2,
                start_min=0,
                start_sec=0,
            )


if __name__ == "__main__":
    # two args - filename and which code we want to run (ruchas stem code or clustering)
    # later - add functionality to point at a folder. helper functions for this are already made

    if len(sys.argv) != 2:
        print("Incorrect number of arguments")
        sys.exit(1)

    # If a file is passed as an argument, get the file type. Will help us know what to do with the file
    if sys.argv[1]:
        filetype = get_filetype(sys.argv[1])

        if filetype is None:
            print("File does not exist or file of wrong type passed")
            sys.exit(1)

        # if no results folder, create it
        if not os.path.exists("results"):
            os.makedirs("results")

        print(sys.argv[1])  # debug
        print(filetype)  # debug

        # if file is single video, process it
        if filetype == ".mp4":
            video = cv2.VideoCapture(sys.argv[1])
            sample_video(video, sys.argv[1], sample_rate=2, start_min=0, start_sec=0)

        if filetype == "dir":
            process_folder(sys.argv[1])

    # Get the file type
    # filetype = get_filetype("frames")
    # print(filetype)

# take command line input
path=$1

echo "path is $path"


# pass this path to sample_frames.py
python sample_frames.py $path

# pass every file in the results subfolders to clustering.py
find results/ -mindepth 2 -type f -exec python clustering.py {} \;

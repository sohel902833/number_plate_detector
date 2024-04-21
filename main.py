
import util
from util import write_csv,delete_file_if_exists
from add_missing_data import  add_missing_data_into_csv
from visualize import  generate_video_from_csv
from csv_generator import  generate_frame_as_csv
import os


def play_video(video_path):
    try:
        # Get the operating system
        operating_system = os.name

        # Open the video file with the default application based on the OS
        if operating_system == 'nt':  # Windows
            os.system(f'start "" "{video_path}"')
        elif operating_system == 'posix':  # Linux or macOS
            os.system(f'xdg-open "{video_path}"')
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print(f"Error: {e}")
def _start(open_video=False,generate_for_frame=None):
    #input and output locations
    generate_video_for_frame =generate_for_frame;
    csvFileLocation = "./output/test.csv"
    interpolatedFileLocation = "./output/test_modified.csv"
    outputVideoFile = "./output/with_marking.mp4"
    inputVideoFile = "./sample.mp4"
    #input and output locations end

    #generate frame for csv
    #delete previous generated files
    print("Deleting Previously Generated Data....")
    delete_file_if_exists(csvFileLocation)
    delete_file_if_exists(interpolatedFileLocation)
    delete_file_if_exists(outputVideoFile)
    print("Deleting Completed Previously Generated Data....")

    print("Generating CSV From Frames...........")
    results=generate_frame_as_csv(generate_video_for_frame,inputVideoFile)
    print("CSV Generation Completed Successfully From Frames...........")
    print("Writing Results Into CSV File...........")
    # write results
    write_csv(results, csvFileLocation)
    print("CSV File Result Writing Completed...........")


    print("Adding Missing Data Into Csv File And Creating Brand New One...........")
    #interpolation of values to match up for the missing frames and smooth output
    add_missing_data_into_csv(csvFileLocation,interpolatedFileLocation)
    print("Modified Version of csv is generated..........")

    print("Generating Video From CSV..........")
    #generate video with marking the number palates from csv
    generate_video_from_csv(generate_video_for_frame,interpolatedFileLocation,inputVideoFile,outputVideoFile)
    print("Video Generation Completed..........")
    if open_video:
        play_video(outputVideoFile)



_start(True,40)

from utils.video_utils import read_video, save_video, detect_vehicles
from model.objectTracker.tracker import Tracker


def main():
    frames = read_video("dataset/videoData/2303099-uhd_2560_1440_30fps.mp4")

    track = Tracker()
    result = track.process_video(frames)

if __name__ == '__main__':
    main()

# utils/__init__.py
if __name__ == "__main__":
    from video_utils import read_video
    from video_utils import save_video
    from video_utils import detect_vehicles
    from utils import write_csv
    from utils import license_complies_format
    from utils import format_license
    from utils import get_car

else:
    from .video_utils import read_video
    from .video_utils import save_video
    from .video_utils import detect_vehicles
    from .utils import write_csv
    from .utils import license_complies_format
    from .utils import format_license
    from .utils import get_car

# 🚦 ANPR and ATCC for Smart Traffic Management

## 🧑‍💻 Project Overview
This project implements an intelligent traffic management system utilizing Automatic Number Plate Recognition (ANPR) and Automatic Traffic Classification and Control (ATCC). By leveraging Deep Learning and Object Detection techniques, the system automates traffic monitoring and control in smart city environments.

### Key Features
- 📝 Automatic Number Plate Recognition (ANPR)
- 🚦 Automatic Traffic Classification and Control (ATCC)
- 📊 Data interpolation for accurate tracking
- 📈 Visualization capabilities

### Results
- you can checkout the results by using this link [click here](https://drive.google.com/file/d/1ZrEksJ87AzWtnCYuIVE8WAEb3p6m1VFQ/view?usp=sharing)


<p align="center">
  <img src="output/main.gif" alt="Demo GIF" />
</p>

## 📂 Project Structure
```
├── CV_Basics/                              # Computer vision and OCR learning materials
├── internship_artifacts/                   #agile reports
├── Testing                                 # all the methods and procedures we tried as a part of the project
├── model/object_tracker/                   # Main detection and vehicle tracking code
├── number_plate_detection_model_training/  # Model training files
├── output/                                 # Generated result videos
├── results/                                # Initial detection CSV files
├── utils/                                  # Scripts for video and data processing
├── .gitignore                              # Git ignore rules
├── add_missing_data.py                     # Data interpolation script
├── main.py                                 # Main execution file
├── requirements.txt                        # Project dependencies
└── visualize.py                            # Video visualization script
```

##  Workflow
Execute `main.py` to perform vehicle detection and generate CSV file in `results/` directory .
 It performs data interpolation and generate enhanced CSV file in `results/` directory
. It create visualization video using interpolated data, saved in `output/` directory


while the output video is creating it autoplay the video on your screen before completion.

## 🛠️ Setup and Installation
1. Clone the repository:
```bash
    git clone git@github.com:udaykirankoruvada/ANPR-and-ATCC-for-Smart-Traffic-Management.git
    cd ANPR-and-ATCC-for-Smart-Traffic-Management
```

2. Create and activate virtual environment (recommended):
```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
  pip install -r requirements.txt
```


## 🏃‍♀️ Running the Project


1. Replace the path to your input video and your desired output directory.

2. Run the main detection:
```bash
  python main.py
```

### 🪪 LICENSE 
ANPR and ATCC for Smart Traffic Management is released under the [MIT License](LICENSE), allowing you to freely use, modify, and distribute the project.


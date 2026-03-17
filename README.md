# Programming-for-Psyc-Lecture-7-HW
Repository for Lecture 7 Homework

# Go/No-Go Task: Food-Specific Response Inhibition

## Description
This repository contains a Python script (`gonogo.py`) that runs a behavioral Go/No-Go task implemented in PsychoPy. It is adapted from the protocol by Price et al. (2016) for an anorexia nervosa intervention. 

The task consists of 50 trials (40 "Go" trials and 10 "No-Go" trials). Participants are presented with images of high-fat (HF) and low-fat (LF) foods paired with a colored dot:
* **Green Dot (Go):** Indicates a low-fat food trial. Participants must press the spacebar as quickly as possible.
* **Red Dot (No-Go):** Indicates a high-fat food trial. Participants must withhold their response and not press any key.

Each trial consists of a fixation cross (500 ms), the food image and cue (750 ms), and a blank screen (500 ms). 

## Modifications for Assignment
As per the assignment requirements, the following features are included:
1. **Instructions:** Added an initial text screen explaining the task rules and visual cues to the participant before the trials began.
2. **Visual Cues:** Implemented green and red dot stimuli overlaid on the food images to cue the participant on whether to make or withhold a response.

## Files Included
* `gonogo.py`: The main Python script to run the experiment.
* `HF_LF_60.csv`: The spreadsheet containing the trial information, food image filenames, and fat content categorization (1 = HF, 0 = LF).
* `stimuli copy/`: A folder containing the image files used during the task.

## Prerequisites
To run this task, you need to have Python installed along with the following libraries:
* `psychopy`
* `pandas`

## How to Run
1. Download all files and keep them in the same directory.
2. Run `gonogo.py` using your preferred Python IDE (like the PsychoPy Coder) or via the terminal.
3. A dialogue box will appear asking for the participant's number and age.
4. Follow the on-screen instructions to complete the task.
5. The data (responses, reaction times, and accuracy) will automatically save as a new CSV file named `[participant_nr]_gonogo.csv` in your folder.

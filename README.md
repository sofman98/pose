# pose
Real-time Hand Pose Recognition and Dataset Generation With Mediapipe

NOTE: 
The GPU was used to predict and generate the dataset because it is much faster, the CPU version was almost unusable, a GPU is needed.


INSTALLATION:
- Follow the mediapipe installation tutorial for Ubuntu on:
https://github.com/google/mediapipe/blob/master/mediapipe/docs/install.md#installing-on-debian-and-ubuntu
- merge the mediapipe folder with the installation folder and choose to replace the existing files when asked.

HOW TO GENERATE THE DATASET:
- cd into the installation folder:
$cd mediapipe

- Build the program with:
$bazel build -c opt --copt -DMESA_EGL_NO_X11_HEADERS mediapipe/examples/desktop/hand_tracking:hand_tracking_out_gpu

- Run the program:
$bazel-bin/mediapipe/examples/desktop/hand_tracking/hand_tracking_out_gpu --	calculator_graph_config_file=mediapipe/graphs/hand_tracking/hand_tracking_desktop_live.pbtxt

- Run Landmarks_classification/dataset_managing.py in order to process the data

HOW TO TRAIN SVM:
- Run Landmarks_classification/train.py


HOW TO PREDICT:
- Build the program with:
$bazel build -c opt --copt -DMESA_EGL_NO_X11_HEADERS mediapipe/examples/desktop/hand_tracking:hand_tracking_predict_gpu

- Run the program:
$bazel-bin/mediapipe/examples/desktop/hand_tracking/hand_tracking_predict_gpu --calculator_graph_config_file=mediapipe/graphs/hand_tracking/hand_tracking_desktop_live.pbtxt

- Run Landmarks_classification/predict.py

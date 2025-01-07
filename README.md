# mosquito_classification

## Running
First, build the docker file with ```sudo docker build -t mosquito_classification .``` 
Using the super user is necessary to correctly use the `nvidia-docker-toolkit`.

To run the trainig process use ```sudo docker run --gpus all -v <absolute/path/to/trainings/dir>:/workspace/training -v /tmp/.X11-unix/:/tmp/.X11-unix:rw mosquito_classification train ARGS```.
`train` is just a macro to execute `mmpretrain` train.py script, so the arguments behave the same as mmpretrain scripts.
The first volume binding is conveniently used as working directory for the training process.

To use any scripts that launch GUI windows, it's necessary to run ```xhost +``` on the host machine.

Other implemented macros are for `confusion_matrix`, `browse_dataset`, `test`, and `analyze_logs`.

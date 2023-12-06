from yolov5.detect import detect_object
from real_stream import track_noise
from head_pose import pose
from object_with_headpose import pose_1
from multiprocessing.context import Process

windows_object_process = None
windows_noise_process = None
windows_head_process = None
windows_head_object_process = None 



def start_object_tracking_process():
    global windows_object_process
    windows_object_process = Process(target=detect_object)
    windows_object_process.start()

def start_noise_tracking_process():
    global windows_noise_process
    windows_noise_process = Process(target=track_noise)
    windows_noise_process.start()

def start_head_and_eye_tracking_process():
    global windows_head_process
    windows_head_process = Process(target=pose)
    windows_head_process.start()

def start_head_object_process():
    global windows_head_object_process
    windows_head_object_process = Process(target= pose_1)
    windows_head_object_process.start()

def start_proctoring_processes():
    start_head_object_process()
    start_noise_tracking_process()    
def stop_processes():
    global windows_object_process, windows_head_object_process, windows_noise_process, windows_head_process
    if windows_object_process:
        windows_object_process.terminate()
        windows_object_process.join()
        windows_object_process = None
    if windows_noise_process:
        windows_noise_process.terminate()
        windows_noise_process.join()
        windows_noise_process = None
    if windows_head_object_process:
        windows_head_object_process.terminate()
        windows_head_object_process.join()
        windows_head_object_process = None 
    if windows_head_process:
        windows_head_process.terminate()
        windows_head_process.join()
        windows_head_process = None 

from django.shortcuts import render
from django.http import HttpResponse
import json
from start_stop import start_head_and_eye_tracking_process,start_noise_tracking_process
from start_stop import start_object_tracking_process,start_proctoring_processes
from start_stop import stop_processes
def index_view(request):
    return render(request, 'online_proctoring/index.html')
def ai_proctoring(request):
    start_proctoring_processes()
    return render(request, 'online_proctoring/ai_proct.html')


def detect_noise(request):
    start_noise_tracking_process()
    return render(request, 'online_proctoring/nosie_rec.html')

def detect_object_y5(request):
    start_object_tracking_process()
    return render(request, 'online_proctoring/obj_trac.html')   

def head_and_eye(request):
    start_head_and_eye_tracking_process()
    return render(request, 'online_proctoring/head_eye_tracking.html')

def object_tracked(request):
    with open('objects_detected.json', 'r') as json_file:
        data = json.load(json_file)        
    context = {
        'data': data,
    }
    return render(request, 'online_proctoring/object_tracking.html',context)


def noise_tracking(request):
    # Read JSON data from the file
    with open('noise_data.json', 'r') as json_file:
        data = json.load(json_file)

    # Pass the data to the template
    return render(request, 'online_proctoring/noise_tracking.html', {'data': data})

def noise_plot(request):
    # You don't need to pass any data to this view.
    return render(request, 'online_proctoring/noise_plot.html')

def stop_process(request):
    stop_processes()
    return render(request, 'online_proctoring/index.html')

def head_nose_tracked(request):
    with open('head_pose_data.json', 'r') as json_file:
        data = json.load(json_file)        
    context = {
        'data': data,
    }
    return render(request, 'online_proctoring/head_pose_trac.html',context)
    


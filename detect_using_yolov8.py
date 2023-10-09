from ultralytics import YOLO

model = YOLO('yolov8n.pt')
def object_detect_v8():
    model.predict(source=0, show =True) 


# changes to do in result.py at line 271

# time_stamp = time.strftime('%m/%d/%y %H:%M:%S', time.localtime())
# data[time_stamp] = log_string
# # objects_detect.append(data)
# with open('objects_detected_yv8.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)
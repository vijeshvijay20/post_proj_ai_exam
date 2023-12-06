import argparse
import csv
import os
import sys
from pathlib import Path
import cv2

import torch
from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_requirements, non_max_suppression, scale_coords
from utils.plots import plot_one_box

model = None
weights = 'yolov5s.pt'  # Path to yolov5s.pt
device = 'cpu'  # Choose 'cpu' or '0' for GPU

# Function to perform YOLOv5 object detection on an image
def detect_object(source, save_csv=False):
    img_size = 640  # Inference size (height, width)
    iou_thres = 0.45  # NMS IoU threshold
    conf_thres = 0.25  # Confidence threshold
    max_det = 1000  # Maximum detections per image

    img = torch.zeros((1, 3, img_size, img_size), device=device)  # Create an empty image tensor

    # Capture video from webcam (source = 0)
    cap = cv2.VideoCapture(source)

    while True:
        ret, frame = cap.read()  # Read a frame from the webcam

        if not ret:
            break

        # Load and preprocess the frame
        img0 = frame  # Use the captured frame
        img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        img0 = img0.transpose(2, 0, 1)  # Transpose to CHW format
        img0 = torch.from_numpy(img0).to(device)  # Convert to tensor
        img0 = img0.float() / 255.0  # Normalize

        img[0] = img0  # Set image tensor

        # Run inference
        pred = model(img)  # Get predictions

        # Apply non-maximum suppression
        pred = non_max_suppression(pred, conf_thres, iou_thres, max_det=max_det)

        # Process and save results
        if save_csv:
            save_path = 'detections.csv'
            with open(save_path, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Class', 'Confidence', 'XMin', 'YMin', 'XMax', 'YMax'])  # Write header

                for det in pred[0]:  # Iterate through detections
                    if det is not None and len(det):
                        det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img0.shape).round()  # Rescale coordinates
                        for *xyxy, conf, cls in reversed(det):
                            xyxy = [int(val) for val in xyxy]
                            writer.writerow([model.names[int(cls)], f'{conf:.2f}', *xyxy])  # Write detection info

        # Visualize detections (optional)
        for det in pred[0]:  # Iterate through detections
            if det is not None and len(det):
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img0.shape).round()  # Rescale coordinates
                for *xyxy, conf, cls in reversed(det):
                    label = f'{model.names[int(cls)]} {conf:.2f}'
                    plot_one_box(xyxy, img0, label=label, color=(0, 255, 0), line_thickness=3)

        # Display the image with detections (optional)
        cv2.imshow('Result', img0)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Call the detect_object function with webcam as the source
detect_object(source=0, save_csv=True)

import os
import pyaudio
import librosa
import numpy as np
import matplotlib.pyplot as plt
import keras
import json
import time
import yamnet.params as params
import yamnet.yamnet as yamnet_model


def empty_data_json():
    if os.path.exists('data.json'):
        with open('data.json', 'w') as json_file:
            json.dump([], json_file)
            print("Emptied data.json.")

def track_noise():
    empty_data_json()
    start =True
    data_list = []
    noice_dectected={}
    yamnet = yamnet_model.yamnet_frames_model(params)
    yamnet.load_weights('yamnet/yamnet.h5')
    yamnet_classes = yamnet_model.class_names('yamnet/yamnet_class_map.csv')
    frame_len = int(params.SAMPLE_RATE * 10)  # 1sec
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=params.SAMPLE_RATE,
                    input=True,
                    frames_per_buffer=frame_len)
    cnt = 0
    try:
        while start:
            # data read
            data = stream.read(frame_len, exception_on_overflow=False)

            # byte --> float
            frame_data = librosa.util.buf_to_float(data, n_bytes=2, dtype=np.int16)

            # model prediction
            scores, melspec = yamnet.predict(np.reshape(frame_data, [1, -1]), steps=1)
            prediction = np.mean(scores, axis=0)

            top5_i = np.argsort(prediction)[::-1][:5]
            plt.imshow(melspec.T, cmap='jet', aspect='auto', origin='lower')
            plt.savefig('static/mel_spectrogram.png')
            # Append data to the list
            data_list.append('Current event:\n' + '\n'.join('  {:12s}: {:.3f}'.format(yamnet_classes[i], prediction[i])
                    for i in top5_i))
            time_stamp = time.strftime('%m/%d/%y %H:%M:%S', time.localtime())
            noice_dectected[time_stamp]=data_list    
            with open('noise_data.json', 'w') as json_file:
                json.dump(noice_dectected, json_file, indent=4)
                print("Data saved to JSON.")

            # print(cnt)
            cnt += 1
    except KeyboardInterrupt:
        pass
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
# track_noise()


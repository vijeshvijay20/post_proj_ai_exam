{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6374e0d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Copyright 2019 The TensorFlow Authors All Rights Reserved.\n",
    "#\n",
    "# Licensed under the Apache License, Version 2.0 (the \"License\");\n",
    "# you may not use this file except in compliance with the License.\n",
    "# You may obtain a copy of the License at\n",
    "#\n",
    "#     http://www.apache.org/licenses/LICENSE-2.0\n",
    "#\n",
    "# Unless required by applicable law or agreed to in writing, software\n",
    "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
    "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
    "# See the License for the specific language governing permissions and\n",
    "# limitations under the License.\n",
    "# ==============================================================================\n",
    "\n",
    "\"\"\"Hyperparameters for YAMNet.\"\"\"\n",
    "\n",
    "# The following hyperparameters (except PATCH_HOP_SECONDS) were used to train YAMNet,\n",
    "# so expect some variability in performance if you change these. The patch hop can\n",
    "# be changed arbitrarily: a smaller hop should give you more patches from the same\n",
    "# clip and possibly better performance at a larger computational cost.\n",
    "SAMPLE_RATE = 16000\n",
    "STFT_WINDOW_SECONDS = 0.025\n",
    "STFT_HOP_SECONDS = 0.010\n",
    "MEL_BANDS = 64\n",
    "MEL_MIN_HZ = 125\n",
    "MEL_MAX_HZ = 7500\n",
    "LOG_OFFSET = 0.001\n",
    "PATCH_WINDOW_SECONDS = 0.96\n",
    "PATCH_HOP_SECONDS = 0.48\n",
    "\n",
    "PATCH_FRAMES = int(round(PATCH_WINDOW_SECONDS / STFT_HOP_SECONDS))\n",
    "PATCH_BANDS = MEL_BANDS\n",
    "NUM_CLASSES = 521\n",
    "CONV_PADDING = 'same'\n",
    "BATCHNORM_CENTER = True\n",
    "BATCHNORM_SCALE = False\n",
    "BATCHNORM_EPSILON = 1e-4\n",
    "CLASSIFIER_ACTIVATION = 'sigmoid'\n",
    "\n",
    "FEATURES_LAYER_NAME = 'features'\n",
    "EXAMPLE_PREDICTIONS_LAYER_NAME = 'predictions'"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

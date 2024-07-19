# yaapt.torch

Implementation of the YAAPT pitch tracker in PyTorch.  
This version relies solely on PyTorch, does not hog all CPU threads (making it possible to use in a dataloader),
is torch.jit-able, and is batch compatible.

### Setup

For using (no development required)

```bash
pip install yaapt.torch
```

To install for development, clone the repository, and then run the following from
within the root directory.

```bash
pip install -e .
``` 

### Usage

```python
import torchaudio, yaapt_torch
audio, sr = torchaudio.load("audio.wav")

yaapt_opts = {
    "sr": sr,
    "frame_length": 35.0,
    "frame_space": 20.0,
    "nccf_thresh1": 0.25,
    "tda_frame_length": 25.0,
}

pitch = yaapt_torch.yaapt(
    audio, # (Batch, feature) torch.tensor input
    yaapt_opts,
)
print(pitch) # (Batch, F0) torch.tensor output
```

### Credits

* The original NumPy/SciPy/Python program was written by Bernardo Jose B. (https://github.com/bjbschmitt).
* The original MATLAB program was written by Hongbing Hu and Stephen A. Zahorian (http://www.ws.binghamton.edu/zahorian/yaapt.htm).

This repository aims to wrap up these implementations in easy-installable PyPi
packages, which can be used directly in PyTorch based neural network training.

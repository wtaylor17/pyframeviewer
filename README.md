# pyframeviewer
navigate the frames of a video using matplotlib and imageio

# Usage
First run `pip install .` (after cloning) or `pip install git+https://github.com/wtaylor17/pyframeviewer.git` (without cloning). To run the program, do the following:

```
python -m frame_viewer <path-to-video>
```

To use the package programmatically, import the `launch_viewer` function:

```python
from frame_viewer.__main__ import launch_viewer
```

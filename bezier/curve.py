from typing import List
from lg.vector import Vector2

def calc_curve(controls: List[Vector2], steps: int) -> List[Vector2]:
    step_length = 1 / steps
    # get the total number of control points we have
    n = len(controls)
    t = 0
    qs = []

    while t <= 1:
        ms = controls
        num_segments = n - 1
        while num_segments > 0:
            temp_ms = []
            for i in range(len(ms) - 1):
                m =  ms[i] * t +  ms[i + 1] * (1 - t)
                temp_ms.append(m)
            num_segments -= 1
            ms = temp_ms
        t += step_length
        qs.append((ms[0].x, ms[0].y))
    
    return qs
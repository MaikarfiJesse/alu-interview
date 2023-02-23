#!/usr/bin/python3
""" Calculating how many square units of water will be retained after it rains 
given a list of non-negative integers represent the heights of walls with unit 
width 1 as if viewing the cross-section of a relief map
"""

def rain(walls):
    """Documentation"""
     n = len(walls)
        left_max = [0] * n
        right_max = [0] * n
        water = 0

    # Find the highest wall on the left side of each wall
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i-1])

    # Find the highest wall on the right side of each wall
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i+1])

    # Calculate the amount of water retained 
    for i in range(1, n-1):
        diff = min(left_max[i], right_max[i]) - walls[i]
        if diff > 0:
            water += diff
    
    return water

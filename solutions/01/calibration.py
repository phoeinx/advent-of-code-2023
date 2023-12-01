from sys import stdin 
import re

calibration_sum = 0
for line in stdin:
    nums = re.findall(r'\d', line)
    calibration_sum += int(f"{nums[0]}{nums[-1]}")
print(calibration_sum)
from sys import stdin 
import re

digit_dict = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}

calibration_sum = 0
for line in stdin:
    #find overlapping matches using lookahead and matching the zero length string before each found lookahead group
    nums = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    nums = [digit_dict[num] if num in digit_dict else num for num in nums]
    calibration_sum += int(f"{nums[0]}{nums[-1]}")
print(calibration_sum)
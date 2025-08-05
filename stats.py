import math

def calculateStats(numbers):
  Stats = {}
  numbers_wihout_nan = [num for num in numbers if not math.isnan(num)]
  if numbers_wihout_nan:
    Stats["avg"] = sum(numbers_wihout_nan)/len(numbers_wihout_nan)
    Stats["max"] = max(numbers_wihout_nan)
    Stats["min"] = min(numbers_wihout_nan)
  else:
    Stats["avg"] = float('nan')
    Stats["max"] = float('nan')
    Stats["min"] = float('nan')
  return Stats

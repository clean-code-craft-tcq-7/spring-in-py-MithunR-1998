import math
def remove_absurd_value(numbers):
  final_list = []
  for i in numbers:
    if i>=0 and i <=200:
      final_list.append(i)
  return final_list

def calculateStats(numbers):
  Stats = {}
  numbers_wihout_nan = [num for num in numbers if not math.isnan(num)]
  final_list_no_absurd = []
  final_list_no_absurd = remove_absurd_value(numbers_wihout_nan)
  if final_list_no_absurd:
    Stats["avg"] = sum(final_list_no_absurd)/len(final_list_no_absurd)
    Stats["max"] = max(final_list_no_absurd)
    Stats["min"] = min(final_list_no_absurd)
  else:
    Stats["avg"] = float('nan')
    Stats["max"] = float('nan')
    Stats["min"] = float('nan')
  return Stats

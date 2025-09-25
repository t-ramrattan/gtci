def string_to_int_list(input):
  nums = []
  vals = input.split(',')
  for val in vals:
    nums.append(int(val))
  return nums

def minimum_number_of_train_platforms(inputs: list, outputs: list):
  input_index = 1
  output_index = 0
  counter = 1
  max_counter = counter
  for i in range(1, len(inputs)):
    if outputs[output_index] > inputs[input_index]:
      counter += 1
      input_index += 1
    else:
      counter -= 1
      output_index += 1

    if max_counter < counter:
      max_counter = counter
  
  return max_counter


inputs = sorted(list(map(float, input().split(", "))))
outputs = sorted(list(map(float, input().split(", "))))

print(minimum_number_of_train_platforms(inputs, outputs))

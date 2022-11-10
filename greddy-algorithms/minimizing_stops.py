def minimizing_stops(end: int, full_tank: int, number_of_stops: int, stops: list) -> int:
  stops.append(end)
  current_tank = full_tank
  stop_counter = 0
  for i in range(number_of_stops - 1):
    if i > 0:
      distance = stops[i + 1] - stops[i]
    else:
      distance = stops[i]
    
    if current_tank - distance <= 0:
      current_tank = full_tank
      stop_counter += 1

    if distance > full_tank:
      return -1
    else:
      current_tank -= distance
      
  return stop_counter


end = int(input())
full_tank = int(input())
stop_count = int(input())
stops = list(map(int, input().split()))

print(minimizing_stops(end, full_tank, stop_count, stops))

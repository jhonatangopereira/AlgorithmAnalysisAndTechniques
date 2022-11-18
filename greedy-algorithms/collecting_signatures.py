def collecting_signatures(schedules: list) -> dict:
  counter = 1
  compare = schedules[0][1]
  visited_schedules = [compare]
  for i in range(1, len(schedules)):
    if schedules[i][0] > compare:
      counter += 1
      compare = schedules[i][1]
      visited_schedules.append(compare)

  return {"counter": counter, "schedules": visited_schedules}
  

n = int(input())
schedules = sorted([list(map(int, input().split())) for i in range(n)], key=lambda x: x[1])

response = collecting_signatures(schedules)
print(response["counter"])
print(*response["schedules"])

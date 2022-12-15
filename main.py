
def count_batteries_by_usage(cycles):
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  battery=[]
  n=int(input("enter the number of batteries : "))
  for i in range(n):
    k=int(input("enter the number : "))
    battery.append(k)
  counts = count_batteries_by_usage(battery)
  for i in range(len(battery)):
    if battery[i]<310:
      lowCount+=1
    elif (battery[i]<310 and battery[i]>929):
          mediumCount+=1
    else:
      highCount+=1
  
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
  
    
  

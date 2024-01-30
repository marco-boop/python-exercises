jobs = [
    {
      "deadline": 1,
      "payment": 1
    },
    {
      "deadline": 2,
      "payment": 1
    },
    {
      "deadline": 3,
      "payment": 1
    },
    {
      "deadline": 4,
      "payment": 1
    },
    {
      "deadline": 5,
      "payment": 1
    },
    {
      "deadline": 6,
      "payment": 1
    },
    {
      "deadline": 7,
      "payment": 1
    },
    {
      "deadline": 8,
      "payment": 1
    },
    {
      "deadline": 9,
      "payment": 1
    },
    {
      "deadline": 10,
      "payment": 1
    }
  ]

def optimalFreelancing(jobs):
    days = [0] * 7

    sortedJobs = sorted(jobs, key=lambda x: x["payment"], reverse = True)
    
    for job in sortedJobs:
        print(job)
        index = job["deadline"] - 1
        print("index is", index)
        value = job["payment"]
        if index > 6:
            print("Changed index down to 6")
            index = 6
        while index >= 0:
            if days[index] == 0:
                print("Adding value to array", value)
                days[index] = value
                if all(item is not None for item in days):
                    print("Array is full")
                    break
            else:
                index -= 1
    finalSum = 0
    print("Final sum is: ",finalSum)
    for value in days:
        if value is not None:
            finalSum += value
    return finalSum

answer = optimalFreelancing(jobs)
print("Final answer: ", answer)
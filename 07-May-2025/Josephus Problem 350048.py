# Problem: Josephus Problem - https://www.geeksforgeeks.org/josephus-problem/

def Josh(person, k, index):
  
  # Base case , when only one person is left
  if len(person) == 1:
    print(person[0])
    return
  index = ((index+k)%len(person))
  person.pop(index)
  Josh(person,k,index)

# Driver Program to test above function
n = 14 
k = 2
k-=1   

index = 0 
person=[]
for i in range(1,n+1):
  person.append(i)

Josh(person,k,index)
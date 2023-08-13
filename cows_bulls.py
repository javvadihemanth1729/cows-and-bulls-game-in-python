from random import randint
def random():
  while True:
    n=str(randint(100,999))
    if not (n[0]==n[1] or n[1]==n[2] or n[0]==n[2]):
      return n 
print("Please Enter your name")
name=input()
print("Hi!!", name ,"welcome to Cows and Bulls game ")
print("How many chances you need to guess the number")
chances=int(input())
cows=0
bulls=0
num=str(random())
while chances>0:
  print("You have",chances,"chances more")
  n=str(input("Enter your guess:"))
  if num==n:
    print("Great!!!,Your guess is correct")
    break
  else:
      for i in range(0,3):
        if n[i]==num[i]:
          bulls=bulls+1
        elif n[i] in num:
            cows=cows+1
      print("Well keep going on you have",bulls,"bulls and ",cows,"cows in your guess")
      cows=0
      bulls=0
      chances=chances-1
print("The correct number is",num)


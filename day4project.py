#Rock paper Scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
a = int(input('Type 0 for rock,1 for paper,2 for scissors: '))
designs = [rock, paper, scissors]
print(designs[a])

print('Coputer choice')
b = random.randint(0, 2)
print(b)
if b == 0:
    print(rock)
elif b == 1:
    print(paper)
elif b == 2:
    print(scissors)

if a == 0 and b == 2 or b == 1:
    print('You Win')
elif a == b:
    print('Draw')
elif a == 1 and b == 0:
    print('You Win')
elif a == 1 and b == 2:
    print('You lose')
elif a == 2 and b == 0:
    print('You lose')
elif a == 2 and b == 1:
    print('You Win')

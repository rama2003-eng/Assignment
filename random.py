import random
fortune_1="Total will be lucky day"
fortune_2="You will meet someone new and interesting"
fortune_3="Watch out for obstacles in your path"
fort_numb=random.randint(1,5)
if fort_numb==1:
    print(fortune_1)
elif fort_numb==2:
    print(fortune_2)
else:
    print(fortune_3)

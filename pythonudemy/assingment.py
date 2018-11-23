from random import randint

y=randint(1,100);
len=0;
while True:
    x=int(input('enter number'));
    if(x == y):
        print('bingo');
        print(f'you got answer in {len} chance');

        break;
    if(x>y):
        print('your guesss in larger');
        len=len+1;
    if(x<y):
        print("your guess is lesser to number");
        len=len+1;


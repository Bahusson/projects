#Skrót do powtórzenia w pętl
def short2 ():
    while True:
        x1 = input('What wants to play? 1? 2? 3?')
        try:
            x = int(x1)
        except:
            print ('giv snek da number not blah blah...')
            continue
        if x1 == 1 or 2 or 3 :
            break
    x = int(x1)
    snek(x)

#pętla Y/N do powtórzeń
def short1 ():
    while True:
          line = input('Wants to start again? y/n')
          for value in [line] :
            if value == 'y' :
                order = 1
            elif value == 'n' :
                order = 2
            else :
                order = 3
          if order == 3 :
              continue
          elif order == 1 :
              short2()
              break
          elif order == 2 :
              print ('Good snek... :3')
              quit()

#Skrócone ciało sneka,dla praktyki...
def snek (task):
    while True:
        if task == 1:
            while True:
                n1 = input ("Countdown from:   ")
                try:
                    n = int(n1)
                except:
                    print ('giv snek da number not blah blah...')
                    continue
                if n > 50000 :
                    print ('your pushin da snek...')
                    continue
                elif n < 1 :
                    print ('Ur insane!')
                    continue
                elif n != 0 :
                    break
            while True :
                print(n)
                n=n-1
                if n == 0 :
                    print ('kaboom!')
                    short1()
                    break


        elif task == 2:
            while True:
                hrs1 = input("Enter Hours:")
                try:
                    hrs = (float(hrs1))
                except:
                    print ('giv snek da number not blah blah...')
                    continue
                if type(hrs) == float :
                    break

            while True:
                rat1 = input("Enter Rate:")
                try:
                    rat = (float(rat1))
                except:
                    print ('giv snek da number not blah blah...')
                    continue
                if type(hrs) == float :
                    break

            ot = (float(hrs) - 40)*0.5
            if ot < 0 :
                ot = 0

            py = (float(hrs) + float(ot)) * float(rat)
            print("Pay:",py)
            short1()

        elif task == 3:
            while True:
                score1 = input("Enter score: ")
                try:
                    score = float(score1)
                except:
                    print ('please enter a numeric value between 0 and 1')
                    continue
                if float(score) > 1 :
                    print ('please enter a numeric value between 0 and 1')
                    continue
                elif float(score) < 0 :
                    print ('please enter a numeric value between 0 and 1')
                    continue
                elif float(score) >= 0.9 :
                    print ('A')
                    short1()
                    break
                elif float(score) >= 0.8 :
                    print ('B')
                    short1()
                    break
                elif float(score) >= 0.7 :
                    print ('C')
                    short1()
                    break
                elif float(score) >= 0.6 :
                    print ('D')
                    short1()
                    break
                elif float(score) >= 0 :
                    print ('F')
                    short1()
                    break


        else :
            print ('type 1, 2 or 3')
            continue

#Powitanie Sneka
inp = input('What Sneks name?    ')
print("Hello",inp)
short2()

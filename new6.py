score1 = input("Enter score: ")

try:
    score = float(score1)
except:
    print ('please enter a numeric value between 0 and 1')
    quit()

if float(score) > 1 :
    print ('please enter a numeric value between 0 and 1')
    quit()
elif float(score) >= 0.9 :
    print ('A')
elif float(score) >= 0.8 :
    print ('B')
elif float(score) >= 0.7 :
    print ('C')
elif float(score) >= 0.6 :
    print ('D')
elif float(score) >= 0 :
    print ('F')
else:
    print ('please enter a numeric value between 0 and 1')
    quit()

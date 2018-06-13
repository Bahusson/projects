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
          #short2()
          print ('short2 would be launched now')
          break
      elif order == 2 :
          print ('Good snek... :3')
          quit()

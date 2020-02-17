def taxi_zum_zum(moves):

    coordinates=[0,0]
    direction='north'
    if type(moves)==str:
      for move in moves:
        if move=='R' and direction=="north":
            direction='east'
        elif move=="R" and direction=="east":
            direction ='south'
        elif move=='R' and direction=='south':
            direction='west'
        elif move =='R' and direction=='west':
            direction = 'north'
        elif move=='L' and direction =='north':
            direction ='west'
        elif move=='L' and direction =='west':
            direction='south'
        elif move =='L' and direction=='south':
            direction='east'
        elif move =='L' and direction=='east':
            direction='north'
        elif move=='F'and direction=='north':
            coordinates[1]+=1
        elif move =='F' and direction =='south':
            coordinates[1]-=1
        elif move =="F" and direction =='east':
            coordinates[0]+=1
        elif move =='F' and direction=='west':
            coordinates[0]-=1

        return coordinates# have to change this stupid return thing otherwise good to go !
    else:
        return coordinates





print(taxi_zum_zum('FFLLLFRLFLRFRLRRL'))





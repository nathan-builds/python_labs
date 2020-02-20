def domino_cycle(domino):

   if domino==[]:
       return True
   else:

        i = 1
        if len(domino) == 1 and domino[0][0] == domino[0][1]:  # The occurence of a one tile list passed
            return True
        else:
            if domino[0][0] == domino[len(domino) - 1][1]:  # checks that the first and last tile are correct
                for pair in domino:
                    if i < len(domino):
                        if pair[1] == domino[i][0]:
                            i += 1

                        else:
                            return False
            else:
                return False

        return True


test = [(4, 4)]

print(domino_cycle(test))

# just handle empty list now
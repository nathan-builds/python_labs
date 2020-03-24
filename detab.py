def detab(text, n=8, sub='$'):
    final_string = ''
    count=0
    for character in text:

        if character == '\t':
            final_string+=sub
            count+=1
            while count % n != 0:
                final_string += sub
                count += 1
        else:
            final_string += character

            count += 1

    return final_string


string = 'Ilkka\tMarkus\tKokkarinen'

print(detab(string,4,'-'))

"""
Tim Dwight
CS 1210
Programming Assignment
"""

if __name__ == '__main__':
    response = input('Does it have five petals or numerous petals? f or n: ')
    if response.lower() == 'f':
        #five petals
        response = input('Is it red or yellow? r or y: ')
        if response.lower() == 'r':
            #color red
            print('I think it is a scarlet pimpernel')
        elif response.lower() == 'y':
            #color yellow
            print('I think it is a wood sorrel')
        else:
            print('Invalid choice for color!')
    elif response.lower() == 'n':
        #numerous petals
        response = input('Is it yellow or white? y or w: ')
        if response.lower() == 'y':
            #color yellow
            print('I think it is a common dandelion')
        elif response.lower() == 'w':
            #color white
            print('I think it is a lawn daisy')
        else:
            print('Invalid choice for color!')
    else:
        print('Invalid choice for petals!')
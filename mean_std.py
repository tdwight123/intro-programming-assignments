"""
Tim Dwight
CS 1210
Programming Assignment
"""

def mean(numbers):
    return sum(numbers) / len(numbers)

def std_dev(numbers):
    average = mean(numbers)
    start_num = 0
    
    for number in numbers:
        start_num += (number - average) ** 2
        
    return (start_num / len(numbers)) ** 0.5

if __name__ == '__main__':
    numbers = []
    while True:
        response = (input('Enter a real number or q to end data entry: '))
        if response.lower() == 'q':
            break
        numbers.append(float(response))
    if len(numbers) == 0:
        print('No data!')
    else:
        print(f'The mean is {mean(numbers)} and the standard deviation is '
              f'{std_dev(numbers):.2f}')
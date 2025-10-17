import random , string

"""Writ a function which generates a six digit/character random_user_id.
  print(random_user_id());
  '1ee33d'
"""

def random_user_id():
    alphapets = string.ascii_letters + string.digits
    return ''.join(random.choices(alphapets, k=6))

print(random_user_id())


"""
Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
"""

"""
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
"""

def user_id_gen_by_user(a,b):
    numOfCharacters = a
    numOfIds = b
    alphapets = string.ascii_letters + string.digits
    for _ in range(numOfIds):
        print(''.join(random.choices(alphapets, k=numOfCharacters)))

user_id_gen_by_user(16,5)


"""
Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
"""


def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return f'rgb({r},{g},{b})'

print(rgb_color_gen())

#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols,
# 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).


def list_of_hexa_colors(a):
    hexa_colors = []
    for _ in range(a):
        hexa_colors.append('#' + ''.join(random.choices('0123456789abcdef', k=6)))
    return hexa_colors

print(list_of_hexa_colors(6))

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(a):
    rgb_colors = []
    for _ in range(a):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb_colors.append(f'rgb({r},{g},{b})')
    return rgb_colors
print(list_of_rgb_colors(6))

"""Write a function generate_colors which can generate any number of hexa or rgb colors.
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
"""


def generate_colors(color_type, number_of_colors):
    colors = []
    if color_type == 'hexa':
        for _ in range(number_of_colors):
            colors.append('#' + ''.join(random.choices('0123456789abcdef', k=6)))
    elif color_type == 'rgb':
        for _ in range(number_of_colors):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            colors.append(f'rgb({r},{g},{b})')
    return colors

#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    random.shuffle(lst)
    return lst


#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_numbers():
    return random.sample(range(10), 7)
print(unique_random_numbers())
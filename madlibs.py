
def call_input():
    words = input('Choose your story or press "q" to quit: ')
    return words


def print_stories():
    print('Story List:\n'
          'Month Story\n'
          'Star Wars\n')


# choose story
def choose_story(story):
    if story == 'Month Story':
        month_story()
    elif story == 'Star Wars':
        StarWars_story()
    else:
        pass


def month_story():
    month = input('Month: ')
    name = input('Name: ')
    place = input('Place: ')
    noun = input('Plural Noun: ')
    sport = input('Sport: ')
    print()
    print (f'In this month of {month}, {name} went to the {place}\n'
           f'with the boys and some {noun} to play {sport}. They\n'
           f'played all day until the sun set.')


def StarWars_story():
    place = input('Place: ')
    num1 = input('Number: ')
    num2 = input('Number: ')
    adj1 = input('Adjective: ')
    noun1 = input('Noun: ')
    verb1 = input('Verb: ')
    adj2 = input('Adjective: ')
    adv = input('Adverb: ')
    adj3 = input('Adjective: ')
    verb2 = input('Verb: ')
    noun2 = input('Noun: ')
    verb3 = input('Verb: ')
    print()
    print(f'Chewbacca is a Wookie from the planet {place}.\n'
          f'He is more than {num1} feet tall and {num2}\n'
          f'years old, with {adj1} fur covering his {noun1}.\n'
          f"Wookies don't {verb1} like humans; they make\n"
          f'{adj2} noises instead. They are {adv} {adj3} and\n'
          f"know how to {verb2}. Chewie is Han Solo's friend\n"
          f'and co-pilot of{noun2} ship, the Millennium\n'
          f'Falcon. Together, they helped The Resistance\n'
          f'{verb3} the Empire.')


def madlibs_game():
    print('Welcome to MadLibs!!')
    words = ''
    while words != 'q':
        print()
        print_stories()
        words = call_input()
        if words is not ('' or 'q' or 'Month Story' or 'Star Wars'):
            print('This is not a valid story. Try again.')
            continue
        choose_story(words)
    print('Thanks for playing!')

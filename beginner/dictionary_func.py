def build_person (first_name, last_name, age = None):
    '''Return a dictionary of information about a person'''
    person = {'first' : first_name.title(), 'last' : last_name.title()}
    if age: 
        '''if the age != none, do this. Otherwise skip this conditional. ps cant put these commends on the same line you start a branch aka conditional'''
        person['age'] = age
    elif age == None:
        '''PS originally i had (elif age == False), apparently None equates to False in conditionals...BUT FALSE DOES NOT EQUATE TO NONE'''
        person['age'] = 'there was no given age'
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
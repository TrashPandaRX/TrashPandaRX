def build_person (first_name, last_name):
    person = {'first' : first_name.title(), 'last' : last_name.title()}
    return person

check = 'not done'
list_of_people = []
print('When you are done adding people, type in "done". Otherwise type in "not done".\n')
while(check != 'done'):
    check = input(f'Type not done if you want to add another person: ', ) 
    if (check == 'not done' ):
        list_of_people.append(build_person(input(f'Provide a first name: ', ), input(f'Provide a last name: ', )))
    elif (check == 'done'):
        print('Alright here are the names you added!')
        '''this then goes to the while loop beginning, and because check == done, breaks out'''
    else:
        print('You typed something we dont understand, please try again.')
        '''if something invalid is typed then just loop back to beginning of while and repeat the input prompt for check'''

for x in list_of_people:
    print({list_of_people[x]})


'''it breaks when i get down to where i need to print the list_of_people because it says its "an unhashable type: list" ?'''
'''
aliens.py was a list filled with dictionaries, here we work
with dictionaries in other capacities

**The following is an example of a LIST of DICTIONARIES:

alien0 = {'color' : 'green', 'points' : 5}
alien1 = {'color' : 'blue', 'points' : 7}
alien2 = {'color' : 'gray', 'points' : 9}

aliens = [alien0, alien1, alien2]

**The following is an example of a DICTIONARY that has LISTS:

weird_fetishes = {
    'men' : ['futunari', 'kicked in nards', 'wearing womens clothes', 'dildo in butt'],
    'women' : ['rape', 'vampires'],
    'both' : ['banged by horse', 'pretend to be animals', 'eat poop', '50 shades of Gray']
}
->You can nest a list inside of a dictionary any time you want more
than one value to be assocated with a single key in a dictionary.
When we loop through the dictionary, the value associated with each
person would be a list of fetishes rather than a single fetish.
Inside the dictionary's for loop we use another for loop to run through
the list of fetishes associated with each gender.
->HOWEVER you should NOT nest lists and dictionaries too deeply. if youre nesting items
deeper than what you would see in the preceeding examples or you're working with someone
else's code with significant levels of nesting, theres likely a more simple solution
to solve the problem.

**The following is an example of a dictionary in a dictionary:
*cant use this one the part where their super names are posted isnt standardized to work
Compendium_of_Comics = {
    'Marvel_Superheroes' : {
        'Spiderman' : 'Peter Parker',
        'Mr. Fantastic' : 'Reed Richards',
        'The Hulk' : 'Bruce Banner'
    },

    'DC_Superheroes' : {
        'Superman' : 'Clark Kent',
        'Batman' : 'Bruce Wayne',
        'The Flash' : 'Wally West'
    },

    'Bad_Guys' : {
        'Venom' : 'Eddie Brock',
        'Carnage' : 'Cletus Kassidy',
        'Bald Nerd' : 'Lex Luthor'
    }
}
'''

Comics = {
    'Marvel_Superheroes' : {
        'super #1' : 'Spiderman',
        'super #2' : 'Mr. Fantastic',
        'super #3' : 'The Hulk'
    },

    'DC_Superheroes' : {
        'super #1' : 'Superman',
        'super #2' : 'Batman',
        'super #3' : 'The Flash'
    },

    'Bad_Guys' : {
        'super #1' : 'Venom',
        'super #2' : 'Carnage',
        'super #3' : 'Lex Luthor'
    }
}

#i made an error earlier here i was getting a  "too many values to unpack error", because i hadn't added ".items()" to Comics in the for loop portion
for affiliation, names in Comics.items():
    print(f"\nAffiliation: {affiliation}")
    supers = f"Whom? {names['super #1']}, {names['super #2']}, {names['super #3']}"

    print(f"\tSupers: {supers}")


    



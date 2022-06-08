:- initialization set_facts, is_bigger(X,Y).

set_facts :-
	bigger(elephant, horse).
	bigger(horse, donkey).
	bigger(donkey, dog).
	bigger(dog, monkey).

is_bigger(X,Y) :-
	bigger(X,Y).

is_bigger(X,Y) :-
	bigger(X,Z), is_bigger(Z,Y).

% DOES NOT WORK, i think because im not setting the rules appropriately. see Sizes3.pl to see if setting the rules along with the set_facts
% from the get-go with the rules works.
% PS FROM THE FUTURE!!! Sizes3.pl works like a charm!
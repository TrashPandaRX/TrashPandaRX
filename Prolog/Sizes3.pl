	bigger(elephant, horse).
	bigger(horse, donkey).
	bigger(donkey, dog).
	bigger(donkey, monkey).
	bigger(dog, mouse).
	bigger(monkey, mouse).

	%this was just to test to see what happened, please remove the following fact if using to actually test code.
	%bigger(mouse, elephant).

	is_bigger(X,Y) :- bigger(X,Y).
	is_bigger(X,Y) :- bigger(X,Z), is_bigger(Z,Y).
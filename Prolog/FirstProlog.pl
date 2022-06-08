:- initialization FirstProlog, halt.
FirstProlog :-
	write('Hello, World!'), nl.

//Remove this portion, but the above does NOT work! (F)irstProlog CANNOT have the (F) Capitalized! it needs to be lowercase.
//the initialization is basically calling a method, and the (F)irstProlog :- is setting what the method does like usual programming!

:- initialization firstProlog, halt.
firstProlog :-
	write('Hello, World!'), nl.

//Remove this portion, the above works fabulously if you have lines 8-10 alone in a file! be sure to type into terminal the following:
//Gil:Desktop gilco$ swipl -q -l PROGRAMS_FILENAME_HERE.pl
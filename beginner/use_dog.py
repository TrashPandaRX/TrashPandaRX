'''visit kit.com/python/answers/how-to-import-a-class-from-another-file-in-python for inst on how to import classes '''
''' sys.path.append(".") strange, after i removed this the program worked perfectly...unless you only use 'sys.path()' and 'sys.path.append(dir) for .py files not in the same directory as the rest of the files '''

from dog_maker import Dog

my_dog = Dog("rocky", 17)
my_dog.sit()
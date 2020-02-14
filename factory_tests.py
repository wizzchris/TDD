import factory_functions

while True:
    if __name__ == '__main__':
        print('Select 1 to test, 2 to make bread')
        user_input = input('>>>>>').strip()
        if user_input == '1':
            print('Going to run some tests')
            from factory_functions import *
        elif user_input == '2':
            print ('Welcome to the factory')
            arg1 = input('What is your first ingredient')
            arg2 = input('What is your second ingredient')
            arg3 = input('What is your theird ingredient')
            result = run_factory(arg1,arg2,arg3)
            print(result)
        elif user_input == 'exit':
            break
        else:
            

print('Testing make_dough() with water flour and eggs. Expected dough')
make_bread('water','flour','eggs') == 'dough'
print ('Got:' + make_bread('water','flour','eggs') == 'dough')
print('Testing bakwe() with dough expected brioche')
bake('dough') == 'brioche'
print ('Got :' + bake('dough'))
print ('Testing make_doiugh() with water cement and gravle expected not dough')
make_bread('water','cement','gravel') == 'not dough'
print('Got : ' + make_bread('water','cement','gravel'))
print ('Testing bake with not dough exoected not brioche')
bake('not dough') == 'not brioche'
print ('Got :' + bake('not dough'))

# As a user I want to be able to run a facotry function. Give it flour water and eggs and recieve brioch.
#Simple integration test
print ('testing run_factory() with water flour and eggs. Expected brioche')
print(run_factory('cement', 'flour', 'eggs'))


if __name__ == '__main__':
    print('Welcome our factory!')
    print('Going to run some tests')
    #little demos
#statring a game
#running tests


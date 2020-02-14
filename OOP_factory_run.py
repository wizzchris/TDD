from oop_factory import Car

while True:
    if __name__ == '__main__':
        print('Type 0 to make a car Type 1 for tests and 2 for car factory')
        user_input = input('>>>>>')
        if user_input == '0':
            car_name = input('What would you like the car to be called')
            car_name = Car()
        if user_input == '1':
            import OOP_tests
        elif user_input == '2':
            ob1 = input('First item to add to factory')
            ob2 = input('Second item to add to factory')
            car = car_name.factory_build(ob1,ob2)
            print(car)
        else:
            print ('please pick valid choice')



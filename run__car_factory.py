from car_factory_functions import make_parts, build_car, run_car_factory

while True:
    if __name__ == '__main__':
        print('Type 1 for tests and 2 for car factory')
        user_input = input('>>>>>')
        if user_input == '1':
            import car_factory_tests
        elif user_input == '2':
            ob1 = input('First item to add to factory')
            ob2 = input('Second item to add to factory')
            ob3 = input('Theird item to add to factory')
            car = run_car_factory(ob1,ob2,ob3)
            print(car)
        else:
            print ('please pick valid choice')
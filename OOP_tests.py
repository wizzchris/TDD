#As a user I want to be able to class something as a car
#As a user I want to be able to run a factory with metal and hardwork to make a car

from oop_factory import Car

print('Test for build parts. Expected Shiny parts')
car = Car()
car.build_parts('metal','hard_work') == 'Shiny Parts'
print('Got : ' + car.build_car('metal','hard_work'))

print('Test for build car. Expected Shiny car')
car = Car()
car.build_car('Shiny Parts') == 'Shiny Parts'
print('Got : ' + car.build_car('Shiny Parts'))

#As a user I wamt to not be able to build a car if the wrong thigns are addeded

print('Test for build parts. Expected Broken parts')
car = Car()
car.build_parts('metal','no_work') == 'Broken Parts'
print('Got : ' + car.build_car('metal','no_work'))

print('Test for build car. Expected broken car')
car = Car()
car.build_car('broken Parts') == 'broken Parts'
print('Got : ' + car.build_car('broken Parts'))

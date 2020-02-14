
#As a user I want to be able to give metal, leather, and hard_work to a function make_parts which then gives out shiny parts in any order
#As a user I want to be able to make a car with build_car using shiny parts
#As a user I want it to not give parts out if there isnt the right

from car_factory_functions import make_parts, build_car

print('Test for make_parts. Given metal, leather and hard_work. Expected shiny parts')
make_parts('metal', 'leather', 'hard_work') == 'shiny_parts'
print('Got : ' + make_parts('metal', 'leather', 'hard_work'))

print('Test for make_parts. Given leather, metal, hard work. Expected shiny parts')
make_parts('leather', 'metal', 'hard_work') == 'shiny_parts'
print('Got : ' + make_parts('leather', 'metal', 'hard_work'))


print('Test for build_car. Expected shiny_car')
build_car('shiny_parts') == 'shiny_car'
print('Got : ' + build_car('shiny_parts'))


print('Test for make_parts. Given metal, plastic and no work. Expected broken parts')
make_parts('metal', 'plastic', 'no work') == 'broken_parts'
print('Got : ' + make_parts('metal', 'plastic', 'no work'))


print('Test for build_car. Expected broken_car')
build_car('broken_parts') == 'broken_car'
print('Got : ' + build_car('broken_parts'))





def make_parts(metal, leather, hard_work):
    list = []
    list.append(metal)
    list.append(leather)
    list.append(hard_work)
    if 'metal' in list and 'leather' in list and hard_work in list:
        return 'shiny_parts'
    else:
        return 'broken_parts'

def build_car(shiny_parts):
    if shiny_parts == 'shiny_parts':
        return 'shiny_car'
    else:
        return 'broken_car'

def run_car_factory(arg1,arg2,arg3):
    part = make_parts(arg1,arg2,arg3)
    car = build_car(part)
    return car




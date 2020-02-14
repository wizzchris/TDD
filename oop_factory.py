class Car:
    def build_parts(self, metal, hard_work):
        list = []
        list.append(metal)
        list.append(hard_work)
        if 'metal' in list and 'hard_work' in list:
            return 'Shiny Parts'
        else:
            return 'Broken Parts'

    def build_car(self,shiny_parts):
        if shiny_parts == 'Shiny Parts':
            return 'Shiny Car'
        else:
            return 'Broken Car'

    def factory_build(self, metal, hard_work):
        car = self.build_parts(metal, hard_work)
        return self.build_car(car)
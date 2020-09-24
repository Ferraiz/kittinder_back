class CatFacade:
    def name_validation(self, name):
        result = False
        if len(name) > 0:
            result = True
        return result


cat_facade = CatFacade()

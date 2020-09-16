import re


class UserFacade:
    def email_validation(self, email):
        result = False
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.match(regex, email):
            result = True
        return result


user_facade = UserFacade()

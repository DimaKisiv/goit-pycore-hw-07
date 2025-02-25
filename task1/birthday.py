from field import Field
from datetime import datetime
from exceptions import WrongBirthDate

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
            if (self.value.date() >= datetime.now().date()):
                raise WrongBirthDate()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        except WrongBirthDate:
            raise ValueError("Date can't be later then today")
            
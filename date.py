MONTHS_LENGTH = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    # ...
}


ROME_MONTHS = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    # ...
}


MONTHS_NAMES = {
    1: 'jan',
    2: 'feb',
    3: 'mar',
    4: 'apr',
    # ...
}

class Date:
    def __init__(self, day, month, year):
        # day - число, двузначное, 01-31
        # month - число, двузначное, 01-12
        # year - число целое

        # TODO: обрабатывать високосный год

        if month > 12 or month < 1:
            raise ValueError("Incorrect month")

        days_in_month = MONTHS_LENGTH[month]

        if day > days_in_month or day < 1:
            raise ValueError("Incorrect day")

        self.year = year
        self.month = month
        self.day = day

    def get_rome_month(self):
        return ROME_MONTHS[self.month]

    def get_month_name(self):
        return MONTHS_NAMES[self.month]

    def is_ac(self):
        return self.year > 0

    def parse(self):
        pass

    def user_format(self):
        # 1 jan 1999 BC
        value = ""

        value += str(self.day)
        value += " "

        value += self.get_month_name()
        value += " "

        value += str(self.year)
        value += " "

        if self.is_ac():
            value += "AC"
        else:
            value += "BC"

        return value


d1 = Date(1, 1, 12)
print(d1.get_rome_month())
d2 = Date(2, 1, 12)

# 1999-01-01 BC

# 2018-06-23 AC
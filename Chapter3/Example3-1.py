#Example 3 - 1 Dict Comprehensions

def Ex3_1():
    dial_codes = [
            (880, 'Bangladesh'),
            (55, 'Brazil'),
            (86, 'China')
            ]

    country_dial = {country: code for code, country in dial_codes}

    #Country : Code
    print(country_dial)

    #Code : Country
    code_dial = {code: country.upper() for country, code in sorted(country_dial.items())}
    print(code_dial)


Ex3_1()

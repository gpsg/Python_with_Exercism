def convert(number):
    raindrops = {3: "Pling", 5: "Plang", 7: "Plong"}
    result = ""
    for i in raindrops:
        if number % i == 0:
            result += raindrops[i]
    if result:
        return result
    return f'{number}'

def convert_after_mentor(number):
    raindrops = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    result = "".join(drop for divisor, drop in raindrops.items() if number % divisor == 0)
    return result if result else f'{number}'

def convert_mentor(number):
    msg = "".join(drop for divisor, drop in {3: 'Pling', 5: 'Plang', 7: 'Plong'}.items() if number % divisor == 0)
    return msg if msg else str(number)
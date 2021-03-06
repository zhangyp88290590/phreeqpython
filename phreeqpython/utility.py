from periodictable import formula as chemform

def convert_units(formula, amount, from_units='mol', to_units='mmol'):
    if from_units == to_units:
        return amount

    if from_units == 'mol':
        if to_units == 'mmol':
            return amount*1e3
        if to_units == 'mg':
            return chemform(formula).mass * amount * 1e3

    if from_units == 'mmol':
        if to_units == 'mol':
            return amount * 1e-3
        if to_units == 'mg':
            return chemform(formula).mass * amount

    if from_units == 'mg':
        if to_units == 'mol':
            return amount / chemform(formula).mass * 1e-3

        if to_units == 'mmol':
            return amount / chemform(formula).mass

def describe_city(city, country='united arab emirates'):

    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('sharjah')
describe_city('CDO', 'phillipines')
describe_city('abu dhabi')
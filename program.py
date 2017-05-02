
def main():
    print_the_header()

    code = input('What zipcode do you want thgite weather for (94611)? ')

    get_html_from_web(code)
    # parse the html
    # display for the forecast
    print('hello from main')


def print_the_header():
    print('-------------------------------')
    print('         WEATHER APP')
    print('-------------------------------')
    print('')


def get_html_from_web():
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    print(url)


if __name__ == '__main__':
    main()
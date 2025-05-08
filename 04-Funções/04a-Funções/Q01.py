def fahrenheit (tCelsius):
    tFahrenheit = (tCelsius * 1.8 + 32)
    print(f'Fahrenheit: {tFahrenheit:.2f}')


def kelvin (tCelsius):
    tKelvin = (tCelsius + 273.15)
    print(f'Kelvin: {tKelvin:.2f}')

fahrenheit(25)
kelvin(25)
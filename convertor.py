class Convertor:

    # конвертация температуры {

    def CelsiumToKelvin (C):

        if C > -273.15:
            return C + 273.15
        else:
            return print("Температура не может быть ниже Абсолютного нуля.")

    def KelvinToCelsium (K):

        if K >= 0: 
            return K - 273.15
        else: 
            return print("Теспература не может быть ниже Абсолютного нуля.")

    # конвертация температуры }

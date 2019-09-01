def timeConverter(seconds):
    from datetime import timedelta
    seconds = float(input('Segundos: '))
    formated = timedelta(seconds=seconds)
    return formated
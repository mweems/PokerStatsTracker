import datetime

def _getDate(text):
    date = text.split("/")
    return datetime.date(int(date[0]), int(date[1]), int(date[2]))


def _getStakes(text):
    int_stakes = {
        "small_blind": float(text[0]),
        "big_blind": float(text[1])
    }
    return int_stakes

import time

def panel_show_date():
    t = time.asctime()
    d = int(t[7:10])
    m = t[4:7]

    month = {'Sep': 'сен', 'Oct': 'окт', 'Nov': 'нояб', 'Dec': 'дек', 'Jan': 'янв', 'Feb': 'фев', 'Mar': 'мар',
             'Apr': 'апр', 'May': 'мая', 'Jun': 'июн',
             'Jul': 'июл', 'Aug': 'авг'}
    month2 = {'Sep': 'окт', 'Oct': 'нояб', 'Nov': 'дек', 'Dec': 'янв', 'Jan': 'фев', 'Feb': 'мар', 'Mar': 'апр',
              'Apr': 'мая', 'May': 'июн', 'Jun': 'июл',
              'Jul': 'авг', 'Aug': 'сен'}
    d_month = {'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31, 'Jan': 31, 'Feb': 28, 'Mar': 31,
               'Apr': 30, 'May': 31, 'Jun': 30,
               'Jul': 31, 'Aug': 31}

    if d_month[m] == 31:
        if d <= 20:
            Inl
        elif d >= 27:
            pass
        else:
            pass




panel_show_date()
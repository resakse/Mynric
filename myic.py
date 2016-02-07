from datetime import datetime
from dateutil.relativedelta import relativedelta
import re


class myic(object):
    malay=False

    def __init__(self, ic, language=None):
        self.ic = ic
        self.language = language
        if self.language:
            if (self.language.lower() =='malay') or (self.language.lower()=='m'):
                self.malay=True

        dob = self.ic[0:6]
        try:
            self.dob = datetime.strptime(dob, '%y%m%d')
        except:
            raise ValueError

    @property
    def ic(self):
        return self._ic

    @ic.setter
    def ic(self, v):
        panjang = len(v) # panjang = nric length
        if (panjang < 11) or (panjang > 14):
            raise ValueError
        self._ic = re.sub('[-!@#$%^&]', '', v)

    def age(self):
        today = datetime.now()
        age = relativedelta(today, self.dob)

        if self.malay:
            data = "%d tahun %d bulan dan %d hari" % (age.years, age.months, age.days)
        else:
            data = "%d years %d month and %d days" % (age.years, age.months, age.days)

        return data

    def birthday(self):
        data = self.dob.strftime("%d %b %Y")
        return data

    def upcoming(self):
        today = datetime.today()
        hari = self.dob.day
        bulan = self.dob.month
        if (bulan < today.month) or (bulan == today.month and hari < today.day):
            tahun = (datetime.today().year) + 1
        else:
            tahun = datetime.today().year

        data = datetime(tahun, bulan, hari)
        upcome = relativedelta(data, today)
        if upcome.months == 0:
            if upcome.days == 0:
                if hari == datetime.now().timetuple().tm_mday and bulan == datetime.now().timetuple().tm_mon:
                    bila = 'Hari ini!!' if self.malay else 'Today!'
                else:
                    bila = 'dalam masa %d jam lagi' % upcome.hours if self.malay else "in %d more hours" % upcome.hours
            elif upcome.days == 1:
                bila = "dalam masa %d hari dan %d jam" % (upcome.days, upcome.hours) if self.malay else "in %d days and %d hours" % (upcome.days, upcome.hours)
            else:
                bila = "dalam masa %d hari lagi" % (upcome.days) if self.malay else "in %d more days" % (upcome.days)
        else:
            bila = "dalam masa %d bulan dan %d hari" % (upcome.months, upcome.days) if self.malay else "in %d month and %d days" % (upcome.months, upcome.days)

        return bila

    def gender(self):
        if int(self.ic) % 2 == 0:
            return 'Perempuan' if self.malay else 'Female'
        return 'Lelaki' if self.malay else 'Male'

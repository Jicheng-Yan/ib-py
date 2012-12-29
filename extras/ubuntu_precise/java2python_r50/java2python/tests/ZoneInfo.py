#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TZType(Serializable):
    """ generated source for TZType

    """
    serialVersionUID = 1L
    offset = 0
    name = ""
    isdst = bool()

    def __init__(self, name, offset, dst):
        self.name = self.name
        self.offset = self.offset
        self.isdst = dst

    def toString(self):
        return "TzType: " + self.name + " : offs=" + self.offset + " dst=" + self.isdst

class ZoneInfo(TimeZone):
    """ generated source for ZoneInfo

    """
    class TZDump(object):
        """ generated source for TZDump

        """
        zone = ""
        tz = ZoneInfo()
        cal = GregorianCalendar()
        fmt = DateFormat.getDateTimeInstance(DateFormat.LONG, DateFormat.LONG)

        def __init__(self, zone):
            if self.zone is not None:
                self.tz = ZoneInfo(self.zone)
            else:
                self.tz = ZoneInfo()
                self.zone = "localtime"
            self.zone = self.zone
            self.cal.setTimeZone(self.tz)
            self.fmt.setCalendar(self.cal)

        def dumplcl(self, time):
            return self.fmt.format(Date(time * 1000L))

        def dump(self, time):
            t = self.tz.localtime(time)
            print self.zone + ' ' + self.tz.gmtime(time + " = " + self.dumplcl(time))

        def dumpdst(self):
            ## for-while
            i = 0
            while i < self.tz.transTimes.length:
                t = self.tz.transTimes[i]
                self.dump(t - 1)
                self.dump(t)
                i += 1

        def dumpleap(self):
            ## for-while
            i = 0
            while i < self.tz.leapSecs.length:
                t = self.tz.leapSecs[i]
                self.dump(t - 1)
                self.dump(t)
                self.dump(t + 1)
                i += 2

        now = System.currentTimeMillis() / 1000

        @classmethod
        def dumpzone(cls, tzname):
            cls.tz = TZDump(tzname)
            print cls.tz.cls.dumplcl(cls.now)
            cls.tz.cls.dump(Integer.MIN_VALUE)
            cls.tz.cls.dumpdst()
            cls.tz.cls.dumpleap()
            cls.tz.cls.dump(Integer.MAX_VALUE)

        @classmethod
        def main(cls, argv):
            if (argv.length == 0):
                cls.dumpzone(None)
            else:
                ## for-while
                i = 0
                while i < argv.length:
                    cls.dumpzone(argv[i])
                    i += 1

    class tm(object):
        """ generated source for tm

        """
        tm_hour = 0
        tm_min = 0
        tm_sec = 0
        tm_wday = 0
        tm_year = 0
        tm_yday = 0
        tm_mon = 0
        tm_mday = 0
        tm_isdst = bool()
        tm_zone = ""
        f = DecimalFormat("#0")
        f0 = DecimalFormat("00")

        def toString(self):
            return self.f.format(self.tm_mon + 1) + '/' + self.f0.format(self.tm_mday) + '/' + self.f0.format(self.tm_year + 1900) + ' ' + self.f.format(self.tm_hour) + ':' + self.f0.format(self.tm_min) + ':' + self.f0.format(self.tm_sec) + ' ' + "NUL" if self.tm_zone is None else self.tm_zone

        @overloaded
        def __init__(self):
            pass

        @__init__.register(object, int, int, int, int)
        def __init___0(self, year, mon, day, tm_secs):
            self.tm_year = year
            self.tm_mon = mon
            self.tm_mday = day
            self.setSecs(tm_secs)

        def setSecs(self, tm_secs):
            self.tm_hour = tm_secs / self.SECSPERHOUR
            rem = tm_secs % self.SECSPERHOUR
            self.tm_min = rem / self.SECSPERMIN
            self.tm_sec = rem % self.SECSPERMIN

        def compareTo(self, t):
            if (self.tm_year != t.tm_year):
                return self.tm_year - t.tm_year
            if (self.tm_mon != t.tm_mon):
                return self.tm_mon - t.tm_mon
            if (self.tm_mday != t.tm_mday):
                return self.tm_mday - t.tm_mday
            if (self.tm_hour != t.tm_hour):
                return self.tm_hour - t.tm_hour
            if (self.tm_min != t.tm_min):
                return self.tm_min - t.tm_min
            return self.tm_sec - t.tm_sec

        def __eq__(self, obj):
            return isinstance(obj, (tm)) and (self.compareTo(obj) == 0)

        def hashCode(self):
            return self.tm_year << 24 + self.tm_mon << 20 + self.tm_mday << 15 + self.tm_hour << 10 + self.tm_min << 5 + self.tm_sec

        def setClock(self, clock, offset):
            days = clock / self.SECSPERDAY
            tm_secs = clock % self.SECSPERDAY
            tm_secs += offset
            while tm_secs < 0:
                tm_secs += self.SECSPERDAY
                days -= 1
            while tm_secs >= self.SECSPERDAY:
                tm_secs -= self.SECSPERDAY
                days += 1
            self.setSecs(tm_secs)
            doc = days + self.DAYSADJ
            self.tm_wday = self.CENT_WDAY + doc % self.DAYSPERWEEK
            leapyear = 2
            self.tm_year = doc - doc / 1461 + 364 / 365
            self.tm_yday = doc - self.tm_year - 1 * 1461 / 4
            if (self.tm_year % 4 == 0):
                leapyear = 1
            if self.tm_yday > 59 and self.tm_yday > 60 or (leapyear == 2):
                self.tm_yday += leapyear
            self.tm_mon = 269 + self.tm_yday * 9 / 275
            self.tm_mday = self.tm_yday + 30 - 275 * self.tm_mon / 9
            self.tm_mon -= 1

    serialVersionUID = 1L
    transTimes = None
    transTypes = None
    tz = None
    leapSecs = None
    rawoff = 0
    normaltz = TZType()

    @overloaded
    def set___init__(self, f):
        ds = DataInputStream(BufferedInputStream(FileInputStream(f)))
        try:
            ds.skip(28)
            leapcnt = ds.readInt()
            timecnt = ds.readInt()
            typecnt = ds.readInt()
            charcnt = ds.readInt()
            self.transTimes = [int() for __idx0 in range(timecnt)]
            ## for-while
            i = 0
            while i < timecnt:
                self.transTimes[i] = ds.readInt()
                i += 1
            self.transTypes = [strval() for __idx0 in range(timecnt)]
            ds.readFully(self.transTypes)
            offset = [int() for __idx0 in range(typecnt)]
            dst = [strval() for __idx0 in range(typecnt)]
            idx = [strval() for __idx0 in range(typecnt)]
            ## for-while
            i = 0
            while i < typecnt:
                offset[i] = ds.readInt()
                dst[i] = ds.readByte()
                idx[i] = ds.readByte()
                i += 1
            strval = [strval() for __idx0 in range(charcnt)]
            ds.readFully(strval)
            self.tz = [TZType() for __idx0 in range(typecnt)]
            ## for-while
            i = 0
            while i < typecnt:
                pos = idx[i]
                end = pos
                while (strval[end] != 0):
                    end += 1
                self.tz[i] = TZType(String(strval, pos, end - pos), offset[i], (dst[i] != 0))
                i += 1
            self.leapSecs = [int() for __idx0 in range(leapcnt * 2)]
            ## for-while
            i = 0
            while leapcnt > 0:
                self.leapSecs[i += 1] = ds.readInt()
                self.leapSecs[i += 1] = ds.readInt()
                leapcnt -= 1
        finally:
            ds.close()
        n = 0
        while self.tz[n].isdst and n < self.tz.length:
            n += 1
        self.normaltz = self.tz[n]
        ts = System.currentTimeMillis() / 1000
        ## for-while
        i = 0
        while i < 9:
            currTz = self.getTZ(ts + self.secsPerThreeMonths * i)
            if not currTz.isdst:
                self.normaltz = currTz
                break
            i += 1
        setID(self.normaltz.name)

    secsPerThreeMonths = 60 * 60 * 24 * 30 * 3

    def getRawOffset(self):
        return self.normaltz.offset * 1000 + self.rawoff

    def setRawOffset(self, millis):
        self.rawoff = millis - self.normaltz.offset * 1000

    def getOffset(self, era,
                        year,
                        month,
                        day,
                        dow,
                        millis):
        if (era != GregorianCalendar.AD):
            return self.getRawOffset()
        secs = millis / 1000
        then = tm(year - 1900, month, day, secs)
        ts = long()
        try:
            ts = self.mktime(then, True)
        except (IllegalArgumentException, ), x:
            return self.getRawOffset()
        offset = self.getTZ(ts).offset
        ## for-while
        y = self.leapSecs.length
        while y -= 2 >= 0:
            ls_trans = self.leapSecs[y]
            ls_corr = self.leapSecs[y + 1]
            if ts >= ls_trans:
                offset -= ls_corr
                break
        return offset * 1000 + self.rawoff

    def inDaylightTime(self, d):
        self.tz = self.getTZ(d.getTime() / 1000)
        return self.tz.isdst

    def useDaylightTime(self):
        return self.tz.length > 1

    SECSPERMIN = 60
    MINSPERHOUR = 60
    HOURSPERDAY = 24
    DAYSPERWEEK = 7
    SECSPERHOUR = SECSPERMIN * MINSPERHOUR
    SECSPERDAY = SECSPERHOUR * HOURSPERDAY
    TM_SUNDAY = 0
    TM_MONDAY = 1
    TM_TUESDAY = 2
    TM_WEDNESDAY = 3
    TM_THURSDAY = 4
    TM_FRIDAY = 5
    TM_SATURDAY = 6
    EPOCH_WDAY = TM_THURSDAY
    EPOCH_YEAR = 1970
    DAYSADJ = 25203
    CENT_WDAY = EPOCH_WDAY - DAYSADJ % 7

    def gmtime(self, clock):
        t = tm()
        t.setClock(clock, 0)
        t.tm_zone = "GMT"
        return t

    def utctime(self, clock):
        t = tm()
        self.timesub(clock, None, t)
        return t

    @overloaded
    def localtime(self, clock, t):
        return self.timesub(clock, self.getTZ(clock), t)

    def getTZ(self, clock):
        if self.transTimes.length > 0 and clock >= self.transTimes[0]:
            i = 1
            ## for-while
            while i < self.transTimes.length:
                if clock < self.transTimes[i]:
                    break
                i += 1
            return self.tz[self.transTypes[i - 1]]
        return self.normaltz

    @localtime.register(object, long)
    def localtime_0(self, clock):
        t = tm()
        self.localtime(clock, t)
        return t

    @overloaded
    def mktime(self, yourtm):
        return self.mktime(yourtm, False)

    @mktime.register(object, tm, bool)
    def mktime_0(self, yourtm, raw):
        t = 0
        bits = 31
        offset = self.getRawOffset() / 1000
        mytm = tm()
        ## for-while
        while %s:
            if raw:
                mytm.setClock(t, offset)
            else:
                self.localtime(t, mytm)
            direction = mytm.compareTo(yourtm)
            if (direction == 0):
                yourtm.tm_wday = mytm.tm_wday
                yourtm.tm_yday = mytm.tm_yday
                yourtm.tm_isdst = mytm.tm_isdst
                yourtm.tm_zone = mytm.tm_zone
                return t
            if bits -= 1 < 0:
                raise IllegalArgumentException("bad time: " + yourtm)
            if bits < 0:
                t -= 1
            else:
                if direction > 0:
                    t -= 1 << bits
                else:
                    t += 1 << bits

    def timesub(self, clock, tz, t):
        hit = False
        offset = 0 if self.tz is None else self.tz.offset
        ## for-while
        y = self.leapSecs.length
        while y -= 2 >= 0:
            ls_trans = self.leapSecs[y]
            ls_corr = self.leapSecs[y + 1]
            if clock >= ls_trans:
                if (clock == ls_trans):
                    hit = (y == 0) and ls_corr > 0 or ls_corr > self.leapSecs[y - 1]
                offset -= ls_corr
                break
        t.setClock(clock, offset)
        if hit:
            t.tm_sec += 1
        if self.tz is not None:
            t.tm_isdst = self.tz.isdst
            t.tm_zone = self.tz.name
        else:
            t.tm_isdst = False
            t.tm_zone = "UTC"
        return offset

    @classmethod
    def main(cls, argv):
        cls.tz = ZoneInfo("EST5EDT")
        now = System.currentTimeMillis() / 1000
        System.err.println("Now = " + cls.tz.cls.localtime(now))
        cal = GregorianCalendar()
        cal.setTimeZone(cls.tz)
        cal.setTime(Date())
        System.err.println("Now = " + cal)

    def get___init__(self):
        super(ZoneInfo, self).__init__(File("/etc/localtime"))

    @set___init__.register(object, str)
    def set___init___0(self, tzname):
        super(ZoneInfo, self).__init__(File("/usr/share/zoneinfo", tzname))

    __init__ = property(get___init__, set___init__)


class Band:
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        self.instances.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.solo)
        return solos

    @classmethod
    def to_list(cls):
        print(cls.instances)
        return cls.instances


class Musician:
    def __init__ (self, name, instrument="bad subclass", solo="bad subclass"):
        self.name = name
        self.instrument = instrument
        self.solo = solo

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{type(self).__name__} instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Guitarist(Musician):
    def __init__(self, name, instrument="guitar", solo="face melting guitar solo"):
        Musician.__init__(self, name, instrument, solo)


class Bassist(Musician):
    def __init__(self, name, instrument="bass", solo="bom bom buh bom"):
        Musician.__init__(self, name, instrument, solo)


class Drummer(Musician):
    def __init__(self, name, instrument="drums", solo="rattle boom crash"):
        Musician.__init__(self, name, instrument, solo)


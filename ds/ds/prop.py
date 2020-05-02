from datetime import datetime, timedelta

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        now = datetime.now()
        if now < self.expires:
            return False
        else:
            return True


#future_date = NOW + timedelta(days=1)
#newsletter_promo = Promo('newsletter', future_date)

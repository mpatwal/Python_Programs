class ottsubs:
    def __init__(self, s_id, plan, payment):
        self.s_id = s_id
        self.plan = plan
        self.payment = payment

    def subscribe(self):
        print(
            f"user with subscription {self.s_id} id has subscribed to {self.plan} plan")

    def unsubscribe(self):
        print(f"user with {self.s_id} id unsubscribed from {self.plan} plan")


class premium(ottsubs):
    def __init__(self, s_id, plan, payment, quality):
        super().__init__(s_id, plan, payment)
        self.quality = quality

    def set_quality(self, quality):
        self.quality = quality
        print(
            f"Video quality enhanced to {self.quality} quality ,in the premium plan")


p = premium(234, "quaterly", 1000, 5)
p.set_quality(3)
p.unsubscribe()


'''o = ottsubs(232, "monthly", 500)
print(o.plan)
print(o.payment)'''

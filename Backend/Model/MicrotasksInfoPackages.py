import json


class MicrotaskEnrollment:
    def __init__(self, company_name, crowdsourcer_name, microtask_name):
        self.companyName = company_name
        self.crowdsourcerName = crowdsourcer_name
        self.microtaskName = microtask_name


class MicrotaskPayment:
    def __init__(self, company_name, crowdsourcer_name, microtask_name, payment):
        self.companyName = company_name
        self.crowdsourcerName = crowdsourcer_name
        self.microtaskName = microtask_name
        self.payment = payment

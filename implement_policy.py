class ImplementPolicy:
    masks = False
    lockdowns = False
    reinfections = True

    infection_chance = 0.05
    people_met = 20

    mask_case_threshold = 0.001
    lockdown_case_threshold = 0.05

    def refresh_policy(self, cases, population):
        if self.masks:
            if cases / population > self.mask_case_threshold:
                self.infection_chance = 0.025
            else:
                self.infection_chance = 0.05
        if self.lockdowns:
            if cases / population > self.lockdown_case_threshold:
                self.people_met = 1
            else:
                self.people_met = 20
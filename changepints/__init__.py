import numpy as np
import ruptures as rpt
import matplotlib.pyplot as plt
import fire

class ChangePints:

    def __init__(self, model="rbf", penalty=3):
        self.model = model
        self.penalty = penalty

    def data(self, source):
        self.signal = np.array(source)
        algo = rpt.Pelt(model=self.model).fit(self.signal)
        self.bkpts = algo.predict(pen=self.penalty)
        return self

    def breakpoints(self):
        return self.bkpts

    def crossed_threshold(self, nbkpts=1):
        "If number of breakpoints > nbkpts, return False"
        return len(self.breakpoints()) > nbkpts

    def show(self):
        rpt.display(self.signal, self.breakpoints())
        plt.show()


def main():
    fire.Fire(ChangePints)

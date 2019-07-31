import numpy as np
import ruptures as rpt
import matplotlib.pyplot as plt
import fire
from .data import ChangePintsData

class ChangePints:

    def __init__(self, model="rbf", penalty=2):
        self.model = model
        self.penalty = penalty

    def load(self, source):
        self.data = ChangePintsData(source).data
        self.signal = np.array(self.data.score)
        algo = rpt.Pelt(model=self.model).fit(self.signal)
        self.bkpts = algo.predict(pen=self.penalty)
        return self

    def breakpoints(self):
        return self.bkpts

    def show(self):
        rpt.display(self.signal, self.breakpoints())
        plt.show()


def main():
    fire.Fire(ChangePints)

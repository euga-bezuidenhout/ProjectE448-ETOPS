class ETOPS:

    import numpy as np
    import matplotlib.pyplot as plt
    import time

    def __init__(self, theta_aoa):

        # angle of arrival (degrees)
        self.theta = self.np.pi / 180 * theta_aoa
        # self.wideband = wideband

        self.K = 1  # Number of signals
        self.N = 2   # Number of array elements
        self.M = 10000  # Number of signal snapshots
        self.F_s = 1. / 0.0001  # sampling frequency [Hz]
        self.Amp = 2  # Signal amplitude
        self.f1 = 10  # base signal frequency [Hz]
        # Speed of sound in Gordan's Bay @ ~15.5 C, 4% salinity:
        self.c = 1539.21294117647

        self.t = self.np.arange(self.M) / self.M  # time intervals

        # Steering vector
        self.__init_steering_vector()

    def __init_steering_vector(self):

from base_tn import BaseTNComparisons


class SokalSneath2(BaseTNComparisons):
    """Class to calculate the Sokal-Sneath 2 index.

    n=2 formula:
        (2 * a + 2 * d)/(p + a + d)

    Attributes
    ----------
    fingerprints : {np.ndarray, int}
        Numpy array with the fingerprints that will be compared.
        The fingerprints must be also given as Numpy arrays.
        If an int is given it assumes that one is comparing
        n random fingerprints of infinite length.
    c_threshold : {None, 'dissimilar', int}
        Coincidence threshold.
    characters : list
        List with the possible characters.
    n_characters : int
        Number of different characters.

    Properties
    ----------
    n_fingerprints : int
        Number of fingerprints that will be compared.

    Methods
    -------
    __init__(self, fingerprints, c_threshold=None, w_factor="fraction")
        Initialize the object.
    assign_characters(characters)
        Assign characters.
    assign_fingerprints(fingerprints)
        Assign fingerprints.
    assign_c_threshold(c_threshold)
        Assign coincidence threshold.
    matches()
        Calculate the matches between the fingerprints.
    set_general_coincidences()
        Calculate the general coincidence matrix.
    set_reduced_coincidences()
        Calculate the reduced coincidence vector.
    set_matches()
        Calculate the matches between the fingerprints.
    set_d_vector()
        Calculate the d vector.
    set_w_factor(w_factor)
        Calculate weight factors.
    set_weighted_matches()
        Calculate weighted matches.
    set_counters()
        Calculate the counters.
    set_p()
        Calculate p.
    set_weighted_p()
        Calculate weighted p.
    ss2_1sim_wdis()
        Calculate the index with 1-sim-counters and with weighted denominator.
    ss2_1sim_dis()
         Calculate the index with 1-sim-counters and with unweighted denominator.
    """

    def __init__(self, fingerprints, characters=[0, 1], c_threshold=None, w_factor="fraction"):
        """Initialize the object.

        Parameters
        ----------
        fingerprints : np.ndrarray
            Numpy array with the fingerprints that will be compared.
            The fingerprints must be also given as Numpy arrays.
        c_threshold : {None, 'dissimilar', int}
            Coincidence threshold.
        w_factor : {"fraction", "power_n"}
            Type of weight function that will be used.
        """
        super().__init__(fingerprints, characters, c_threshold, w_factor)
        self.ss2_1sim_wdis()
        self.ss2_1sim_dis()

    def ss2_1sim_wdis(self):
        """Calculate the index with 1-sim-counters and with weighted denominator.

        Note
        ----
        (2 * w_a + 2 * w_d)/(w_p + w_a + w_d)
        """
        numerator = 2 * self.total_w_sim
        denominator = self.w_p + self.total_w_sim
        self.SS2_1sim_wdis = numerator/denominator

    def ss2_1sim_dis(self):
        """Calculate the index with 1-sim-counters and with unweighted denominator.

        Note
        ----
        (2 * w_a + 2 * w_d)/(p + a + d)
        """
        numerator = 2 * self.total_w_sim
        denominator = self.p + self.total_sim
        self.SS2_1sim_dis = numerator/denominator

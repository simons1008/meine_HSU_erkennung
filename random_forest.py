try:
    from time import ticks_us, ticks_diff
except ImportError:
    from time import time_ns

    def ticks_us(): return int(time_ns() * 1000)
    def ticks_diff(a, b): return a - b

class RandomForestClassifier:
    """
    # RandomForestClassifier(base_estimator=deprecated, bootstrap=True, ccp_alpha=0.0, class_name=RandomForestClassifier, class_weight=None, criterion=gini, estimator=DecisionTreeClassifier(), estimator_params=('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha'), max_depth=None, max_features=sqrt, max_leaf_nodes=20, max_samples=None, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, n_estimators=7, n_jobs=None, num_outputs=3, oob_score=False, package_name=everywhereml.sklearn.ensemble, random_state=None, template_folder=everywhereml/sklearn/ensemble, verbose=0, warm_start=False)
    """

    def __init__(self):
        """
        Constructor
        """
        self.latency = 0
        self.predicted_value = -1

        self.votes = [0.00000000000, 0.00000000000, 0.00000000000]

    def predict(self, x):
        """
        Predict output from input vector
        """
        self.predicted_value = -1
        started_at = ticks_us()

        self.votes = [0.00000000000, 0.00000000000, 0.00000000000]

        idx, score = self.tree0(x)
        self.votes[idx] += score
        
        idx, score = self.tree1(x)
        self.votes[idx] += score
        
        idx, score = self.tree2(x)
        self.votes[idx] += score
        
        idx, score = self.tree3(x)
        self.votes[idx] += score
        
        idx, score = self.tree4(x)
        self.votes[idx] += score
        
        idx, score = self.tree5(x)
        self.votes[idx] += score
        
        idx, score = self.tree6(x)
        self.votes[idx] += score

        # get argmax of votes
        max_vote = max(self.votes)
        self.predicted_value = next(i for i, v in enumerate(self.votes) if v == max_vote)

        self.latency = ticks_diff(ticks_us(), started_at)
        return self.predicted_value

    def latencyInMicros(self):
        """
        Get latency in micros
        """
        return self.latency

    def latencyInMillis(self):
        """
        Get latency in millis
        """
        return self.latency // 1000

    def tree0(self, x):
        """
        Random forest's tree #0
        """
        if x[124] <= 7.5:
            return 2, 6.0
        else:
            if x[51] <= 5.5:
                return 1, 3.0
            else:
                return 0, 1.0

    def tree1(self, x):
        """
        Random forest's tree #1
        """
        if x[137] <= 11.5:
            return 1, 4.0
        else:
            if x[243] <= 14.5:
                return 2, 2.0
            else:
                return 0, 4.0

    def tree2(self, x):
        """
        Random forest's tree #2
        """
        if x[37] <= 9.0:
            return 1, 4.0
        else:
            if x[121] <= 9.5:
                return 0, 2.0
            else:
                return 2, 4.0

    def tree3(self, x):
        """
        Random forest's tree #3
        """
        if x[38] <= 11.5:
            return 1, 5.0
        else:
            if x[124] <= 9.5:
                return 2, 2.0
            else:
                return 0, 3.0

    def tree4(self, x):
        """
        Random forest's tree #4
        """
        if x[108] <= 13.0:
            if x[105] <= 12.0:
                return 0, 2.0
            else:
                return 2, 5.0
        else:
            return 1, 3.0

    def tree5(self, x):
        """
        Random forest's tree #5
        """
        if x[232] <= 13.5:
            if x[126] <= 14.5:
                return 2, 2.0
            else:
                return 1, 3.0
        else:
            return 0, 5.0

    def tree6(self, x):
        """
        Random forest's tree #6
        """
        if x[230] <= 11.5:
            return 2, 7.0
        else:
            if x[99] <= 5.5:
                return 0, 2.0
            else:
                return 1, 1.0
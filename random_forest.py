try:
    from time import ticks_us, ticks_diff
except ImportError:
    from time import time_ns

    def ticks_us(): return int(time_ns() * 1000)
    def ticks_diff(a, b): return a - b

class RandomForestClassifier:
    """
    # RandomForestClassifier(base_estimator=deprecated, bootstrap=True, ccp_alpha=0.0, class_name=RandomForestClassifier, class_weight=None, criterion=gini, estimator=DecisionTreeClassifier(), estimator_params=('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha'), max_depth=None, max_features=sqrt, max_leaf_nodes=20, max_samples=None, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, n_estimators=20, n_jobs=None, num_outputs=3, oob_score=False, package_name=everywhereml.sklearn.ensemble, random_state=None, template_folder=everywhereml/sklearn/ensemble, verbose=0, warm_start=False)
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
        
        idx, score = self.tree7(x)
        self.votes[idx] += score
        
        idx, score = self.tree8(x)
        self.votes[idx] += score
        
        idx, score = self.tree9(x)
        self.votes[idx] += score
        
        idx, score = self.tree10(x)
        self.votes[idx] += score
        
        idx, score = self.tree11(x)
        self.votes[idx] += score
        
        idx, score = self.tree12(x)
        self.votes[idx] += score
        
        idx, score = self.tree13(x)
        self.votes[idx] += score
        
        idx, score = self.tree14(x)
        self.votes[idx] += score
        
        idx, score = self.tree15(x)
        self.votes[idx] += score
        
        idx, score = self.tree16(x)
        self.votes[idx] += score
        
        idx, score = self.tree17(x)
        self.votes[idx] += score
        
        idx, score = self.tree18(x)
        self.votes[idx] += score
        
        idx, score = self.tree19(x)
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
        if x[115] <= 12.0:
            if x[233] <= 13.5:
                if x[137] <= 10.0:
                    if x[84] <= 12.0:
                        return 1, 11.0
                    else:
                        return 0, 19.0
                else:
                    return 2, 22.0
            else:
                if x[201] <= 8.5:
                    if x[135] <= 11.5:
                        return 1, 11.0
                    else:
                        return 2, 22.0
                else:
                    return 0, 19.0
        else:
            if x[80] <= 10.5:
                return 2, 22.0
            else:
                return 1, 11.0

    def tree1(self, x):
        """
        Random forest's tree #1
        """
        if x[215] <= 13.0:
            if x[23] <= 14.0:
                return 1, 14.0
            else:
                return 2, 10.0
        else:
            if x[231] <= 8.5:
                return 1, 14.0
            else:
                return 0, 28.0

    def tree2(self, x):
        """
        Random forest's tree #2
        """
        if x[120] <= 14.0:
            if x[130] <= 13.5:
                if x[30] <= 13.0:
                    return 2, 17.0
                else:
                    return 0, 20.0
            else:
                if x[107] <= 11.0:
                    return 0, 20.0
                else:
                    return 1, 15.0
        else:
            return 2, 17.0

    def tree3(self, x):
        """
        Random forest's tree #3
        """
        if x[114] <= 13.5:
            if x[233] <= 6.0:
                return 2, 12.0
            else:
                if x[217] <= 1.5:
                    return 2, 12.0
                else:
                    return 0, 20.0
        else:
            if x[132] <= 7.0:
                if x[230] <= 13.0:
                    return 2, 12.0
                else:
                    return 0, 20.0
            else:
                return 1, 20.0

    def tree4(self, x):
        """
        Random forest's tree #4
        """
        if x[214] <= 14.5:
            if x[52] <= 8.5:
                if x[244] <= 14.0:
                    return 2, 18.0
                else:
                    return 1, 15.0
            else:
                return 2, 18.0
        else:
            return 0, 19.0

    def tree5(self, x):
        """
        Random forest's tree #5
        """
        if x[214] <= 14.5:
            if x[108] <= 14.0:
                if x[215] <= 14.5:
                    return 2, 11.0
                else:
                    return 1, 18.0
            else:
                if x[226] <= 14.5:
                    return 2, 11.0
                else:
                    return 1, 18.0
        else:
            return 0, 23.0

    def tree6(self, x):
        """
        Random forest's tree #6
        """
        if x[229] <= 14.5:
            if x[98] <= 6.5:
                return 2, 11.0
            else:
                if x[122] <= 4.0:
                    return 0, 28.0
                else:
                    if x[20] <= 10.5:
                        return 2, 11.0
                    else:
                        return 1, 13.0
        else:
            if x[199] <= 12.0:
                if x[91] <= 10.0:
                    return 2, 11.0
                else:
                    return 1, 13.0
            else:
                return 0, 28.0

    def tree7(self, x):
        """
        Random forest's tree #7
        """
        if x[104] <= 11.5:
            if x[200] <= 8.0:
                return 1, 12.0
            else:
                return 0, 24.0
        else:
            if x[140] <= 12.5:
                if x[217] <= 13.5:
                    if x[24] <= 9.5:
                        return 1, 12.0
                    else:
                        return 2, 16.0
                else:
                    return 0, 24.0
            else:
                return 1, 12.0

    def tree8(self, x):
        """
        Random forest's tree #8
        """
        if x[23] <= 13.5:
            return 1, 18.0
        else:
            if x[120] <= 12.0:
                return 0, 23.0
            else:
                if x[88] <= 12.0:
                    return 0, 23.0
                else:
                    if x[34] <= 14.5:
                        return 2, 11.0
                    else:
                        return 1, 18.0

    def tree9(self, x):
        """
        Random forest's tree #9
        """
        if x[216] <= 13.5:
            if x[137] <= 12.5:
                if x[254] <= 10.0:
                    return 2, 15.0
                else:
                    return 1, 16.0
            else:
                return 2, 15.0
        else:
            if x[54] <= 8.0:
                return 1, 16.0
            else:
                return 0, 21.0

    def tree10(self, x):
        """
        Random forest's tree #10
        """
        if x[131] <= 14.5:
            if x[117] <= 14.5:
                return 0, 26.0
            else:
                if x[115] <= 14.0:
                    return 2, 13.0
                else:
                    return 1, 13.0
        else:
            if x[194] <= 0.5:
                return 2, 13.0
            else:
                return 1, 13.0

    def tree11(self, x):
        """
        Random forest's tree #11
        """
        if x[214] <= 14.0:
            if x[22] <= 14.5:
                return 1, 16.0
            else:
                return 2, 14.0
        else:
            return 0, 22.0

    def tree12(self, x):
        """
        Random forest's tree #12
        """
        if x[117] <= 14.5:
            if x[213] <= 9.5:
                if x[136] <= 14.5:
                    return 1, 16.0
                else:
                    return 2, 12.0
            else:
                if x[20] <= 6.0:
                    return 1, 16.0
                else:
                    return 0, 24.0
        else:
            return 2, 12.0

    def tree13(self, x):
        """
        Random forest's tree #13
        """
        if x[214] <= 14.5:
            if x[137] <= 13.5:
                if x[184] <= 11.0:
                    return 2, 17.0
                else:
                    return 1, 12.0
            else:
                return 2, 17.0
        else:
            return 0, 23.0

    def tree14(self, x):
        """
        Random forest's tree #14
        """
        if x[130] <= 13.5:
            if x[103] <= 13.0:
                return 0, 17.0
            else:
                return 2, 19.0
        else:
            if x[93] <= 10.5:
                if x[124] <= 0.5:
                    return 0, 17.0
                else:
                    return 2, 19.0
            else:
                return 1, 16.0

    def tree15(self, x):
        """
        Random forest's tree #15
        """
        if x[118] <= 13.5:
            if x[105] <= 12.0:
                if x[131] <= 14.5:
                    return 0, 19.0
                else:
                    return 1, 14.0
            else:
                if x[98] <= 8.5:
                    return 0, 19.0
                else:
                    return 1, 14.0
        else:
            return 2, 19.0

    def tree16(self, x):
        """
        Random forest's tree #16
        """
        if x[214] <= 14.5:
            if x[146] <= 11.5:
                if x[188] <= 1.0:
                    return 1, 18.0
                else:
                    return 2, 10.0
            else:
                if x[19] <= 11.5:
                    return 2, 10.0
                else:
                    return 1, 18.0
        else:
            return 0, 24.0

    def tree17(self, x):
        """
        Random forest's tree #17
        """
        if x[24] <= 13.5:
            return 1, 16.0
        else:
            if x[216] <= 14.5:
                return 2, 20.0
            else:
                return 0, 16.0

    def tree18(self, x):
        """
        Random forest's tree #18
        """
        if x[103] <= 14.5:
            if x[28] <= 14.5:
                if x[37] <= 6.5:
                    return 1, 13.0
                else:
                    return 0, 21.0
            else:
                if x[116] <= 1.5:
                    if x[248] <= 14.5:
                        return 1, 13.0
                    else:
                        return 0, 21.0
                else:
                    return 1, 13.0
        else:
            if x[52] <= 0.5:
                return 1, 13.0
            else:
                if x[132] <= 3.5:
                    if x[135] <= 8.5:
                        return 0, 21.0
                    else:
                        return 2, 18.0
                else:
                    return 2, 18.0

    def tree19(self, x):
        """
        Random forest's tree #19
        """
        if x[24] <= 13.5:
            return 1, 19.0
        else:
            if x[120] <= 14.5:
                if x[190] <= 11.5:
                    return 2, 17.0
                else:
                    if x[131] <= 14.5:
                        return 0, 16.0
                    else:
                        return 1, 19.0
            else:
                return 2, 17.0
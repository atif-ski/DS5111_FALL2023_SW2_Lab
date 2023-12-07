'''
Module Doctring
'''
class Perceptron:
    '''
    doctring to get rid of C0114
    '''

    def __init__(self):
        '''
        Intialize
        '''
        self._weights = None

    def train(self, inputs, labels):
        '''
        C0116
        '''
        dummied_inputs = [var_x + [-1] for var_x in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])

        for _ in range(5000):
            for some_input, label in zip(dummied_inputs, labels):
                label_delta = label - self.predict(some_input)
                for index, val  in enumerate(some_input):
                    self._weights[index] += .1 * val * label_delta
    def predict(self, another_input):
        '''
        C0116
        '''
        if len(another_input) == 0:
            return None
        another_input = another_input + [-1]
        return int(0 < sum([x[0]*x[1] for x in zip(self._weights, another_input)])) #pylint: disable=R1728

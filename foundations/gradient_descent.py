class Solution:
    @staticmethod
    def f(x):
        return x ** 2

    @staticmethod
    def df(x):
        return 2 * x

    def get_minimizer(self, iterations, learning_rate, init):
        x = init

        for _ in range(iterations):
            x -= learning_rate * self.df(x)

        return round(x, 5)
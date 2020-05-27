class Evaluator:
    def zip_evaluate(self, coef, words):
        if len(coef) != len(words):
            return -1
        nbr = [i * len(j) for i, j in zip(coef, words)]
        ret = sum(nbr)
        print(ret)

    def enumerate_evaluate(self, coef, words):
        if len(coef) != len(words):
            return -1
        ret = [cvalue * len(words[i]) for i, cvalue in enumerate(coef)]
        ret = sum(ret)
        print(ret)


print("EVALUATE")
words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
evalu = Evaluator()
evalu.zip_evaluate(coefs, words)
print("ENUMERATE")
evalu.enumerate_evaluate(coefs, words)

words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
evalu.enumerate_evaluate(coefs, words)

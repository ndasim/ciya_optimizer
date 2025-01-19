from tester import Tester

tester = Tester()
params = tester.get_params()

# Test the strategy with the random params
random_params = tester.get_random_params(params)

# Test the strategy with the random params
score = tester.test(random_params)

print(score)

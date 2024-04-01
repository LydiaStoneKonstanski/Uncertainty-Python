import string
from typing import Union
import random

list1 = ["Red"] * 4 + ["Green"] * 4
list2 = ["Red"] * 4 + ["Green"] * 4 + ["Yellow"] * 10
list3 = ["Green"] * 4 + ["Yellow"] * 10
list4 = ["Red"] * 3 + ["Blue"] * 4
bag1 = tuple(list1)
bag2 = tuple(list2)
bag3 = tuple(list3)
bag4 = tuple(list4)

def probability(successes: Union[int, float], possibilities: Union[int, float])-> float:
    try:
        return(successes/possibilities)
    except ZeroDivisionError:
        return "You can't divide by zero!"


def pick_token(container):
    return random.choice(container)
#print(bag2)

def probability_of_tokens(container: tuple, num_of_reps: int, desired_token_color: str):
    samples = [random.choice(container) for _ in range(num_of_reps)]
    p_of_tokens = (sum(token == desired_token_color for token in samples)) / num_of_reps
    #if len(samples) == num_of_reps:
    return p_of_tokens
    #return samples
    print(probability_of_tokens(bag2, 10000, "Red"))
    #else:
        #print("pick_samples not ample")


def sample_experiment(bag):
    """
    This samples a token from a given bag and then
    selects a coin with a given probability.

    If the sampled token is red then the probability
    of selecting heads is 2/3 otherwise it is 1/2.

    This function returns both the selected token
    and the coin face.
    """
    selected_token = pick_token(container=bag)

    if selected_token == "Red":
        probability_of_selecting_heads = 4 / 5
    else:
        probability_of_selecting_heads = 2 / 5

    if random.random() < probability_of_selecting_heads:
        coin = "Heads"
    else:
        coin = "Tails"
    return selected_token, coin
print(sample_experiment(bag2))

def samples_with_heads(bag, num_of_reps):
    samples = [sample_experiment(bag) for i in range(num_of_reps)]
    return sum(coin == "Heads" for token, coin in samples) / num_of_reps
#print(samples_with_heads(bag2, 10000))
#Expect around 0.56944444

def prob_of_red_if_heads(bag):
    s = [(token, coin) for token, coin in sample_experiment(bag) if coin == "Heads"]
    return sum(token == "Red" for token, coin in s) / len(s)
print(prob_of_red_if_heads(bag2))
# #Expect around 0.48780488


print("1)\n" + "Probability of 2/7 is " + str(probability(2,7)))
print("Probability of 1/10 is " + str(probability(1,10)))
print("Probability of 1/100 is " + str(probability(1,100)))
print("Probability of 1/100 is " + str(probability(1,1)))

print("2)\n" + "Probability of picking a red token from bag 1 is " + str(probability_of_tokens(bag1, 10000, "Red")))
print("Probability of picking a red token from bag 2 is " + str(probability_of_tokens(bag2, 10000, "Red")))
print("Probability of picking a red token from bag 3 is " + str(probability_of_tokens(bag3, 10000, "Red")))

print("3)\n" + "Probability of picking a red token from bag 4 is " + str(probability_of_tokens(bag4, 10000, "Red")))
print("Probability of Heads is " + str(samples_with_heads(bag4, 10000)))
#print("Probability of Red with Heads is " + str(prob_of_red_if_heads(bag4)))

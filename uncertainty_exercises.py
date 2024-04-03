import string
from typing import Union
import random

list1 = ["Red"] * 4 + ["Green"] * 4
list2 = ["Red"] * 4 + ["Green"] * 4 + ["Yellow"] * 10
list3 = ["Green"] * 4 + ["Yellow"] * 10
list4 = ["Red"] * 3 + ["Blue"] * 4
list5 = ["Car"] * 3 + ["Bike"] * 2 + ["Foot"] * 1
bag1 = tuple(list1)
bag2 = tuple(list2)
bag3 = tuple(list3)
bag4 = tuple(list4)
token_dict = {"Red":4.0/5.0, "Blue":2.0/5.0}
commute = tuple(list5)
commute_dict = {"Car":1.0/5.0, "Bike":2.0/5.0, "Foot":1.0/10.0}

def probability(successes: Union[int, float], possibilities: Union[int, float])-> float:
    try:
        return(successes/possibilities)
    except ZeroDivisionError:
        return "You can't divide by zero!"

def first_pick(container)-> str:
    return random.choice(container)
#print(bag2)

def prob_of_event_a(container: tuple, num_of_reps: int, desired_pick: str)-> float:
    '''Generates random samples from a given tuple of choices and calculates simple probability.
    Returns the probability of your color of choice.'''
    samples = [first_pick(container) for n in range(num_of_reps)]
    p_of_first_pick = (sum(pick == desired_pick for pick in samples)) / num_of_reps
    return p_of_first_pick

def prob_of_event_b(container: tuple, picks_n_chances_dict: dict, key: str, value: int):
    '''This is a more utilitarian version of the sample experiment function available in the
    tutorial. It does the same thing, drawing a sample and returning it with an associated
    conditional probability.'''
    pick = first_pick(container)
    b = 1
    if picks_n_chances_dict.get(key) == pick:
        b = value
    event = random.random() < b
    return pick, event

def prob_event_b_is_true(container: tuple, num_of_reps: int, picks_n_chances_dict: dict, key: str, value: float):
    '''Unchanged from the original, except for variable names and the addition of the dict. Given a tuple, a dict,
    as well as the key and value to look for, returns probability of True for the conditional probability.'''
    samples = [prob_of_event_b(container, picks_n_chances_dict, key, value) for n in range(num_of_reps)]
    return sum(event == 1 for pick, event in samples) / num_of_reps

def prob_of_a_and_b(container: tuple, picks_n_chances_dict: dict, key: str, value: float, num_of_reps):
    '''Unchanged from the original, except variable names and the addition of the dict.
    Given 5 arguments, this function calculates the conditional likelihood of event b in the case of a.'''
    b = [prob_of_event_b(container, picks_n_chances_dict, key, value) for n in range(num_of_reps)]
    t = [(pick, event) for pick, event in b if event == 1]
    return sum(pick == key for pick, event in t) / len(t)

drivers = prob_of_a_and_b(commute, commute_dict, "Car", 1/5, 10000)
bikers = prob_of_a_and_b(commute, commute_dict, "Bike", 2/5, 10000)

print("1)\n" + "Probability of 2/7 is " + str(probability(2,7)))
print("Probability of 1/10 is " + str(probability(1,10)))
print("Probability of 1/100 is " + str(probability(1,100)))
print("Probability of 1/100 is " + str(probability(1,1)))

print("2)\n" + "Probability of picking a red token from bag 1 is " + str(prob_of_event_a(bag1, 10000, "Red")))
print("Probability of picking a red token from bag 2 is " + str(prob_of_event_a(bag2, 10000, "Red")))
print("Probability of picking a red token from bag 3 is " + str(prob_of_event_a(bag3, 10000, "Red")))

print("3)\n" + "Probability of picking a red token from bag 4 is " + str(prob_of_event_a(bag4, 10000, "Red")))
print("Probability of Heads is " + str(prob_event_b_is_true(bag4, 10000, token_dict, "Red", 4/5 )))
print("Probability of Red with Heads is " + str(prob_of_a_and_b(bag4, token_dict, "Red", 4/5, 10000 )))

print("4)\n" + "Probability of a commuter being on foot and late is " + str(probability(1,3)*probability(1,10)))
print("Probability a commuter is not late is " + str((1-probability(4,5)) * (1-(probability(3,5))) * (1-probability(9,10))))
print("Probability a commuter is late and NOT on foot is " + str(drivers + bikers))

# def probability_of_tokens(container: tuple, num_of_reps: int, desired_token_color: str):
#     '''First draft based on the tutorial: generates random samples of token draws and
#     calculates the probability of the token being your color of choice.'''

#     samples = [random.choice(container) for _ in range(num_of_reps)]
#     p_of_tokens = (sum(token == desired_token_color for token in samples)) / num_of_reps
#     return p_of_tokens
#     #print(probability_of_tokens(bag2, 10000, "Red"))

# def sample_experiment(bag):
#     """
#     This samples a token from a given bag and then
#     selects a coin with a given probability.
#
#     If the sampled token is red then the probability
#     of selecting heads is 2/3 otherwise it is 1/2.
#
#     This function returns both the selected token
#     and the coin face.
#     """
#     selected_token = first_pick(container=bag)
#
#     if selected_token == "Red":
#         probability_of_selecting_heads = 4 / 5
#         #probability_of_selecting_heads = 2 /3
#     else:
#         probability_of_selecting_heads = 2 / 5
#         #probability_of_selecting_heads = 1 / 2
#     if random.random() < probability_of_selecting_heads:
#         coin = "Heads"
#     else:
#         coin = "Tails"
#     return selected_token, coin
#print(sample_experiment(bag2))

# def samples_with_heads(bag, num_of_reps):
#     samples = [sample_experiment(bag) for _ in range(num_of_reps)]
#     return sum(coin == "Heads" for token, coin in samples) / num_of_reps
#print(samples_with_heads(bag2, 10000))
#Expect around 0.56944444

# def prob_of_red_if_heads(bag, num_of_reps):
#     s = [ sample_experiment(bag) for _ in range(num_of_reps)]
#     h = [(token, coin) for token, coin in s if coin == "Heads"]
#     return sum(token == "Red" for token, coin in h) / len(h)

# bag_t = ["Red"] * 5 + ["Blue"] * 7
# print(prob_of_red_if_heads(bag_t, 1000000))


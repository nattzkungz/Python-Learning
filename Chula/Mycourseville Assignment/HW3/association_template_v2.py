from itertools import permutations, combinations

#############################################
# FUNCTIONS (FILL CODE IN THIS PART)
#############################################
def read_transactions(file):
    # Input: read transactions from file, where each row refers to one transaction.
    # Return: (1) a list of sets (transactions) and (2) a set of all products
    
    # the code below can be deleted. It just gives an idea of outputs.
    import csv
    all_transactions = open(file, "r")
    check_dup = []
    transactions = []
    for _ in csv.reader(all_transactions):
        transactions.append(set(_))
        for i in _:
            if i not in check_dup:
                check_dup.append(i)
    return transactions, check_dup

def generate_frequent_itemsets(transactions, min_support=0.5):
    # Input:
    #    transactions: a list of transaction sets.
    #    min_support: % of minimum support that must be converted to frequency with ROUND to be integer.
    # Return: "frequent_itemsets": a dictionary that stores itemsets whose frequency has passsed minimum frequency.
    #    key is a tuple of items, value is frequency
    # the code below can be deleted. It just gives an idea of outputs.
    item_freq = {}
    for i in transactions:
        for _ in i:
            if _ not in item_freq:
                item_freq[_] = 1
            else:
                item_freq[_] += 1

    z = list(combinations(item_freq, 2))
    print(z)
    print(item_freq)

def generate_association_rules(frequent_itemsets, n, min_confidence=0.7):
    # Input:
    #    frequent_itemsets: a dictionary that stores itemsets whose frequency has passsed minimum frequency.
    #    n: #total_transaction
    #    min_confidence: minimum confidence in %
    # Return: rules: association rules whose confidence has passed the minimum confidence.
    #         It is in form of dictionary: key is "rule-string" & value is a list of [conf,sup].
    #         Confidence and support must be rounded with 4 dicimal points.
    #         All rules must be sorted by confidence and support in descending orders.
    #            If they are still equal, they must be sorted by alphabettically order "rule-string"
    
    # the code below can be deleted. It just gives an idea of outputs.
    rules = {'banana=>coconut': [1.0, 0.6],
             'coconut=>banana': [0.75, 0.6]}
    return rules

def recommend_best_rule(input_set, rules):
    # Input:
    #    input_set: an input string to be recommended (LHS)
    #    rules: association rules
    # Return:
    #    output_set: a recommended string (RHS) with the highest score (the first one from the rules).
    #    if LHS is not founded, print 'NO RECOMMEND'
    
    # the code below can be deleted. It just gives an idea of outputs.
    input_set =  'banana'
    output_set = 'coconut'
    return output_set

#############################################
# GIVEN FUNCTIONS (DO NOT CHANGE THIS PART)
#############################################
def show_first_itemsets(itemsets,n):
    # if n=0, show all
    i = 0
    for k,v in itemsets.items():
        i += 1
        idx = "Itemset"+str(i)+")"
        print(idx,k, ":", v)
        if n != 0 and i >= n:
            break
        
def show_first_rules(rules,n):
    # if n=0, show all
    i = 0
    for k,v in rules.items():
        i += 1
        idx = "Rule"+str(i)+")"
        print(idx,k,":", v)
        if n != 0 and i >= n:
            break

#############################################
# MAIN (DO NOT CHANGE THIS PART)
#############################################

# Step1: read transactions
transactions,products = read_transactions('/Users/thanakrittr/Desktop/VSCode/Python-Learning/Chula/Mycourseville Assignment/HW3/transactions.csv')
print('#transactions = ',len(transactions))
print('#products = ',len(products))

# Step2: generate frquent itemsets
print('Enter minimum support & confidence:')
min_sup,min_conf = [float(e) for e in input().split()]
frequent_itemsets = generate_frequent_itemsets(transactions, min_sup)
print('#frequent_itemsets = ',len(frequent_itemsets))
show_first_itemsets(frequent_itemsets, 20)

# Step3: generate association rules
rules = generate_association_rules(frequent_itemsets, len(transactions), min_conf)
show_first_rules(rules, 20)

# Step4: recommend
print('Enter query products to be recommended (q to quit):')
input_set = input()
while input_set.lower() != 'q':
    print(recommend_best_rule(input_set, rules))
    print('Enter query products to be recommended (q to quit):')
    input_set = input()
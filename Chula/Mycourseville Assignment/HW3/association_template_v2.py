from itertools import permutations, combinations

#############################################
# FUNCTIONS (FILL CODE IN THIS PART)
#############################################

def read_transactions(file):
    # Input: read transactions from file, where each row refers to one transaction.
    # Return: (1) a list of sets (transactions) and (2) a set of all products
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

    item_freq = {}
    for i in transactions:
        for _ in i:
            if _ not in item_freq:
                item_freq[_] = 1
            else:
                item_freq[_] += 1

    all_comb = list(combinations(item_freq, 2))

    for payment in transactions:
        for comb in all_comb:
            check = []
            for item in comb:
                if item in payment and item not in check:
                    check.append(item)
            if len(check) == 2:
                if tuple(check) not in item_freq:
                    item_freq[tuple(check)] = 1
                elif tuple(check) in item_freq:
                    item_freq[tuple(check)] += 1
    
    re_this = {}
    for bill in item_freq:
        if item_freq[bill]/len(transactions) >= min_support:
            re_this[bill] = item_freq[bill]

    return re_this


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
    all_itemsets = {}
    itemset_with_permutations = 
    
    for itemset in frequent_itemsets:
        if len(itemset) == 2:
            support = round(frequent_itemsets[itemset]/n, 4)
            for i in frequent_itemsets:
                if itemset[0] == i:
                    item_count = frequent_itemsets[i]
            confidence = round(frequent_itemsets[itemset]/item_count, 4)
            text = itemset[0] + "=>" + itemset[1]
            all_itemsets[text] = [confidence, support]
    
    sorted_itemsets_list = sorted(all_itemsets, key=all_itemsets.get, reverse=True)

    sorted_itemsets_dict = {}

    for value in sorted_itemsets_list:
        sorted_itemsets_dict[value] = all_itemsets[value]
    
    return sorted_itemsets_dict


def recommend_best_rule(input_set, rules):
    # Input:
    #    input_set: an input string to be recommended (LHS)
    #    rules: association rules
    # Return:
    #    output_set: a recommended string (RHS) with the highest score (the first one from the rules).
    #    if LHS is not founded, print 'NO RECOMMEND'
    
    # the code below can be deleted. It just gives an idea of outputs.
    
    split_rules = []
    for suggestion in rules:
        split_rules.append(suggestion.split("=>"))

    re_this = "NO RECOMMEND"
    for items in split_rules:
        if items[0] == input_set:
            re_this = items[1]
    
    return re_this
        

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


#############################################

# Step1: read transactions
transactions,products = read_transactions('Chula/Mycourseville Assignment/HW3/transactions.csv')
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
print('#rules = ',len(rules))
show_first_rules(rules, 20)
print()

# Step4: recommend
print('Enter query products to be recommended (q to quit):')
input_set = input()
while input_set.lower() != 'q':
    print(recommend_best_rule(input_set, rules))
    print('Enter query products to be recommended (q to quit):')
    input_set = input()
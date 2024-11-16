# # # # import random

# # # # foundRoyal = False
# # # # runCount = 0
# # # # while foundRoyal is False:
# # # #     deck = []
# # # #     number = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
# # # #     suit = ["Club", "Spade", "Heart", "Diamond"]

# # # #     while len(deck) < 52:
# # # #         card = (random.choice(number), random.choice(suit))
# # # #         if card in deck:
# # # #             pass
# # # #         else:
# # # #             deck.append(card)

# # # #     player1 = []
# # # #     player2 = []
# # # #     player3 = []
# # # #     player4 = []

# # # #     for i in range(13):
# # # #         selectedCard = random.choice(deck)
# # # #         player1.append(selectedCard)
# # # #         deck.remove(selectedCard)
# # # #         selectedCard = random.choice(deck)
# # # #         player2.append(selectedCard)
# # # #         deck.remove(selectedCard)
# # # #         selectedCard = random.choice(deck)
# # # #         player3.append(selectedCard)
# # # #         deck.remove(selectedCard)
# # # #         selectedCard = random.choice(deck)
# # # #         player4.append(selectedCard)
# # # #         deck.remove(selectedCard)

# # # #     royalCombination1 = [("A", "Spade"), ("K", "Spade"), ("Q", "Spade"), ("J", "Spade"), ("10", "Spade")]
# # # #     royalCombination2 = [("A", "Heart"), ("K", "Heart"), ("Q", "Heart"), ("J", "Heart"), ("10", "Heart")]
# # # #     royalCombination3 = [("A", "Club"), ("K", "Club"), ("Q", "Club"), ("J", "Club"), ("10", "Club")]
# # # #     royalCombination4 = [("A", "Diamond"), ("K", "Diamond"), ("Q", "Diamond"), ("J", "Diamond"), ("10", "Diamond")]

# # # #     royalCheck1 = True
# # # #     for card in royalCombination1:
# # # #         if card not in player1:
# # # #             royalCheck1 = False

# # # #     royalCheck2 = True
# # # #     for card in royalCombination2:
# # # #         if card not in player2:
# # # #             royalCheck2 = False

# # # #     royalCheck3 = True
# # # #     for card in royalCombination3:
# # # #         if card not in player3:
# # # #             royalCheck3 = False

# # # #     royalCheck4 = True
# # # #     for card in royalCombination4:
# # # #         if card not in player4:
# # # #             royalCheck4 = False

# # # #     if royalCheck1 is True or royalCheck2 is True or royalCheck3 is True or royalCheck4 is True:
# # # #         foundRoyal = True
# # # #     print(runCount)
# # # #     runCount += 1

# # # # print(player1, player2, player3, player4)
# # # # print(runCount)
# # # ################################################# from gpt
# # # # import random

# # # # def draw_hand(deck, hand_size=13):
# # # #     """Draw a hand of 'hand_size' cards from the deck."""
# # # #     return random.sample(deck, hand_size)

# # # # def has_double_royal_flush_and_three_of_a_kind(hand):
# # # #     """Check if the hand contains both a double royal flush and a three of a kind."""
# # # #     # Separate hand by rank and suit
# # # #     rank_count = {}
# # # #     suit_count = {}
# # # #     for card in hand:
# # # #         rank, suit = card
# # # #         rank_count[rank] = rank_count.get(rank, 0) + 1
# # # #         suit_count[suit] = suit_count.get(suit, 0) + 1
    
# # # #     # Check for double royal flush
# # # #     royal_ranks = {'A', 'K', 'Q', 'J', '10'}
# # # #     royal_flush_suits = []
# # # #     for suit in suit_count:
# # # #         suit_cards = {rank for rank, s in hand if s == suit}
# # # #         if suit_cards >= royal_ranks:
# # # #             royal_flush_suits.append(suit)
    
# # # #     # We need exactly two suits with a royal flush
# # # #     if len(royal_flush_suits) < 2:
# # # #         return False
    
# # # #     # Check for a three of a kind in a non-royal rank
# # # #     for rank, count in rank_count.items():
# # # #         if count == 3 and rank not in royal_ranks:
# # # #             return True  # Three of a kind found in a non-royal rank
    
# # # #     return False

# # # # # Initialize deck and set up simulation
# # # # deck = [(rank, suit) for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# # # #         for suit in ['hearts', 'diamonds', 'clubs', 'spades']]
# # # # trials = 0
# # # # found = 0
# # # # max_trials = 100000000000000000000000000000000  # Number of trials to simulate

# # # # for _ in range(max_trials):
# # # #     hand = draw_hand(deck)
# # # #     if has_double_royal_flush_and_three_of_a_kind(hand):
# # # #         found += 1
# # # #         print(f"Found a matching hand: {hand}")
# # # #     trials += 1

# # # # # Probability estimation
# # # # probability = found / trials if trials > 0 else 0
# # # # print(f"After {trials} trials, found {found} hands with a double royal flush and a three of a kind.")
# # # # print(f"Estimated probability: {probability:.10f} ({probability * 100:.8f}%)")
# # # ####################################### multi core process

# # # import random
# # # import multiprocessing
# # # from concurrent.futures import ProcessPoolExecutor

# # # def draw_hand(deck, hand_size=13):
# # #     """Draw a hand of 'hand_size' cards from the deck."""
# # #     return random.sample(deck, hand_size)

# # # def has_double_royal_flush_and_three_of_a_kind(hand):
# # #     """Check if the hand contains both a double royal flush and a three of a kind."""
# # #     # Separate hand by rank and suit
# # #     rank_count = {}
# # #     suit_count = {}
# # #     for card in hand:
# # #         rank, suit = card
# # #         rank_count[rank] = rank_count.get(rank, 0) + 1
# # #         suit_count[suit] = suit_count.get(suit, 0) + 1
    
# # #     # Check for double royal flush
# # #     royal_ranks = {'A', 'K', 'Q', 'J', '10'}
# # #     royal_flush_suits = []
# # #     for suit in suit_count:
# # #         suit_cards = {rank for rank, s in hand if s == suit}
# # #         if suit_cards >= royal_ranks:
# # #             royal_flush_suits.append(suit)
    
# # #     # We need exactly two suits with a royal flush
# # #     if len(royal_flush_suits) < 2:
# # #         return False
    
# # #     # Check for a three of a kind in a non-royal rank
# # #     for rank, count in rank_count.items():
# # #         if count == 3 and rank not in royal_ranks:
# # #             return True  # Three of a kind found in a non-royal rank
    
# # #     return False

# # # def simulate_trials(num_trials, deck):
# # #     """Run a specified number of trials and count hands with the double royal flush + three of a kind."""
# # #     found = 0
# # #     for _ in range(num_trials):
# # #         hand = draw_hand(deck)
# # #         if has_double_royal_flush_and_three_of_a_kind(hand):
# # #             found += 1
# # #     return found

# # # def main(total_trials, num_workers=8):
# # #     # Set multiprocessing start method to "spawn" for M1 optimization
# # #     multiprocessing.set_start_method("spawn", force=True)
    
# # #     # Initialize deck
# # #     deck = [(rank, suit) for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# # #             for suit in ['hearts', 'diamonds', 'clubs', 'spades']]
    
# # #     # Determine trials per worker
# # #     trials_per_worker = total_trials // num_workers

# # #     # Use ProcessPoolExecutor for parallel execution with "spawn" method
# # #     with ProcessPoolExecutor(max_workers=num_workers) as executor:
# # #         # Run simulations in parallel
# # #         futures = [executor.submit(simulate_trials, trials_per_worker, deck) for _ in range(num_workers)]
# # #         results = [future.result() for future in futures]

# # #     # Aggregate results
# # #     found = sum(results)
# # #     probability = found / total_trials if total_trials > 0 else 0
    
# # #     print(f"After {total_trials} trials with {num_workers} workers, found {found} hands with a double royal flush and a three of a kind.")
# # #     print(f"Estimated probability: {probability:.10f} ({probability * 100:.8f}%)")

# # # # Run the main function with a specified number of total trials and CPU cores
# # # if __name__ == "__main__":
# # #     main(total_trials=10000000000000000000000000000000000000000000000, num_workers=8)  # Adjust total_trials based on available resources

# # import random
# # import multiprocessing
# # import psutil
# # import time
# # from concurrent.futures import ProcessPoolExecutor
# # from threading import Thread

# # def draw_hand(deck, hand_size=13):
# #     """Draw a hand of 'hand_size' cards from the deck."""
# #     return random.sample(deck, hand_size)

# # def has_double_royal_flush_and_three_of_a_kind(hand):
# #     """Check if the hand contains both a double royal flush and a three of a kind."""
# #     # Separate hand by rank and suit
# #     rank_count = {}
# #     suit_count = {}
# #     for card in hand:
# #         rank, suit = card
# #         rank_count[rank] = rank_count.get(rank, 0) + 1
# #         suit_count[suit] = suit_count.get(suit, 0) + 1
    
# #     # Check for double royal flush
# #     royal_ranks = {'A', 'K', 'Q', 'J', '10'}
# #     royal_flush_suits = []
# #     for suit in suit_count:
# #         suit_cards = {rank for rank, s in hand if s == suit}
# #         if suit_cards >= royal_ranks:
# #             royal_flush_suits.append(suit)
    
# #     # We need exactly two suits with a royal flush
# #     if len(royal_flush_suits) < 2:
# #         return False
    
# #     # Check for a three of a kind in a non-royal rank
# #     for rank, count in rank_count.items():
# #         if count == 3 and rank not in royal_ranks:
# #             return True  # Three of a kind found in a non-royal rank
    
# #     return False

# # def simulate_trials(num_trials, deck):
# #     """Run a specified number of trials and count hands with the double royal flush + three of a kind."""
# #     found = 0
# #     for _ in range(num_trials):
# #         hand = draw_hand(deck)
# #         if has_double_royal_flush_and_three_of_a_kind(hand):
# #             found += 1
# #     return found

# # def monitor_cpu_utilization(interval=1):
# #     """Monitor and display CPU utilization in real-time."""
# #     try:
# #         while True:
# #             # Get the current CPU utilization and print it
# #             cpu_percent = psutil.cpu_percent(interval=interval)
# #             print(f"CPU Utilization: {cpu_percent}%")
# #     except KeyboardInterrupt:
# #         # Exit monitoring when the main program completes
# #         print("Stopped CPU monitoring.")

# # def main(total_trials, num_workers=8):
# #     # Set multiprocessing start method to "spawn" for M1 optimization
# #     multiprocessing.set_start_method("spawn", force=True)
    
# #     # Initialize deck
# #     deck = [(rank, suit) for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# #             for suit in ['hearts', 'diamonds', 'clubs', 'spades']]
    
# #     # Determine trials per worker
# #     trials_per_worker = total_trials // num_workers

# #     # Start the CPU monitoring thread
# #     cpu_monitor_thread = Thread(target=monitor_cpu_utilization)
# #     cpu_monitor_thread.daemon = True  # Daemonize thread to exit with the main program
# #     cpu_monitor_thread.start()

# #     # Use ProcessPoolExecutor for parallel execution with "spawn" method
# #     with ProcessPoolExecutor(max_workers=num_workers) as executor:
# #         # Run simulations in parallel
# #         futures = [executor.submit(simulate_trials, trials_per_worker, deck) for _ in range(num_workers)]
# #         results = [future.result() for future in futures]

# #     # Aggregate results
# #     found = sum(results)
# #     probability = found / total_trials if total_trials > 0 else 0
    
# #     print(f"After {total_trials} trials with {num_workers} workers, found {found} hands with a double royal flush and a three of a kind.")
# #     print(f"Estimated probability: {probability:.10f} ({probability * 100:.8f}%)")

# # # Run the main function with a specified number of total trials and CPU cores
# # if __name__ == "__main__":
# #     main(total_trials=1000000, num_workers=8)  # Adjust total_trials based on available resources

import random
import multiprocessing
import psutil
import time
from concurrent.futures import ProcessPoolExecutor
from threading import Thread

def draw_hand(deck, hand_size=13):
    """Draw a hand of 'hand_size' cards from the deck."""
    return random.sample(deck, hand_size)

def has_double_royal_flush_and_three_of_a_kind(hand):
    """Check if the hand contains both a double royal flush and a three of a kind."""
    # Separate hand by rank and suit
    rank_count = {}
    suit_count = {}
    for card in hand:
        rank, suit = card
        rank_count[rank] = rank_count.get(rank, 0) + 1
        suit_count[suit] = suit_count.get(suit, 0) + 1
    
    # Check for double royal flush
    royal_ranks = {'A', 'K', 'Q', 'J', '10'}
    royal_flush_suits = []
    for suit in suit_count:
        suit_cards = {rank for rank, s in hand if s == suit}
        if suit_cards >= royal_ranks:
            royal_flush_suits.append(suit)
    
    # We need exactly two suits with a royal flush
    if len(royal_flush_suits) < 2:
        return False
    
    # Check for a three of a kind in a non-royal rank
    for rank, count in rank_count.items():
        if count == 3 and rank not in royal_ranks:
            return True  # Three of a kind found in a non-royal rank
    
    return False

def simulate_trials(num_trials, deck):
    """Run a specified number of trials and count hands with the double royal flush + three of a kind."""
    found = 0
    for _ in range(num_trials):
        hand = draw_hand(deck)
        if has_double_royal_flush_and_three_of_a_kind(hand):
            found += 1
    return found

def monitor_system_utilization(interval=1):
    """Monitor and display CPU, RAM, and CPU temperature in real-time."""
    try:
        while True:
            # Get CPU and RAM usage
            cpu_percent = psutil.cpu_percent(interval=interval)
            ram_usage = psutil.virtual_memory().percent
            
            # Attempt to get CPU temperature
            try:
                temperatures = psutil.sensors_temperatures()
                if 'coretemp' in temperatures:
                    temp = temperatures['coretemp'][0].current
                    print(f"CPU Utilization: {cpu_percent}% | RAM Usage: {ram_usage}% | CPU Temp: {temp}°C")
                else:
                    print(f"CPU Utilization: {cpu_percent}% | RAM Usage: {ram_usage}% | CPU Temp: Not available")
            except (AttributeError, KeyError):
                print(f"CPU Utilization: {cpu_percent}% | RAM Usage: {ram_usage}% | CPU Temp: Not supported")
    except KeyboardInterrupt:
        print("Stopped system monitoring.")

def main(total_trials, num_workers=8):
    # Set multiprocessing start method to "spawn" for M1 optimization
    multiprocessing.set_start_method("spawn", force=True)
    
    # Initialize deck
    deck = [(rank, suit) for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
            for suit in ['hearts', 'diamonds', 'clubs', 'spades']]
    
    # Determine trials per worker
    trials_per_worker = total_trials // num_workers

    # Start the system monitoring thread
    system_monitor_thread = Thread(target=monitor_system_utilization)
    system_monitor_thread.daemon = True  # Daemonize thread to exit with the main program
    system_monitor_thread.start()

    # Use ProcessPoolExecutor for parallel execution with "spawn" method
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        # Run simulations in parallel
        futures = [executor.submit(simulate_trials, trials_per_worker, deck) for _ in range(num_workers)]
        results = [future.result() for future in futures]

    # Aggregate results
    found = sum(results)
    probability = found / total_trials if total_trials > 0 else 0
    
    print(f"After {total_trials} trials with {num_workers} workers, found {found} hands with a double royal flush and a three of a kind.")
    print(f"Estimated probability: {probability:.10f} ({probability * 100:.8f}%)")

# Run the main function with a specified number of total trials and CPU cores
if __name__ == "__main__":
    main(total_trials=1000000000000000000000000000000, num_workers=8)  # Adjust total_trials based on available resources

# import random
# import multiprocessing
# import psutil
# import time
# from concurrent.futures import ProcessPoolExecutor
# from threading import Thread

# def draw_hand(deck, hand_size=13):
#     """Draw a hand of 'hand_size' cards from the deck."""
#     return random.sample(deck, hand_size)

# def has_double_royal_flush_and_three_of_a_kind(hand):
#     """Check if the hand contains both a double royal flush and a three of a kind."""
#     # Separate hand by rank and suit
#     rank_count = {}
#     suit_count = {}
#     for card in hand:
#         rank, suit = card
#         rank_count[rank] = rank_count.get(rank, 0) + 1
#         suit_count[suit] = suit_count.get(suit, 0) + 1
    
#     # Check for double royal flush
#     royal_ranks = {'A', 'K', 'Q', 'J', '10'}
#     royal_flush_suits = []
#     for suit in suit_count:
#         suit_cards = {rank for rank, s in hand if s == suit}
#         if suit_cards >= royal_ranks:
#             royal_flush_suits.append(suit)
    
#     # We need exactly two suits with a royal flush
#     if len(royal_flush_suits) < 2:
#         return False
    
#     # Check for a three of a kind in a non-royal rank
#     for rank, count in rank_count.items():
#         if count == 3 and rank not in royal_ranks:
#             return True  # Three of a kind found in a non-royal rank
    
#     return False

# def simulate_trials(deck):
#     """Keep running trials until a hand with both a double royal flush and a three of a kind is found."""
#     found = False
#     while not found:
#         hand = draw_hand(deck)
#         found = has_double_royal_flush_and_three_of_a_kind(hand)
#     return hand  # Return the valid hand once found

# def monitor_system_utilization(interval=1):
#     """Monitor and display CPU, RAM, and CPU temperature in real-time."""
#     try:
#         while True:
#             # Get CPU and RAM usage
#             cpu_percent = psutil.cpu_percent(interval=interval)
#             ram_usage = psutil.virtual_memory().percent
            
#             # Attempt to get CPU temperature
#             try:
#                 temperatures = psutil.sensors_temperatures()
#                 if 'coretemp' in temperatures:
#                     temp = temperatures['coretemp'][0].current
#                     print(f"CPU Utilization: {cpu_percent}% | RAM Usage: {ram_usage}% | CPU Temp: {temp}°C")
#                 else:
#                     print(f"CPU Utilization: {cpu_percent}% | RAM Usage: {ram_usage}% | CPU Temp: Not available")
#             except (AttributeError, KeyError):
#                 print(f"CPU Utilization: {cpu_percent}% | RAM Usage: {ram_usage}% | CPU Temp: Not supported")
#     except KeyboardInterrupt:
#         print("Stopped system monitoring.")

# def time_elapsed(start_time):
#     """Function to calculate and display the elapsed time."""
#     elapsed_time = time.time() - start_time
#     elapsed_seconds = int(elapsed_time)
#     minutes = elapsed_seconds // 60
#     seconds = elapsed_seconds % 60
#     return f"{minutes}m {seconds}s"

# def main():
#     # Set multiprocessing start method to "spawn" for M1 optimization
#     multiprocessing.set_start_method("spawn", force=True)
    
#     # Initialize deck
#     deck = [(rank, suit) for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#             for suit in ['hearts', 'diamonds', 'clubs', 'spades']]

#     # Start the system monitoring thread
#     system_monitor_thread = Thread(target=monitor_system_utilization)
#     system_monitor_thread.daemon = True  # Daemonize thread to exit with the main program
#     system_monitor_thread.start()

#     # Record start time
#     start_time = time.time()

#     # Use ProcessPoolExecutor for parallel execution with "spawn" method
#     with ProcessPoolExecutor(max_workers=8) as executor:
#         future = executor.submit(simulate_trials, deck)
#         valid_hand = future.result()

#     # Calculate elapsed time
#     elapsed_time = time_elapsed(start_time)
    
#     print(f"Found a hand with both a double royal flush and a three of a kind:")
#     print(valid_hand)
#     print(f"Time elapsed: {elapsed_time}")

# # Run the main function
# if __name__ == "__main__":
#     main()

#!/usr/bin/env python3

"""
greedy_algorithms.py

Demonstrates different situations that encapsulate the concept of a greedy algorithm
"""

_author_ = "Patrick Seo"
_version_ = "2024-05-17"

def coin_change(coins, amount):
    """
    Make a certain amount of change using the fewest number of coins from a given set of denominations
    """
    coins.sort(reverse=True)  # sort coins in descending order
    change = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            change.append(coin)
    return change

def activity_selection(start_times, finish_times):
    n = len(start_times)
    activities = list(zip(start_times, finish_times))
    activities.sort(key=lambda x: x[1])  # Sort activities by finish time
    selected_activities = [activities[0]]
    last_finish_time = activities[0][1]
    for i in range(1, n):
        current_start, current_finish = activities[i]
        if current_start >= last_finish_time:
            selected_activities.append(activities[i])
            last_finish_time = current_finish
    return selected_activities
    
def schedule(intervals):
    intervals.sort(key=lambda x: x[1]) 
    # print(intervals) 
    # counting the events 
    count = 0
    # keeping track of ending of intervals 
    end = 0
    # list of the intervals in which person will attend the events 
    answer = [] 
    # traversing the list of intervals 
    for interval in intervals: 
        # starting time of next interval will >= ending  
        # time of previous interval 
        if(end <= interval[0]): 
            # update the and 
            end = interval[1] 
            # increment the count by one 
            count += 1
            # insert the non-conflict interval in the list 
            answer.append(interval) 
    return answer

def main():
    print("This is a test program that demonstrates the concept of the greedy algorithm in different scenarios")
    choice = eval(input("Please enter a number choice correlating to the situation you'd like to view: 1) coin change, 2) activity selection problem, 3) schedule"))
    if (choice == 1):
        coins = [1, 5, 10, 25]
        amount = 37
        print(coin_change(coins, amount))  # Output: [25, 10, 1, 1]
    elif (choice == 2):
        start_times = [1, 3, 0, 5, 8, 5]
        finish_times = [2, 4, 6, 7, 9, 9]
        selected_activities = activity_selection(start_times, finish_times)
        print("Selected Activities:", selected_activities)
    elif (choice == 3):
        intervals = [(4, 5), (0, 2), (2, 7), (1, 3), (0, 4)]  
        print("Interval Scheduling:", schedule(intervals))
    else:
        print("Rerun the program. Please choose one of the options.")

if __name__ == "__main__":
    main()
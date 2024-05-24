#!/usr/bin/env python3

"""
greedy_algorithms.py

Demonstrates different situations that encapsulate the concept of a greedy algorithm
"""

_author_ = "Patrick Seo"
_version_ = "2024-05-17"

def coin_change(coins, amount):
    change = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            change.append(coin)
    return change

def activity_selection(start_times, finish_times):
    n = len(start_times)
    activities = list(zip(start_times, finish_times))
    activities.sort(key=lambda x: x[1])
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
    count = 0
    end = 0
    answer = [] 
    for interval in intervals: 
        if(end <= interval[0]): 
            end = interval[1] 
            count += 1
            answer.append(interval) 
    return answer

def main():
    print("This is a test program that demonstrates the concept of the greedy algorithm in different scenarios")
    choice = eval(input("Please enter a number choice correlating to the situation you'd like to view: 1) coin change, 2) activity selection problem, 3) schedule"))
    if (choice == 1):
        coins = [25, 10, 5, 1]
        amount = 42
        print("There will be coin values 1, 5, 10, and 25. Add up to the amount of 37 in the least amount of coins possible.")
        print(coin_change(coins, amount))
        print("Expected output: [25, 10, 1, 1]")
    elif (choice == 2):
        start_times = [1, 3, 0, 5, 8, 5]
        finish_times = [2, 4, 6, 7, 9, 9]
        print("Given start and finish times for various activities (start times: [1, 3, 0, 5, 8, 5]; finish times: [2, 4, 6, 7, 9, 9]), find the four activities that take the least amount of time (least difference between start and finish time).")
        selected_activities = activity_selection(start_times, finish_times)
        print("Selected Activities:", selected_activities)
        print("Expected Output: [(1, 2), (3, 4), (5, 7), (8, 9)]")
    elif (choice == 3):
        print("Trying to schedule your day, pick the activities to do that would not conflict with each other but will take the least amount of time to do.")
        intervals = [(4, 5), (0, 2), (2, 7), (1, 3), (0, 4)]  
        print("Interval Scheduling:", schedule(intervals))
    else:
        print("Rerun the program. Please choose one of the options.")

if __name__ == "__main__":
    main()
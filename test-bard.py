def main():
    # Initialize the distances of each friend from A
    distances = {
        "B": -100,
        "C": -200,
        "D": 250,
        "E": 300
    }

    # 1. Show which friend is the outermost from A
    outermost_friend = max(distances, key=distances.get)
    print(f"The outermost friend from A is {outermost_friend}.")

    # 2. Calculate the average distance of A's friends
    total_distance = sum(distances.values())
    average_distance = total_distance / len(distances)
    print(f"The average distance of A's friends is {average_distance:.2f} meters.")

    # 3. Ask the user to give an input of a travel from one friend to another friend
    start_friend = input("Please enter the starting friend: ")
    end_friend = input("Please enter the ending friend: ")

    # Check if the input friends are valid
    if start_friend not in distances or end_friend not in distances:
        print("Invalid friend names. Please enter valid friend names.")
        return

    # Calculate the distance of the travel
    travel_distance = abs(distances[end_friend] - distances[start_friend])
    print(f"The distance of the travel from {start_friend} to {end_friend} is {travel_distance} meters.")

    # Determine the friends passed on the travel
    passed_friends = []
    if distances[start_friend] < distances[end_friend]:
        for friend, distance in distances.items():
            if distance > distances[start_friend] and distance < distances[end_friend]:
                passed_friends.append(friend)
    else:
        for friend, distance in distances.items():
            if distance < distances[start_friend] and distance > distances[end_friend]:
                passed_friends.append(friend)

    # Display the friends passed on the travel
    if len(passed_friends) > 0:
        print(f"The friends passed on the travel from {start_friend} to {end_friend} are: {', '.join(passed_friends)}.")
    else:
        print("There are no friends passed on the travel from {start_friend} to {end_friend}.")


if __name__ == "__main__":
    main()

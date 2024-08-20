# Wedding Guest Manager
# Stage 1
confirmed_guests = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"]
waitlist = []
print("\n\nStage 1")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 2
waitlist = ["Ken", "Jack", "Ivy"]
print("\n\nStage 2")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 3
waitlist.extend(["Noah", "Oliver"])
print("\n\nStage 3")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 4
confirmed_guests.remove("Alice")
first_waitlisted_guest = waitlist.pop(0)
confirmed_guests.append(first_waitlisted_guest)
print("\n\nStage 4")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)



# Stage 5
is_charlie_on_guestlist = "Charlie" in confirmed_guests
print("\n\nStage 5")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print(f"It is {is_charlie_on_guestlist} that Charlie is in the guest list")

# Stage 6
confirmed_guests.remove("David")
confirmed_guests.remove("Eve")
print("\n\nStage 6")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
# print(f"It is {is_charlie_on_guestlist} that Charlie is in the guest list")


# Stage 7
second_waitlisted_guest = waitlist.pop(0)
third_waitlisted_guest = waitlist.pop(0)
confirmed_guests.append(second_waitlisted_guest)
confirmed_guests.append(third_waitlisted_guest)
print("\n\nStage 7")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist) 


# Stage 8
waitlist.remove("Oliver")
print("\n\nStage 8")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist) 


# Stage 9
last_three = confirmed_guests[-3:]
print("\n\nStage 9")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist) 
print("Last Three: ", last_three) 


# Stage 10
move_waitlisted_guest = waitlist.pop(0)
confirmed_guests.append(move_waitlisted_guest)
print("\n\nStage 10")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist) 


# Stage 11
confirmed_guests_length = len(confirmed_guests)
print("\n\nStage 11")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist) 
print(confirmed_guests_length)


# Stage 12
print("\n\nStage 12")
print("Confirmed guests: ", confirmed_guests)





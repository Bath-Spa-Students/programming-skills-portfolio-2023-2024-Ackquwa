invitees = ['guido van rossum', 'jack turner', 'lynn hill']

for invitee in invitees:
    print(f"{invitee.title()}, you are invited to dinner.")

print(f"\nSorry, {invitees[1].title()} can't make it to dinner.")
invitees[1] = 'gary snyder'


for invitee in invitees:
    print(f"\n{invitee.title()}, you are invited to dinner.")


print("\nWe have a larger table!")
additional_guests = ['frida kahlo', 'reinhold messner', 'elizabeth peratrovich']
invitees = [additional_guests[0]] + [invitees[0]] + [additional_guests[1]] + [invitees[1]] + [invitees[2]] + [additional_guests[2]]


for invitee in invitees:
    print(f"{invitee.title()}, you are invited to dinner.")


print("\nSorry, we can only invite two people to dinner.")
while len(invitees) > 2:
    removed_guest = invitees.pop()
    print(f"Sorry, {removed_guest.title()}, there's no room at the table.")

for invitee in invitees:
    print(f"{invitee.title()}, you are invited to dinner.")

invitees.clear()

print(invitees)
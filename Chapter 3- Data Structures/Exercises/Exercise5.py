guests = ['Baron', 'Louis', 'Matthew']

name = guests[0].title()
print(name + ", Baron Come.")

name = guests[1].title()
print(name + ", Thy Loius is Invited.")

name = guests[2].title()
print(name + ", Come now Mathhew.")

name = guests[1].title()
print("\nSorry, " + name + " will not be able to make it to dinner.")

del(guests[1])
guests.insert(1, 'Angelo')

# Print the invitations again.
name = guests[0].title()
print("\n" + name + ", Baron Come.")

name = guests[1].title()
print(name + ", Angelo please come, you are invited.")

name = guests[2].title()
print(name + ", Come now Mathhew.")
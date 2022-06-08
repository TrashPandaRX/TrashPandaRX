unconfirmed_users =['earl', 'doug', 'beemo']
confirmed_users =[]

while unconfirmed_users:                  #while unconfirmed_users isnt false (ie empty), enter loop
    current_user = unconfirmed_users.pop()  #because pop removes an element from the top of the stack and returns the value

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("The following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
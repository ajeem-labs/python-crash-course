users = ['ajeem', 'federer', 'murray', 'nadal', 'djokovic', 'admin']

for i in range(len(users)):
    del(users[0])
if not users:
    print("We need to find some users:")
else:
    for user in users:
        if user == 'admin':
            print("Hello Admin, would you like to see a user report?")
        else: 
            print("Hello,",user + ",","Thanks for looging in again.")
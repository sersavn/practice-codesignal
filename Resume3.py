



accounts = [10, 100, 20, 50, 30]
requests = ["withdraw 5 10", "transfer 5 1 20", "deposit 5 20", "transfer 3 4 15"]


for command in requests:
    print(command)

    if 'withdraw' in command:
        print('command', command)
        command = (command.split())[1:]
        command = list(map(int, command))
        accounts[command[0]-1] = accounts[command[0]-1] - command[1]

    if 'transfer' in command:
        command = (command.split())[1:]
        command = list(map(int, command))
        accounts[command[0]-1] = accounts[command[0]-1] + command[2]
        accounts[command[1]-1] = accounts[command[0]-1] - command[2]

    if 'deposit' in command:
        command = (command.split())[1:]
        command = list(map(int, command))
        accounts[command[0]-1] = accounts[command[0]-1] + command[1]

print(accounts)


###
#Test 1
#Input:
#accounts: [10, 100, 20, 50, 30]
#requests: ["withdraw 2 10",
# "transfer 5 1 20",
# "deposit 5 20",
# "transfer 3 4 15"]
#Output:
#Run the code to see output
#Expected Output:
#[30, 90, 5, 65, 30]
#Console Output:
#Empty

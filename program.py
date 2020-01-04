import journal



def print_header():
    print('---------------------')
    print('    JOURNAL APP')
    print('---------------------')

def run_event_loop():
    print("what would you like to do?")
    user_command= 'EMPTY'
    journal_name='The Times'
    #journal_name=input('What would you like to name your journal?')
    journal_data=journal.load(journal_name)
    while user_command !='x' and user_command:
        user_command=input("You can [a]dd, [l]ist or e[x]it.")
        user_command=user_command.lower().strip()
        if user_command== 'l':
            list_entries(journal_data)
        elif user_command== 'a':
            add_entry(journal_data)
        elif user_command!= 'x' and user_command:
            print("Sorry, don't understand")

    print("Goodbye")
    journal.save(journal_name,journal_data)

def list_entries(data):
    print('Your entries are as follows:')
    for (idx,entry) in enumerate(data):
        print('Journal {} is {}'.format(idx+1,entry))


def add_entry(data):
    entry=input('Please type your entry')
    journal.add_entry(entry,data)

    #data.append(entry)














def main():
    print_header()
    run_event_loop()


if __name__=="__main__":
    main()


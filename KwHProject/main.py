state_dict = {}
# available_kwh = 2530


def initialization():
    state_dict[1] = 420
    state_dict[2] = 320
    state_dict[3] = 450
    state_dict[4] = 340
    state_dict[5] = 380
    state_dict[6] = 300
    state_dict[7] = 320


def initialization2():
    state_dict[1] = 300
    state_dict[2] = 300
    state_dict[3] = 330
    state_dict[4] = 340
    state_dict[5] = 390
    state_dict[6] = 420
    state_dict[7] = 430

def implementation(available_kwh=2450):
    # Initialization phase with the data
    initialization2()

    # Sort dictionary based on values
    new_state_dict = dict(sorted(state_dict.items(), key=lambda x: x[1]))

    print('Initial state(ordered) ', new_state_dict)
    closeout_count = 1

    while available_kwh > 0 and new_state_dict.__len__() != 0:
        print('\n\nThe remaining available kwh are ', available_kwh)

        # Obtain the smallest kwh value that we must satisfy
        while( list(new_state_dict.values())[0] == 0 ):
            print("Customer with id ", list(new_state_dict.keys())[0], " is already satisfied")
            new_state_dict.pop(list(new_state_dict.keys())[0])

        min_val = list(new_state_dict.values())[0]

        # print('Min consumption for that phase ', min_val)
        print("Phase Closeout ", closeout_count)
        closeout_count += 1

        # Check that we are able to satisfy all of the customers
        if new_state_dict.__len__() * min_val < available_kwh:

            for key, val in new_state_dict.items():
                new_state_dict[key] -= min_val
                print("The customer with the id ", key, " has gained ", min_val," KwH ")

            available_kwh -= new_state_dict.__len__() * min_val
            new_state_dict.pop(
                list(new_state_dict.keys())[0])  # Pop the first element of the dictionary now that we satisfied it
        else:
            print("We have remaining ", available_kwh, " KwH for ", new_state_dict.__len__(), "customers")
            cons_distribution = available_kwh/new_state_dict.__len__()
            print()

            for nkey in new_state_dict.keys():
                print("The customer with id ", nkey, " has gained ", cons_distribution," KwH ")

            # Clear the remaining elements on the dict since we covered them
            new_state_dict.clear()
            break;



if __name__ == '__main__':
    implementation()

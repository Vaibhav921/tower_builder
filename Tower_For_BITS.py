def convert_to_list(input_string):
    # Split the string into a list of strings
    string_list = input_string.split(' ')
    # Convert each string in the list to an integer
    integer_list = [int(num) for num in string_list]
    return integer_list

def validate_inputs(days, sequence_of_disks):
    # this should also check length of sequence_of_disks equals days

    # Check if all elements in 'sequence_of_disks' are in the range 1 to 'days'    
    if not all(1 <= i <= days for i in sequence_of_disks):
        raise Exception("All elements in 'sequence_of_disks' should be in the range 1 to 'days'.")
    

def looking_for(last_disk_placed, biggest_disk_size):
    looking_for_number: int
    if last_disk_placed == 0:
        looking_for_number = biggest_disk_size
    else:
        looking_for_number = last_disk_placed - 1
    
    print( "\nlooking for: " + str(looking_for_number))
    return looking_for_number
    

def pop_all_before_current( stack: list, looking_for_value: int, days: int):
    if len(stack) <= 0:
        return

    # print( "here...1 - last disk placed: " + str(last_disk_placed))

    value_found_in_stack = False
    for i in range(len(stack)):
        print( "Item at index: " + str(i) + " => " + str( stack[i]))
        if stack[i] == looking_for_value:
            print( "Placing the disk: " + str(stack[i]))
            value_found_in_stack = True
            looking_for_value = looking_for_value - 1
            print( str(stack[i]), end = " ")
            stack.pop(i)
            break
    
    if value_found_in_stack:
        pop_all_before_current( stack, looking_for_value, days)

    
def build_tower(days, sequence_of_disks):
    stack = []
    last_disk_placed = 0

    # Loop for each day
    for day, disk in enumerate(sequence_of_disks):
        print( "Day: " + str(day + 1))
        stack.insert( day, disk)

        print( stack)

        if stack[-1] == looking_for( last_disk_placed, days):
            last_disk_placed= stack[-1]
            pop_all_before_current( stack, last_disk_placed, days)
            # last_disk_placed = looking_for( last_disk_placed, days)
            # print(str(stack.pop()) + " ")
        # else:
        #     print("\n")



def main():
    print("Welcome to BITS Tower Design")

    with open("inputPS1.txt", "r") as f:
        lines = f.readlines()

    days =              int(lines[0])
    sequence_of_disks = convert_to_list(lines[1])

    print( "Total days: " + str(days) + "\nsequence_of_disks: " + lines[1])

    validate_inputs(days, sequence_of_disks)

    build_tower(days, sequence_of_disks)


if __name__ == "__main__":
  main()
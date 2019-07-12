

def print_melon_delivery_report(the_file, day):
        print(day)
        the_file = open(the_file)

        for line in the_file:
                line = line.rstrip()
                words = line.split('|')

                melon = words[0]
                count = words[1]
                amount = words[2]

                print("Delivered {} {}s for total of ${}".format(count, melon, amount))
                
        the_file.close()

print_melon_delivery_report("um-deliveries-20140519.txt", "Day 1")
print_melon_delivery_report("um-deliveries-20140520.txt", "Day 2")
print_melon_delivery_report("um-deliveries-20140521.txt", "Day 3")

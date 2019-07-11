log_file = open("um-server-01.txt")
# opens the file, and sets the contents to a variable


def sales_reports(log_file):
# defines the function sales reports that takes the text file as input
    for line in log_file:
    # loops over the lines in the text file 
        line = line.rstrip()
        # for each line, removes the trailing characters and sets the new output to a variable line
        day = line[0:3]
        # only takes the first 3 characters of each line, and set this output to a varaible day 
        if day == "Mon":
        # sets the condition if the first 3 characters of each line match the string, then execute
            print(line)
            # print the variable line


sales_reports(log_file)
# call the function, passing in the text file

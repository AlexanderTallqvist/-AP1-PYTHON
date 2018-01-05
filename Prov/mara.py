# Uppg. 1

def sum_ints(m, n):
    counter  = n - m
    ret_value = 0

    while counter >= 0:
        temp_value = m + counter
        ret_value  = temp_value + ret_value
        counter    = counter - 1

    return ret_value

print sum_ints(11,20)


# Uppg. 2

def file_to_list(file_name):
    return_list = []

    try:
      infil = open(file_name, "r")
    except IOError:
      return "Error: File does not appear to exist."

    for line in infil.readlines():
        return_list.append(line)

    infil.close()
    return return_list

def print_temp_list(temp_list):
    for item in temp_list:
        print item.replace(";", " ").strip()

temp_list = file_to_list('tempdata.csv')
print_temp_list(temp_list)

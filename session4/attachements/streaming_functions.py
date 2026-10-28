def read_large_file(path):
    with open(path, "r") as f:
        for line in f:            # file objects are already iterators!
            yield line.strip()
 
def count_errors(path):
    return sum(1 for line in read_large_file(path) if "ERROR" in line)



def read_large_file_count(path):
    errors = 0
    with open(path, "r") as f:
        for line in f:            # file objects are already iterators!
            if "ERROR" in line :
                errors += 1
            else:
                continue
        return errors 
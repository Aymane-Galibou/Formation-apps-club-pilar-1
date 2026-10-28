import csv 
from itertools import islice

def stream_csv_file(path,chunksize=10):
    with open(path,'r') as f :
        reader = csv.DictReader(f)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) == chunksize:
                yield chunk
                chunk=[]

        if chunk:
            yield chunk


"""
with open('result.csv','a') as f :
    writer = None
    for chunk in islice(stream_csv_file('laptops_train.csv'),3):
        for row in chunk:
            if writer is None:
                writer= csv.DictWriter(f,fieldnames=row.keys())
                writer.writeheader()

            writer.writerow(row)
"""

with open("result.csv", "a", newline="") as f:
    writer = None
    for chunk in islice(stream_csv_file('laptops_train.csv'),3):
        if writer is None:
            writer= csv.DictWriter(f,fieldnames=chunk[0].keys())
            writer.writeheader()

        writer.writerows(chunk)

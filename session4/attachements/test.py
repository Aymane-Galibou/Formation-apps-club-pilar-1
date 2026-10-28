from itertools import islice
import csv

def process_csv(path,batch_size=10):

    with open(path) as file :
        chunk = []
        reader = csv.DictReader(file)

        for row in reader :
            if len(chunk) == batch_size:
                yield chunk
                chunk = []

            chunk.append(row)

        if chunk :
            yield chunk


with open('result1.csv','a') as output:
    writer = None

    for chunk in islice(process_csv('laptops_train.csv',15),3) :

        if writer is None:
            writer = csv.DictWriter(output,fieldnames=chunk[0].keys())
            writer.writeheader()

        writer.writerows(chunk)
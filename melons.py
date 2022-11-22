
import csv

class Melon:
    def __init__(self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless

    def __repr__(self):
        """ Convenience method to show information about melon in console. """
        return (f"<Melon: {self.melon_id}, {self.common_name}>")
        
    def price_str(self):
        """ Return price formatted as a string $x.xx """
        return f'${self.price:.2f}'

melon_dict = {}

with open('melons.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        melon_id = row['melon_id']
        melon = Melon(
            melon_id,
            row['common_name'],
            float(row['price']),
            row['image_url'],
            row['color'],
            eval(row['seedless'])
        )

        melon_dict[melon_id] = melon

def find_melon(melon_id):
    return melon_dict[melon_id]

def get_all():
    return list(melon_dict.values())

print(find_melon('cren'))

import json

class country_list:
    index = 0
    output = {}

    def __init__(self, path):
        self.path = path
        with open('countries.json') as input_file:
            self.data = dict(json.load(input_file))

    def __iter__(self):
        return self

    def __next__(self):
        if self.index != len(self.data.items()):
            country = self.data[str(self.index)]
            link = 'https://ru.wikipedia.org/wiki/' + country
            self.index += 1
            self.output[country] = link
        else:
            with open('links.json', 'w', encoding='utf-8') as output_file:
                json.dump(self.output, output_file, ensure_ascii=False, indent=2)
            raise StopIteration
        return link

if __name__ == '__main__':
    for country in country_list('countries.json'):
        print(country)
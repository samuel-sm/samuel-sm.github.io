import json
import os

def main():
# Open and read the JSON file
    with open('cards.json', 'r', encoding="utf8") as file:
        data = json.load(file)

        for d in data:
            os.makedirs(d['codigo'])

if __name__ == "__main__":
    main()
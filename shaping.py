import csv
import re

def get_text():
    id_list = []
    with open('text-list.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            id_list.append(row['国文研書誌ID'])
    return id_list

def get_text_path(id):
    return 'text/' + id + '/text/' + id + '_text.txt'

def shap_text(id):
    path = get_text_path(id)
    # Read the text file into a variable
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Remove <Image: ~~~~ > tag using regular expression
    text = re.sub(r'<Image:[^>]*>', '', text)

    # Remove blank lines
    text = '\n'.join(line for line in text.splitlines() if line.strip())

    # Write the modified text back to the file
    with open('shaped-text/' + id + '.txt', 'w', encoding='utf-8') as f:
        f.write(text)

def main_shaping():
    id_list = get_text()
    for id in id_list:
        shap_text(id)

def genji_shaping():
    path = "text/200003803/text/200003803_text.txt"
    # Read the text file into a variable
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    text = re.sub(r'Ｌ[０-９]+', '', text)
    text = re.sub(r'L[0-9]+', '', text)
    text = re.sub(r'Ｐ[０-９]+', '', text)
    text = re.sub(r'（絵）', '', text)

        # Remove blank lines
    text = '\n'.join(line for line in text.splitlines() if line.strip())
        # Write the modified text back to the file
    with open('shaped-text-test/200003803.txt', 'w', encoding='utf-8') as f:
        f.write(text)


if __name__ == '__main__':
    main_shaping()
    genji_shaping()
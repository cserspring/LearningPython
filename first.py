import random
import urllib.request

foods = ['bacon', 'tuna', 'ham', 'sausage', 'beef']

for f in foods[:2]:
    print(f)
    print(len(f))

for x in range(10, 40, 5):
    print(x)

buttcrack = 5
while buttcrack < 10:
    print(buttcrack)
    buttcrack += 1

magicNumber = 26
# This program find a magic number
'''
  This is a comment line.
  This is another command line.
'''
for n in range(101):
    if n is magicNumber:
        print(n, " is the magic number.")
        break
    else:
        print(n)


def get_gender(sex='Unknown'):
    if sex is 'm':
        sex = 'Male'
    elif sex is 'f':
        sex = 'Female'
    print(sex)

get_gender('m')
get_gender('f')
get_gender()


def add_numbers(*args):
    total = 0
    for i in args:
        total += i
    print(total)

add_numbers(45, 21, 32, 6)

classmates = {'A':'a', 'B':'b', 'C':'c'}
for k, v in classmates.items():
    print(k, v)


# Download an image from the web
def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("http://cdn2-b.examiner.com/sites/default/files/styles/image_content_width/hash/52/f7/52f749886f63c2b4c2002addd56267c8.png?itok=e3Nh3wo0")

# Read and write files
fw = open("sample.txt", "w")
fw.write("Writing some stuff in my text file\n")
fw.write("I like bacon\n")
fw.close()

fr = open("sample.txt", "r")
text = fr.read()
print(text)
fr.close()

goog_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=6&e=20&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv"


def download_stock_data(csv_url):
    response = urllib.request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)
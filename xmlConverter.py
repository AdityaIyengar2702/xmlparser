from flask import Flask, request #import main Flask class and request object
import xml.etree.ElementTree as ET #import xml lib to read
import csv  #import csv lib to perform csv operations
from flask import jsonify # <- `jsonify` instead of `json`

app = Flask(__name__)
#<URL>/xmlConverter
@app.route('/xmlConverter', methods=['GET', 'POST']) #allow both GET and POST requests
def xmlToCSVConverter():
    if request.method == 'POST':
        data = request.data

        # # create element tree object
        # tree = ET.parse(data)
        #
        # # get root element
        # root = tree.getroot()


        #As the data, if used in ET.parse(), will be passed as a pathname and if the xml content is huge, it will
        #throw a "File too lang error".
        #Hence use ET.fromstring() - This parses XML from a string directly into an Element, which is the root element of the parsed tree
        root = ET.fromstring(data)

        # create empty list for text block
        textItems = []

        # iterate over data
        for item in root.findall('TextBlock'): #Assuming <Layout> in the xml file as the root

            # empty block
            block = {}

            # iterate child elements of item
            for child in item:
                block[child.tag] = child.text.encode('utf8')

            #append block to textItems
            textItems.append(block)

        return jsonify(textItems)
        # return ','.join(textItems)

def savetoCSV(textItems, filename):

    # specifying the fields for csv file
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']

    # writing to csv file
    with open(filename, 'w') as csvfile:

        # creating a csv  writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(newsitems)


def main():

    # parse xml file
    textItems = xmlToCSVConverter()

    # store xml in a csv file
    savetoCSV(textItems, 'table.csv')


if __name__ == "__main__":
    # app.run(debug=true,port=8080) - Used to test by running the server locally

    # calling main function
    main()

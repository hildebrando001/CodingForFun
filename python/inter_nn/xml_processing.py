# Python has two different ways to work with XML data: (SAX model or DOM model)
# SAX = Simple API for XML # SAX is Recommended when there are a large XML file or limited memory. Only can read files
# DOM = Document Object Model # You may read and change the file
import xml.sax # Takes the XML file and converts into a python script
# handler = xml.sax.ContentHandler() # In this example the handler will be customized
class GroupHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs): # This method starts the element
        self.current = name
        if self.current == "person":
            print("-----PERSON-----")
            print(f"ID: {attrs['id']}") # It prints only the id

    def characters(self, content): # Lets print all the other values
        if self.current == "name": # The current will be junping between elements
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content

    def endElement(self, name):
        if self.current == "name":
            print(f"Name: {self.name}")
        elif self.current == "age":
            print(f"Age: {self.age}")
        elif self.current == "weight":
            print(f"Weight: {self.weight}")
        elif self.current == "height":
            print(f"Height: {self.height}")
        self.current = ""


handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')

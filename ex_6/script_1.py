import xml.dom.minidom
import xml.sax


class BookHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.title = ""
        self.author = ""
        self.year = ""
        self.tags = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "book":
            print("***BOOKS***")
        if tag == "tags":
            tag = attributes["tag"]
            print("Tag: ", tag)

    def endElement(self, tag):
        if self.CurrentData == "title":
            print("Title: ", self.title)
        elif self.CurrentData == "author":
            print("Author: ", self.author)
        elif self.CurrentData == "year":
            print("Year: ", self.year)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "author":
            self.author = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "tags":
            self.tags = content


doc = xml.dom.minidom.parse("xml_file.xml")

print(doc.nodeName)
print(doc.firstChild.tagName)

tags = doc.getElementsByTagName("tags")
for tag in tags:
    print(tag.getAttribute("tag"))

new_tag = doc.createElement("tags")
new_tag.setAttribute("tag", "story_for_kids")
doc.firstChild.appendChild(new_tag)
print("\n")

tags = doc.getElementsByTagName("tags")
for tag in tags:
    print(tag.getAttribute("tag"))

with open('xml_file_modified.xml', 'w') as f:
    f.write(doc.toxml())

parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = BookHandler()
parser.setContentHandler(Handler)
parser.parse("xml_file_modified.xml")

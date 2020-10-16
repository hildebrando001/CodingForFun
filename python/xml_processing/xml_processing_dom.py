import xml.dom.minidom # Minimal implementation of the DOM model

domtree = xml.dom.minidom.parse('data.xml') # domtree will receive all the xml file
group = domtree.documentElement # take all the tags in the file # The root of the domtree

persons = group.getElementsByTagName('person') # collect all the elements with the TagName <person>

for person in persons:
    print('-----PERSON-----')
    if person.hasAttribute('id'):
        print(f"ID: {person.getAttribute('id')}")

    print(f"Name: {person.getElementsByTagName('name')[0].childNodes[0].data}")
    print(f"Age: {person.getElementsByTagName('age')[0].childNodes[0].data}")
    print(f"Weight: {person.getElementsByTagName('weight')[0].childNodes[0].data}")
    print(f"Height: {person.getElementsByTagName('height')[0].childNodes[0].data}")

# Manipulating the xml file...
persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = "New Name"
persons[0].setAttribute('id', '100')
persons[3].getElementsByTagName('age')[0].childNodes[0].nodeValue = "-10"
domtree.writexml(open('data2.xml', 'w')) # We can write it in a new file or in the same file

# Create/add new elements to the xml file
newperson = domtree.createElement('person')
newperson.setAttribute('id', '6')

name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('paul Green'))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('19'))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode('80'))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('179'))

# Now we have independent elements, we need to add to a new person
newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

# Now ew need to add the person to the group element
group.appendChild(newperson)
domtree.writexml(open('data2.xml', 'w'))
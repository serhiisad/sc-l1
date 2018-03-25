from lxml import etree
from task_package import member, request

import xml.etree.ElementTree as ET


# parsing xml
def parse_xml(xml_file):
    with open(xml_file) as fobj:
        xml = fobj.read()
    root = etree.fromstring(xml)
    for region in root.getchildren():
        for field in region.getchildren():
            if field.tag == "channels":
                for channel in field.getchildren():
                    print('Channel: ' + channel.text)
            else:
                print(field.tag + ": " + field.text)


# writing parsed data to result.xml
def write_result_xml(responseData, xml_result_file):
    # building XML tree
    result = ET.Element('result')
    items = ET.SubElement(result, 'items')
    for elem in responseData:
        item = ET.SubElement(items, 'item')
        item.text = elem

    et = ET.ElementTree(result)
    et.write(xml_result_file, encoding="utf-8", xml_declaration=True) # pretty_print=True не пахает тут (

    # XMLdata = ET.tostring(result)
    # file = open(xml_result_file, "wb")
    # file.write(XMLdata)


# parse_xml('./channels.xml')
m = member.Member('US', '2018-03-13', '21:00', '22:00')
with open('./channels.xml') as f:
    xml = f.read()
root = etree.fromstring(xml)
for ch in root.getchildren():
    for f in ch.getchildren():
        if f.tag == "channels":
            for channel in f.getchildren():
                m.add_channel(channel.text)
# print(m.get_channels())

r = request.Request()
r.set_date(m.get_date())
r.set_region(m.get_region())
r.set_time(m.get_start_time(), m.get_end_time())

# r.get_infos("NBC")
# print("__________________")

# s = r.get_infos_List("ABC")
# print(s)
write_result_xml(r.get_infos_List("ABC"), "result.xml")





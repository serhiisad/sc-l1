from lxml import etree
from task_package import member, request

import xml.etree.ElementTree as ET
from xml.dom import minidom


def parse_xml_member(xml_file):
    mem = member.Member()
    with open(xml_file) as f:
        file = f.read()
    r = ET.fromstring(file)
    for ch in r.getchildren():
        if ch.tag == "region":
            for child in ch.getchildren():
                startTime = None
                endTime = None
                if child.tag == "name":
                    mem.set_region(child.text)
                if child.tag == "date":
                    mem.set_date(child.text)
                if child.tag == "startTime":
                    startTime = child.text
                if child.tag == "endTime":
                    endTime = child.text
                if(startTime is not None) and (endTime is not None):
                    print(startTime + "\n" + endTime)
                    mem.set_time(startTime, endTime)
    return mem


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
        channel = ET.SubElement(items, 'сhannel')
        channel.set("name", elem[0])
        for programm in elem[1]:
            pr = ET.SubElement(channel, 'tmp')
            pr.text = programm
    et = ET.tostring(result, 'utf-8')
    parsed = minidom.parseString(et)
    pretty = parsed.toprettyxml(indent="\t")
    with open(xml_result_file, "w") as f:
        f.write(pretty)

# parse_xml('./channels.xml')
m = member.Member('US', '2018-03-13', '00:00', '22:00')

with open('./channels.xml') as f:
    xml = f.read()

root = etree.fromstring(xml)
for ch in root.getchildren():
    for f in ch.getchildren():
        if f.tag == "channels":
            for channel in f.getchildren():
                m.add_channel(channel.text)

r = request.Request()
r.set_date(m.get_date())
r.set_region(m.get_region())
r.set_time(m.get_start_time(), m.get_end_time())

channels = m.get_channels()
result = []
for channel in channels:
    loop_result = []
    loop_result.append(channel)
    loop_result.append(r.get_infos_List(channel))
    result.append(loop_result)

print(result)

write_result_xml(result, "result.xml")

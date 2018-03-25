from lxml import etree
from task_package import member,request

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


# parse_xml('./channels.xml')
m = member.Memeber('US', '2018-03-13', '00:00', '01:00')
with open('./channels.xml') as f:
    xml = f.read()
root = etree.fromstring(xml)
for ch in root.getchildren():
    for f in ch.getchildren():
        if f.tag == "channels":
            for channel in f.getchildren():
                m.add_channel(channel.text)
# print(m.get_channels())
r = request.Request();
r.set_date(m.get_date())
r.set_region(m.get_region())
r.set_time(m.get_start_time(), m.get_end_time())
r.get_infos('CBS')
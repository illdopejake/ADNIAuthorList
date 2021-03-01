from collections import OrderedDict

def get_startpoint(): 
    responded = False
    while not responded:
        string = 'What number should I start the ADNI affiliations?'
        string += ' (Enter a number)'
        startpoint = input(string)
        # validate
        if not startpoint.isnumeric():
            print("WHOOPS! I didn't recognize %s. Please enter an integer"%(startpoint))
        else:
            startpoint = int(startpoint)
            responded=True
    return startpoint

my_file = open("ADNI_authorlist.txt", "r")
content_list = my_file.readlines()

startpoint = get_startpoint()
modifier = startpoint - 4

# get info
new_list = OrderedDict()
for i,l in enumerate(content_list[4:]):
    l = l.split('\n')[0]
    if not l: continue
    num,loc = l.split(') ')
    num = num.split('(')[-1]
    loc = loc.lstrip()
    new_list.update({int(num)+modifier:loc})

names = OrderedDict()
for entry in content_list[2].split(','):
    nm,num = entry.split(' (')
    nm = nm.lstrip()
    num = num.split(')')[0]
    names.update({nm:int(num)+modifier})

# build strings
superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹"}
trans = str.maketrans(
    ''.join(superscript_map.keys()),
    ''.join(superscript_map.values()))
print('\n\n')

# author string
auth_str = ''
count=1
for nm,num in names.items():
    nmstr = '%s%s'%(nm,str(num).translate(trans))
    if count != len(names.keys()):
        auth_str += '%s, '%nmstr
    else:
        auth_str += nmstr
    count+=1
print(auth_str)

print('\n\n')
# institution string
for num,loc in new_list.items():
    print(str(num).translate(trans), loc)
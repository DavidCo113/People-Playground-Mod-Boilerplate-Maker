import os
import json

#Default Settings START
dict = {}
path = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\People Playground\\Mods\\' #Don't remove the slashes at the end.
dict['Author'] = 'No Name' #Change this.
dict['ModVersion'] = '1.0'
dict['ThumbnailPath'] = 'thumb.png'
dict['EntryPoint'] = 'Mod.Mod' #If changing this, make sure to change the namespace and class in basescript.cs accordingly, because I'm too lazy to make the program do that for you.
#Default Settings END

dict['Name'] = input('Mod Name: ')
dict['Description'] = input('Description: ')
dict['GameVersion'] = input('Intended game version(s): ')

tag = input('Add a tag (enter to cancel): ')
dict['Tags'] = []
while tag!="":
    dict['Tags'].append(tag)
    tag = input('Add a tag (enter to cancel): ')

script = input('Add a script (no ".cs", enter to cancel): ')
dict['Scripts'] = []
while script!='':
    dict['Scripts'].append(script + '.cs')
    script = input('Add a script (no ".cs", enter to cancel): ')

os.mkdir(path + dict['Name'])
with open(path + dict['Name'] + '\\mod.json', 'x') as f:
    json.dump(dict, f)

for item in dict['Scripts']:
    open(path + dict['Name'] + '\\' + item, 'xb').write(open('basescript.cs', 'rb').read())

open(path + dict['Name'] + '\\' + dict['ThumbnailPath'], 'xb').write(open('basethumb.png', 'rb').read())

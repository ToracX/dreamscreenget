import socket
import sys
import optparse
import time
import pydreamscreen

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

parser = optparse.OptionParser()
parser.add_option('-i', '--ip', dest='ip')
parser.add_option('-t', '--type', action='store_true', dest='type')
parser.add_option('-n', '--name', action='store_true', dest='name')
parser.add_option('-g', '--group', action='store_true', dest='group')
parser.add_option('-m', '--mode', action='store_true', dest='mode')
parser.add_option('-b', '--brightness', action='store_true', dest='brightness')
parser.add_option('-c', '--color', action='store_true', dest='color')
parser.add_option('-a', '--ambient scene', action='store_true', dest='scene')
options, args = parser.parse_args()

if options.ip:
        payload = options.ip.split('.')
        if len(payload) == 4:
            for i in range(len(payload)):
                int(payload[i])
                device_state = pydreamscreen.get_state(options.ip)
                global dict
                dict = device_state
        else:
            print("There was an error in your IP's length")

if options.group:
    try:
        print(dict.get('group_number'))      
    except:
        print("error: source not a valid number")
        sys.exit(0)

if options.mode:
    try:
        print(dict.get('mode'))      
    except:
        print("error: mode not a valid number")
        sys.exit(0)

if options.color:
    try:
        print(dict.get('ambient_color'))      
    except:
        print("There was an error, please make sure you are using the right format: '255 255 255' for white")

if options.name:
    try:
        print(dict.get('name'))      
    except:
        print("error: source not a valid number")
        sys.exit(0)
        
if options.type:
    try:
        print(dict.get('device_type'))      
    except:
        print("error: source not a valid number")
        sys.exit(0)
        
if options.scene:
    try:
        print(dict.get('ambient_scene'))      
    except:
        print("error: source not a valid number")
        sys.exit(0)

if options.brightness:
    try:
        print(dict.get('brightness'))
    except:
        print("error: brightness not a valid number")
        sys.exit(0)

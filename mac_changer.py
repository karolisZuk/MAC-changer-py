#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-m", "--mac", dest="new_mac", help="New mac valid MAC address. For example 'e4-ff-75-ee-3e-8e'")
    parser.add_option("-i","--interface",dest="interface",help="Interface to change MAC address. Usually 'en0'")
    (options, args) =  parser.parse_args()
    if not options.interface:
        parser.error("[-] Specify interface. You are probably looking for 'en0'")
    elif not options.new_mac:
        parser.error("[-] Specify new MAC address. Use --help for more info.")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call([ "sudo", "/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport", "-z" ])
    subprocess.call([ "sudo", "ifconfig", interface, "ether", new_mac ])
    subprocess.call([ "networksetup", "-detectnewhardware" ])
    subprocess.call([ "sudo", "ifconfig", interface, "up" ])

options = get_arguments()
change_mac(options.interface, options.new_mac)
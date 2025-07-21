from django.shortcuts import render
from dna_center_cisco.dnac_network import DNAC_Manager
import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

def show_token(request):
    dnac = DNAC_Manager()
    success = dnac.get_auth_token(display_token=False)
    token = dnac.token if success else None

    client = MongoClient(MONGODB_URI)
    db = client['automation_logs']
    db.logs.insert_one({
        "timestamp": datetime.datetime.utcnow(),
        "action": "Authentication",
        "result": "Success" if success else "Failed"
    })

    return render(request, "dna_center_cisco/token.html", {"token": token})


def show_devices(request):
    dnac = DNAC_Manager()
    success = dnac.get_auth_token(display_token=False)
    devices = dnac.get_network_devices() if success else None

    client = MongoClient(MONGODB_URI)
    db = client['automation_logs']
    db.logs.insert_one({
        "timestamp": datetime.datetime.utcnow(),
        "action": "Device List",
        "result": "Success" if devices else "Failed"
    })

    return render(request, "dna_center_cisco/devices.html", {"devices": devices})


def show_interfaces(request):
    dnac = DNAC_Manager()
    success = dnac.get_auth_token(display_token=False)
    interfaces = None
    device_ip = None
    if request.method == "POST":
        device_ip = request.POST.get("device_ip")
        if device_ip:
            interfaces = dnac.get_device_interfaces(device_ip)

            client = MongoClient(MONGODB_URI)
            db = client['automation_logs']
            db.logs.insert_one({
                "timestamp": datetime.datetime.utcnow(),
                "action": "Interface List",
                "device_ip": device_ip,
                "result": "Success" if interfaces else "Failed"
            })

    return render(request, "dna_center_cisco/interfaces.html", {"interfaces": interfaces, "device_ip": device_ip})

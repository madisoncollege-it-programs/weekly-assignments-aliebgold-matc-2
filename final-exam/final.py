#!/usr/bin/env python3

import argparse
import bs4
import json
import requests
import socket

parser = argparse.ArgumentParser(description="Final")
parser.add_argument('-f', '--function', dest='function',type=int,metavar="[what funtion]", required=True, help="<required> Enter a simple Integer")
parser.add_argument('-i', '--ipaddress', dest='ip', type=str,metavar="[Enter this IP Address 172.31.29.252]", required=True, help="Enter an IP address")

args = parser.parse_args()

ip = args.ip
function = args.function


url = f"http://{ip}/q{function}"
print("Name: Aaron Liebgold")
print(url)

def get_response():
    response = requests.get(url)
    print(f"ANSWER: {response.text}")

def parse_string():
    response = requests.get(url)
    myHTML = bs4.BeautifulSoup(response.text,features="html.parser")
    links = myHTML.find_all('h3')
    OKC = str(links)
    will = OKC[9]
    connect = OKC[11]
    at = OKC[13]
    end = OKC[15]
    of  = OKC[17]
    string = OKC[19]
    f0r = OKC[21]
    one = OKC[23]
    word = OKC[25]
    total = will + connect + at + end + of + string + f0r + one + word
    print(f"ANSWER: {total} Aaron Liebgold ")

def parse_header():
    response = requests.get(url)
    print(f"ANSWER: {response.headers['MATC-HEADER']}")
    myHtml = bs4.BeautifulSoup(response.text,features="html.parser")
    links = myHtml.find_all('h3')

def parse_json():

    jsonResponse = requests.get(url)
    dictResponse = json.loads(jsonResponse.text)
    for key in dictResponse:
        for a in dictResponse[key]:
            if "The Shining" in str(a):
                BD = str(a)
                GD = BD.replace("{", "")
                GG = GD.replace("}", "")
                FF = GG.split(",")
                for a in FF:
                    if "publisher" in a:
                        r = a.replace("publisher", "")
                        d = r.replace("'", "")
                        g = d.replace(":", "")
                        print(f"ANSWER: {g.replace(' ', '')}")

def socket_client():
    C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SND_DATA = "secret"
    RCV_DATA = ""

    list = []

    for port in range(5000,6000):

        try:
            C_SOCK.connect((ip, port))
            #list.append(port)
            C_SOCK.send(bytearray(SND_DATA, "utf8"))
            RCV_DATA = C_SOCK.recv(1024)
            print(f"ANSWER: {RCV_DATA.decode()}")

        except:
            pass


if args.function == 1:
    get_response()

if args.function == 2:
    parse_string()

if args.function == 3:
    parse_header()

if args.function == 4:
    parse_json()

if args.function  == 5:
    socket_client()

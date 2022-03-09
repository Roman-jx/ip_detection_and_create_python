# import imp;
import folium
# from tkinter import font;
import requests
from urllib import response
from pyfiglet import Figlet


# Create func for info about ip address -?
def get_ip(ip="127.0.0.1"):
# Create an error check -?
  try:
    # If you follow this link you will get information about your ip -?
    # In {ip} you can add any ip -?
    response = requests.get(url=f"http://ip-api.com/json/{ip}").json();
    # Indicate what information we want to see -?
    data = {
      "|IP info| " : response.get("query"),
      "|Internet Provider| " : response.get("isp"),
      "|Organization| ": response.get("org"),
      "|Country| " : response.get("country"),
      "|City| " : response.get("city"),
      "|Region| " : response.get("regionName"),
      "|Post code| " : response.get("zip"),
      "|Latitude| " : response.get("lat"),
      "|Longitude| " : response.get("lon")
    }
    # Passability according to our dictionary -?
    for key, value in data.items():
      print("{0} : {1}".format(key, value));
    # Map format (HTML) -?
    map_area = folium.Map(location=[response.get("lat"), response.get("lon")]);
    map_area.save(f"{response.get('query')}_{response.get('city')}");
  # If there are problems with the connection -?
  except requests.exceptions.ConnectionError:
    print('|?| -x-> Bro, check your connection, and try again!');

def main():
  about_program = Figlet(font="slant");
  print(about_program.renderText("-------\nIP SCAN\n-------"));
  # Work with user -?
  ip = input('Enter a ip here: ');
  get_ip(ip=ip);

if __name__ == "__main__":
  main();
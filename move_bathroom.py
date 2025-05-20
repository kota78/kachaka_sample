import kachaka_api
client = kachaka_api.KachakaApiClient("192.168.11.5:26400")
import math

##client.move_shelf("S01", "L01")
##client.move_to_location("L01")

client.move_to_pose(4.1, -2.0,3.14)
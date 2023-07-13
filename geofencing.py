import requests
def test_api_function(camera_name, function_name, data, url):
    post_data = {
        "camera_name": camera_name,
        "function_name": function_name,
        "data": data
    }
    r = requests.post(url, json=post_data)
    print(f"Status Code: {r.status_code}, Response: {r.json()}")
    return f"Status Code: {r.status_code}, Response: {r.json()}"
"""
DOCS
gps_from_px()
camera_name : str
pixel_points: [[width pixel, height pixel], ...]  image position
camera_position:[x, y, z] = [heading, tilt, zoom] ONVIF format
return: [[latitude, longitude], ...]
url = "http://192.168.22.24:20001/process/"
camera_name = "mandela"
function_name = "gps_from_px"
camera_position  = [0, 0.45, 0] #x onvif, y onvif y zoom
list_pixel_point = [[512, 512]]
data = [list_pixel_point, camera_position]
print(test_api_function(camera_name, function_name, data, url))
"""

import requests
import json
import turtle

iss = turtle.Turtle()

def setup(window):
    global iss
    window = turtle.Screen()
    window.setup(1000, 500)
    window.bgpic('earth.gif')
    window.setworldcoordinates(-180, -90, 180, 90)
    turtle.register_shape('iss.gif')
    iss.shape('iss.gif')
    iss.color('red')


def mov_iss(lat, longt):
    global iss
    iss.pendown()
    iss.goto(longt, lat)
    iss.penup()

def track_iss():
    url = 'http://api.open-notify.org/iss-now.json'
    res = requests.get(url)
    if (res.status_code == 200):
        res_dict = json.loads(res.text)
        position = res_dict['iss_position']
        print('International Space Station at ' +
            position['latitude'] + ',' + position['longitude'])
        lat = float(position['latitude'])
        longt = float(position['longitude'])
        mov_iss(lat, longt)
    else:
        print('error', res.status_code)
    widget = turtle.getcanvas()
    widget.after(1000,track_iss)

def main():
    global iss
    disp = turtle.Screen()
    setup(disp)
    track_iss()


if __name__ == '__main__':
    main()
    turtle.mainloop()
    
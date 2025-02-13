import time
import RPi.GPIO as GPIO
from flask import Flask, Response
from flask_socketio import SocketIO
import cv2
import threading

app = Flask(__name__)
socketio = SocketIO(app)

def read_camera():
        global latest_frame
        cam = cv2.VideoCapture(0)
        while True:
                success, frame = cam.read()
                if success:
                        ret, buffer = cv2.imencode('.jpg', frame)
                        latest_frame = buffer.tobytes()
                time.sleep(0.5)

@app.route('/')
def index():
        if latest_frame:
                return Response(latest_frame, mimetype='image/jpeg')
        else:
                return "No frame available", 500

@socketio.on('message')
def handle_message(message):
        try:
                print(f"Received {message}")
                command_map = {
                        'w':w,
                        'a':a,
                        's':s,
                        'd':d,
                        'stop':stop
                }
                command_func = command_map.get(message.split(':')[0])
                strength = message.split(':')[1]
                strength = int(strength)
                if command_func:
                        command_func(strength)
        except Exception as e:
                print(f"Exception: {e}")

def start_server():
        socketio.run(app, host='0.0.0.0', port=5000)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = {
        'MAF':10,
        'MAB':9,
        'MBF':8,
        'MBB':7
}

STOPTIME = 0.25

apins = {}

for pin_name, pin_number in pins.items():
        GPIO.setup(pin_number, GPIO.OUT)
        apins['PWM' + pin_name] = GPIO.PWM(pin_number, 20)
        apins['PWM' + pin_name].start(0)

pins.update(apins)

def set(apin, value, strength=100):
        pwm_instance = pins.get('PWM' + apin)
        if pwm_instance:
                if value == 1:
                        pwm_instance.ChangeDutyCycle(strength)
                elif value == 0:
                        pwm_instance.ChangeDutyCycle(0)
        else:
                print(f"PWM instance for pin {apin} not found.")

def stop(_):
        for pin_name in pins:
                if pin_name.startswith('PWM'):
                        set(pin_name[3:], 0)


def w(strength):
    set('MAF', 1, strength=strength)
    set('MBF', 1, strength=strength)

def a(strength):
    set('MAB', 1, strength=strength)
    set('MBF', 1, strength=strength)

def s(strength):
    set('MAB', 1, strength=strength)
    set('MBB', 1, strength=strength)

def d(strength):
    set('MAF', 1, strength=strength)
    set('MBB', 1, strength=strength)



if __name__ == '__main__':
        camera_thread = threading.Thread(target=read_camera)
        camera_thread.daemon = True
        camera_thread.start()
        try:
                start_server()
        except KeyboardInterrupt:
                GPIO.cleanup()
                print("Bye!")

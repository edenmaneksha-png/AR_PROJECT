from flask import Flask, render_template
import cv2
import mediapipe as mp
import mediapipe as mp
print(dir(mp))

app = Flask(__name__)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

@app.route("/")
def home():
    return render_template("index.html")

def camera():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            print("Hand detected")

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()

if __name__ == "__main__":
    camera()
    app.run(debug=True)
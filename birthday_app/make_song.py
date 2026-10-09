"""Generates assets/happy_birthday.wav (music-box style Happy Birthday, public-domain melody).
Run once:  python make_song.py
To use a real song instead, just drop an MP3 named  assets/birthday_song.mp3  (the app prefers it)."""
import wave
from pathlib import Path
import numpy as np

SR = 22050
BEAT = 0.58
N = {"C3":130.81,"F3":174.61,"G3":196.0,"E3":164.81,"G4":392.0,"A4":440.0,"B4":493.88,"C5":523.25,
     "D5":587.33,"E5":659.25,"F5":698.46,"G5":783.99,"C4":261.63,"E4":329.63,"F4":349.23,"D4":293.66}

melody = [
    ("G4",.75),("G4",.25),("A4",1),("G4",1),("C5",1),("B4",2),
    ("G4",.75),("G4",.25),("A4",1),("G4",1),("D5",1),("C5",2),
    ("G4",.75),("G4",.25),("G5",1),("E5",1),("C5",1),("B4",1),("A4",2),
    ("F5",.75),("F5",.25),("E5",1),("C5",1),("D5",1),("C5",3),
]
# bass / chord roots: (start_beat, root, third, fifth)
chords = [(0,"C3","E4","G4"),(3,"C3","E4","G4"),(6,"G3","B4","D5"),(9,"G3","B4","D5"),
          (12,"C3","E4","G4"),(15,"C3","E4","G4"),(19,"F3","A4","C5"),(22,"C3","E4","G4"),(25,"C3","E4","G4")]

def tone(f, dur, vol=1.0, decay=3.2):
    t = np.arange(int(SR * (dur + 0.9))) / SR
    env = np.minimum(t / 0.008, 1) * np.exp(-decay * t)
    s = (np.sin(2*np.pi*f*t) + .35*np.sin(2*np.pi*2*f*t) + .12*np.sin(2*np.pi*3*f*t) + .05*np.sin(2*np.pi*5.4*f*t))
    return vol * env * s

total_beats = sum(d for _, d in melody) + 2
buf = np.zeros(int(SR * (total_beats * BEAT + 1.5)))

def add(sig, start_beat):
    i = int(start_beat * BEAT * SR)
    buf[i:i+len(sig)] += sig[:len(buf)-i]

b = 0
for note, d in melody:
    add(tone(N[note], d*BEAT, .55), b); b += d
for sb, root, third, fifth in chords:
    add(tone(N[root], BEAT, .45, 2.2), sb)
    add(tone(N[third]/2, BEAT, .18, 2.8), sb + 1)
    add(tone(N[fifth]/2, BEAT, .18, 2.8), sb + 2)

# soft echo
d = int(.28 * SR)
echo = buf.copy()
echo[d:] += .30 * buf[:-d]
echo[2*d:] += .12 * buf[:-2*d]
echo /= np.max(np.abs(echo)) * 1.15

out = Path(__file__).parent / "assets" / "happy_birthday.wav"
out.parent.mkdir(exist_ok=True)
with wave.open(str(out), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((echo * 32767).astype(np.int16).tobytes())
print("saved", out, round(len(echo)/SR, 1), "sec")

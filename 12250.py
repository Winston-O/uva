
import sys

lang_map = {
    "HELLO" : "ENGLISH",
    "HOLA" : "SPANISH",
    "HALLO" : "GERMAN",
    "BONJOUR" : "FRENCH",
    "CIAO" : "ITALIAN",
    "ZDRAVSTVUJTE" : "RUSSIAN"

}
count = 0
for line in sys.stdin:
    N = line.strip()
    if N == "#":
        break

    if N in lang_map:
        Ori = lang_map[N]
    else:
        Ori = "UNKNOWN"
    count += 1
    print ("Case " + str(count) + ": " + Ori)

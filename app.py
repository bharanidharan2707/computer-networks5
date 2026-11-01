from flask import Flask, render_template, jsonify
from scapy.all import sniff, IP, TCP, UDP, ICMP
import threading

app = Flask(__name__)

packets = []
capturing = False

def capture_packets():
    global capturing

    def process_packet(packet):
        if IP in packet:
            protocol = "Other"

            if TCP in packet:
                protocol = "TCP"
            elif UDP in packet:
                protocol = "UDP"
            elif ICMP in packet:
                protocol = "ICMP"

            packets.append({
                "source": packet[IP].src,
                "destination": packet[IP].dst,
                "protocol": protocol,
                "size": len(packet)
            })

            if len(packets) > 100:
                packets.pop(0)

    sniff(
        filter="ip",
        prn=process_packet,
        store=False,
        stop_filter=lambda packet: not capturing
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start")
def start():
    global capturing

    if not capturing:
        packets.clear()
        capturing = True
        threading.Thread(
            target=capture_packets,
            daemon=True
        ).start()

    return jsonify({"status": "Packet capture started"})

@app.route("/stop")
def stop():
    global capturing
    capturing = False
    return jsonify({"status": "Packet capture stopped"})

@app.route("/packets")
def get_packets():
    return jsonify(packets)

if __name__ == "__main__":
    app.run(debug=False, port=5004)
from flask import Flask, render_template, request, jsonify
import socket
import threading

app = Flask(__name__)

def tcp_scan(ip, startPort, endPort):
    open_ports = []
    for port in range(startPort, endPort + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.settimeout(0.5)
            if not tcp.connect_ex((ip, port)):
                open_ports.append(port)
            tcp.close()
        except Exception:
            pass
    return open_ports

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    ip = request.form['ip']
    start_port = int(request.form['start_port'])
    end_port = int(request.form['end_port'])
    
    open_ports = tcp_scan(ip, start_port, end_port)
    port_links = [f"<a href='http://{ip}:{port}' target='_blank'>Port {port}</a>" for port in open_ports]
    
    return jsonify({'open_ports': port_links})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

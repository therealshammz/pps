# Port Scanner Web Application

This project is a simple yet effective TCP port scanner built using Python, Flask, and a minimalistic web interface. The primary objective of the project is to allow users to scan a specific host or a network subnet for open TCP ports, giving immediate feedback via a web-based front-end. The tool is lightweight, easy to use, and is perfect for network administrators, cybersecurity enthusiasts, and anyone interested in network security.

Features:

TCP Port Scanning: The application allows you to scan a range of ports (from a specified start to end port) on either a single host or an entire network. It will identify open TCP ports, helping you assess the security posture of a network.

Real-Time Results: As the scan progresses, users can see the open ports being discovered, providing immediate feedback without waiting for the entire scan to complete.

Web Interface: The front-end is simple, intuitive, and easy to use, making the tool accessible to both technical and non-technical users. The scan can be initiated through a simple HTML form.

Fast and Optimized Scans: With a low socket timeout configuration, the tool can conduct port scans in an efficient and timely manner.

Customizable: Users can specify the IP address and the port range, allowing for a tailored scan depending on the task at hand.

Easy Setup: All you need to run the application is Python, Flask, and the necessary dependencies. A simple installation and setup process ensures you can quickly get up and running.

Technologies:

Back-End: The port scanning functionality is implemented using Python’s socket library, and the web server is powered by Flask, a lightweight Python framework.

Front-End: The web interface is built using HTML, CSS, and JavaScript (with jQuery for AJAX functionality). This allows for a dynamic, real-time user experience without needing to refresh the page.

Libraries:

Flask: For handling HTTP requests and rendering templates.
socket: For performing the actual TCP port scans.
jQuery: For handling asynchronous requests (AJAX) between the front-end and back-end.

How It Works:

User Input: The user provides an IP address (or network range) and a range of ports to scan through the web form.
Port Scanning: The Python back-end (using the socket library) performs the TCP port scan by attempting to establish connections to each port in the specified range.
Real-Time Feedback: As each open port is discovered, the results are sent back to the front-end via AJAX and displayed to the user.
Output: The results are shown in an ordered list, displaying each open port found during the scan. If no open ports are detected, the application notifies the user that no open ports were found.

Use Cases:

Network Security: This tool can be used by cybersecurity professionals to audit the security of a network, identifying which ports are open and possibly vulnerable to exploitation.
Network Administration: Network administrators can use the scanner to troubleshoot connectivity issues or monitor the status of servers and services across a network.
Educational: This project can serve as a learning tool for those interested in learning about networking concepts, TCP protocols, and web development.

Installation:

Clone the Repository: First, clone the repository to your local machine using Git:
```
git clone https://github.com/your-username/your-repository-name.git
```
Navigate to the Project Directory: Change into the directory of the cloned repository:
```
cd pps
```
Install Dependencies: You will need Python and Flask installed. You can install the necessary dependencies using pip:
```
pip install flask
```
Run the Flask Development Server: Once Flask is installed, start the Flask server:
```
python pps.py
```
Access the Application: After running the Flask server, open your web browser and go to:

http://127.0.0.1:5000

This will load the port scanner application, where you can start scanning.

This will start a local web server. You can open your web browser and go to http://127.0.0.1:5000 to start using the port scanner.


License:
  This project is licensed under the MIT License, which means you are free to use, modify, and distribute the code with proper attribution.

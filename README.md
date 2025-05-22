# Figma-Style Collaborative Cursor App

**Live Demo:** [https://collab-demo.onrender.com](https://collab-demo.onrender.com)  
**GitHub Repo:** [https://github.com/KalminX/collab_demo](https://github.com/KalminX/collab_demo)

Real-time collaborative mouse tracking inspired by Figma. Each user sees the live cursor position of all others in a shared session, represented by a color-coded dot.

---

## Features

- Real-time cursor movement synced across all users
- Unique color per user for easy identification
- Auto room join — all users share the same space
- Smooth animation with lightweight frontend logic
- Docker-ready and easily deployable to services like Render

---

## Tech Stack

- **Backend:** Flask, Flask-SocketIO, Eventlet  
- **Frontend:** HTML, CSS, JavaScript (vanilla)  
- **Deployment:** Docker, Render.com

---

## Getting Started

### Clone the Repo

git clone https://github.com/KalminX/collab_demo.git
cd collab_demo

Run Locally

Install dependencies:

pip install -r requirements.txt

Start the server:

python app.py

Open your browser at:

http://localhost:5000

Open multiple tabs or devices to see live cursor interaction.


---

Using Docker

Build the Image

docker build -t figma-cursor .

Run the Container

docker run -p 5000:5000 figma-cursor

Then go to http://localhost:5000


---

Deployment on Render

1. Push your code to GitHub.


2. Log in to https://render.com.


3. Click "New Web Service".


4. Choose "Docker" as your environment.


5. Connect your GitHub repo and deploy.


6. Set port to 5000.



App will be live at a public URL like:

https://your-app-name.onrender.com


---

Project Structure

.
├── app.py               # Main Flask app with Socket.IO setup
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build config
├── templates/
│   └── index.html       # Frontend interface


---

Contributing

Pull requests and feedback are welcome!
Feel free to open an issue or fork the project.


---

License

MIT License © 2025 KalminX

Let me know if you’d like me to add:
- A project logo
- Live preview GIF
- README badges for deployment, license, etc.

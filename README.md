## How to run the code
1. Install python 3.10
2. create python virtual environment: `python -m venv facedetection`
3. install dependencies: `pip install -r requirements.txt`
4. start the server: `python main.py`
5. test the server: `curl -F image=@josh.webp http://127.0.0.1:5001/detect_faces`

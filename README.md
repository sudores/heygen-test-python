## How to run the code
1. Install python 3.12
2. create python virtual environment: `python3 -m venv facedetection`
3. enable virtuan env: `source venv/bin/activate`
4. install dependencies: `pip install -r requirements.txt`
5. start the server: `python main.py`
6. test the server: `curl -F image=@josh.webp http://127.0.0.1:5001/detect_faces`

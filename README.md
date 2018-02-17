# barcode-microservice
Microservice to read and generate barcodes and QR Codes written in Python and Flask

# Installation
- Make a new python3 virtual environment
```
    python3 -m venv barcode-env
```
- Activate the virtual environment
```
    source barcode-env/bin/activate
```
- Install the dependencies
```
    pip install -r requirements.txt
```
- You could either run the app using Flask's inbuilt development server for testing or use gunicorn  or use Docker to run it in a container with gunicorn
```
    python app/application.py => Flask Development server on http://localhost:5000

    OR

    pip install gunicorn
    gunicorn -w 4 -b 0.0.0.0:5000 application:app => run inside app/, this starts a server on http://localhost:5000    
```

# TODO
- Frontend
- QR Code Generation
- Barcode Generation
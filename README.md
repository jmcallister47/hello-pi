## Hello Pi

Hello Pi is a simple project designed to greet visitors. The project consists of a Raspberry Pi, camera and speaker connected via AUX or bluetooth. 

The Pi uses [opencv](https://opencv.org/) to constantly poll for faces over an interval without crashing/overheating. If at any point one or more faces is detected, the Pi then sends a request to the Microsoft Face API. The api-training portion of the code consists of scripts to train the API to recognize the faces of any expected visitors. Based on the individual recognized, the Pi then says a custom message using a local text to audio controller.

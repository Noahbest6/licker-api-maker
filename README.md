# Licker API Maker

Licker API Maker is a simple and easy-to-use API generator written in Python. It allows you
to quickly and easily create APIs from plain text files.

## Getting Started

1. Clone the repository or download the source code.
2. Install the dependencies by running pip install -r requirements.txt in the terminal.
3. Create a text file in the lists folder. The name of the file is up to you, but make sure it has a .txt extension.
4. In the text file, enter any text you want. To specify the data that will be returned by the API, surround the text with --namehere-- and --namehere end--. For example:
```
--main--
apple
banana
cherry
--main end--
```

The text between the --namehere-- and --namehere end-- tags will be randomly
selected and returned by the API as a JSON object:
```
{"data": "randomItem"}
```
Note: There must be two --namehere-- tags in the file to work properly.c

##  Running the API

Licker API Maker runs on port 1237 and uses Flask to handle incoming requests. 
To run the API, simply run the following command in the terminal:
```
python main.py
```
Once the API is running, you can access it using the URL specified in the output.txt file.

##  Limitations
Currently, Licker API Maker only works on Linux-based systems and has been tested on a Raspberry Pi. 
Windows support may be added in the future.

##  Contributing
If you would like to contribute to the development of Licker API Maker, 
please feel free to submit a pull request or reach out to the developers.

## Thank You
Thank you for taking the time to read this README. We hope you find Licker API Maker useful and look forward to hearing from you.

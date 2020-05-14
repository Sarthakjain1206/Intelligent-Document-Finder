# Intelligent-Document-Finder
A tool which can find your any document using **semantic search**

# What is Intelligent Document Finder ?
How easy do you find it to remember the exact location of a document that you created last year? Not very easy, right? Big Organizations/people deal with hundreds of documents daily and forget about them, most of the time.
<br>
But what if we want that old documentation again for some work, but unfortunately you do not remember the name or the actual content of that document to retrieve it from the large storage of your computer.
<br>
In such cases, use of a __Intelligent document finder__ can really make a huge difference. As, it can Search for the document(```semantically```) of your need based on a query input. This will not only help in faster access to the document, but will also help in grouping similar documents together and in analysing them.
<br>
# Note: 
Currently this repositry is using predefined database of news articles gathered by web scraping. Due to the github restrictions on uploading the large files, we cannot upload it here. 
<br><br>
Soon, we will add the support of the dynamic databases, so that you can use this tool for your own databases to build your own custom search engine.
<br>
# Technologies Used
**```Python3.6```**
__```JavaScript```__
__```HTML/CSS```__
<br>
<h4>Database Used:</h4>
 SQlite
<br>
<h4>For implementing searching:</h4>
 Various NLP(Natural Language Processing) techniques is used.
<br>
<h4>For website(Local Host):</h4>

- Python-based Web framework : Flask
- JavaScript/JQuery

# Program Flow
<img src="https://github.com/Sarthakjain1206/Intelligent-Document-Finder/blob/master/Flowchart.png" alt="Trulli" width="700" height="500">

# Compatibility
- Backend (AI part) is compatible on any machine that has python and required dependencies installed.
- Recommended browsers: Mozilla Firefox and Google Chrome.

# How to Install and Use?

```> mkdir IntelligentDocumentFinder```
<br>
<br>
```> cd IntelligentDocumentFinder```
<br>
<br>
```> git clone https://github.com/Sarthakjain1206/Intelligent-Document-Finder```
<br>

Install Vitual Environment if not installed
<br>
- On Linux/MacOs
```> python3 -m pip install --user virtualenv```
- On windows
```> py -m pip install --user virtualenv```

Create Virtual Environment
- On macOS and Linux:
```> python3 -m venv env```
- On Windows:
```> py -m venv env```

Activate Environment:
- On macOS and Linux:
```> source env/bin/activate```
- On Windows:
```> .\env\Scripts\activate```

```> pip install -r requirements.txt```

__Download Glove Word Embeddings__ from this [link](https://www.kaggle.com/terenceliu4444/glove6b100dtxt), decompress it and copy the ```glove.6B.100d``` file in ```DataBase``` folder

then, 
run initial_file.py through this command
```> python initial_file.py```

Now you are good to go.. Just type this command everytime you want to access it, and open the website in chrome/firefox
<br>
```> python src/app.py```


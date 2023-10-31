Stanford Question Answering Dataset (SQuAD) 2.0
--- 

![[DALL·E 2022-10-12 21.58.00 - Make It Look More Technological.png]]
  
Question Answering (QA) is a sub-domain of Machine Comprehension (MC) and is one of the more challenging tasks in Artificial Intelligence (AI). The field of Natural Language Processing (NLP) has experienced a fast evolution in recent years thanks to the development of [[Deep Learning]] research and the advent of [[Transfer Learning]] techniques. These advances have led to the development of powerful pre-trained NLP models such as OpenAI's [[OpenAI's GTP-3]], Google's MUM, and BigScience's BLOOM. With such progress, improved systems, and applications for NLP tasks, there has been rapid development, such as the 
  
### Open-domain QA 

Open-domain QA is a type of question answering in which the answer can be found in any text document, regardless of its topic or content. This type of QA contrasts closed-domain QA, where the answer is restricted to a specific domain or set of documents. Open-domain QA is more complex than closed-domain QA because the search space is much larger. However, it has the advantage of being able to answer any question, regardless of the topic. One example of an open domain question answering system is DrQA. DrQA is an Open-domain QA developed by Meta Research that uses a large base of Wikipedia articles as its knowledge source. 

### Closed-domain QA 

The cdQA-suite is a collection of tools that makes it easy to build a closed-domain QA system. Closed-domain QA is a type of question answering in which the answer is restricted to a specific domain or set of documents. This is in contrast to open-domain QA, in which the answer can be found in any text document, regardless of its topic or content. Closed-domain QA is less complicated than open-domain QA because the search space is smaller than the larger counterpart. However, it has the disadvantage of being unable to answer questions outside the specific domain.

![[Pasted image 20221013160902.png]]

## cdQA-suite

![[Pasted image 20221012230259.png]]

[cdQA-suite](https://github.com/cdqa-suite) is a set of three tools used to build a question-answering system.

1. The first tool,  [cdQA](https://github.com/cdqa-suite/cdQA), is a Python package to implement a QA pipeline.
2. The second tool, [cdQA-annotator](https://github.com/cdqa-suite/cdQA-annotator), is a tool to annotate question-answering datasets.
3. The third tool,[cdQA-ui](https://github.com/cdqa-suite/cdQA-ui), is a user interface to connect the back-end system to a website.

This library is not longer maintained on GitHub. A maintained alternative to cdQA is [[2. Areas Personal/Technology and applied sciences/Computing/Computer science/Artificial Intelligence/Natural Language Processing/Question-Answering/Haystack/Overview|Haystack]].

This article guides the reader through creating a quality assurance system using various software modules. Each module will be covered in detail so that a system tailored to specific needs develops.

## cdQA

![[Screen-Shot-2020-08-07-at-10.webp]]

The cdQA system has two main parts: the Retriever and the Reader. The retriever gets documents from a particular source, and the reader looks at and pulls information from those documents.

### Retriever

A retriever is a component in a question-answering system responsible for retrieving relevant documents from an extensive collection of documents. The primary purpose of the retriever is to reduce the amount of text the reader component needs to process. 

There are two main types of retrievers: sparse retrievers and dense retrievers. Sparse retrievers use the bm25 model to complete the document retrieval function, while dense retrievers use the DPR model.

### Reader  

A reader is a deep learning model trained to retrieve the text segment with the highest correlation with the queried question text from a small amount of text outputted by the retriever. This allows the reader to output the answer to the question without reading through the entire text.

### Data Preparation

Data preparation involves different techniques, including cleaning, normalization, and transformation. Each of these techniques is important in its own right, and the specific techniques used will depend on the dataset and the machine learning algorithm used.

1. Data Cleaning: Data cleaning is identifying and cleaning up inaccuracies and inconsistencies in data. Data cleaning is a vital step in data preparation, starting before other techniques.
2. Data Normalization: Data normalization is the process of rescaling data to a standard range. Data normalization is a vital step in data preparation after data cleaning.
3. Data Transformation: Data transformation is converting data from one format to another. Data transformation is a vital step in data preparation after data normalization.


### Mechanism of cdQA pipeline

A cdQA pipeline typically consists of three components: a question-processing component, a document retrieval component, and an answer-processing component. 

The cdQA pipeline takes in a question and outputs the most likely answer to that question.

The system first retrieves a list of documents from the database that will likely contain the answer to the question. It then sends the question and the retrieved documents to the reader, a pre-trained Deep Learning model. The reader outputs the most probable answer it can find in each document. Finally, the system compares the answers using an internal score function and outputs the most likely answer.

### cdQA Python Package

This package can no longer be installed using pip. To install, clone the repository from the source.


```jupyter
# This package can no longer be installed using pip
# Instead, download it from the source code on Github
!git clone https://github.com/cdqa-suite/cdQA.git &&
!cd cdQA &&
!pip install -e .
```



Reminder: 
- [ ] (@2022-11-06 23:46)

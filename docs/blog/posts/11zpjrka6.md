---
title: Building an Indexing Pipeline for LinkedIn Skill Assessments Quizzes Repository
description: Creating an efficient indexing pipeline for the 'linkedin-skill-assessments-quizzes' repository involves systematic cloning, data processing, indexing, and query service setup. This comprehensive guide will walk you through each step with detailed code snippets, leveraging the `Whoosh` library for indexing.
authors: [harmindersinghnijjar]
date: 2023-11-14
tags: [Python, Whoosh, Indexing, LinkedIn, Skill Assessments, Quizzes]
categories: [Python, Whoosh, Indexing, LinkedIn, Skill Assessments, Quizzes]
toc: true
comments: true
---

# Building an Indexing Pipeline for LinkedIn Skill Assessments Quizzes Repository

Creating an efficient indexing pipeline for the `linkedin-skill-assessments-quizzes` repository involves systematic cloning, data processing, indexing, and query service setup. This comprehensive guide will walk you through each step with detailed code snippets, leveraging the `Whoosh` library for indexing.

## Pre-requisites

You want to create a new directory and name it `linkedin_skill_assessments_quizzes`, you need to first open the command prompt in the current working directory. To do this, you can use the following command in the command prompt.

```bash
cd path_to_your_current_working_directory

```
Replace `path_to_your_current_working_directory` with the actual path where you want to create the new directory.  

Alternatively, on Windows, you can open the command prompt in the current working directory by clicking on the address bar and typing `cmd`, and pressing enter.  

Once you are in the desired working directory, create a new directory named linkedin_skill_assessments_quizzes by executing the following command:  

```bash
mkdir linkedin_skill_assessments_quizzes
```

Now navigate to this new directory by executing the following command:

```bash
cd linkedin_skill_assessments_quizzes
```

This is where you will be cloning the repository and creating the indexing pipeline.

## Introduction

LinkedIn Skill Assessments Quizzes is a repository of quizzes for various skills. It contains MD files for each quiz. The repository is available on <a href="https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes" target="_blank" rel="noopener noreferrer">GitHub</a>. The repository has over 27,400 stars and 13,600 forks. It is a popular repository that is used by many people to prepare for interviews and improve their skills.


## Step 1: Cloning the Repository

Start by cloning the repository to your local environment. This makes the content available for processing.

```bash
git clone https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes.git
```
<img src="../../resources/Images/cmd_G8ccMvc9ce.png" alt="Cloning the repository" style="display: block; margin-top: 20px; margin-bottom: 20px;">


## Step 2: Converting the MD Files to JSON

Processing the data involves parsing the MD files converting them to JSON format to extract the relevant information. The following code snippet demonstrates how to extract the question, answer, image, and options from the MD files and save them in a JSON file. This is required for indexing the data which we will cover in the next step.

Add the following code to a file named `process_data.py` in the same directory where you cloned the repository.


```python
import os
import json
import markdown2
import re

# Get the markdown files directory

cloned_repository_directory = r"C:\Users\Harminder Nijjar\Desktop\blog\kb-blog-portfolio-mkdocs-master\scripts\linkedin-skill-assessments-quizzes"

# Create a folder to store the JSON files

output_folder = os.path.join(cloned_repository_directory, "json_output")

# Create the output folder if it doesn't exist

os.makedirs(output_folder, exist_ok=True)

# Create a list to store data for each MD file

data_for_each_md = []

# Iterate through the Markdown files (\*.md) in the current directory and its subdirectories

for root, dirs, files in os.walk(cloned_repository_directory):
    for name in files:
        if name.endswith(".md"): # Construct the full path to the Markdown file
            md_file_path = os.path.join(root, name)

            # Read the Markdown file
            with open(md_file_path, "r", encoding="utf-8") as md_file:
                md_content = md_file.read()

            # Split the content into sections for each question and answer
            sections = re.split(r"####\s+Q\d+\.", md_content)

            # Remove the first empty section
            sections.pop(0)

            # Create a list to store questions and answers for this MD file
            questions_and_answers = []

            # Iterate through sections and extract questions and answers
            for section in sections:
                # Split the section into lines
                lines = section.strip().split("\n")

                # Extract the question
                question = lines[0].strip()

                # Extract the answers
                answers = [line.strip() for line in lines[1:] if line.strip()]

                # Create a dictionary for this question and answers
                qa_dict = {"question": question, "answers": answers}

                # Append to the list of questions and answers
                questions_and_answers.append(qa_dict)

            # Create a dictionary for this MD file
            md_data = {
                "markdown_file": name,
                "questions_and_answers": questions_and_answers,
            }

            # Append to the list of data for each MD file
            data_for_each_md.append(md_data)

# Save JSON files in the output folder

for md_data in data_for_each_md:
    json_file_name = os.path.splitext(md_data["markdown_file"])[0] + ".json"
    json_file_path = os.path.join(output_folder, json_file_name)
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(md_data, json_file, indent=4)

print(f"JSON files created for each MD file in the '{output_folder}' folder.")w
```

![](/docs/resources/Images/cmd_yMKIdojeL3.png)


## Step 3: Indexing the Data

After processing the data, you can index it to make it searchable. Indexing refers to the process of creating an index for the data. The following code snippet demonstrates how to index the data using the `Whoosh` library. This is how the indexing pipeline will work.

Add the following code to a file named `indexing_pipeline.py` in the same directory where you cloned the repository.

```python
import os
import json
import whoosh
from whoosh.fields import TEXT, ID, Schema
from whoosh.index import create_in

# Define the directory where your processed JSON files are located

json_files_directory = r"C:\Users\Harminder Nijjar\Desktop\blog\kb-blog-portfolio-mkdocs-master\scripts\linkedin-skill-assessments-quizzes\json_output"

# Define the directory where you want to create the Whoosh index

index_directory = r"C:\Users\Harminder Nijjar\Desktop\blog\kb-blog-portfolio-mkdocs-master\scripts\linkedin-skill-assessments-quizzes\index"

# Create the schema for the Whoosh index

schema = Schema(
markdown_file=ID(stored=True),
question=TEXT(stored=True),
answers=TEXT(stored=True),
)

# Create the index directory if it doesn't exist

os.makedirs(index_directory, exist_ok=True)

# Create the Whoosh index

index = create_in(index_directory, schema)

# Open the index writer

writer = index.writer()

# Iterate through JSON files and add documents to the index

for json_file_name in os.listdir(json_files_directory):
    if json_file_name.endswith(".json"):
        json_file_path = os.path.join(json_files_directory, json_file_name)
        with open(json_file_path, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file) # Extract 'question' and 'answers' from the JSON file
            question = json_data.get("question", "")
            answers = json_data.get("answers", []) # Combine 'question' and 'answers' into a single field for searching
            content = f"{question} {' '.join(answers)}"
            writer.add_document(
                markdown_file=json_file_name,
                question=content,
                answers=answers, # Use the extracted 'answers' or an empty list if not present
            )

# Commit changes to the index

writer.commit()

print("Indexing completed.")
```

![](/docs/resources/Images/cmd_LrggXREfsw.png)

## Step 4: Setting Up the Query Service

After indexing the data, you can set up a query service to search the index for a given search term. The following code snippet demonstrates how to set up a query service using the `Whoosh` library. This is how the query service will work.

```python
import os
import json
import re
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import MultifieldParser
from whoosh.analysis import StemmingAnalyzer

# Define the schema for the index

schema = Schema(
question=TEXT(stored=True, analyzer=StemmingAnalyzer()),
answer=TEXT(stored=True),
image=ID(stored=True),
options=TEXT(stored=True),
)

def create_search_index(json_files_directory, index_dir):
    if not os.path.exists(index_dir):
        os.makedirs(index_dir)

    index = create_in(index_dir, schema)
    writer = index.writer()

    for json_filename in os.listdir(json_files_directory):
        json_file_path = os.path.join(json_files_directory, json_filename)
        if json_file_path.endswith(".json"):
            try:
                with open(json_file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    for question_data in data["questions_and_answers"]:
                        question_text = question_data["question"]
                        answer_text = "\n".join(question_data["answers"])
                        image_id = data.get("image_id")
                        options = question_data.get("options", "")
                        writer.add_document(
                            question=question_text,
                            answer=answer_text,
                            image=image_id,
                            options=options,
                        )
            except Exception as e:
                print(f"Failed to process file {json_file_path}: {e}")

    writer.commit()
    print("Indexing completed successfully.")

def extract_correct_answer(answer_text):
    # Use regular expression to find the portion with "- [x]"
    match = re.search(r"- \[x\].\*", answer_text)
    if match:
        return match.group()
    return None

def search_index(query_str, index_dir):
    try:
        ix = open_dir(index_dir)
        with ix.searcher() as searcher:
            parser = MultifieldParser(["question", "options"], schema=ix.schema)
            query = parser.parse(query_str)
            results = searcher.search(query, limit=None)
            print(f"Search for '{query_str}' returned {len(results)} results.")
            return [
                {
                    "question": result["question"],
                    "correct_answer": extract_correct_answer(result["answer"]),
                    "image": result.get("image"),
                }
                for result in results
            ]
    except Exception as e:
        print("An error occurred during the search.")
        return []

if __name__ == "__main__":
    json_files_directory = r"C:\Users\Harminder Nijjar\Desktop\blog\kb-blog-portfolio-mkdocs-master\scripts\linkedin-skill-assessments-quizzes\json_output" # Replace with your JSON files directory path
    index_dir = "index" # Replace with your index directory path

    create_search_index(json_files_directory, index_dir)

    original_string = "Why would you use a virtual environment?"  # Replace with your actual search term
    # Remove the special characters from the original string
    query_string = re.sub(r"[^a-zA-Z0-9\s]", "", original_string)
    query_string = query_string.lower()
    query_string = query_string.strip()
    search_results = search_index(query_string, index_dir)

    if search_results:
        for result in search_results:
            print(f"Question: {result['question']}")
            # Remove the "- [x]" portion from the answer
            print(f"Correct answer: {result['correct_answer'].replace('- [x] ', '')}")
            if result.get("image"):
                print(f"Image: {result['image']}")
            print("\n")
        print(f"Search for '{original_string}' completed successfully.")
        print(f"Found {len(search_results)} results.")
    else:
        print("No results found.")
```

![](/docs/resources/Images/cmd_NFJKOMMqPw.png)


## Conclusion

Creating an efficient indexing pipeline for the 'linkedin-skill-assessments-quizzes' repository involves systematic cloning, data processing, indexing, and query service setup. This comprehensive guide has walked you through each step with detailed code snippets, leveraging the `Whoosh` library for indexing. You should now be able to query the index and get the results. The script will print the question, answer, and image (if available) for each result. 

Since the data is indexed, you can easily search for a given term and get the results. This can be useful for finding the answers to specific questions or searching for a particular topic. You can also use the query service to create a web application that allows users to search the index and get the results.

## References

- <a href = "https://whoosh.readthedocs.io/en/latest/intro.html" target = "_blank" rel = "noopener noreferrer">Whoosh Documentation</a>



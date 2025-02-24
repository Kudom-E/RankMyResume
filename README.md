# 📄 RankMyResume

This project is a platform built using python.

**Document contents**

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation-and-setup)
  1. [Clone the Repository](#1-clone-the-repository)
  2. [Enter Directory](#2-enter-directory)
  3. [Install Dependencies](#3-install-dependencies)
  4. [Run the Script](#4-run-the-script)


## 📌 Overview
**RankMyResume** is a Python script that ranks PDF resumes based on their relevance to a job description extracted from an HTML file. It leverages OpenAI's `text-embedding-ada-002` model to convert text into embeddings and uses cosine similarity to determine the best-matching resumes.

## 🚀 Features
- 📂 Processes multiple resumes from a specified directory  
- 🌐 Extracts job descriptions from an HTML file  
- 🤖 Uses OpenAI's embedding model to generate text vectors  
- 📊 Computes cosine similarity to rank resumes by relevance  
- 📝 Outputs ranked results  


## 📦 Installation and Setup

### Prerequisites
- **Python 3.8+** installed on your system.
- **OpenAI API key** (for embeddings).
- **Git** (optional, for cloning the repository).

### **1. Clone the Repository**

```bash
git clone https://github.com/Kudom-E/RankMyResume.git

```

### **2. Enter Directory**

```bash
cd RankMyResume

```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt

```

### **4. Run the Script**

```bash
python main.py
```



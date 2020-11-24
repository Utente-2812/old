#!/usr/bin/env python
# coding: utf-8

# In[18]:


import os, docx2txt

def get_doc_text(filepath, file):
    if file.endswith('.docx'):
        text = docx2txt.process(file)
        return text
    elif file.endswith('.doc'):
        doc_file = filepath + file
        docx_file = filepath + file + 'x'
        if not os.path.exists(docx_file):
            os.system('antiword ' + doc_file + ' > ' + docx_file)
            with open(docx_file) as f:
                text = f.read()
            os.remove(docx_file) #docx_file was just to read, so deleting
        else:
            print('Info : file with same name of doc exists having docx extension, so we cant read it')
            text = ''
        return text


# In[19]:


filepath = "C:/Users/rod12/dani/"
files = os.listdir(filepath)
print(files)


for file in files:
    text = get_doc_text(filepath, file)
    print(text)


# In[ ]:





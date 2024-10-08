# Task1

def word_count(file_name:str, output_file:str):
    text_file = open(file_name)
    lines = text_file.readlines()
    lines_count = len(lines)
    word_count = 0
    character_count = 0
    for line in lines:
         print(line)
         word = line.split()
         word_count += len(word)
         character_count += len(line)
    out_file = open(output_file,"x")
    out_file.write(f"lines count is {lines_count}\nwords count is {word_count}\ncharacters count is {character_count}\n")         

# print(word_count("text.txt","result.txt"))


# Task2

import json

def filter_json_data(input_file, output_file, attribute, value):
    try:
        inp_file = open(input_file)
        data = json.load(inp_file)
        inp_file.close()
        if not isinstance(data,list) or not all([isinstance(elem,dict) for elem in data]):
            print("JSON file must contain a list of dictionaries")
        else:
            ls = [i for i in data if i.get(attribute) == value]
            out_file = open(output_file,"w")
            json.dump(ls,out_file,indent=4)
            out_file.close()
            print(f"output is in {output_file}")
    except FileNotFoundError:
        print(f"{inp_file} not found")
    except json.JSONDecodeError:
        print("check input file")

# filter_json_data("data.json","filtered_data.json","Hello","world")

# Task3

import inspect

def decorator(func):
    def wrapper(*args,**kwargs):
            for i in args:
                 if i <= 0 or not isinstance(i,int):
                      raise ValueError("Enter valid number")
            for j in kwargs.values():
                 if j <= 0 or not isinstance(j,int):
                      raise ValueError("Enter valid number for keyword argument")
            return func(*args,**kwargs)
    wrapper.__name__ = func.__name__
    wrapper.__annotations__ = func.__annotations__
    wrapper.__doc__ = func.__doc__
    wrapper.__signature__ = inspect.signature(func)
    return wrapper

@decorator
def foo(a,b):
     return a * b

# try:
#     print(foo(5,b = 7.5))
# except Exception as e:
#      print(e)
     
# Task4

import time
from typing import Callable

def retry(retries:int = 2,delay:float = 1.0):
        def decorator(func:Callable):
            def wrapper(*args,**kwargs):
                  attempt = 0
                  while attempt < retries:
                        try:
                            return func(*args,**kwargs)
                        except Exception:
                            attempt += 1
                            if attempt >= retries:
                                 print(f"function failed after {retries}")
                                 raise
                            print(f"Retrying... ({attempt}/{retries})")
                            time.sleep(delay)
            return wrapper
        return decorator

@retry(retries=5,delay=3)
def read_file(path:str)->str:
     x = open(path,"r")
     text = x.read()
     x.close()
     return text

# try:
#     read_file("text.txt")
# except:
#      print("file not found")

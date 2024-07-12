import requests
from bs4 import BeautifulSoup
import textract
fileIn = "E:\Immortal-Ferdowsi\Data Gathering\DataSet/Ferdousi.epub"
fileOut = "E:\Immortal-Ferdowsi\Data Gathering\DataSet/DataSet.txt"
class Preprocessor:
      def __init__(self,InputPath,OutputPath):
            self.InputPath=InputPath
            self.OutputPath=OutputPath
      def Extract(self):
            # Extract the text out of ferdowsi.epub and write it to DataSet.txt
            content = textract.process(self.InputPath, encoding='utf-8').decode()  
            with open(self.OutputPath, 'w', encoding='utf-8') as fout:
                fout.write(content)
      def Clean(self):
           # Remove All the lines that contain بخش if they are not part of word like ببخشید or ببخش  
           Lines=[]
           with open(self.OutputPath,'r', encoding='utf-8') as fout:
                Lines=fout.readlines()
           with open(self.OutputPath, "w", encoding='utf-8') as f:
                for line in Lines:
                     if not(line.__contains__("بخش ") and (not line.__contains__("ببخش "))):
                          f.write(line)
                          
                        
'''DataProcessor=Preprocessor(fileIn,fileOut)
DataProcessor.Extract()
DataProcessor.Clean()'''
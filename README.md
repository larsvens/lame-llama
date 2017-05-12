# lame-llama

Dependencies:   
Python > 2.7   
PyBuilder for testing
pip install pybuilder
pip install xmlrunner
pip install unittest-xml-reporting

for sound (optional)
sudo add-apt-repository ppa:videolan/stable-daily
sudo apt-get update && sudo apt-get install vlc

run:
import nltk
nltk.download() 
at python prompt, and download the all-corpus with GUI. 

Build instructions:   
Possible to build with PyInstaller or CX_freeze   


Test instructions:   
Add methods to src/unittest/python/rhyme_thyme_tests.py   
Use unittest.assertX()   
Then run pyb at root to run PyBuilder, all tests are executed, as well as code coverage. If code coverage < 70% build is not successfull.

Run instruction:   
Enter the following in your terminal:   
python src/main/python/rhyme_thyme.py   
When prompted, use your keyboard to enter a word, confirm with <ENTER>   



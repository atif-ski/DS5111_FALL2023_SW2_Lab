# DS5111_FALL2023_SW2_Lab
DS5111_FALL2023_SW2_Lab

1) What did you have to do to get make to work?

Had to run the command "sudo apt install make" to make it work. This was recommeded by linux server when I tried to run the make command. 

2) Similarly for python3 -m venv env, what did you have to do? 

Had to run a similar install command on ubuntu "sudo apt install python3 -venv". It would have been extremely difficult without a clear error and correction recommendation from ubuntu server to have identified the problem. Concise and clear error message helped to get this corrected in an efficient manner.

3) Why can't we just do that on a separate line? In other words, why do we have to do that in one line and separate the commands with a ; ?

Its more readable and efficient. Shell does not have to create a separate process for a new command line. Running two commands on one line can be more convenient than running them on two separate lines.

4) As it is, both the env and tests jobs run differently in that only one runs if the directory exists. This is as intended and all is well. What do you think about the job run? What would happen if you accidentaly had a file called run in your directory? What can we do to fix this?

We would need an entry in the .PHONY for a run command. If you have a target that has the same name as a real file on disk, make will not execute the recipe for the target if the file already exists. To avoid this, you can mark the target as a phony target.

5) The code provided to you for the test file starts with two lines, seemingly to append something to sys.path. What is the purpose of these lines?

By appending the current directory to the sys.path list, we are telling the Python interpreter to look for modules in the current directory when we import them.


## Extra credit (Add these to your README at the bottom):

1)  Execute sudo apt install tree, and use that application to print out the file and directory structure, just as it is shown in this document at the top. You will have to look up in the reading, or google it in stackoverflow, what flag you need to exclude the 'env' directory. No need to cut and paste the structure, just include the full line you used to get it working.

tree -aL 2 -I 'env|.git|.pytest_cache|__pycache__'

2)Your .gitignore has 'env/', and also a callout to ignore the compiled python files, the ones in __pycache__ folders. What is the meaning of the **/* ?

list all files and directories in the current directory and all subdirectories. Syntax looks for all the compiled Python code in current and all sub directories.

3)
do a pip list or pip freeze and call out versions of the pytest and pylint packages in your requirements.txt. Include them in your requirements.txt, and for the extra credit, just add a note reminding me you included them.

Note : I have updated the Requirements.txt to reflect the versions of packaages from pip freeze. 

4) In the sample code from the book, why does the line if __name__=="__main__": allow the script to run if called directly, but not otherwise? What's going on there?a

special variable __name__ contains the name of the module that is currently being executed. When a script is called directly, its __name__ is set to "__main__". When a module is imported, its __name__ is set to the name of the module.


5) If you add two print statements, (or any statements for that matter), one above and one below the if __name__... line, what would happen when I do an import of the file? What happens when I call the file directly with python <filename>. Most importantly, why?.

Contd from above question. for the import : The top print will work while the inner print statement will not work since the py file is being imported and does not belong to the file ebing executed. 
For a DIrect call of the .py file : Both the print statements should ideally work. since the __main__ is part of the same .py file. 

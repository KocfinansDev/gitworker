import subprocess
import re
import os


def run(*args):
    return subprocess.check_call(['git'] + list(args))

def run_(*args,folder):
    return subprocess.check_call(['git'] + list(args),cwd=folder)

def clone(repo):
    __project__ = "project_name"
    __repo__ = repo
    
    run('clone', "ssh:$git_url" + __project__ + "/" + __repo__ + ".git", "$path"+__repo__)
    
    change(repo)

def commit(folder):
    commit_message = "$commit_message"
    run_("commit", "-am", commit_message,folder=folder)
     
def branch(folder):
    #br = "$branch_name"
    #run_("checkout", "-b", br,folder=folder)
    #run_("push", "-u", "origin", br,folder=folder)
    run_("push",folder=folder)

def change(repo):  
    drc = '$path'+repo
    pattern = re.compile('$find_str')
    oldstr = '$find_str'
    newstr = '$change_str'

    for dirpath, dirname, filename in os.walk(drc):#Getting a list of the full paths of files
        for fname in filename:
            path = os.path.join(dirpath, fname) #Joining dirpath and filenames
            strg = open(path,encoding = "ISO-8859-1").read() #Opening the files for reading only
            if re.search(pattern, strg):#If we find the pattern ....
                strg = strg.replace(oldstr, newstr) #We will create the replacement condistion
                f = open(path, 'w') #We open the files with the WRITE option
                f.write(strg) # We are writing the the changes to the files
                f.close() #Closing the files 

    commit(drc) 
    branch(drc)              
   

   
def main():

    repos=["repo_names"]

    for repo in repos: 
        clone(repo)



main()

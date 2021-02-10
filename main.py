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

    for dirpath, dirname, filename in os.walk(drc):
        for fname in filename:
            path = os.path.join(dirpath, fname) 
            strg = open(path,encoding = "ISO-8859-1").read()
            if re.search(pattern, strg):
                strg = strg.replace(oldstr, newstr) 
                f = open(path, 'w')
                f.write(strg) 
                f.close() 

    commit(drc) 
    branch(drc)              
   

   
def main():

    repos=["repo_names"]

    for repo in repos: 
        clone(repo)



main()

# args= relative_your_module_path, git_url, relative_path 
# look at pyproject.toml to find a pure python path, if more than one ask the user which one
# create a "__dependencies__/repos" folder in the relative_your_module_path or the root path if not a project
# create a "__dependencies__/modules" folder
# clone the git_url into "__dependencies__/repos"
# look for a pyproject.toml file in the git repo
# either use project path from toml, or ask for path project argument
# subrepo clone into "__dependencies__/repos" then relative symlink the source folder into the 



# import ppp # hacks the sys.path, adds modules under a hashed-folder name
# rumel.yaml = ppp.import("url@tag")

# pureify would try to find import statements, then switch them to be ppp statements. Could be done as a patching step
from fs.osfs import OSFS
projects_fs = OSFS('.')
print sum(projects_fs.getsize(path)
          for path in projects_fs.walkfiles(wildcard="*.py"))

# from fs.osfs import OSFS
# my_fs = OSFS('.')
# my_fs.tree()

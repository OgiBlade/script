import os
main_dir = os.getcwd()

def get_files(directory):
  if len(os.listdir(main_dir)) == 0: return []
 
  for path in os.listdir(directory):    
    path = os.path.join(directory, path)
    
    if os.path.isfile(path):
      print(path)
    else:
      get_files(path)
          
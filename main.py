def information_count(data): #return calculated sum and information format
  sums, data_formats = 0, ["B", "KB", "MB", "GB"]
  max_format, max_format_index = 'B', 0
  for i in data: #Find MAX information Format in data
    if i[3] in data_formats:
      if data_formats.index(i[3]) > max_format_index:
        max_format_index = data_formats.index(i[3])
        max_format = i[3] 
  
  for i in data: #calc sums
    if i[3] == max_format:
      sums += int(i[2])
    else:
      while i[3] != max_format: 
        i[2] = float(i[2])/1024
        i[3] = data_formats[data_formats.index(i[3])+1]      
      sums += i[2]
  
  return (round(sums), max_format)


files = []
with open('input.txt', 'r') as f:
  for i in f.readlines():
    i = i.split()
    j = i[0].split('.')
    files.append(j+i[1:])    
#sort by extension
files = sorted(files, key=lambda file: file[1])
files_dict = {}

for i in files: #fill dict of extensions 
  try:
    files_dict[i[1]].append(i)
  except KeyError:
    files_dict[i[1]] = [i]

#sort by file_name
for i in files_dict:
  files_dict[i] = sorted(files_dict[i], key=lambda x: x[0])
 
with open('output.txt', 'w') as out:  
  for i in files_dict:    
    for j in files_dict[i]:    
      #print files names  
      out.write(f'{j[0]}.{j[1]}\n')

    #calc Summary
    cur_data = information_count(files_dict[i])  

    out.write('-'*10 + '\n')
    out.write(f"Summary: {cur_data[0]} {cur_data[1]}\n\n")
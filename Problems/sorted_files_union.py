'''
having a set of files that contain sorted entries, create a union of all the files in sorted order
'''

from collections import namedtuple

FileData = namedtuple('FileData', 'timestamp, index, file_index')

def sort_files(docs):
    heap = Heap(len(docs))
    for file_index, doc in enumerate(docs):
        heap.add(FileData(doc.get_timestamp(0), 0, file_index))
    
    while not heap.Empty():
        file_data = heap.next()
        store(file_data)
        if docs[file_data.file_index].row_count > file_data.index + 1:
            heap.add(FileData(doc.get_timestamp(file_data.index+1), file_data.index + 1, file_data.file_index)) 

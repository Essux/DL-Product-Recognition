import os
from glob import glob
import shutil
from math import floor

# delete existing folders to prevent repeated elements
print('Remember that train and test folders must be empty')

root_path = '.\\processed'

folders = [f for f in os.listdir(root_path) if f not in ['train', 'test']]

files = [glob(os.path.join(root_path, f)+'/*') for f in folders]

# Returns a 3-tuple with train, dev and test data respectively
def train_dev_test_split(arr, train_size, dev_size):
    train_id = floor(len(arr)*train_size)
    test_id = floor(len(arr)*dev_size) + train_id
    return arr[:train_id], arr[test_id:], arr[train_id:test_id]

for i, f in enumerate(files):
    data_partitioned = train_dev_test_split(f, train_size=0.6, dev_size=0.2)
    folder_names = ('train', 'dev', 'test')
    for partition, part_folder in zip(data_partitioned, folder_names):
        for part_file in partition:
            folder = os.path.basename(os.path.dirname(part_file))
            filename = os.path.basename(part_file)
            new_path = os.path.join('.\processed', part_folder, folder, filename)
            new_folder = os.path.dirname(new_path)
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
            shutil.copyfile(part_file, new_path)

    print(folder)
    for part_name, part_size in zip(folder_names, map(len, data_partitioned)):
        print('{}: {}'.format(part_name, part_size), end=' ')
    print()
import os

source_dir = 'Move'
target_dir = '02.labeled'

# Ensure the target directory exists
os.makedirs(target_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    if filename.endswith('.png'):
        base_name, ext = os.path.splitext(filename)
        target_path = os.path.join(target_dir, filename)
        
        # If file already exists, rename it with an incremented number
        count = 1
        while os.path.exists(target_path):
            target_path = os.path.join(target_dir, f'{base_name}.{count}.png')
            count += 1

        # Move the file
        source_path = os.path.join(source_dir, filename)
        os.rename(source_path, target_path)
        print(f'Moved {filename} to {target_path}')

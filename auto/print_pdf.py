import os

def merge_markdown_files(source_directory, merged_file_name):
    """
    Merge all markdown files from a specified directory into a single markdown file,
    excluding lines starting with ':::'.
    """
    index_file = os.path.join(source_directory, 'index.md')
    markdown_files = [index_file] if os.path.exists(index_file) else []

    for root, _, files in os.walk(source_directory):
        for file in files:
            if file.endswith('.md') and file != 'index.md':
                markdown_files.append(os.path.join(root, file))

    with open(merged_file_name, 'w', encoding='utf-8') as output_file:
        for file_path in markdown_files:
            with open(file_path, 'r', encoding='utf-8') as input_file:
                contents = input_file.readlines()
                filtered_contents = [line for line in contents if not line.strip().startswith(':::')]
                output_file.write(''.join(filtered_contents) + '\n\n')

    print(f"All Markdown files have been merged into {merged_file_name}")

def process_subdirectories(base_directory):
    """
    Process each subdirectory within a given base directory, merging all markdown files.
    """
    if not os.path.exists(base_directory):
        print("Directory does not exist")
        return

    for root, dirs, _ in os.walk(base_directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            merge_markdown_files(dir_path, f"{dir_name}.md")



directory = 'template'
process_subdirectories(directory)

import os
from tkinter import filedialog, Tk
from collections import Counter
from dataclasses import dataclass

@dataclass
class Stats:
    folder : str
    files_count : int
    total_size_mb : float
    most_common_types : list[tuple[str, int]]


def analyze_folder(path : str) -> tuple[str, int, int, float, Counter[str]]:
    folder : str = os.path.abspath(path)
    files_count : int = 0
    excluded_files_count : int = 0
    folder_size : float = 0
    extension_counter : Counter[str] = Counter()
    
    for curr_dir, _sub_dir, file_names in os.walk(path):
        for file_name in file_names:
            files_count += 1
            full_path : str = os.path.join(curr_dir, file_name)
            
            try:
                file_size : int = os.path.getsize(full_path)
                folder_size += file_size
            except OSError:
                excluded_files_count += 1
            
            extension : str = os.path.splitext(file_name)[1]
            extension_counter[extension.lower()] += 1
    
    return (folder, files_count, excluded_files_count, folder_size, extension_counter)

def folder_stats() -> Stats | None:
    root : Tk = Tk()
    root.withdraw()
    folder_path : str = filedialog.askdirectory(title="Select a folder to analyze")
    
    if not folder_path:
        print("No, folder selected.")
        return None
    
    folder_name, files_count, _excluded_files_count, total_size, extension_counter =  analyze_folder(folder_path)
    
    total_size_mb : float = round(total_size/(1024 * 1024), 2)
    most_common_extensions : list[tuple[str, int]] = extension_counter.most_common(5)
    
    return Stats(
        folder = folder_name,
        files_count = files_count,
        total_size_mb = total_size_mb,
        most_common_types = most_common_extensions
    )

def main() -> None:
    file_stats : Stats | None = folder_stats()

    if file_stats:
        print(f"Folder: {file_stats.folder}")
        print(f"Number of files: {file_stats.files_count}")
        print(f"Total Size (MB): {file_stats.total_size_mb} mb")
        print("Most common file types: ")
        for extension, count in file_stats.most_common_types:
            print(f"{extension} : {count} files")


if __name__ == "__main__":
    main()
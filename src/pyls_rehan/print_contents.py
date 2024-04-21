import argparse
import json
from datetime import datetime


def load_json(input_json_path):
    with open(input_json_path) as f:
        data = json.load(f)
        return data


def get_relative_path_contents(content_list, relative_path):
    relpath_list = relative_path.strip("/").split("/")
    if relpath_list[0] == ".":
        relpath_list.pop(0)
    if not relpath_list:
        return content_list
    
    for path in relpath_list:
        found = False
        for content in content_list:
            if content["name"] == path:
                if "contents" in content:
                    content_list = content["contents"]
                else:
                    content_list = [content]
                found = True
                break
        if not found:
            raise Exception(f"cannot access {relative_path}: No such file or directory")
    return content_list


def filter_contents(content_list, filter_by_type, show_all):
    output = []
    for content in content_list:
        if content["name"].startswith(".") and not show_all:
            continue
        if filter_by_type == "dir" and content["permissions"].startswith("d"):
            output.append(content)
        elif filter_by_type == "file" and content["permissions"].startswith("-"):
            output.append(content)
        elif filter_by_type is None:
            output.append(content)
    return output


def format_size(nbytes):
    suffixes = ['B', 'K', 'M', 'G', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    val = f"{nbytes:.1f}".rstrip('0').rstrip('.')
    return f"{val}{suffixes[i]}"


def print_longformat(dir_contents, human_readable):
    print(f"Total {len(dir_contents)}")
    for content in dir_contents:
        timestamp = datetime.utcfromtimestamp(content["time_modified"]).strftime('%b %d %H:%M')
        if human_readable:
            size = format_size(content["size"])
        else:
            size = content["size"]
        print(content["permissions"], "\t", size,"\t", timestamp, "\t", content["name"])


def print_simple(dir_contents):
    for content in dir_contents:
        print(content["name"], end =" "*4)
    print("")


def print_content(dir_contents, args):
    if args.relative_path:
        dir_contents = get_relative_path_contents(dir_contents, args.relative_path)
    
    dir_contents = filter_contents(dir_contents, args.filter, args.show_all)
    
    if args.timeordered:
        dir_contents = sorted(dir_contents, key=lambda d: d["time_modified"])
    else:
        dir_contents = sorted(dir_contents, key=lambda d: d["name"])
    
    if args.reverse_results:
        dir_contents = dir_contents[::-1]
    
    if args.long_format:
        print_longformat(dir_contents, args.human_readable)
    else:
        print_simple(dir_contents)


def main():
    parser = argparse.ArgumentParser(
                        prog="pyls",
                        description="Prints the contents of input json file to console in the style of unix 'ls' utility",
                        add_help=False)
    
    parser.add_argument("input_json_path", type=str, action="store",
                        help="Path of input JSON file")
    parser.add_argument("-A", "--all", dest='show_all', action="store_true", default=False,
                        help="Display all files and directories including hidden files starting with '.'")
    parser.add_argument("-l", "--longformat", dest='long_format', action="store_true", default=False,
                        help="Display the results vertically with detailed information in long format.")
    parser.add_argument("-r", "--reverse", dest="reverse_results", action="store_true", default=False,
                        help="Display the results in reverse order.")
    parser.add_argument("-t", dest="timeordered", action="store_true", default=False,
                        help="Display the results sorted by time_modified field (oldest first).")
    parser.add_argument("-h", dest="human_readable", action="store_true",
                        help="Display the file sizes in human readable format.")
    parser.add_argument("--filter", choices=("file", "dir"),
                        help="Filter the output based on given options: file or dir.")
    parser.add_argument("relative_path", nargs="?", type=str,
                        help="Display only the contents of the relative path within the input JSON.")
    parser.add_argument('--help', action="help",
                        help="Show this help message and exit")

    args = parser.parse_args()
    
    data = load_json(args.input_json_path)
    top_level_contents = []
    if "contents" in data:
        top_level_contents = data['contents']
    
    print_content(top_level_contents, args)


if __name__ == "__main__":
    main()

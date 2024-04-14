# This file contains a function that prompts the user for the name of a file and then outputs that file’s media type, in example for web browsers


def main():
    file_name = input("File name: ").lower().strip().rsplit(".", 1)[-1]

    match file_name:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


main()

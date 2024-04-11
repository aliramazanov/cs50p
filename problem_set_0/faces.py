# This script replaces emoticons in a text with emojis.

text_with_emoticons = input("Enter a text with emoticons: ")

text_with_emojis = text_with_emoticons.replace(":)", "🙂").replace(":(", "🙁")

print("Emoji version:", text_with_emojis)

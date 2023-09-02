#         Regex Query Tool - A tool that allows the user to enter a text string and then in a 
#         separate control enter a regex pattern. It will run the regular expression
#         against the source text and return any matches or flag errors in the regular expression.

import re

def regex_query_tool():
    try:
        text = input("Enter the text string: ")
        regex_pattern = input("Enter the regex pattern: ")

        match = re.search(regex_pattern, text)

        if match:
            print("Match found:", match.group(0))
        else:
            print("No match found.")

    except re.error as e:
        print("Regex Error:", e)

regex_query_tool()

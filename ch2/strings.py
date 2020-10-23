# coding: utf-8
"""strings in single and double quotes"""
tab_string = "\t"
len(tab_string)
len("t")
r"\t"
len(r"\t")
multi_line_string = """This is the first line.
and the second line...
and the third line before closing"""
multi_line_string
first_name = "Paul"
last_name = "Apivat"
full_name_f_string = f"{first_name} {last_name}"
full_name_f_string
"""string.format"""
full_name_string_format = "{0} {1}".format(first_name, last_name)
full_name_string_format
get_ipython().run_line_magic('save', 'strings 58-73')

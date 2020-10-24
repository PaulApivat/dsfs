# coding: utf-8
single_quoted_string = 'data science'
double_quoted_string = "data science"
tab_string = "\t"
tab_string
len(tab_string)
not_tab_string = r"\t"
len(not_tab_string)
n_string = "\n"
len(n_string)
raw_n_string = r"\n"
len(raw_n_string)
first_name = "Paul"
last_name = "Apivat"
string_addition = first_name + " " + last_name
string_addition
string_format = "{0} {1}".format(first_name, last_name)
string_format
f_string = f"{first_name} {last_name}"
f_string
get_ipython().run_line_magic('save', 'strings 2-3 5-22')

# Tools for using a Jupyter notebook as a lab notebook.
# These tools are specificly to aid instructors in setting
# up notebook templates with embedded instructions and tools
# for students.
# J. Gutow <jgutow@new.rr.com> January 30, 2020
# license GPL V3 or greater.

from IPython.display import HTML
from IPython.display import Javascript as JS

import os
# Instructor tools menu
from input_table import * #import the input table builder
from JPSLUtils import * # import the Utilities
# Locate JupyterPiDAQ package directory
mydir = os.path.dirname(__file__)  # absolute path to directory containing this file.

def instmenu_act():
    """
    Adds the instructor menu to the Jupyter menu bar
    :return:
    """
    tempJSfile = open(os.path.join(mydir, 'javascript', 'InstructorToolsmnu.js'))
    tempscript = '<script type="text/javascript">'
    tempscript += tempJSfile.read() + '</script>'
    tempJSfile.close()
    display(HTML(tempscript))
    OTJS('createInstructorToolsMenu()')
    warnstr = "This cell should only contain `import InstructorTools`"
    warnstr += " as it will be deleted when the tools"
    warnstr+= " are deactivated.\n\nWARNING: if you select the '!deactivate "
    warnstr+= " permanently!' option to make a student worksheet, the menu "
    warnstr+= "cannot be reactivated. Only use that option on a copy you "
    warnstr+= "intend to pass out to students."
    print(warnstr)
    pass

def instmenu_deact():
    """
    Removes the instructor menu from the Jupyter menu bar
    :return:
    """
#    tempJSfile = open(os.path.join(mydir, 'javascript', 'InstructorToolsmnu.js'))
#    tempscript = '<script type="text/javascript">'
#    tempscript += tempJSfile.read() + '</script>'
#    tempJSfile.close()
#    display(HTML(tempscript))
    display(JS('deleteInstructorToolsMenu()'))
    print("Delete this cell after the menu has been removed.")
    pass

instmenu_act()
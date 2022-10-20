#######################################################################
#                                                                     #
#  Simple python "judge" GUI for determinstic program output/inputs.  #
#                        By Chansol Yang                              #
#                                                                     #
#  This program is extensively commented;                             #
#  Either with class/method docstrings or with comments.              #
#  Enjoy.                                                             #
#                                                                     #
#######################################################################


## Below is a code that will attatch a custom error handler
## So the console won't close on its own when an uncaught exception happens.
## Makes for easy debugging.
if __name__ == "__main__":
    import sys
    import traceback


    ## This will make it so the console won't close on its own when an exception is raised.
    def show_exception_and_exit(exc_type, exc_value, tb):
        if not str(exc_value) == 'name \'exit\' is not defined':
            print("\n\n---ERROR---\n")
            traceback.print_exception(exc_type, exc_value, tb)
            input("\nPress any key to exit.")
        sys.exit(-1)


    sys.excepthook = show_exception_and_exit

## Imports
import subprocess  # For spawning a seperate python process
import io  # For interacting with that process
import sys  # To get the system encoding used
import webbrowser  # For a web URL link in the UI.

## Tkinter imports.
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog


class SliderPlus(Frame):
    '''Slider with a label and a value display.
    REQUIRES these keyword argumemts:
    plus_name, plus_max,plus_min,plus_divisions,plus_format
    '''

    def __init__(self, **kw):
        # Variables
        self._plus_name = kw["plus_name"]
        self._plus_max = kw["plus_max"]
        self._plus_min = kw["plus_min"]
        self._plus_divisions = kw["plus_divisions"]
        self._plus_format = kw["plus_format"]
        self._plus_value = self._plus_min

        # This is ugly.(duh)
        del kw["plus_name"]
        del kw["plus_max"]
        del kw["plus_min"]
        del kw["plus_divisions"]
        del kw["plus_format"]

        try:
            self._plus_display_override = kw['plus_display_override']
            del kw['plus_display_override']
        except KeyError:
            self._plus_display_override = None
            pass

        super().__init__(**kw)

        # Label
        self._plus_label = Label(self, text=self._plus_name)
        self._plus_label.grid(row=1, column=1)

        # Slider
        self._plus_slider = Scale(self, orient=HORIZONTAL, length=200, from_=0, to=self._plus_divisions, value=0,
                                  command=self._plus_slider_changed)
        self._plus_slider.grid(column=2, row=1, padx=5, sticky=(W, E))
        self.columnconfigure(2, weight=1)
        self._plus_slider.bind("<ButtonRelease>", self._slider_released)
        self.columnconfigure(2, weight=1)
        # Value
        self._plus_value_str_label = Label(self, text=str(self._plus_min))
        self._plus_value_str_label.grid(column=3, row=1, sticky=(W, E))

        self._plus_slider_changed(self._plus_min)

    def _slider_released(self, evt):
        pass

    def _plus_slider_changed(self, x):
        self._plus_value = int(round(float(x))) / self._plus_divisions * (
            self._plus_max - self._plus_min) + self._plus_min
        # print(type(self._plus_value))
        if self._plus_display_override == None:
            self._plus_value_str_label.configure(text=("{:." + str(self._plus_format) + "f}").format(self._plus_value))
        else:
            self._plus_value_str_label.configure(text=self._plus_display_override(self._plus_value))
    def plus_set(self,val):
        self._plus_slider.set(int(self._plus_divisions*(val-self._plus_min)/(self._plus_max-self._plus_min)))
    def plus_get_value(self):
        return self._plus_value


class CodePanel(LabelFrame):
    '''
    A Tk widget for displaying program outputs.
    It provides an easy way to display multiple lines of interactive code.
    This class inherits from a ttk.LabelFrame and can be used just like any other tk widget.
    '''

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._code_area = Text(self, font=("Consolas", 10), width=60, relief=RIDGE, borderwidth=2)
        self._code_area.grid(row=1, column=1, padx=5, pady=5, sticky=(N, S, E, W))
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self._code_area.tag_config("out", foreground="black")
        self._code_area.tag_config("in", foreground="blue")
        self._code_area.tag_config("err", foreground="red")
        self._code_area.tag_config("wrong", background="#FBB")
        self._code_area.configure(state='disabled')

    def new_in(self, s):
        '''
        Append a given input string (usually stdin).
        It will show up as a blue text.
        '''

        self._code_area.configure(state='normal')
        self._code_area.insert("end", s, ("in",))
        self._code_area.configure(state='disabled')

    def new_out(self, s, highlight=None):
        '''
        Append a given output string (usually stdout).
        It will show up as a plain black text.

        An optional list of character indices to highlight can be provided;
        For example, passing (0,1) will highlight the first and second characters red.
        Used for marking wrong answers.
        '''

        if highlight == None:
            to_highlight = []
        else:
            to_highlight = list(highlight)

        self._code_area.configure(state='normal')
        for idx in range(len(s)):
            tag = ("out",)
            if idx in to_highlight:
                tag = ("wrong",)
            self._code_area.insert("end", s[idx], tag)
        self._code_area.configure(state='disabled')

    def new_err(self, s):
        '''
        Append a given error string (usually stderr).
        It will show up as a red text.
        '''

        self._code_area.configure(state='normal')
        self._code_area.insert("end", s, ("err",))
        self._code_area.configure(state='disabled')

    def clear(self):
        '''
        Clear all text.
        '''
        self._code_area.configure(state='normal')
        self._code_area.delete('1.0', END)
        self._code_area.configure(state='disabled')


class AbstractScript():
    '''
    Base class for script interfaces.
    Not really useful right now, but may become useful if we add support for languages other than Python.
    '''

    def __init__(self):
        pass

    def read(self):
        '''
        Read a program's output from stdout.
        '''
        pass

    def write(self, s):
        '''
        Write a given string to the program's stdin.
        '''
        pass


class PythonScriptError(Exception):
    '''
    Exception for python interface related error.
    '''
    pass


class PythonScript(AbstractScript):
    '''
    An interface for communicating with an external python script.
    
    Provides an easy-to-use interface with an external python script, hiding away all the complications
    that arise when using pipes to communicate between processes.
    '''

    def __init__(self, path):
        super().__init__()
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        try:
            self.p = subprocess.Popen(['py', path],
                                      stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT,
                                      bufsize=1, startupinfo=startupinfo)
        except:
            raise PythonScriptError("Error in starting python script. Did you select a .py file?")

    def read(self):
        '''
        Read from the stdout of the python script.
        
        Please note that read() may not return results when you call it immediately after initializing the object
        or write()-ing, even if the script does in the command line.
        This is due to buffer taking time to flush (I think)
        You should wait (A time.sleep() would work) about 0.5 seconds before attempting to read.
   
        May raise a PythonScriptError;
        This usually indicates that the program has terminated.
        '''
        try:
            self.p.stdout.flush()
            self.p.stdout.seek(0, io.SEEK_END)
            end = self.p.stdout.tell()
            self.p.stdout.seek(0, io.SEEK_SET)
            res = self.p.stdout.read(end).decode(sys.stdout.encoding).replace("\r\n", "\n")
            # print(repr(res))
            return res
        except OSError:
            raise PythonScriptError("OSError")

    def write(self, s):
        '''
        Write a given string to the stdin of the python script.
        
        May raise a PythonScriptError;
        This usually indicates that the program has terminated.
        '''
        try:
            self.p.stdin.write(s.encode(sys.stdin.encoding))
            self.p.stdin.flush()

        except OSError:
            raise PythonScriptError("OSError")


class Interaction():
    '''
    A class for representing a program interaction.
    An interaction is a series of inputs and outputs from and to the program.
    
    An instance of Interaction is state-based.
    That is, once an Interaction is built, you can step through it one by one, getting the input/outputs.
    
    Example:
        Say there is a program that greets the user, gets a string from the user, and tells how long the input was.
        A representation of the above program in an Interaction object might look like this:
        
        [0] OUTPUT : "Hello user! Enter string: "
        [1] INPUT  : "asdf\\n"
        [2] OUTPUT : "The string is 4 characters long.\\n"
        
        You can build the above object like so:
        inter=Interaction()
        inter.add_in("Hello user! Enter string: ")
        inter.add_out("asdf\\n")
        inter.add_in("The string is 4 characters long.\\n")
        
        And traverse through it like so:
        inter.rewind()
        inter.next() # You have to call next() to get the first result.
        inter.get_state() >> returns "OUT"
        inter.get_string() >> returns "Hello user! Enter string: "
        inter.next()
        
        and so on.
    '''

    def __init__(self):
        self.data = list()
        self.position = -1

    def add_in(self, s):
        '''
        Add a given input to the interaction.
        '''
        self.data.append(("IN", str(s) + "\n"))

    def add_in_raw(self, s):
        '''
        Add a given input to the interaction. A string conversion is not done, and a newline is not added.
        '''
        self.data.append(("IN", s))

    def add_out(self, s):
        '''
        Add a given output to the interaction.
        '''
        self.data.append(("OUT", s))

    def get_position(self):
        '''
        Get the current position of the interaction.
        Zero-indexed.
        '''
        return self.position

    def get_percentage(self):
        return (self.position + 1) / len(self.data) * 100

    def rewind(self):
        '''
        Reset the interaction to the -1th position.
        '''
        self.position = -1

    def next(self):
        '''
        Go to next state.
        '''
        self.position += 1
        return self.data[self.position]

    def get_state(self):
        '''
        Get the state of the current step; "IN", "OUT" or "NOT STARTED"
        '''
        if self.position == -1:
            return "NOT STARTED"
        return self.data[self.position][0]

    def get_string(self):
        '''
        Get the string of the current step.
        '''
        if self.position == -1:
            return "NOT STARTED"
        return self.data[self.position][1]

    def over(self):
        '''
        Check if the interaction is over;
        That is, check if calling next() once more will be invalid.
        '''
        return self.position + 1 >= len(self.data)


class DummyInteraction(Interaction):
    '''
    Subclass of Interaction;
    Represents an interaction WHERE THE OUTPUTS ARE UNDEFINED.
    That is, outputs are all None.
    Used for generating databases.
    '''

    def __init__(self, *args):
        super().__init__()
        self._make_template(*args)

    def set(self, s):
        '''
        Set the current step's data.
        '''
        self.data[self.position] = (self.data[self.position][0], s)

    def _make_template(self, *args):
        for i in args:
            self.add_out(None)
            self.add_in(i)
        self.add_out(None)


## Some global variables.
py_file = None
python = None


def get_goal_interaction():
    '''
    Get the Interaction object corresponding to the selected Question and Test Case.
    '''
    return database[root_case_question_VAR.get()][root_case_selection.current()]


def validation_start():
    '''
    Start validating code.
    '''

    global had_error, keep_looping, python, root_codes_lpanel, root_codes_rpanel, goal_interaction, root, database, root_file_question_VAR, root_case_selection_VAR

    update_status("Initializing Python script...", progress=0)

    goal_interaction = get_goal_interaction()
    goal_interaction.rewind()

    root_codes_lpanel.clear()
    root_codes_rpanel.clear()

    ## Try to start a Python process; Display error if failed.
    try:
        python = PythonScript(py_file)
    except PythonScriptError:
        root_codes_lpanel.new_err("Script load failed.\nDid you select a .py file?")
        return

    ## Set some loop variables
    keep_looping = True
    had_error = False

    ## tkinter's waiting function; We use this to loop.
    root.after(get_initialdelay(), tk_loop_read)


def validation_stop():
    '''
    Abort loop.
    '''
    global keep_looping
    keep_looping = False


## Global loop variables.
goal_interaction = None
keep_looping = False
had_error = False


def tk_loop_read():
    '''
    A function to be called in the reading phase of the program.
    '''
    global python, had_error, goal_interaction, root, root_codes_lpanel, root_codes_rpanel, keep_looping

    ## Loop break
    if not keep_looping:
        update_status("STOPPED BY USER")
        return

    ## Advance and notify
    goal_interaction.next()
    update_status("TEST IN PROGRESS (out)", progress=goal_interaction.get_percentage())

    ## Try to read from the python script
    ## If there the script was terminated, display error.
    try:
        py_out = python.read()
    except PythonScriptError:
        root_codes_lpanel.new_err("** Program terminated **")
        update_status("Test completed and ERRORS FOUND.", progress=100, color="red")
        return

    ## Get the "Goal" output.
    goal_out = goal_interaction.get_string()

    if get_verbose_output():
        goal_out=verbosify_string(goal_out)
        py_out=verbosify_string(py_out)

    if goal_out == None:
        ## This is test case generating run
        goal_interaction.set(py_out)
        root_codes_rpanel.new_out("????")
        root_codes_lpanel.new_out(py_out)
    else:
        ## Below code splits and compares outputs line-by-line.
        ## It was briefly used, only in 0.2.4
        ## However, I've realized that some rare errors may get masked in the process, Espicially stray newlines.
        ## So, I've reverted the changes in 0.2.5
        '''
        ## A normal run
        root_codes_rpanel.new_out(goal_out)

        ## For each line...
        py_split = py_out.split("\n")
        goal_split = goal_out.split("\n")

        ## Match length
        while len(py_split) < len(goal_split):
            py_split.append("")
        while len(py_split) > len(goal_split):
            goal_split.append("")

        for lineidx in range(len(py_split)):
            py_line = py_split[lineidx]
            goal_line = goal_split[lineidx]


            ## Match the string lengths by appending blanks after.
            while len(py_line) < len(goal_line):
                if get_space_strict():
                    py_line = py_line + "â–¯"
                else:
                    py_line=py_line+" "

            diff = []
            for charidx in range(len(py_line)):
                try:
                    if (py_line[charidx] != goal_line[charidx]):
                        diff.append(charidx)

                except IndexError:
                    diff.append(charidx)

            ## Display those differences
            root_codes_lpanel.new_out(py_line, highlight=diff)
            if lineidx != len(py_split) - 1:
                root_codes_lpanel.new_out("\n")

            if len(diff) > 0:
                had_error = True
        '''

        ## Below is the code from 0.2.3 that was put back in.

        ## A normal run
        root_codes_rpanel.new_out(goal_out)

        ## Match the string lengths by appending â–¯s after.
        while len(py_out) < len(goal_out):
            py_out = py_out + "â–¯"

        if py_out != goal_out:
            ## Mismatch

            ## Get differences
            diff = []
            for idx in range(len(py_out)):
                try:
                    if py_out[idx] != goal_out[idx]:
                        diff.append(idx)
                except IndexError:
                    diff.append(idx)

            ## Display those differences
            root_codes_lpanel.new_out(py_out, highlight=diff)

            had_error = True
        else:
            ## Matched
            root_codes_lpanel.new_out(py_out)
    ## Go the the write phase after 1 second
    root.after(get_delay(), tk_loop_write)


def tk_loop_write():
    '''
    A function to be called in the writing phase of the program.
    '''
    global python, goal_interaction, root, root_codes_lpanel, root_codes_rpanel, keep_looping

    ## Loop break conditions
    if not keep_looping:
        update_status("STOPPED BY USER")
        return

    if goal_interaction.over():
        tk_loop_terminated()
        return

    ## advance state
    goal_interaction.next()

    update_status("TEST IN PROGRESS (in)", progress=goal_interaction.get_percentage())

    ## read from the interaction what to write.
    to_write = goal_interaction.get_string()

    ## Try to write to the python script
    ## If there the script was terminated, display error.
    try:
        python.write(to_write)
    except PythonScriptError:
        root_codes_lpanel.new_err("** Program terminated **")
        update_status("Test completed and ERRORS FOUND.", progress=100, color="red")
        return

    if get_verbose_output():
        to_write=verbosify_string(to_write)
    ## Display
    root_codes_lpanel.new_in(to_write)
    root_codes_rpanel.new_in(to_write)

    ## Go the the read phase after 1 second
    root.after(get_delay(), tk_loop_read)


def tk_loop_terminated():
    '''
    A function to be called when the validation completes correctly.
    '''
    global root_case_selection, keep_looping

    ## Just abort if the user pressed stop/
    if not keep_looping:
        update_status("STOPPED BY USER")
        return

    ## Display accordingly.
    if had_error:
        update_status("Test completed and ERRORS FOUND.", progress=100, color="red")
    else:
        update_status("Test passed with no errors.", progress=100, color="blue")

    ## If auto-next is on, load the next case and restart validation.
    if root_case_auto_VAR.get() == 1 and not had_error:
        update_status("Test passed. Continuing to next case...", indeterminate=True, color="blue")

        ## Check if this is the last one. In that case, stop.
        size = len(root_case_selection["values"])
        current_idx = root_case_selection.current()
        next_idx = current_idx + 1
        if next_idx >= size:
            update_status("Test passed with no errors.", progress=100, color="blue")
            return

        root_case_selection.current(next_idx)

        ## Go to validation start phase after 1 second.
        root.after(1000, validation_start)


def get_file():
    '''
    callback for "Open File"
    '''
    f = filedialog.askopenfilename(title="Image Folder", initialdir="")
    if f == None or f == '':
        return
    global root_file_selected_VAR, py_file
    root_file_selected_VAR.set(f)
    py_file = f


def reload_testcases():
    '''
    Reload testcases and refresh UI.
    Called when a new problem is selected.
    '''
    global root_case_selection, root_case_question_VAR
    cases = database[root_case_question_VAR.get()]
    root_case_selection["values"] = ["Test case " + str(i) for i in list(range(1, len(cases) + 1))]
    root_case_selection.current(0)


def print_interaction(interaction):
    '''
    Prints a code that evaluates to an interaction.
    Used for embedding database into python source code.
    '''
    print("temp_interaction=Interaction()")
    for i in interaction.data:
        if i[0] == "IN":
            print("temp_interaction.add_in_raw({})".format(repr(i[1])))
        elif i[0] == "OUT":
            print("temp_interaction.add_out({})".format(repr(i[1])))
        else:
            raise


def print_testcases(interactions):
    '''
    Prints code that evaluates to a list of interactins.
    '''
    print("temp_interactions=[]")
    for i in interactions:
        print_interaction(i)
        print("temp_interactions.append(temp_interaction)")


def print_database():
    '''
    prints code that evaluates to a dictionary of interactions.
    This is embedded into the source code.
    '''
    global database
    print("#### BEGIN AUTO-GENERATED CODE ####\n")
    print("database={}")
    for key in database:
        print_testcases(database[key])
        print("database[{}]=temp_interactions".format(repr(key)))
    print("\n##### END AUTO-GENERATED CODE #####")

def verbosify_string(s):
    #return repr(s)[1:-1].replace(" ","â£")
    return s.replace(" ", "â†’").replace("\n","â†“\n")

## DATABASE GENERATING INPUTS L4
## This is a "Dummy" database used for building the actual test cases.
## This "Dummy" database is composed of DummyInteractions, which only has an input, and no outputs.
## When you run the program with this database, the program will add the program's outputs
## to the DummyInteraction object. This turns it into a fully built test case.
## Then, the database can be printed with print_database()
## Which prints out the built test case database
database = {"Problem 1": [DummyInteraction(1, 2, 3, 4, 0),
                          DummyInteraction(0),
                          DummyInteraction(12, 45, 789, 0),
                          DummyInteraction(100, 10, 1000, 0)],
            "Problem 2": [DummyInteraction()],
            "Problem 3": [DummyInteraction("F", 0),
                          DummyInteraction("N", "f", "F", 100),
                          DummyInteraction("c", "C", -1000, 100),
                          DummyInteraction("C", -274, -273),
                          DummyInteraction("F", -460, -459)],
            "Problem 4": [DummyInteraction(12345),
                          DummyInteraction(5),
                          DummyInteraction(10000000000),
                          DummyInteraction(99999999999)],
            "Problem 5": [DummyInteraction(512),
                          DummyInteraction(1024),
                          DummyInteraction(2048),
                          DummyInteraction(4096),
                          DummyInteraction(6400),
                          DummyInteraction(8192)],
            "Problem 6": [DummyInteraction(16),
                          DummyInteraction(36),
                          DummyInteraction(1024),
                          DummyInteraction(101),
                          DummyInteraction(1)]
            }

#### BEGIN AUTO-GENERATED CODE ####

database={}
temp_interactions=[]
temp_interaction=Interaction()
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('1\n')
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('2\n')
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('3\n')
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('4\n')
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('0\n')
temp_interaction.add_out('Sum: 10\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('0\n')
temp_interaction.add_out('Sum: 0\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('12\n')
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('45\n')
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('789\n')
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('0\n')
temp_interaction.add_out('Sum: 57\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('100\n')
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('10\n')
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('1000\n')
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('0\n')
temp_interaction.add_out('Sum: 110\n')
temp_interactions.append(temp_interaction)
database['Problem 1']=temp_interactions
temp_interactions=[]
temp_interaction=Interaction()
temp_interaction.add_out('  1  2  3  4  5  6  7  8  9 10\n 11 12 13 14 15 16 17 18 19 20\n 21 22 23 24 25 26 27 28 29 30\n 31 32 33 34 35 36 37 38 39 40\n 41 42 43 44 45 46 47 48 49 50\n 51 52 53 54 55 56 57 58 59 60\n 61 62 63 64 65 66 67 68 69 70\n 71 72 73 74 75 76 77 78 79 80\n 81 82 83 84 85 86 87 88 89 90\n 91 92 93 94 95 96 97 98 99100\n')
temp_interactions.append(temp_interaction)
database['Problem 2']=temp_interactions
temp_interactions=[]
temp_interaction=Interaction()
temp_interaction.add_out('This program will convert temperatures (Fahrenheit/Celsius)\nEnter (F) to convert Fahrenheit to Celsius\nEnter (C) to convert Celsius to Fahrenheit\nEnter selection: ')
temp_interaction.add_in_raw('F\n')
temp_interaction.add_out('Enter temperature to convert: ')
temp_interaction.add_in_raw('0\n')
temp_interaction.add_out('0 degrees Fahrenheit equals -17.8 degrees Celsius\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('This program will convert temperatures (Fahrenheit/Celsius)\nEnter (F) to convert Fahrenheit to Celsius\nEnter (C) to convert Celsius to Fahrenheit\nEnter selection: ')
temp_interaction.add_in_raw('N\n')
temp_interaction.add_out("Please enter 'F' or 'C': ")
temp_interaction.add_in_raw('f\n')
temp_interaction.add_out("Please enter 'F' or 'C': ")
temp_interaction.add_in_raw('F\n')
temp_interaction.add_out('Enter temperature to convert: ')
temp_interaction.add_in_raw('100\n')
temp_interaction.add_out('100 degrees Fahrenheit equals 37.8 degrees Celsius\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('This program will convert temperatures (Fahrenheit/Celsius)\nEnter (F) to convert Fahrenheit to Celsius\nEnter (C) to convert Celsius to Fahrenheit\nEnter selection: ')
temp_interaction.add_in_raw('c\n')
temp_interaction.add_out("Please enter 'F' or 'C': ")
temp_interaction.add_in_raw('C\n')
temp_interaction.add_out('Enter temperature to convert: ')
temp_interaction.add_in_raw('-1000\n')
temp_interaction.add_out('Enter temperature to convert: ')
temp_interaction.add_in_raw('100\n')
temp_interaction.add_out('100 degrees Celsius equals 212.0 degrees Fahrenheit\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('This program will convert temperatures (Fahrenheit/Celsius)\nEnter (F) to convert Fahrenheit to Celsius\nEnter (C) to convert Celsius to Fahrenheit\nEnter selection: ')
temp_interaction.add_in_raw('C\n')
temp_interaction.add_out('Enter temperature to convert: ')
temp_interaction.add_in_raw('-274\n')
temp_interaction.add_out('Enter temperature to convert: ')
temp_interaction.add_in_raw('-273\n')
temp_interaction.add_out('-273 degrees Celsius equals -459.4 degrees Fahrenheit\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('This program will convert temperatures (Fahrenheit/Celsius)\nEnter (F) to convert Fahrenheit to Celsius\nEnter (C) to convert Celsius to Fahrenheit\nEnter selection: ')
temp_interaction.add_in_raw('F\n')
temp_interaction.add_out('Enter temperature to convert: ')
temp_interaction.add_in_raw('-460\n')
temp_interaction.add_out('Enter temperature to convert: ')
temp_interaction.add_in_raw('-459\n')
temp_interaction.add_out('-459 degrees Fahrenheit equals -272.8 degrees Celsius\n')
temp_interactions.append(temp_interaction)
database['Problem 3']=temp_interactions
temp_interactions=[]
temp_interaction=Interaction()
temp_interaction.add_out('Enter a number: ')
temp_interaction.add_in_raw('12345\n')
temp_interaction.add_out('The number 12345 contains 5 digits\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter a number: ')
temp_interaction.add_in_raw('5\n')
temp_interaction.add_out('The number 5 contains 1 digit\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter a number: ')
temp_interaction.add_in_raw('10000000000\n')
temp_interaction.add_out('The number 10000000000 contains 11 digits\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter a number: ')
temp_interaction.add_in_raw('99999999999\n')
temp_interaction.add_out('The number 99999999999 contains 11 digits\n')
temp_interactions.append(temp_interaction)
database['Problem 4']=temp_interactions
temp_interactions=[]
temp_interaction=Interaction()
temp_interaction.add_out('Enter the taxable income in USD: ')
temp_interaction.add_in_raw('512\n')
temp_interaction.add_out('Tax due: 5.12 USD\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter the taxable income in USD: ')
temp_interaction.add_in_raw('1024\n')
temp_interaction.add_out('Tax due: 12.98 USD\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter the taxable income in USD: ')
temp_interaction.add_in_raw('2048\n')
temp_interaction.add_out('Tax due: 33.46 USD\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter the taxable income in USD: ')
temp_interaction.add_in_raw('4096\n')
temp_interaction.add_out('Tax due: 96.34 USD\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter the taxable income in USD: ')
temp_interaction.add_in_raw('6400\n')
temp_interaction.add_out('Tax due: 200.00 USD\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter the taxable income in USD: ')
temp_interaction.add_in_raw('8192\n')
temp_interaction.add_out('Tax due: 301.52 USD\n')
temp_interactions.append(temp_interaction)
database['Problem 5']=temp_interactions
temp_interactions=[]
temp_interaction=Interaction()
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('16\n')
temp_interaction.add_out('root: 4, pwr: 2\nroot: 2, pwr: 4\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('36\n')
temp_interaction.add_out('root: 6, pwr: 2\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('1024\n')
temp_interaction.add_out('root: 32, pwr: 2\nroot: 4, pwr: 5\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('101\n')
temp_interaction.add_out('No matching pair of integers found\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Your number: ')
temp_interaction.add_in_raw('1\n')
temp_interaction.add_out('root: 1, pwr: 2\nroot: 1, pwr: 3\nroot: 1, pwr: 4\nroot: 1, pwr: 5\n')
temp_interactions.append(temp_interaction)
database['Problem 6']=temp_interactions

##### END AUTO-GENERATED CODE #####



## From here on it's all UI Setup.
## Not too hard to understand.
root = Tk()
root.title("CP Checker")

root_title = Frame(root)
root_title.grid(column=1, row=1, padx=10, pady=5, sticky=(W, E, N, S))
root.columnconfigure(1, weight=1)

root_title_website = Label(root_title, text="ì›¹ì‚¬ì´íŠ¸ - ì‚¬ìš©ë²• / ì—…ë°ì´íŠ¸ / ë‹¤ìŒ ëž© ë‹¤ìš´ë¡œë“œ", font=("ë§‘ì€ ê³ ë”•", 8), foreground="blue",
                           cursor="hand2")
root_title_website.bind("<Button-1>",
                        lambda e: webbrowser.open_new(r"http://chanspi.ddns.net/Yonsei/CPChecker"))
root_title_website.grid(column=1, row=1, sticky=(W, E, N, S))

txt = '''ì»´í“¨í„°í”„ë¡œê·¸ëž˜ë° ê³¼ì œ ê°€ì±„ì ê¸° v0.2.5 [Database: Lab 4 v3]
Â©ì»´í“¨í„°ê³¼í•™ê³¼ ì–‘ì°¬ì†” - ë¬´ë‹¨ ë°°í¬ í—ˆìš©

í”„ë¡œê·¸ëž¨ì˜ ì¶œë ¥ì´ ì œë•Œ ë‚˜íƒ€ë‚˜ì§€ ê°™ìœ¼ë©´ ì•„ëž˜ Settingsì˜ Read/Write Delay ê°’ì„ ì˜¬ë ¤ ë³´ì„¸ìš”.
í”„ë¡œê·¸ëž¨ì˜ ì´ˆê¸° ì¶œë ¥ì´ ì œëŒ€ë¡œ ë‚˜ì˜¤ì§€ ì•Šìœ¼ë©´ ì•„ëž˜ Settingsì˜ Initial Delay ê°’ì„ ì˜¬ë ¤ ë³´ì„¸ìš”.
â–¯ëŠ” ë¬¸ìžê°€ ìžˆì–´ì•¼ í•  ê³³ì— ë¬¸ìžê°€ ì—†ìŒì„ ëœ»í•©ë‹ˆë‹¤.
ê³µë°± ë¬¸ìžë“¤ì„ ë” ìž˜ ë³´ê³  ì‹¶ë‹¤ë©´ Verbose Stringsë¥¼ ì²´í¬í•˜ì„¸ìš”.

ì°¸ê³ ë§Œ í•˜ì„¸ìš”... í‹€ë ¤ë„ ì € ì±…ìž„ ëª»ì ¸ìš”...
í”„ë¡œê·¸ëž¨ ìžì²´ì— ì˜¤ë¥˜ ìžˆìœ¼ë©´ í†¡ ì£¼ì„¸ìš”.'''
root_title_text = Label(root_title, text=txt, font=("ë§‘ì€ ê³ ë”•", 8))
root_title_text.grid(column=1, row=2, sticky=(W, E, N, S))

root_file = LabelFrame(root, text="Python file")
root_file.grid(column=1, row=2, padx=10, pady=5, sticky=(W, E, N, S))

root_file_selectbutton = Button(root_file, text="Open", command=get_file)
root_file_selectbutton.grid(column=1, row=1, padx=5, pady=5, sticky=(W, E))

root_file_selected_VAR = StringVar()
root_file_selected = Label(root_file, textvariable=root_file_selected_VAR)
root_file_selected.grid(column=2, row=1, padx=5, pady=5, sticky=(W, E))
root_file.columnconfigure(2, weight=1)

root_case = LabelFrame(root, text="Case select")
root_case.grid(column=1, row=3, padx=10, pady=5, sticky=(W, E, N, S))

root_case_question_VAR = StringVar()
root_case_question = Combobox(root_case, textvariable=root_case_question_VAR)
root_case_question.bind("<<ComboboxSelected>>", lambda evt: reload_testcases())
db_keys = list(database.keys())
db_keys.sort()
root_case_question["values"] = db_keys
root_case_question.current(0)
root_case_question.grid(column=1, row=1, padx=5, pady=5, sticky=(W, E))

root_case_selection_VAR = StringVar()
root_case_selection = Combobox(root_case, textvariable=root_case_selection_VAR)
root_case_selection.grid(column=2, row=1, padx=5, pady=5, sticky=(W, E))

root_case_auto_VAR = IntVar()
root_case_auto_VAR.set(1)
root_case_auto = Checkbutton(root_case, text="Go to next automatically", variable=root_case_auto_VAR)
root_case_auto.grid(column=3, row=1, padx=5, pady=5, sticky=(W, E))

root_case_start = Button(root_case, text="Start", command=validation_start)
root_case_start.grid(column=4, row=1, padx=5, pady=5, sticky=(W, E))

root_case_stop = Button(root_case, text="Stop", command=validation_stop)
root_case_stop.grid(column=5, row=1, padx=5, pady=5, sticky=(W, E))

root_case_startall = Button(root_case, text="Debug", command=print_database)
#root_case_startall.grid(column=6, row=1, padx=5, pady=5, sticky=(W, E))

root_status = LabelFrame(root, text="Status")
root_status.grid(column=1, row=4, padx=10, pady=5, sticky=(W, E, N, S))


def update_status(s, progress=None, indeterminate=False, color="black"):
    '''
    Function for updating progress bar and status text.
    '''
    global root_status_label, root_status_bar_VAR, root_status_bar
    root_status_label.configure(text=s, foreground=color)

    if indeterminate:
        root_status_bar_VAR.set(0)
        root_status_bar.configure(mode="indeterminate", maximum=20)
        root_status_bar.start()
    else:
        root_status_bar.stop()
        root_status_bar.configure(mode="determinate", maximum=100)

    if progress == None:
        pass
    else:
        root_status_bar_VAR.set(progress)


root_status_bar_VAR = Variable()
root_status_bar = Progressbar(root_status, orient=HORIZONTAL, length=200,
                              mode='determinate', variable=root_status_bar_VAR)
root_status_bar.grid(column=1, row=1, padx=5, pady=5, sticky=(W, E))

root_status_label = Label(root_status, text="Standby")  # , justify=CENTER, anchor=CENTER, font=(None, 24))
root_status_label.grid(column=2, row=1, padx=5, pady=5, sticky=(W, E, N, S))
root_status.columnconfigure(2, weight=1)
root_status.rowconfigure(1, weight=1)

root_settings = LabelFrame(root, text="Settings")
root_settings.grid(column=1, row=5, padx=10, pady=5, sticky=(W, E, N, S))


def get_delay():
    return int(root_settings_delay.plus_get_value() * 1000)


root_settings_delay = SliderPlus(master=root_settings, plus_name="Read/Write delay", plus_max=5.0, plus_min=0.1,
                                 plus_divisions=1000, plus_format=1)
root_settings_delay.plus_set(0.5)
root_settings_delay.grid(column=1, row=1, padx=5, pady=5)
root_settings.columnconfigure(1, weight=1)


def get_initialdelay():
    return int(root_settings_initialdelay.plus_get_value() * 1000)


root_settings_initialdelay = SliderPlus(master=root_settings, plus_name="Initialize delay", plus_max=5.0, plus_min=0.1,
                                        plus_divisions=1000, plus_format=1)
root_settings_initialdelay.plus_set(1)
root_settings_initialdelay.grid(column=2, row=1, padx=5, pady=5)
root_settings.columnconfigure(2, weight=1)


def get_verbose_output():
    return root_settings_verboseoutput_VAR.get() == 1


root_settings_verboseoutput_VAR = IntVar()
root_settings_verboseoutput_VAR.set(0)
root_settings_verboseoutput = Checkbutton(root_settings, text="Verbose Strings", variable=root_settings_verboseoutput_VAR)
root_settings_verboseoutput.grid(column=3, row=1, padx=5, pady=5, sticky=(W, E))


root_codes = Frame(root)
root_codes.grid(column=1, row=6, padx=5, pady=5, sticky=(W, E, N, S))
root.rowconfigure(6, weight=1)

root_codes_lpanel = CodePanel(root_codes, text="Your Code")
root_codes_lpanel.grid(column=1, row=1, padx=5, pady=5, sticky=(W, E, N, S))
root_codes.columnconfigure(1, weight=1)
root_codes.rowconfigure(1, weight=1)

root_codes_rpanel = CodePanel(root_codes, text="Answer")
root_codes_rpanel.grid(column=3, row=1, padx=5, pady=5, sticky=(W, E, N, S))
root_codes.columnconfigure(3, weight=1)

## Gotta do this for the first time.
reload_testcases()

## Start Tk.
root.mainloop()

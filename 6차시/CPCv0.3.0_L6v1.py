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
import traceback

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




def stdin_encoding():
    global root_settings_cp949_VAR
    if root_settings_cp949_VAR.get() == 1:
        return "cp949"
    return sys.stdin.encoding
def stdout_encoding():
    global root_settings_cp949_VAR
    if root_settings_cp949_VAR.get()==1:
        return "cp949"
    return sys.stdout.encoding


class PythonScriptError(Exception):
    '''
    Exception for python interface related error.
    '''
    pass

class PipeEncodingError(Exception):
    '''
    Exception for encoding error in the pipe communication.
    '''
    pass


class ImportedPythonScript(AbstractScript):
    def __init__(self,path):
        super().__init__()
        self.path=path
        self.out=None
        self.namespace=dict()
        with open(path,"r") as f:
            code=f.read()
            exec(code,self.namespace)

    def read(self):
        if self.out!=None:
            tmp=self.out
            self.out=None
            return repr(tmp)
        return ""
    def write(self,s):
        self.out= eval(s,self.namespace)


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
            try:
                res = self.p.stdout.read(end).decode(stdout_encoding()).replace("\r\n", "\n")
            except UnicodeDecodeError:
                raise PipeEncodingError("Decode Failed")

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
            self.p.stdin.write(s.encode(stdin_encoding()))
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

    def __init__(self,interaction_type="CONSOLE"):
        self.data = list()
        self.position = -1
        self.interaction_type=interaction_type

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
    def get_type(self):
        return self.interaction_type

class DummyInteraction(Interaction):
    '''
    Subclass of Interaction;
    Represents an interaction WHERE THE OUTPUTS ARE UNDEFINED.
    That is, outputs are all None.
    Used for generating databases.
    '''

    def __init__(self, *args, interaction_type="CONSOLE"):
        super().__init__(interaction_type)
        if args:
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
        if goal_interaction.get_type()=="CONSOLE":
            python = PythonScript(py_file)
        elif goal_interaction.get_type()=="IMPORT":
            try:
                python=ImportedPythonScript(py_file)
            except:
                root_codes_lpanel.new_err(traceback.format_exc())
                update_status("Unable to execute", progress=0, color="red")
                return
        else:
            raise
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
    except PipeEncodingError:
        root_codes_lpanel.new_err("** Encoding Error **\nTry checking the \"Force CP949 Encoding\" Checkbox.")
        update_status("INTERNAL ERROR", progress=0, color="red")
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
                    py_line = py_line + "▯"
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

        ## Match the string lengths by appending ▯s after.
        while len(py_out) < len(goal_out):
            py_out = py_out + "▯"

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
    except:
        root_codes_lpanel.new_err(traceback.format_exc())
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
    if interaction.get_type()=="CONSOLE":
        print("temp_interaction=Interaction()")
    elif interaction.get_type()=="IMPORT":
        print("temp_interaction=Interaction(interaction_type=\"IMPORT\")")
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
    #return repr(s)[1:-1].replace(" ","␣")
    return s.replace(" ", "→").replace("\n","↓\n")

## DATABASE GENERATING INPUTS L6
## This is a "Dummy" database used for building the actual test cases.
## This "Dummy" database is composed of DummyInteractions, which only has an input, and no outputs.
## When you run the program with this database, the program will add the program's outputs
## to the DummyInteraction object. This turns it into a fully built test case.
## Then, the database can be printed with print_database()
## Which prints out the built test case database
database = {"Problem 1": [DummyInteraction("1abc%@"),
                          DummyInteraction("a1234567890#@%"),
                          DummyInteraction("qwertyuiopasdfghjklzxcvbnm#0"),
                          DummyInteraction("QWERTYUIOPASDFGHJKLZXCVBNM#0"),
                          DummyInteraction("Hello@5!"),
                          DummyInteraction("PassWoRd123"),
                          DummyInteraction("a bc"),
                          DummyInteraction("4986#"),
                          DummyInteraction("abcd@"),
                          DummyInteraction("CorrectHorseBatteryStaple#1234"),
                          DummyInteraction("a581T#11@aA")],
            "Problem 2": [DummyInteraction("Alice","Banana","Taekhoon","Hwangho","q"),
                          DummyInteraction("Genji","McCree","Pharah","Reaper","Soldier","Sombra","Tracer","q"),
                          DummyInteraction("Bastion","Hanzo","Junkrat","Mei","Torbjorn","Widowmaker","q"),
                          DummyInteraction("DVa","Orisa","Reinhardt","Roadhog","Winston","Zarya","q"),
                          DummyInteraction("Ana","Lucio","Mercy","Symmetra","Zenyatta","q")],
            "Problem 3": [DummyInteraction("apple",200, "apple",300,"mango",200,"q"),
                          DummyInteraction("apple", 1, "q"),
                          DummyInteraction("apple", 12,"banana", 54, "cactus", 125,"durian", 777,   "q"),
                          DummyInteraction("durian", 12537, "cactus", 544, "banana", 785, "apple", 540, "q"),
                          DummyInteraction("pear", 11, "strawberries", 2, "mango", 5453225,"mango", 621,"strawberries",1,"pear", 432, "q"),
                          DummyInteraction("pineapple", 55, "tomato", 8821,"melon", 6785, "q"),
                          DummyInteraction("pineapple", 55, "tomato", 15,"tomato", 8821, "pineapple", 35,"pineapple", 7,"melon", 85, "q")],
            "Problem 4": [DummyInteraction(1,2,3,4,3,0),
                          DummyInteraction(0),
                          DummyInteraction(1000,2000,500,3000,0),
                          DummyInteraction(54,0),
                          DummyInteraction(9999,3837,12,54,1,33,0)],
            "Problem 5": [DummyInteraction("zeroCheck(1,2,3)", interaction_type="IMPORT"),
                          DummyInteraction("zeroCheck(1,0,3)", interaction_type="IMPORT"),
                          DummyInteraction("zeroCheck(1234,2,0)", interaction_type="IMPORT"),
                          DummyInteraction("zeroCheck(287,87555,4522)", interaction_type="IMPORT"),
                          DummyInteraction("zeroCheck(-10,52,3)", interaction_type="IMPORT"),
                          DummyInteraction("zeroCheck(0,0,1)", interaction_type="IMPORT"),
                          DummyInteraction("zeroCheck(1,0,3)", interaction_type="IMPORT")],
            "Problem 6": [DummyInteraction("ordered3(1,2,3)",interaction_type="IMPORT"),
                          DummyInteraction("ordered3(1,1,1)", interaction_type="IMPORT"),
                          DummyInteraction("ordered3(3,2,1)", interaction_type="IMPORT"),
                          DummyInteraction("ordered3(3,2,4)", interaction_type="IMPORT"),
                          DummyInteraction("ordered3(10000,100000,10000000)", interaction_type="IMPORT"),
                          DummyInteraction("ordered3(-1000,0,1000)", interaction_type="IMPORT"),
                          DummyInteraction("ordered3(0,-1,10)", interaction_type="IMPORT"),
                          DummyInteraction("ordered3(77,44,11)", interaction_type="IMPORT"),
                          DummyInteraction("ordered3(3,6,0)", interaction_type="IMPORT")]}


#### BEGIN AUTO-GENERATED CODE ####

database={}
temp_interactions=[]
temp_interaction=Interaction()
temp_interaction.add_out('Enter password: ')
temp_interaction.add_in_raw('1abc%@\n')
temp_interaction.add_out('Your encrypted password is: 1mht)(\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter password: ')
temp_interaction.add_in_raw('a1234567890#@%\n')
temp_interaction.add_out('Your encrypted password is: m1234567890!()\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter password: ')
temp_interaction.add_in_raw('qwertyuiopasdfghjklzxcvbnm#0\n')
temp_interaction.add_out('Your encrypted password is: ivguxczjlnmofkbpweradtyhsq!0\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter password: ')
temp_interaction.add_in_raw('QWERTYUIOPASDFGHJKLZXCVBNM#0\n')
temp_interaction.add_out('Your encrypted password is: IVGUXCZJLNMOFKBPWERADTYHSQ!0\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter password: ')
temp_interaction.add_in_raw('Hello@5!\n')
temp_interaction.add_out('Invalid password!\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter password: ')
temp_interaction.add_in_raw('PassWoRd123\n')
temp_interaction.add_out('Invalid password!\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter password: ')
temp_interaction.add_in_raw('a bc\n')
temp_interaction.add_out('Invalid password!\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter password: ')
temp_interaction.add_in_raw('4986#\n')
temp_interaction.add_out('Invalid password!\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter password: ')
temp_interaction.add_in_raw('abcd@\n')
temp_interaction.add_out('Invalid password!\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter password: ')
temp_interaction.add_in_raw('CorrectHorseBatteryStaple#1234\n')
temp_interaction.add_out('Your encrypted password is: TluugtxPluogHmxxgucOxmnrg!1234\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter password: ')
temp_interaction.add_in_raw('a581T#11@aA\n')
temp_interaction.add_out('Your encrypted password is: m581X!11(mM\n')
temp_interactions.append(temp_interaction)
database['Problem 1']=temp_interactions
temp_interactions=[]
temp_interaction=Interaction()
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Alice\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Banana\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Taekhoon\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Hwangho\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('q\n')
temp_interaction.add_out("Appearance of letter 'a': 6\n")
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Genji\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('McCree\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Pharah\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Reaper\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Soldier\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Sombra\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Tracer\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('q\n')
temp_interaction.add_out("Appearance of letter 'a': 5\n")
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Bastion\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Hanzo\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Junkrat\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Mei\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Torbjorn\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Widowmaker\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('q\n')
temp_interaction.add_out("Appearance of letter 'a': 4\n")
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('DVa\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Orisa\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Reinhardt\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Roadhog\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Winston\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Zarya\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('q\n')
temp_interaction.add_out("Appearance of letter 'a': 6\n")
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Ana\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Lucio\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Mercy\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Symmetra\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('Zenyatta\n')
temp_interaction.add_out('Enter a name (q to quit): ')
temp_interaction.add_in_raw('q\n')
temp_interaction.add_out("Appearance of letter 'a': 5\n")
temp_interactions.append(temp_interaction)
database['Problem 2']=temp_interactions
temp_interactions=[]
temp_interaction=Interaction()
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('apple\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('200\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('apple\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('300\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('mango\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('200\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('q\n')
temp_interaction.add_out('apple, 500kg.\nmango, 200kg.\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('apple\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('1\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('q\n')
temp_interaction.add_out('apple, 1kg.\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('apple\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('12\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('banana\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('54\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('cactus\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('125\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('durian\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('777\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('q\n')
temp_interaction.add_out('apple, 12kg.\nbanana, 54kg.\ncactus, 125kg.\ndurian, 777kg.\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('durian\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('12537\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('cactus\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('544\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('banana\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('785\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('apple\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('540\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('q\n')
temp_interaction.add_out('apple, 540kg.\nbanana, 785kg.\ncactus, 544kg.\ndurian, 12537kg.\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('pear\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('11\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('strawberries\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('2\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('mango\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('5453225\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('mango\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('621\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('strawberries\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('1\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('pear\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('432\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('q\n')
temp_interaction.add_out('mango, 5453846kg.\npear, 443kg.\nstrawberries, 3kg.\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('pineapple\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('55\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('tomato\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('8821\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('melon\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('6785\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('q\n')
temp_interaction.add_out('melon, 6785kg.\npineapple, 55kg.\ntomato, 8821kg.\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('pineapple\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('55\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('tomato\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('15\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('tomato\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('8821\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('pineapple\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('35\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('pineapple\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('7\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('melon\n')
temp_interaction.add_out('Enter the weight in kg: ')
temp_interaction.add_in_raw('85\n')
temp_interaction.add_out('Enter a fruit type (q to quit): ')
temp_interaction.add_in_raw('q\n')
temp_interaction.add_out('melon, 85kg.\npineapple, 97kg.\ntomato, 8836kg.\n')
temp_interactions.append(temp_interaction)
database['Problem 3']=temp_interactions
temp_interactions=[]
temp_interaction=Interaction()
temp_interaction.add_out('Enter the limit L: ')
temp_interaction.add_in_raw('1\n')
temp_interaction.add_out('Sum of the initial 1 term(s): 1.000000\nEnter the limit L: ')
temp_interaction.add_in_raw('2\n')
temp_interaction.add_out('Sum of the initial 2 term(s): 1.500000\nEnter the limit L: ')
temp_interaction.add_in_raw('3\n')
temp_interaction.add_out('Sum of the initial 3 term(s): 1.833333\nEnter the limit L: ')
temp_interaction.add_in_raw('4\n')
temp_interaction.add_out('Sum of the initial 4 term(s): 2.083333\nEnter the limit L: ')
temp_interaction.add_in_raw('3\n')
temp_interaction.add_out('Sum of the initial 3 term(s): 1.833333\nEnter the limit L: ')
temp_interaction.add_in_raw('0\n')
temp_interaction.add_out('')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter the limit L: ')
temp_interaction.add_in_raw('0\n')
temp_interaction.add_out('')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter the limit L: ')
temp_interaction.add_in_raw('1000\n')
temp_interaction.add_out('Sum of the initial 1000 term(s): 7.485471\nEnter the limit L: ')
temp_interaction.add_in_raw('2000\n')
temp_interaction.add_out('Sum of the initial 2000 term(s): 8.178368\nEnter the limit L: ')
temp_interaction.add_in_raw('500\n')
temp_interaction.add_out('Sum of the initial 500 term(s): 6.792823\nEnter the limit L: ')
temp_interaction.add_in_raw('3000\n')
temp_interaction.add_out('Sum of the initial 3000 term(s): 8.583750\nEnter the limit L: ')
temp_interaction.add_in_raw('0\n')
temp_interaction.add_out('')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter the limit L: ')
temp_interaction.add_in_raw('54\n')
temp_interaction.add_out('Sum of the initial 54 term(s): 4.575430\nEnter the limit L: ')
temp_interaction.add_in_raw('0\n')
temp_interaction.add_out('')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction()
temp_interaction.add_out('Enter the limit L: ')
temp_interaction.add_in_raw('9999\n')
temp_interaction.add_out('Sum of the initial 9999 term(s): 9.787506\nEnter the limit L: ')
temp_interaction.add_in_raw('3837\n')
temp_interaction.add_out('Sum of the initial 3837 term(s): 8.829792\nEnter the limit L: ')
temp_interaction.add_in_raw('12\n')
temp_interaction.add_out('Sum of the initial 12 term(s): 3.103211\nEnter the limit L: ')
temp_interaction.add_in_raw('54\n')
temp_interaction.add_out('Sum of the initial 54 term(s): 4.575430\nEnter the limit L: ')
temp_interaction.add_in_raw('1\n')
temp_interaction.add_out('Sum of the initial 1 term(s): 1.000000\nEnter the limit L: ')
temp_interaction.add_in_raw('33\n')
temp_interaction.add_out('Sum of the initial 33 term(s): 4.088798\nEnter the limit L: ')
temp_interaction.add_in_raw('0\n')
temp_interaction.add_out('')
temp_interactions.append(temp_interaction)
database['Problem 4']=temp_interactions
temp_interactions=[]
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('zeroCheck(1,2,3)\n')
temp_interaction.add_out('False')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('zeroCheck(1,0,3)\n')
temp_interaction.add_out('True')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('zeroCheck(1234,2,0)\n')
temp_interaction.add_out('True')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('zeroCheck(287,87555,4522)\n')
temp_interaction.add_out('False')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('zeroCheck(-10,52,3)\n')
temp_interaction.add_out('False')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('zeroCheck(0,0,1)\n')
temp_interaction.add_out('True')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('zeroCheck(1,0,3)\n')
temp_interaction.add_out('True')
temp_interactions.append(temp_interaction)
database['Problem 5']=temp_interactions
temp_interactions=[]
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('ordered3(1,2,3)\n')
temp_interaction.add_out('True')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('ordered3(1,1,1)\n')
temp_interaction.add_out('True')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('ordered3(3,2,1)\n')
temp_interaction.add_out('False')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('ordered3(3,2,4)\n')
temp_interaction.add_out('False')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('ordered3(10000,100000,10000000)\n')
temp_interaction.add_out('True')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('ordered3(-1000,0,1000)\n')
temp_interaction.add_out('True')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('ordered3(0,-1,10)\n')
temp_interaction.add_out('False')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('ordered3(77,44,11)\n')
temp_interaction.add_out('False')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type="IMPORT")
temp_interaction.add_out('')
temp_interaction.add_in_raw('ordered3(3,6,0)\n')
temp_interaction.add_out('False')
temp_interactions.append(temp_interaction)
database['Problem 6']=temp_interactions

##### END AUTO-GENERATED CODE #####


## From here on it's all UI Setup.
## Not too hard to understand.
root = Tk()
root.title("CP Checker")

root_title = Frame(root)
root_title.grid(column=1,row=1, padx=10, pady=5, sticky=(W, E, N, S))
root.columnconfigure(1, weight=1)

root_title_website = Label(root_title, text="웹사이트 - 사용법 / 업데이트 / 다음 랩 다운로드", font=("맑은 고딕", 8), foreground="blue",
                           cursor="hand2")
root_title_website.bind("<Button-1>",
                        lambda e: webbrowser.open_new(r"http://chanspi.ddns.net/Yonsei/CPChecker"))
root_title_website.grid(column=1,  row=1, sticky=(W, E, N, S))

txt = '''컴퓨터프로그래밍 과제 가채점기 v0.3.0 [Database: Lab 6 v1]
©컴퓨터과학과 양찬솔 - 무단 배포 허용

▯는 문자가 있어야 할 곳에 문자가 없음을 뜻합니다.'''

faq_txt='''프로그램의 출력이 제때 나타나지 않으면 >> Read/Write Delay 값을 올림
프로그램의 초기 출력이 제대로 나오지 않으면 >> Initial Delay 값을 올림
공백 문자들을 더 잘 보고 싶다면 >> Show Spaces 체크
인코딩 문제가 있으면 >> Force CP949 Encoding을 체크

이 외에 프로그램 자체에 오류 있으면 톡 주세요.'''

root_title_text = Label(root_title, text=txt, font=("맑은 고딕", 8), anchor=("nw"))
root_title_text.grid(column=1, row=2, sticky=(W, E, N, S))
root_title.columnconfigure(1,weight=1)

root_title_text = Label(root_title, text=faq_txt, font=("맑은 고딕", 8), anchor=("nw"))
root_title_text.grid(column=2, row=1,rowspan=2, sticky=(W, E, N, S))
root_title.columnconfigure(2,weight=1)
root_title.rowconfigure(2,weight=1)

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
root_settings_verboseoutput = Checkbutton(root_settings, text="Show Spaces", variable=root_settings_verboseoutput_VAR)
root_settings_verboseoutput.grid(column=3, row=1, padx=5, pady=5, sticky=(W, E))

def get_cp949():
    return root_settings_verboseoutput_VAR.get() == 1


root_settings_cp949_VAR = IntVar()
root_settings_cp949_VAR.set(0)
root_settings_cp949 = Checkbutton(root_settings, text="Force CP949 Encoding", variable=root_settings_cp949_VAR)
root_settings_cp949.grid(column=4, row=1, padx=5, pady=5, sticky=(W, E))


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

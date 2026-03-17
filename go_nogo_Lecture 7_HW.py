##go no go

#Hi, I’m trying to adapt a GO/NOGO protocol from Price et al., 2016. Food-specific response inhibition,
#dietary restraint and snack intake in lean and overweight/obese adults.
#The task consists in 50 trials (40 go and 10 no-go). During go trials the 
#subject should press a key as fast as possible. During no-go trials, no key should be pressed. 
#Each trial is composed by an image presented for 750ms and was separated by a blank screen for 500 ms 
#and preceded by a fixation cross for 500 ms. The sequence of go/nogo stimuli are predetermined. 
#Two set of images are used: 10 go images (each one is presented 4 times) and 10 no-go images 
#(each one is presented one time). Image order should be randomized across subjects.
# we are going to change for anorexia nervosa intervention

import pandas as pd
import random
from psychopy.gui import DlgFromDict
from psychopy.visual import Window, TextStim, ImageStim, Rect, TextBox, DotStim, Circle
from psychopy.core import Clock, quit, wait
from psychopy.event import Mouse
from psychopy.hardware.keyboard import Keyboard
from psychopy import event, data

##Set Up & Participant Info##
exp_info = {'participant_nr': '', 'age': '21'}
dlg = DlgFromDict(exp_info)

if not dlg.OK:
    quit() ##Exit if the user presses cancel##

p_name= exp_info['participant_nr']

# Initialize a fullscreen window with my monitor (HD format) size
# and my monitor specification called "samsung" from the monitor center
win = Window(size=(1200, 800), fullscr=False)

# Also initialize a mouse, although we're not going to use it
mouse = Mouse(visible=False)

##Initialize keyboard##
kb = Keyboard()

# Initialize a (global) clock
clock = Clock()

##Prepare Stimuli##
f_list = f"/Users/kylasonnier/Downloads/HF_LF_60.csv"
foods = pd.read_csv(f_list)
hf = foods[foods['fat']==1]
lf = foods[foods['fat']==0]

##Sample and create 4:1 Go/No-Go Ratio##
lf = lf.sample(frac=0.4)
hf = hf.sample(frac=0.4)
trial_foods=pd.concat([lf,lf,lf,lf,hf])
trial_foods = trial_foods.sample(frac=1).reset_index(drop=True) ##Reset index for clean iteration##
kb=Keyboard()

##Create Lists to Store Responses##
responses = []
rts = []

##Task Instructions##
instruct_text = (
    "Welcome to the Go No-Go Task.\n\n"
    "You will see food images paired with a colored dot.\n\n"
    "GREEN DOT (GO): Press the SPACEBAR as quickly as possible.\n"
    "RED DOT (NO-GO): Do NOT press any key.\n\n"
    "Press the SPACEBAR when you are ready to begin."
)

instructions = TextStim(win, text=instruct_text, wrapWidth=1.5, color='white')
instructions.draw()
win.flip()
event.waitKeys(keyList=['space'])

##Trial Loop##
for i in range(0,len(trial_foods)):
    trial=trial_foods.iloc[i]
    print(trial)
    t=TextStim(win,"+")
    t.draw()
    win.flip()
    wait(0.5)
    path = "/Users/kylasonnier/Downloads/stimuli copy/" + trial.food
    print(trial.fat)
    if trial.fat==1:
        correct = "nogo"
        dot_color = "red"    ##Set dot color to red for high-fat##
    else: 
        correct = "go"
        dot_color = "green"  ##Set dot color to green for low-fat##
    
    im=ImageStim(win, path)

    ##Create the dot object (hovering slightly above center)##
    dot = Circle(win, radius=0.08, fillColor=dot_color, pos=(0, 0.6), units='norm')
    
    t_clock=Clock()
    response = "nogo"
    rt="NA"
    
    while t_clock.getTime() < .75:
        im.draw()
        dot.draw()  ##Code tells PsychoPy to show the dot##
        win.flip()
        keys = kb.getKeys(['space','escape'], waitRelease=False)
        if keys:
            resp = keys[0].name
            rt = keys[0].rt
            if resp == 'escape':
                win.close()
                quit()
            else:
                response = "go"

    win.flip()
    wait(.5)
    
##Use .loc[i, 'col'] to save data to the specific row, not the whole column##
##(I deleted the two old lines that were right above this that were causing conflicts)##
trial_foods.loc[i, 'response'] = response  
trial_foods.loc[i, 'rt'] = rt
trial_foods.loc[i, 'correct_answer'] = correct ##Added this so you can check their accuracy later!##

##Save using the pandas .to_csv method##
trial_foods.to_csv(f"{p_name}_gonogo.csv", index=False)

## tasks
# 1. figure out what is happening in the task & add instructions
# 2. we need to add go-nogo! How would we do that?

    

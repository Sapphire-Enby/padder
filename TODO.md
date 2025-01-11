# TODO
## Box Selector
1. get mouse position on click
2. check if mouse position is in grid 
    1. (use 00.x and y and -1,-1.x and y to validate)
    2. if inside:
3. for now STUB:
    check notes: sweep row zero for matching x val
    when got:
        make list with `row[ x index ]`for row in 2dArray
        for cell in list check y:
            when match:
                have cell return index.
index should be clicked box.
we can return this if we want box_select() -> tuple(int)
we currently have it set to print but we can flash a global mousecheck to equal false
or a global selected box to equal none on init and only start the box selecting procedure if
selected box is none, else ignore
could even make payload global, check payload["box"] on click, if none fill then init
payload prompt
something like this should work...

when selected box is not none call payload builder
___
## Payload Builder
Dont need to check grid, returns none if not a valid box
payload= {index : None, Color : None}
if box clicked ( if return not none none):
    temp_index = box.index
    temp_color = None
    prompt for color
    Options = ["red", "amber"", "green"", "clear"]
    prompt user
        if get() not in options 
            try again
        else
            temp_color= get()
    payload["index"]=temp_index
    payload["color"=temp_color]

if valid color is selected push payload to ouptput handler
handler(payload)
___
## output handler(inload)
this needs to be able to translate a coord and color to 
something that can pass that command on to the pygame.draw rect 
as well as to whatever method were gonna use to handle the midi part of the process
pygame.draw.rect() needs screen ( returned from python.display.setmode(),) a color (define yellow red and amber beforehand), and a tuple
  tuple is : x0, y0, cell width, cell height, this can easily be a instance function
      NOTE: make it an instance function, call it node.plot()
          _plot(self):
              out = (self.x0, self.y0, self.x1, self.y1 )
              return out 
    if so the args would be   
       Screen, payload["color"], (arr [payload["index"][0]][payload["index"][1]])._plot()
    call send the command to a function that call handle the job
    otherwize we need to send the equivalent command do that launchapd mini:
___

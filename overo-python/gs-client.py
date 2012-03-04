import socket
import Tkinter

FW_COMMAND = 'w'
BACK_COMMAND = 's'
LEFT_COMMAND = 'a'
RIGHT_COMMAND = 'd'

AUTOPILOT_IP = "192.168.23.3"
AUTOPILOT_PORT = 9999

class gs_gui(Tkinter.Tk):
  
    #Track parent
    #Gui's are a hierarchy of thimgs
    #ex: Window-->Tab-->Pane-->Button
    #    (parent) ---> children

  def __init__(self,parent):
    Tkinter.Tk.__init__(self,parent)
    #Good practice to mainatain a reference to your parent
    self.parent = parent
    #Create gui elements
    self.inititalize()
 
  def inititalize(self):
    #Instanstiate a layout manager
    self.grid()
    
    #create a text entry widget
    #we keep a refference to the txt box in order to
    #read / manipulate it later
    #variable to store txt entered
    self.entryVar = Tkinter.StringVar()
    self.entry = Tkinter.Entry(self,textvariable=self.entryVar)
    #self.entryVar.set("Enter Custom Command")
    
    #create a buttons
    #we do not keep a refference to the button since
    #it will not be changed
    button = Tkinter.Button(self,text="Send",command=self.OnButtonClick)
    buttonFw = Tkinter.Button(self,text=" Forward ",command=self.OnFwClick)
    buttonBack = Tkinter.Button(self,text="  Back  ",command=self.OnBackClick)
    buttonLeft = Tkinter.Button(self,text="  <-Left  ",command=self.OnLeftClick)
    buttonRight = Tkinter.Button(self,text="Right->  ",command=self.OnRightClick)

    #add labels
    self.labelVariable = Tkinter.StringVar()
    label = Tkinter.Label(self, textvariable = self.labelVariable, anchor='w', fg="black", bg="white")
    self.labelVariable.set("Zepplin Ground Station")
    
    #Add things to the layout manager
    #sticky EW (East West) sticks it to the vertical edges 
    #of the window
    self.entry.grid(column=0,row=0,columnspan=1,sticky='EW')
    button.grid(column=1,row=0,columnspan=1,sticky='EW')
    label.grid(column=0,row=1,columnspan=2,sticky='EW')
    buttonFw.grid(column=0,row=2,columnspan=2,sticky='EW')
    buttonBack.grid(column=0,row=4,columnspan=2,sticky='EW')
    buttonLeft.grid(column=0,row=3,columnspan=1,sticky='EW')
    buttonRight.grid(column=1,row=3,columnspan=1,sticky='EW')
    
    #Tell the layout manager to resize columns when the window
    #is resized
    self.grid_columnconfigure(0,weight=1)
    self.grid_columnconfigure(1,weight=1)
    self.resizable(True,False)
    
    #add events
    self.entry.bind("<Return>",self.OnPressEnter)
    self.bind("<Up>",self.OnPressFw)
    self.bind("<Down>",self.OnPressBack)
    self.bind("<Left>",self.OnPressLeft)
    self.bind("<Right>",self.OnPressRight)
    
    #init logic
    self.initClient()

  def initClient(self): 
    # Open Port
    self.HOST, self.PORT = AUTOPILOT_IP, AUTOPILOT_PORT
    # SOCK_DGRAM is the socket type to use for UDP sockets
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.byteSent = 0
    
  def OnFwClick(self):
    self.sendCMD(FW_COMMAND)

  def OnBackClick(self):
    self.sendCMD(BACK_COMMAND)
    
  def OnLeftClick(self):
    self.sendCMD(LEFT_COMMAND)
    
  def OnRightClick(self):
    self.sendCMD(RIGHT_COMMAND)
    
  def OnButtonClick(self):
    self.sendCMD(self.entryVar.get())
   
  def sendCMD(self,msg):
    print "Sending: {}".format(msg)
    self.labelVariable.set("Sent : "+msg)
    self.sock.sendto(msg + "\n", (self.HOST, self.PORT))
    self.byteSent = self.byteSent + 1
    print "Sent Total: {} Msgs".format(self.byteSent)
   
  def OnPressFw(self,event):
    self.OnFwClick()
    
  def OnPressBack(self,event):
    self.OnBackClick()
    
  def OnPressLeft(self,event):
    self.OnLeftClick()
    
  def OnPressRight(self,event):
    self.OnRightClick()
    
  def OnPressEnter(self,event):
    self.OnButtonClick()
    
    
if __name__ == "__main__":
    app = gs_gui(None)
    app.title('zepplin gs')
    app.mainloop()
from tkinter import *  # Import tkinter


class SierpinskiTriangle:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Sierpinski Triangle")  # Set a title

        self.width = 200
        self.height = 200
        self.canvas = Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()
        #Add events and binds
        self.canvas.bind("<Key>", self.processKeyEvent)
        self.canvas.focus_set()

        # Add a label, an entry, and a button to frame1
        frame1 = Frame(window)  # Create and add a frame to window
        frame1.pack()

        Label(frame1, text="Enter an order: ").pack(side=LEFT)
        #self.order = StringVar(value=0)
        self.int_order = 0
        self.order = IntVar(value=self.int_order)
        entry = Entry(frame1, textvariable=self.order, justify=RIGHT).pack(side=LEFT)
        Button(frame1, text="Display Sierpinski Triangle", command=self.display).pack(side=LEFT)

        self.display()
        window.mainloop()  # Create an event loop

    def processKeyEvent(self, event):
        print("processKeyEvent(self, event)")
        print("event.char?", event.char)
        if event.char == '+':
            self.processAddEvent(event)
        elif event.char == '-':
            self.processMinusEvent(event)

    def processAddEvent(self, event):
        if self.int_order >= 0:
            self.int_order += 1
            self.order = IntVar(value=self.int_order)
        self.canvas.update()
        self.display()

    def processMinusEvent(self, event):
        if self.order.get() > 0:
            self.int_order -= 1
            self.order = IntVar(value=self.int_order)
        else:
            self.int_order = 0
            self.order = IntVar(value=self.int_order)
        self.canvas.update()
        self.display()

    def display(self):  #Trigger Function, run one time.
        self.canvas.delete("line")
        p1 = [self.width / 2, 10]
        p2 = [10, self.height - 10]
        p3 = [self.width - 10, self.height - 10]
        self.displayTriangles(int(self.order.get()), p1, p2, p3)

    def displayTriangles(self, order, p1, p2, p3):
        """
                    x<-p1


              x<-p2       x<-p3
        """
        if order == 0:  # Base condition
            # Draw a triangle to connect three points
            self.drawLine(p1, p2)
            self.drawLine(p2, p3)
            self.drawLine(p3, p1)
        else:
            # Get the midpoint of each triangle's edge
            p12 = self.midpoint(p1, p2)
            p23 = self.midpoint(p2, p3)
            p31 = self.midpoint(p3, p1)

            # Recursively display three triangles(1 original point with 2 mid points)
            self.displayTriangles(order - 1, p1, p12, p31)
            self.displayTriangles(order - 1, p12, p2, p23)
            self.displayTriangles(order - 1, p31, p23, p3)

    def drawLine(self, p1, p2):
        self.canvas.create_line(
            p1[0], p1[1], p2[0], p2[1], tags="line")

    # Return the midpoint between two points
    def midpoint(self, p1, p2):
        p = 2 * [0]
        p[0] = (p1[0] + p2[0]) / 2
        p[1] = (p1[1] + p2[1]) / 2
        return p


SierpinskiTriangle()  # Create GUI
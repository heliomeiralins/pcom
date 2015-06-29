import tkinter as tk

from line_codes import BinaryData


X0 = 20
Y0 = 100
Y1 = 250
dx = 5
dy = 5
DX = 40
DY = 40


LINE_CODES = {
    'NRZ-L': ('nrz_l', 1),
    'NRZ-M': ('nrz_m', 1),
    'NRZ-S': ('nrz_s', 1),
    'Unipolar RZ': ('unipolar_rz', 2),
    'Polar RZ': ('polar_rz', 2),
    'AMI': ('ami', 2),
    'Manchester': ('manchester', 2),
    'Manchester Diferencial': ('dif_manchester', 2),
}


class LineCodesApp(tk.Frame):

    def __init__(self, master=None):
        self.binary_data = BinaryData()
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("Line Codes - ProjetoPCOM")
        self.createWidgets()

    def createWidgets(self):

        input_frame = tk.Frame(self)

        self.data = tk.StringVar()
        self.data.set("0b10110001101")

        entry_label = tk.Label(input_frame, text="Entrada : ")
        entry_label.grid(row=0, column=0, sticky=tk.W)

        self.entry = tk.Entry(input_frame, textvariable=self.data)
        self.entry.bind('<Key-Return>', self.set_input)
        self.entry.grid(row=0, column=1, sticky=tk.W)

        choices = LINE_CODES.keys()
        self.line_code = tk.StringVar()
        self.line_code.set('Manchester')
        self.box = tk.OptionMenu(
            input_frame, self.line_code, *choices, command=self.change_option)
        self.box.grid(row=1, column=1, sticky=tk.W + tk.E)

        input_frame.pack()

        canvas_frame = tk.Frame(self, width=800, height=600)
        self.canvas = tk.Canvas(
            canvas_frame, bg='#FFFFFF', width=750, height=500,)
        hbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL)
        hbar.pack(side=tk.BOTTOM, fill=tk.X)
        hbar.config(command=self.canvas.xview)
        vbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL)
        vbar.pack(side=tk.RIGHT, fill=tk.Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        self.canvas_items = []
        self.canvas.pack()
        canvas_frame.pack()

        footer_label = tk.Label(
            self, text="Criado pelo grupo 10 para o projeto de PCOM do Prof."
            "Daniel Cunha [CIN, UFPE]")
        footer_label.pack(side=tk.BOTTOM)

        self.set_input()

    def set_input(self, event=None):
        self.binary_data.set_data(self.data.get())
        self.input_points = []

        self.input_points = []
        for i, b in enumerate(self.binary_data):
            self.input_points.append((X0 + i * DX, Y0 - DY * b))
            self.input_points.append((X0 + i * DX + DX, Y0 - DY * b))

        method, step = LINE_CODES[self.line_code.get()]
        coded_data = getattr(self.binary_data, method)()
        self.coded_points = []
        for i, b in enumerate(coded_data):
            self.coded_points.append((X0 + i * DX / step, Y1 - DY * b))
            self.coded_points.append(
                (+ X0 + (i * DX + DX) / step, Y1 - DY * b))
        self.draw_plots()

    def change_option(self, event):
        method, step = LINE_CODES[self.line_code.get()]
        coded_data = getattr(self.binary_data, method)()
        del self.coded_points
        self.coded_points = []
        for i, b in enumerate(coded_data):
            self.coded_points.append((X0 + i * DX / step, Y1 - DY * b))
            self.coded_points.append(
                (+ X0 + (i * DX + DX) / step, Y1 - DY * b))
        self.draw_plots()

    def draw_plots(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_line(
            X0 - dx, Y0, X0 + DX * len(self.binary_data) + dx, Y0)

        self.canvas.create_line(
            X0 - dx, Y1, X0 + DX * len(self.binary_data) + dx, Y1)

        for p1, p2 in zip(self.input_points, self.input_points[1:]):
            self.canvas.create_line(
                p1[0], p1[1], p2[0], p2[1], width=3, fill='blue')

        for p1, p2 in zip(self.coded_points, self.coded_points[1:]):
            self.canvas.create_line(
                p1[0], p1[1], p2[0], p2[1], width=3, fill='blue')

        for i in range(0, len(self.binary_data)):
            self.canvas.create_line(
                X0 + i * DX, Y0 - DY - 2 * dy, X0 + i * DX, Y0 + DY + 2 * dy
            )
            self.canvas.create_line(
                X0 + i * DX, Y1 - DY - 2 * dy, X0 + i * DX, Y1 + DY + 2 * dy
            )

if __name__ == '__main__':
    root = tk.Tk()
    app = LineCodesApp(master=root)
    app.mainloop()

import tkinter


class Renderer:
    COLOR_GRAY = "#808080"
    COLOR_WHITE = "#ffffff"
    COLOR_BLACK = "#000000"

    def render_solution(self, solution: str):
        ws = tkinter.Tk()
        ws.title("Griddler Solver")

        height = 600
        width = 600
        # TODO dynamic width/height compute based on solution
        canvas = tkinter.Canvas(
            ws, height=height, width=width, bg=self.COLOR_GRAY
        )

        rows = solution.splitlines()
        tile_dimension = 100 # TODO compute dynamically
        for row_i, row in enumerate(rows):
            for column_i, tile in enumerate(row):
                color = self.COLOR_WHITE
                if tile == "1":
                    color = self.COLOR_BLACK
                canvas.create_rectangle(
                    0 + row_i*tile_dimension,
                    0 + column_i*tile_dimension,
                    tile_dimension + row_i*tile_dimension,
                    tile_dimension + column_i*tile_dimension,
                    outline=self.COLOR_GRAY,
                    fill=color
                )
        canvas.pack()

        ws.mainloop()
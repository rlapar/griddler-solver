from griddler_solver.renderer import Renderer
from griddler_solver.model import GriddlerModel

# def main():
#     r = Renderer()
#     r.render_solution(solution="""11111
# 10000
# 10000
# 10000
# 10000""")

def main():
    g = GriddlerModel()
    g.from_string("""###10101
###10101
###15151
##/-----
22|?????
03|?????
22|?????
03|?????
22|?????""")

if __name__ == "__main__":
    main()
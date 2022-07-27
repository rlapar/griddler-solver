from griddler_solver.renderer import Renderer

def main():
    r = Renderer()
    r.render_solution(solution="""11111
10000
10000
10000
10000""")

if __name__ == "__main__":
    main()
import subprocess
import os


def run_takaken_solver(solver_path, input_file, output_file, time_limit=600, level_number="all"):
    """
    Runs the takaken74 Sokoban solver with the specified parameters.
    """
    if not os.path.isfile(solver_path):
        print(f"File not found: {solver_path}")
        return

    if not os.path.isfile(input_file):
        print(f"Input file not found: {input_file}")
        return

    # Command to run the solver with the provided parameters
    command = [solver_path, '-in', input_file, '-out', output_file, '-time', str(time_limit), '-level', level_number]

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Errors from the takaken74 solver:\n{result.stderr}")
        else:
            print(f"Output from the takaken74 solver:\n{result.stdout if result.stdout else 'No output received.'}")
            with open(output_file, 'r') as f:
                print(f.read())  # This will print the contents of the output file to the screen
    except Exception as e:
        print(f"Failed to run the takaken74 solver: {e}")


def run_solver_two(solver_path, input_file ,output_file, iterative_mode=True, engine='SAT', steps_num=11):
    """
    Runs the sokoban_solver.exe with the specified parameters directly.
    """
    if not os.path.isfile(solver_path):
        print(f"File not found: {solver_path}")
        return

    # Command to run the solver with the provided parameters
    command = [solver_path, str(iterative_mode), engine, str(steps_num)]

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Errors from the sokoban_solver.exe:\n{result.stderr}")
        else:
            with open(output_file, 'a') as f:  # Append the output to the output file
                f.write("\n--- Sokoban Solver Two Results ---\n")
                f.write(result.stdout if result.stdout else 'No output received.\n')
            print(f"Output from the sokoban_solver.exe:\n{result.stdout if result.stdout else 'No output received.'}")
    except Exception as e:
        print(f"Failed to run the sokoban_solver.exe: {e}")


def run_yass_solver(yass_exe_path, puzzle_file, output_file, levels="1-10", maxtime=600):
    """
    Runs the YASS.exe solver with the specified parameters and appends the results to the output file.
    """
    if not os.path.isfile(yass_exe_path):
        print(f"File not found: {yass_exe_path}")
        return

    if not os.path.isfile(puzzle_file):
        print(f"Puzzle file not found: {puzzle_file}")
        return

    # Create the command as a single string
    command = f'{yass_exe_path} {puzzle_file} -level {levels} -maxtime {maxtime} -optimize moves'

    # Print the command to debug
    print(f"Running command: {command}")

    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if result.returncode != 0:
            print(f"Errors from the YASS.exe solver:\n{result.stderr}")
        else:
            with open(output_file, 'a') as f:  # Append to the output file
                f.write("\n--- YASS Solver Results ---\n")
                f.write(result.stdout if result.stdout else 'No output received.\n')
            print(f"Output from the YASS.exe solver:\n{result.stdout if result.stdout else 'No output received.'}")
    except Exception as e:
        print(f"Failed to run the YASS.exe solver: {e}")


def main():
    # Paths to the solvers
    solver_takaken_path = "takaken74.exe"  # Path to takaken74.exe solver
    solver_two_path = "main.exe"  # Path to sokoban_solver.exe
    yass_exe_path = "YASS.exe"  # Path to YASS.exe

    # Path to the Sokoban board file and output file
    input_file = "boards/board.txt"  # Path to the level file
    output_file = "sokoban_output.txt"  # Path to the output file

    # Parameters for takaken solver
    time_limit = 600  # Time limit in seconds (default: 600)
    level_number = "1"  # Level number (default: all levels)

    # Parameters for sokoban_solver.exes
    iterative_mode = True
    engine = "SAT"
    steps_num = 11

    # Parameters for YASS solver
    levels = "1 - 10"
    yass_maxtime = 600  # Time limit in seconds

    # Run the takaken solver
    print("Running the takaken74 solver...")
    run_takaken_solver(solver_takaken_path, input_file, output_file, time_limit, level_number)

    # Run the sokoban_solver.exe
    print("Running the sokoban_solver.exe...")
    run_solver_two(solver_two_path,input_file , output_file, iterative_mode, engine, steps_num)


    # Run the YASS solver and append results to the output file
    print("Running the YASS.exe solver...")
    run_yass_solver(yass_exe_path, input_file, output_file, levels, yass_maxtime)

if __name__ == "__main__":
    main()



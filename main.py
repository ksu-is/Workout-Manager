# create workout manager as package
class WorkoutManager:
    def __init__(base):
        base.workouts = []

    # create menu to show user options
    def workout_menu(base):
        print("\nWorkout Manager")
        print("1. All Workouts")
        print("2. Add a Workout")
        print("3. Edit a Workout")
        print("4. Delete a Workout")
        print("5. Exit")

    # define view workouts module
    def view_workouts(base):
        if not base.workouts:
            print("No workouts added.")
    #sequence the workouts by adding a number to each workout added
        else:
            for index, workout in enumerate(base.workouts):
                print(f"{i + 1}. {workout[0]} - {workout[1]} reps, {workout[2]} sets")

    # define add workouts module
    def add_workout(base):
        name = input("Enter the workout name: ")
        reps = input("Enter the number of reps: ")
        sets = input("Enter the number of sets: ")
    #add only if the reps and sets inputs are digits
        if name and reps.isdigit() and sets.isdigit():
            base.workouts.append((name, int(reps), int(sets)))
            print(f"Workout '{name}' added successfully!")
        else:
            print("Invalid input. Please try again.")

    # define edit workouts module
    def edit_workout(base):
        base.view_workouts()
        try:
            index = int(input("Enter the number of the workout to edit: ")) - 1
            if 0 <= index < len(base.workouts):
                name = input("Enter the new name for the workout: ")
                reps = input("Enter the new number of reps: ")
                sets = input("Enter the new number of sets: ")
                if name and reps.isdigit() and sets.isdigit():
                    base.workouts[index] = (name, int(reps), int(sets))
                    print("Workout updated successfully.")
                else:
                    print("Invalid input. Please try again.")
            else:
                print("Invalid workout number. Please try again.")

    # define delete workouts module
    def delete_workout(base):
        base.view_workouts()
        try:
            index = int(input("Enter the number of the workout to delete: ")) - 1
            if 0 <= index < len(base.workouts):
                deleted_workout = base.workouts.pop(index)
                print(f"Workout '{deleted_workout[0]}' deleted successfully.")
            else:
                print("Invalid workout number. Please try again.")

    # connect choices on menu to modules above
    def run(base):
    user_input = input("Please enter your name: ")
        while True:
            base.workout_menu()
            choice = input(f"Hello, {user_input}! Please enter your menu choice: ")
            if choice == '1':
                base.view_workouts()
            elif choice == '2':
                base.add_workout()
            elif choice == '3':
                base.edit_workout()
            elif choice == '4':
                base.delete_workout()
            elif choice == '5':
                print("Exiting Workout Manager. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

# call to run the code from the top moodule
if __name__ == "__main__":
    manager = WorkoutManager()
    manager.run()

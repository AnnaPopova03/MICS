from employee_leaf import EmployeeLeaf
from branch import BranchComposite
from department import DepartmentComposite


def choose_level(corporation):
    # available levels and prompt user for a choice
    print("Available levels:")
    print("1. Corporation")
    print("2. Department")
    print("3. Branch")
    ch = input("Choose a level (enter the corresponding number): ")

    try:
        ch = int(ch)
         # return the selected level based on user input
        if ch == 1:
            return corporation
        elif ch == 2:
            return choose_component(corporation)
        elif ch == 3:
            selected_department = choose_component(corporation)
            return choose_component(selected_department)
        else:
            raise ValueError("Invalid choice. Please enter a valid number.")
    except ValueError as e:
        print(f"Error: {e}")
        return choose_level(corporation)

def choose_component(component):
     # available components for the selected level and prompt user for a choice
    print(f"Available components for {component.name}:")
    for i, sub_component in enumerate(component.subordinates):
        print(f"{i + 1}. {sub_component.name}")

    choice = input("Choose a component (enter the corresponding number): ")

    try:
        choice = int(choice)
        # return the selected component based on user input
        if 1 <= choice <= len(component.subordinates):
            return component.subordinates[choice - 1]
        else:
            raise ValueError("Invalid choice. Please enter a valid number.")
    except ValueError as e:
        print(f"Error: {e}")
        return choose_component(component)

def main():
    # create a corporate structure
    corporation = DepartmentComposite("RandomCorp")

    branch1 = BranchComposite("First branch")
    branch1.add_subordinate(EmployeeLeaf("Ivan"))
    branch1.add_subordinate(EmployeeLeaf("Anna"))

    branch2 = BranchComposite("Second branch")
    branch2.add_subordinate(EmployeeLeaf("Daniel"))
    branch2.add_subordinate(EmployeeLeaf("Alex"))
    
    branch3 = BranchComposite("Third branch")
    branch3.add_subordinate(EmployeeLeaf("Sonya"))
    branch3.add_subordinate(EmployeeLeaf("Nikita"))

    hr_department = DepartmentComposite("HR Department")
    hr_department.add_subordinate(branch1)
    hr_department.add_subordinate(branch2)

    marketing_department = DepartmentComposite("Marketing Department")
    marketing_department.add_subordinate(branch3)

    corporation.add_subordinate(hr_department)
    corporation.add_subordinate(marketing_department)

    selected_level = choose_level(corporation)

    action = input("Enter the action to perform (fire, transfer, vacation, bonus, etc.): ")
    selected_level.perform_action(action)

if __name__ == "__main__":
    main()
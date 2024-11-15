# University-Student-Record-Management

We design a program that manages student records at a university.

## Input
- StudentsMajorsList.csv -- contains items listed by row. Each row contains student ID, last name, first name, major, and optionally a disciplinary action indicator
- GPAList.csv -- contains items listed by row. Each row contains student ID and the student GPA.
- GraduationDatesList.csv – contains items listed by row. Each row contains student ID and graduation date.
- StudentsMajorsList.csv -- contains items listed by row. Each row contains student ID, last name, first name, major, and optionally a disciplinary action indicator
- GPAList.csv -- contains items listed by row. Each row contains student ID and the student GPA.
- GraduationDatesList.csv – contains items listed by row. Each row contains student ID and graduation date.

## Output
Processed Inventory Reports:
- FullRoster.csv - all the items listed by row with all their information . The items should be sorted alphabetically by student last name. Each row contain student ID, major, first name, last name, GPA, graduation date and indicate if disciplinary action was taken. The student attributes appear in this order in each row.
- List per major, i.e ComputerInformationSystemsStudents.csv - there is a file for each major and the major needs to be in the file name, the spaces in the major name is eliminated for the file name. Each row of the file contain student ID, last name, first name, graduation date, and indicate if disciplinary action was taken. The students sorted by their student ID.
- ScholarshipCandidates.csv – contain a list of all eligible students with GPAs > 3.8. Students who have graduated or have had disciplinary action taken are not eligible. Each row contain: student ID, last name, first name, major, and GPA. The students appear in the order of GPA from highest to lowest
- DisciplinedStudents.csv – all students that have been disciplined. Each row contain: student ID, last name, first name, and graduation date. The students appear in the order of graduation date from oldest to most recent.
- Interactive Inventory Query Capability. Query the user of an item by asking for a major and GPA with a single query.
  1. Print a message(“No such student”) if the major is not in the roster, more that one major or GPA is submitted. Ignore any other words, so “smart Computer Science student 3.5” is treated the same as “Computer Science 3.5”.
  2. Print “Your student(s):” with the student ID, first name, last item, GPA. Do not provide students that have graduated or had disciplinary action . List all the students within 0.1 of the requested GPA.
  3. Also print “You may, also, consider:” and provide information about the same student type within 0.25 of the requested GPA . Do not provide students that have graduated or had disciplinary action.
  4. If there were no students who satisfied neither ii nor iii above – provide the information about the student within the requested major with closest GPA to that requested. Do not provide students that have graduated or had disciplinary action .
  5. After output for one query, query the user again. Allow ‘q’ to quit.
 



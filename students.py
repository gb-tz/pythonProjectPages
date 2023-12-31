import pandas as pd
from datetime import datetime
import random  # To generate random grades

class Student:
    def __init__(self, id, fname, lname, dateBirth, height,weight, gender):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.dateBirth = dateBirth
        self.height = height
        self.weight = weight
        self.gender = gender
        self.courses = {'Math': -1, 'History': -1, 'Physics': -1, 'English': -1, 'Biology': -1}

    def add_grade(self, course_name, grade):
        self.courses[course_name] = grade

    def average_grade(self):
        if len(self.courses) == 0:
            return -1
        else:
            return sum(self.courses.values()) / len(self.courses)

    def __str__(self):
        return f"id: {self.id} first name: {self.fname}, last name: {self.lname} genter: {self.genter} "

    def get_bmi(self):
        """
        Calculate and return the BMI (Body Mass Index).
        Formula: weight (kg) / height (m)^2
        Note: Height should be converted from cm to m.
        """
        height_m = self.height / 100  # converting height to meters
        bmi = self.weight / (height_m ** 2)
        return bmi

    def get_bmi_category(self):
        """
        Return the BMI category of the student based on their BMI value.

        Categories:
        - Underweight: Below 18.5
        - Normal: 18.5-25
        - Overweight: 25.0-30
        - Obesity: 30 and above
        """
        bmi = self.get_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:  # bmi >= 30
            return "Obesity"



class Classroom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.students = []
        self.filename = room_name + '.csv'

    def add_demo_data(self):
        # Create student instances with specific data
        students_data = [
            [1, "Alice", "Johnson", "2000-01-01", 153, 49, "Female"],
            [2, "Bob", "Smith", "2001-02-02", 165, 59, "Male"],
            [3, "Charlie", "Brown", "2002-03-03", 159, 65, "Male"],
            [4, "Diana", "White", "2003-04-04", 169, 64, "Female"],
            [5, "Eva", "Black", "2004-05-05", 180, 80, "Female"],
            [6, "Frank", "Taylor", "2000-06-06", 165, 78, "Male"],
            [7, "Grace", "Lee", "2001-07-07", 155, 60, "Female"],
            [8, "Henry", "Miller", "2002-08-08", 192, 84, "Male"],
            [9, "Ivy", "Davis", "2003-09-09", 168, 58, "Female"],
            [10, "Jack", "Wilson", "2004-10-10", 178, 72, "Male"],
            [11, "Kathy", "Moore", "2000-11-11", 162, 64, "Female"],
            [12, "Liam", "White", "2001-12-12", 183, 95, "Male"],
            [13, "Mia", "Harris", "2002-01-13", 171, 80, "Female"],
            [14, "Noah", "Nelson", "2003-02-14", 176, 90, "Male"],
            [15, "Olivia", "Martin", "2004-03-15", 181, 71, "Female"],
            [16, "Paul", "Garcia", "2000-04-16", 187, 87, "Male"],
            [17, "Quincy", "Adams", "2001-05-17", 188, 92, "Male"],
            [18, "Rosa", "Martinez", "2002-06-18", 174, 95, "Female"],
            [19, "Sam", "Lee", "2003-07-19", 167, 60, "Male"],
            [20, "Tina", "Turner", "2004-08-20", 164, 54, "Female"]
        ]
        #id, fname, lname, dateBirth, height,weight, gender
        # Courses list
        courses = ['Math', 'History', 'Physics', 'English', 'Biology']
        # Add the students to the classroom
        for data in students_data:
            student = Student(id=data[0], fname=data[1], lname=data[2],
                    dateBirth=datetime.strptime(data[3], "%Y-%m-%d").date(),  # Convert string to datetime
                    height=data[4], weight=data[5], gender=data[6])

            # Add random grades for each course
            for course in courses:
                student.add_grade(course, random.randint(8, 20))  # Assign random grades between 8 and 20

            self.add_student(student)

    def add_student(self, student):
        self.students.append(student)

    def average_grade_class(self):
        if len(self.students) == 0:
            return -1

        total_grades = sum(st.average_grade() for st in self.students)
        return total_grades / len(self.students)

    def get_students_data(self):
        data = []
        for student in self.students:
            data.append({
                'ID': student.id,
                'First Name': student.fname,
                'Last Name': student.lname,
                'Date of Birth': student.dateBirth,
                'Height': student.height,
                'Weight': student.weight,
                'Gender': student.gender,
                'Courses': student.courses
            })
        return data

    def save_students_to_csv(self):
        df = pd.DataFrame(self.get_students_data())
        df.to_csv(self.filename, index=False)

    def load_students_from_csv(self):
        df = pd.read_csv(self.filename)
        self.students = []
        for index, row in df.iterrows():
            student = Student(
                row['ID'],
                row['First Name'],
                row['Last Name'],
                row['Date of Birth'],
                row['Height'],
                row['Weight'],
                row['Gender']
            )
            student.courses = eval(row['Courses'])
            self.students.append(student)

    def search_students(self, fname="", lname=""):
        """
        Search for students based on partial matches for first name and last name.
        If fname or lname is empty or None, it ignores that field in the search.
        """
        df = pd.DataFrame(self.get_students_data() ) # Get the DataFrame of students

        # Convert to lowercase for case-insensitive search
        fname = fname.lower() if fname else ""
        lname = lname.lower() if lname else ""

        # Apply filtering to DataFrame
        if fname:
            df = df[df['First Name'].str.lower().str.contains(fname)]
        if lname:
            df = df[df['Last Name'].str.lower().str.contains(lname)]

        return df

    def student_exists(self,search_id):
        for s in self.students:
            if s.id == search_id :
                return True

        return False


    def get_next_student_id(self):
        if not self.students:
            return 1

        el = [st.id for st in self.students]
        max_id = max(el)

        return max_id +1

    def get_student_by_id(self, id):
        for student in self.students:
            if student.id == id:
                return student

        return None

    def update_student(self, id, fname, lname, dateBirth, height, weight, gender):
        student = self.get_student_by_id(id)
        if student :
            student.fname = fname
            student.lname = lname
            student.dateBirth = dateBirth
            student.height = height
            student.weight = weight
            student.gender = gender

    def delete_student(self,id):
        for i in range(len(self.students)):
            if self.students[i].id == id :
                del self.students[i]
                return True
        return False

    def get_min_student_id(self):
        if not self.students:
            return 1

        el = [st.id for st in self.students]
        min_id = min(el)

        return min_id

    def generate_dataframe(self):
        data = []
        for student in self.students:
            student_data = {
                'ID': student.id,
                'First Name': student.fname,
                'Last Name': student.lname,
                'Date of Birth': student.dateBirth,
                'Height': student.height,
                'Weight': student.weight,
                'Gender': student.gender,
                'Math': student.courses['Math'],
                'History': student.courses['History'],
                'Physics': student.courses['Physics'],
                'English': student.courses['English'],
                'Biology': student.courses['Biology'],
                'Average Grade': student.average_grade(),
                'BMI': student.get_bmi(),
                'BMI Category': student.get_bmi_category()

            }
            data.append(student_data)
        df = pd.DataFrame(data)
        return df

    def sort_students_by_id(self):
        """
        Sort the students by id using Python's built-in sort function.
        """
        self.students.sort(key=lambda student: student.id)

    def bubble_sort_students_by_grade(self):
        """
        Sorts a list of students based on their average grade using bubble sort.

        Parameters:
        - students (list): A list of Student instances.

        Returns:
        list: A list containing sorted Student instances.
        """
        n = len(self.students)
        # Traverse through all elements in the list
        for i in range(1, n):
            # Last i elements are already in place, no need to check them
            for j in range(n - 1, i - 1, -1):

                # Traverse the list from 0 to n-i-1.
                # Swap if the element found is greater than the next element
                if self.students[j - 1].average_grade() < self.students[j].average_grade():
                    self.students[j - 1], self.students[j] = self.students[j], self.students[j - 1]  # swap values

    def sort_students_by_name(self):
        n = len(self.students)
        for i in range(n):
            for j in range(i + 1, n):
                pass

    def selection_sort_students_by_bmi(self):
        n= len(self.students)
        for i in range(n):
            min_idx = i
            for j in range(i+1,n):
                if self.students[min_idx].get_bmi() > self.students[j].get_bmi():
                    min_idx = j
            self.students[i],self.students[min_idx]=self.students[min_idx],self.students[i]

    def binary_search_id(self,target_id):
        left = 0
        right = len(self.students)-1
        while left<=right:
            mid = left+right//2
            if self.students[mid]<target_id:
                left = mid + 1
            elif self.students[mid]>target_id:
                right = mid - 1
            else:
                return self.students[mid]
        return None
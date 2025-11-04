from js import document

def calculate_gwa(event):
    # Get student info
    first = document.getElementById("firstName").value
    last = document.getElementById("lastName").value

    # Subjects and units
    subjects = ["Math", "Science", "ICT", "PE", "English"]
    units = (3, 3, 3, 2, 3)

    # Retrieve grades
    grades = [
        float(document.getElementById("math").value),
        float(document.getElementById("science").value),
        float(document.getElementById("ict").value),
        float(document.getElementById("pe").value),
        float(document.getElementById("english").value)
    ]

    # Compute weighted average
    weighted_sum = sum(g * u for g, u in zip(grades, units))
    gwa = weighted_sum / sum(units)

    # Determine remark
    remark = "Passed 🎓" if gwa >= 75 else "Needs Improvement 📘"

    # Build HTML output
    html = f"""
    <h6><strong>Student:</strong> {first} {last}</h6>
    <h6><strong>Summary of Grades:</strong></h6>
    <ul>
    """
    for subj, grade in zip(subjects, grades):
        html += f"<li>{subj}: {grade}</li>"
    html += f"""
    </ul>
    <h6><strong>General Weighted Average:</strong> <span class='gwa'>{gwa:.2f}</span></h6>
    <p><em>{remark}</em></p>
    """

    document.getElementById("output").innerHTML = html

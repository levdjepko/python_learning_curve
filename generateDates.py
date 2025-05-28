from datetime import datetime

# This procedure generates valid academic years
# it assumes the MS SQL syntax
def generate_grad_years_string():
    currentYear = datetime.now().year
    nextYear = currentYear + 1
    currentMonth = datetime.now().month

    if currentMonth < 7:
        grad_years = [f"{currentYear - 1}-{currentYear}", f"{currentYear}-{nextYear}",
                        f"{nextYear}-{nextYear + 1}", f"{nextYear + 1}-{nextYear + 2}"]
    else:
        grad_years = [f"{currentYear}-{nextYear}", f"{nextYear}-{nextYear + 1}",
                        f"{nextYear + 1}-{nextYear + 2}", f"{nextYear + 2}-{nextYear + 3}"]

    grad_years = str(grad_years).replace('[', '').replace(']', '')
    return grad_years
  
grad_years = generate_grad_years_string()
sqlQuery = "SELECT * from VIEW \
            WHERE GradYear IN (" + grad_years + ") \
            EXCEPT \
            SELECT * FROM staging.VIEW \
            WHERE GradYear IN (" + grad_years + ") "
print(sqlQuery)

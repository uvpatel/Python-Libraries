# 📊 Matplotlib (Data Visualization Library)

Matplotlib is a Python library used for data visualization.
It helps you create line charts, bar graphs, histograms, scatter plots, pie charts, etc.

## 🔹 Installation

```bash
pip install matplotlib
```


## 🔹 Importing Matplotlib


```python
import matplotlib.pyplot as plt
```

## 🔹 Basic Line Plot
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, label="Line Graph", color="blue",  marker="o")
plt.title("Basic Line Plot")
plt.xlabel("X-axis") # lable to axis
plt.ylabel("Y-axis")
plt.legend()
plt.show()
```

## Bar Chart
```python
students = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

plt.bar(students, scores, color="green")
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()

```

## 🔹 Histogram
```bash
import numpy as np
```

```python
data = np.random.randn(1000)  # 1000 random numbers (normal distribution)

plt.hist(data, bins=30, color="orange", edgecolor="black")
plt.title("Histogram Example")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
```

## 🔹 Scatter Plot
```python
x = [5, 7, 8, 7, 6, 9, 5, 6]
y = [99, 86, 87, 88, 100, 86, 103, 87]

plt.scatter(x, y, color="red")
plt.title("Scatter Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()
```

## 🔹 Pie Chart

```python
labels = ["Apples", "Bananas", "Cherries", "Dates"]
sizes = [20, 30, 25, 25]

plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Fruit Distribution")
plt.show()
```

## 🔹 Subplots (Multiple Graphs in One Window)
```
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

plt.subplot(1, 2, 1)  # (rows, cols, plot_number)
plt.plot(x, y1, color="blue")
plt.title("Line Plot")

plt.subplot(1, 2, 2)
plt.plot(x, y2, color="red")
plt.title("Square Numbers")

plt.tight_layout()
plt.show()
```
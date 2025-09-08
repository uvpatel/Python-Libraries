# 🐼 Pandas (Python Data Analysis Library)

Pandas is a Python library used for data analysis and manipulation.
It provides powerful data structures like Series and DataFrame to handle tabular data (like Excel or SQL tables).

## 🔹 Why Pandas?

Easy to handle structured data (rows & columns).

Built on top of NumPy.

Powerful tools for data cleaning, filtering, grouping, and analysis.

Works well with CSV, Excel, SQL, JSON, and more.

## 🔹 Installation

```bash
pip install pandas
```

## 🔹 Importing Pandas
```python
import pandas as pd
```

## 🔹 Pandas Data Structures

### 1️⃣ Series (1D data – like a column)
```python
import pandas as pd

# Create Series from list
s = pd.Series([10, 20, 30, 40])
print(s)

# Custom index
s2 = pd.Series([100, 200, 300], index=["a", "b", "c"])
print(s2)

# Access elements
print(s2["b"])   # 200
```

### 2️⃣ DataFrame (2D data – like an Excel sheet)

```python
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

df = pd.DataFrame(data)
print(df)
```


```txt
Output:
      Name  Age      City
0    Alice   25  New York
1      Bob   30    London
2  Charlie   35     Paris
```

## Reading & Writing Data
```python
# Read CSV file
df = pd.read_csv("data.csv")

# Write to CSV file
df.to_csv("output.csv", index=False)
```

## 🔹 Basic Info & Statistics
```python
print(df.head())        # first 5 rows
print(df.tail())        # last 5 rows
print(df.shape)         # (rows, columns)
print(df.info())        # column info
print(df.describe())    # summary statistics
```

## 🔹 Selecting Data

```python
# Select column
print(df["Name"])

# Select multiple columns
print(df[["Name", "City"]])

# Select row by index
print(df.iloc[1])   # row 1 (Bob)

# Select row by label
print(df.loc[2])    # row with index 2 (Charlie)

# Conditional filtering
print(df[df["Age"] > 25])
```

## 🔹 Modifying Data
```python
# Add new column
df["Country"] = ["USA", "UK", "France"]

# Update values
df.at[0, "Age"] = 26   # change Alice's age to 26

# Drop column
df = df.drop("City", axis=1)

```


## Drop row
```python
df = df.drop(1, axis=0)

🔹 Useful Operations
print(df["Age"].mean())      # Average age
print(df["Age"].max())       # Max age
print(df["Age"].min())       # Min age

# Sorting
print(df.sort_values(by="Age"))

# Grouping
print(df.groupby("Country")["Age"].mean())
```

## Data
| Name    | Age | City     |
| ------- | --- | -------- |
| Alice   | 25  | New York |
| Bob     | 30  | London   |
| Charlie | 35  | Paris    |


 `Note`
- this is a sample dataset for small example there can be any number of lines.

### JSON Data (JavaScript Object Notation)

```json
[
  {
    "Name": "Alice",
    "Age": 25,
    "City": "New York"
  },
  {
    "Name": "Bob",
    "Age": 30,
    "City": "London"
  },
  {
    "Name": "Charlie",
    "Age": 35,
    "City": "Paris"
  }
]

```

### 🔹 Reading JSON with Pandas
```python
Reading JSON with Pandas
import pandas as pd

# Load JSON file
df = pd.read_json("data.json")

# Show DataFrame
print(df)
```
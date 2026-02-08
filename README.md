# Parallelism Projects

This repository contains various implementations of parallel and serial algorithms in multiple programming languages (Java, C#, and Python).

## Project Structure

### 1. MatrixMultiplication
Implementations of matrix multiplication algorithms demonstrating parallel processing concepts.

#### Files:
- **MatrixMult.java** - Parallel matrix multiplication implementation in Java
- **MatrixMultSerial.java** - Serial matrix multiplication implementation in Java (baseline for comparison)

#### Purpose:
- Compare performance between parallel and serial matrix multiplication
- Demonstrates the use of parallelism for CPU-intensive operations

---

### 2. PolynomialEvaluator
Multiple implementations of polynomial evaluation algorithms in different languages. Each language has both parallel and serial versions for performance comparison.

#### C# Implementation
Located in `PolynomialEvaluator/C#/PolynomialEvaluator/`

- **PolynomialEvaluator.csproj** - Parallel polynomial evaluator project (.NET)
  - `PolynomialEvaluator.cs` - Parallel implementation
  - `Program.cs` - Entry point

- **PolynomialEvaluatorSerial.csproj** - Serial polynomial evaluator project (.NET)
  - `PolynomialEvaluatorSerial.cs` - Serial implementation
  - `Program.cs` - Entry point

#### Java Implementation
Located in `PolynomialEvaluator/Java/`

- **PolynomialEvaluator.java** - Parallel polynomial evaluator implementation
- **PolynomialEvaluatorSerial.java** - Serial polynomial evaluator implementation

#### Python Implementation
Located in `PolynomialEvaluator/Python/`

- **PolynomialEvaluator.py** - Parallel polynomial evaluator implementation
- **PolynomialEvaluatorSerial.py** - Serial polynomial evaluator implementation

#### Testing
Located in `PolynomialEvaluator/Testing/`

- **generate_values.py** - Script to generate test polynomial values
- **values.txt** - Pre-generated test values for polynomial evaluation

#### Purpose:
- Evaluate polynomial expressions efficiently
- Compare performance across three languages (C#, Java, Python)
- Benchmark parallel vs. serial implementations in each language

---

### 3. WordCounter
A word counting utility implementation.

- **WordCounter.py** - Python implementation of a word counter

#### Purpose:
- Count word frequencies in text
- Demonstrate text processing capabilities

---

## Getting Started

### Running C# Projects
```bash
cd PolynomialEvaluator/C#/PolynomialEvaluator
dotnet run --project PolynomialEvaluator/PolynomialEvaluator.csproj
dotnet run --project PolynomialEvaluatorSerial/PolynomialEvaluatorSerial.csproj
```

### Running Java Projects
```bash
cd MatrixMultiplication/Java
javac MatrixMult.java
java MatrixMult

javac MatrixMultSerial.java
java MatrixMultSerial

cd PolynomialEvaluator/Java
javac PolynomialEvaluator.java
java PolynomialEvaluator

javac PolynomialEvaluatorSerial.java
java PolynomialEvaluatorSerial
```

### Running Python Projects
```bash
python PolynomialEvaluator/Python/PolynomialEvaluator.py
python PolynomialEvaluator/Python/PolynomialEvaluatorSerial.py
python WordCounter/WordCounter.py

# Generate test values
python PolynomialEvaluator/Testing/generate_values.py
```

---

## Performance Comparison

Each project includes both parallel and serial implementations. You can use these to:
- Measure the performance differences between parallel and serial execution
- Understand scalability characteristics
- Optimize algorithms for multi-core systems

---

## Notes

- All projects use industry-standard frameworks and libraries for their respective languages
- The .NET projects target net10.0
- Compare execution times between parallel and serial versions to see the impact of parallelization

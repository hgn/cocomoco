# Cocomoco

## Models

<img src="https://render.githubusercontent.com/render/math?math=E = a ( KLOC )^{b}">

### Standard Models

- Organic
  - 2-50 KLOC
  - stable dev
  - little innovation
- Semi-detached
  - 50-300 KLOC
  - average abilities
  - medium time-constraints
- Embedded
  - larger 300 KLOC
  - large project team
  - complex
  - innovative
  - severe constraints

### Intermediate Models

Intermediate cocomo introduces cost drivers to the standard models.

- Product Attributes
  - **RELY** Required Software Reliability
  - **DATA** Data Base Size
  - **CPLX** Product Complexity
- Computer Attributes
  - **TIME** Execution Time Constraint
  - **STOR** Main Storage Constraint
  - **VIRT** Virtual Machine Volatility
  - **TURN** Computer Turnaround Time
- Personnel Attributes
  - **ACAP** Analyst Capability
  - **AEXP** Application Experience
  - **PCAP** Programming Capability
  - **VEXP** Virtual Machine Experience
  - **LEXP** Programming Language Experience
- Project Attributes
  - **MODP** Modern Programming Practices
  - **TOOL** Use of Software Tools
  - **SCED** Required Development Schedule

Cocomo commes with a predefined set of values in the following categories: very
low, low, nominal, high, very high, extra high. 

## Show Case

Following chart is created via `python3 -m cocomoco --demo-mode` (as well as other illustrations):

![image](doc/cocomo-standard-models.png)


## Installation

Simple install this module via pip (pip for Python 2 is also supported)

```
pip3 install --user cocomoco
```

## Usage

### As Python Module

```
import cocomoco

result = cocomoco.calculate(100000)
print(result)
```

### As Python Executable

```sh
$ python3 -m cocomoco --sloc <number> [--model <modelname>]
```

# References

- Alan Caine, Constructive Cost Model COCOMO, https://cs.uwaterloo.ca/~apidduck/se362/Lectures/cocomo.pdf

<p align="center">
  <!-- <img src="docs/imgs/logo_react_xss_scanner.png" width="800"> -->
</p>

<h1></h1>

<p align="center">
Markdown code execution tool
</p>

![issues](https://img.shields.io/github/issues/Maaaaru/MarkRun)
![forks](https://img.shields.io/github/forks/Maaaaru/MarkRun)
![stars](https://img.shields.io/github/stars/Maaaaru/MarkRun)
![licence](https://img.shields.io/github/license/Maaaaru/MarkRun)

# What is this

This is a tool that extracts and executes code from a given markdown file

# Instalation

clone this repository

```
$ git clone https://github.com/Maaaaru/MarkRun.git
```

Install dependent libraries

```
pip3 install -r requirements.txt
```

# Start Scan

```
$ cd MarkRun
$ python3 main.py --path ../README.md
```

<!-- <img src="docs/imgs/scan_demo.png" width="800"> -->

# Flags

| Long Form | Short Form | Description                                |
| --------- | ---------- | ------------------------------------------ |
| --help    | -h         | help message                               |
| --path    | -P         | Path to the markdown file you want to run. |

There are currently only two flags, but more will be added in the future

# Licence

MarkRun is licensed under the MIT license. take a look at the [LICENSE](https://github.com/Maaaaru/MarkRun/blob/main/LICENSE) for more information.

# Version

Current Version is 1.0.0

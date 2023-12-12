# Gazillion Port Scanner - Port Lookup

## Overview
Gazillion Port Scanner is a powerful and easy-to-use tool for port scanning. It provides a comprehensive solution for discovering open ports on a target system. Whether you need to check a specific port or scan a range of ports, PortLookup has you covered.

## Features
- **Flexible Port Scanning:**
  - Scan a range of ports effortlessly.
  - Detects open ports in less time.

- **Multi-threaded Scanning:**
  - Improve scanning speed by specifying the number of threads.

## Screenshots 📸 :
<h1 align="center">
  <h2 align="center">Screen Shot 1</h2>
  <h1 align="center"><img align="center" src="https://ik.imagekit.io/d3kzbpbila/thejashari_NxVvgM4OZ" width="700px" alt="screenshot1"></h1>
  <h2 align="center">Screen Shot 2</h2>
 <h1 align="center"> <img align="center" src="https://ik.imagekit.io/d3kzbpbila/thejashari_ZayGXNkUp" width="700px" alt="screenshot2"></h1>
 <h2 align="center">Screen Shot 3</h2>
 <h1 align="center"> <img align="center" src="https://ik.imagekit.io/d3kzbpbila/thejashari_PN0h9Vo47n" width="700px" alt="screenshot3"></h1>


## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/thejas-dev/Port-Scanner.git
    cd Port-Scanner
    ```
    
2. **Install dependencies (if any):**
    ```bash
    pip install -r requirements.txt
    ```

### Making the Tool Global

To make Gazilion Port Scanner globally accessible from any directory, follow these steps:

1. Open your Zsh configuration file (`~/.zshrc`) in a text editor:
    ```bash
    nano ~/.zshrc
    ```
    Replace `nano` with your preferred text editor.

2. Add the following line at the end of the file, replacing `/path/to/tool/directory` with the actual path to the tool directory:
    ```bash
    export PATH=$PATH:/path/to/tool/directory
    ```

3. Save the file and exit the text editor.

4. Reload your Zsh configuration to apply the changes:
    ```bash
    source ~/.zshrc
    ```

Now, you can run Gazilion port scanner from any directory using:
```bash
portLookup.py -h
```

### Usage

#### Options
- **-t <target>:** Specify the target IP or domain name.
- **-p <port or port range>:** Specify the port or port range.
  Examples:
    - Single port or start from port 1 up to the provided port: -p 80
    - Port range: -p 80-100
- **-threads, --threads <number of threads>:** Specify the number of threads.
- **-h, --help:** Display this help message.

#### Example
Run the tool with the following command:
```bash
portLookup.py -t example.com -p 80-100 --threads 20
```

### Connect with me on
<a href="https://www.linkedin.com/in/thejashari/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="linkedin" height="30" width="40" /></a>
<a href="https://instagram.com/nuthejashari" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="instagram" height="30" width="40" /></a>

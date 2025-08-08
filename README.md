# Python Network Scanner

A simple command-line network scanner in Python using sockets to identify open TCP ports on a target machine. This project was a learning experience in network programming and advanced debugging.

### Features

-   **Fast Scanning:** Efficiently checks for open ports on a given IP address or hostname.
-   **Comprehensive Port Range:** Scans a full range of ports from 1 to 65,535.
-   **Informative Output:** Provides a clear banner and reports which ports are open.
-   **Command-Line Interface:** Easy to run and use directly from the terminal.

### Prerequisites

To run this scanner, you will need:
* Python 3.x
* The `pyfiglet` library for the ASCII art banner. You can install it using pip:
    ```bash
    pip install pyfiglet
    ```

### How to Use

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Breat101010/python-network-scanner.git](https://github.com/Breat101010/python-network-scanner.git)
    cd python-network-scanner
    ```

2.  **Run the Scanner:**
    Use the following command, replacing `[ip address or hostname]` with your target.
    ```bash
    python scanner.py localhost
    ```

### Author

-   **Lee-roy Chimuka** www.linkedin.com/in/lee-roy-chimuka - A computer science student and aspiring cyber security professional.

  
### Future Features
    1. Different Scan Modes: Implement options for a stealthy scan, a full-range scan, or a quick scan of common ports.

    2. Output to File: Add a feature to save the scan results to a text file for later analysis.

    3. GUI (Graphical User Interface): Develop a simple front-end to make the scanner more user-friendly for a wider audience.

    4. Integration: Potentially integrate with other security tools for a more comprehensive analysis.
    

### Contributing
Contributions are always welcome! If you have ideas for new features or bug fixes, feel free to open an issue or submit a pull request. This project is a great learning opportunity, and I'm open to collaborating with others to improve it.

### Acknowledgement

*This project was an incredible lesson in persistence. The process of debugging unexpected environmental and permission issues was a significant challenge that highlighted the importance of creative problem-solving and systematic troubleshooting.*

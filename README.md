# Phishing Link Finder

Malicious Link Finder is a Flet-based desktop application that helps users verify whether a suspicious link is legitimate or potentially harmful. The tool compares the IP address of a given link with the official website of the organization to determine if it is trustworthy.

## Features
- **User-Friendly Interface**: Built using Flet, ensuring a seamless and modern UI.
- **Google Search Integration**: Fetches the top official websites of the given organization.
- **IP Address Comparison**: Resolves the IP address of the suspicious link and compares it with the official domain.
- **Real-Time Feedback**: Displays whether the link is legitimate or suspicious in real time.
- **Dark/Light Theme Toggle**: Users can switch between light and dark modes.

## Installation

### Prerequisites
- Python 3.8+
- Install required dependencies:
  ```bash
  pip install flet googlesearch-python
  ```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Nithinbharathi93/PhishingLinkFinder.git
   cd PhishingLinkFinder
   ```
2. Run the script:
   ```bash
   python main.py
   ```
3. Enter the **Source Organization** name.
4. Paste the **Suspicious Link**.
5. Click **Search** to verify the link.

## How It Works
1. The user provides the name of the organization and a suspicious link.
2. The application fetches the official websites of the given organization using Google Search.
3. It resolves the IP address of the suspicious link and compares it with the official website's IPs.
4. Based on the comparison, it displays one of the following:
   - ✅ **It's Legit** (Green) – If the link matches the official website's IP.
   - ⚠️ **Looks Suspicious** (Red) – If the link's IP does not match.
   - 🟠 **Error/No Website Found** – If an issue occurs during the process.

## Demo
![Demo Video](https://github.com/Nithinbharathi93/PhishingLinkFinder/blob/main/Recording%202025-01-08%20211131.mp4)

## Contributing
Contributions are welcome! Feel free to open issues and pull requests.

## License
This project is licensed under the MIT License.

## Author
Developed by [Nithinbharathi.T](https://github.com/Nithinbharathi93)

## Disclaimer
This tool is for educational purposes only. Always verify links through multiple sources before trusting them.



# VersaDiff

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)

**VersaDiff** is a modern open-source web application for comparing multiple code versions. Built with Python, Flask, CodeMirror, and Bootstrap, it provides interactive code editors with dynamic language support and clear, color-coded diff visualizations to help developers quickly analyze code changes.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Multi-Version Comparison:** Compare between 2 to 5 versions of your code.
- **Interactive Code Editors:** Uses [CodeMirror](https://codemirror.net/) for a modern in-browser editing experience with syntax highlighting.
- **Dynamic Language Support:** Choose the language mode for each editor (Python, JavaScript, HTML/XML, CSS, C/C++/Java).
- **Diff Visualization:** Generates clear, color-coded HTML diff tables using Python's `difflib`.
- **Responsive UI:** Styled with [Bootstrap](https://getbootstrap.com/) for a clean, mobile-friendly interface.

## Project Structure

```
VersaDiff/
├── app.py              # Flask backend application
└── templates/          # HTML templates
    ├── index.html      # Landing page for version selection
    ├── compare.html    # Code input page with CodeMirror editors
    └── result.html     # Diff results display page
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/aazzroy/VersaDiff.git
   cd VersaDiff
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install Flask
   ```

4. **Run the Application:**

   ```bash
   python app.py
   ```

5. **Access the Application:**

   Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage

1. **Select Versions:**  
   On the landing page, choose how many code versions you want to compare (2 to 5).

2. **Enter Your Code:**  
   Use the interactive CodeMirror editors to input your code. Select the appropriate language for syntax highlighting using the dropdown provided with each editor.

3. **Generate Diff:**  
   Click on "Compare Code" to generate and display the diff comparisons between consecutive versions.

4. **Review Differences:**  
   The results page will display color-coded diff tables highlighting additions, deletions, and changes between versions.

## Future Enhancements

- **Advanced Diffing:**  
  Integrate libraries like [diff-match-patch](https://github.com/google/diff-match-patch) or [jsdiff](https://github.com/kpdecker/jsdiff) to support non-consecutive and three-way diff views.

- **Extended Language Support:**  
  Add more CodeMirror modes and implement automatic language detection for improved usability.

- **Version Control Integration:**  
  Incorporate Git features to compare commits or branches directly within the application.

- **Enhanced UI/UX:**  
  Further refine the user interface with additional interactive features and a more customizable layout.

## Contributing

Contributions are welcome! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute, including our coding standards and the process for submitting pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Contact

If you have any questions, suggestions, or issues, please open an issue on GitHub or contact the project maintainer at [me@thegaurav.in](mailto:me@thegaurav.in) or visit [thegaurav.in](https://www.thegaurav.in/).
```
